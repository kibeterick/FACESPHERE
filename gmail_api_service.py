"""
Gmail API Service - Alternative to SMTP
Works even when SMTP ports are blocked
"""
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json
from datetime import datetime

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    GMAIL_API_AVAILABLE = True
except ImportError:
    GMAIL_API_AVAILABLE = False


class GmailAPIService:
    """Gmail API service for sending emails when SMTP is blocked"""
    
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    
    def __init__(self):
        self.service = None
        self.credentials_file = 'credentials.json'
        self.token_file = 'token.json'
        
    def authenticate(self):
        """Authenticate with Gmail API"""
        if not GMAIL_API_AVAILABLE:
            return False, "Gmail API libraries not installed"
            
        creds = None
        
        # Load existing token
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, self.SCOPES)
        
        # If no valid credentials, let user log in
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(self.credentials_file):
                    return False, "credentials.json not found"
                    
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, self.SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save credentials
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())
        
        self.service = build('gmail', 'v1', credentials=creds)
        return True, "Authenticated successfully"
    
    def send_email(self, to_email, subject, body, html=False):
        """Send email via Gmail API"""
        if not self.service:
            success, msg = self.authenticate()
            if not success:
                return {'success': False, 'message': msg}
        
        try:
            message = MIMEMultipart('alternative')
            message['to'] = to_email
            message['subject'] = subject
            
            if html:
                message.attach(MIMEText(body, 'html'))
            else:
                message.attach(MIMEText(body, 'plain'))
            
            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            
            send_message = self.service.users().messages().send(
                userId='me',
                body={'raw': raw_message}
            ).execute()
            
            return {
                'success': True,
                'message': 'Email sent via Gmail API',
                'message_id': send_message['id']
            }
            
        except Exception as e:
            return {
                'success': False,
                'message': f'Gmail API error: {str(e)}'
            }


# Global instance
gmail_api = GmailAPIService()
