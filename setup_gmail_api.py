"""
Setup Gmail API - Alternative to SMTP
Run this if SMTP ports are blocked
"""
import os

print("="*60)
print("📧 Gmail API Setup")
print("="*60)

# Check if credentials exist
if not os.path.exists('credentials.json'):
    print("\n❌ credentials.json not found!")
    print("\nTo get credentials.json:")
    print("1. Go to: https://console.cloud.google.com/")
    print("2. Create project: 'AKIRA Email'")
    print("3. Enable Gmail API")
    print("4. Create OAuth 2.0 Client ID")
    print("5. Download as credentials.json")
    print("6. Place in this folder")
    print("\nDetailed guide: https://developers.google.com/gmail/api/quickstart/python")
    exit(1)

# Check if libraries installed
try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    print("\n✅ Gmail API libraries installed")
except ImportError:
    print("\n❌ Gmail API libraries not installed!")
    print("\nInstall with:")
    print("pip install google-auth google-auth-oauthlib google-api-python-client")
    exit(1)

# Authenticate
print("\n🔑 Starting authentication...")
print("   A browser window will open")
print("   Log in with: kibeterick57@gmail.com")
print("   Grant permissions")

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

try:
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    
    # Save token
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
    
    print("\n✅ Authentication successful!")
    print("   token.json created")
    print("\n📧 You can now send emails via Gmail API")
    print("   Even if SMTP ports are blocked!")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
