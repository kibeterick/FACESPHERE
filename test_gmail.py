"""
Test Gmail SMTP Connection
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials
email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')
smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
smtp_port = int(os.getenv('SMTP_PORT', 587))

print("="*60)
print("📧 Testing Gmail SMTP Connection")
print("="*60)
print(f"\nEmail: {email_address}")
print(f"SMTP Server: {smtp_server}:{smtp_port}")
print(f"Password: {'*' * len(email_password) if email_password else 'NOT SET'}")

try:
    # Create test message
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = email_address  # Send to yourself
    msg['Subject'] = 'Test Email from AKIRA - Gmail SMTP Test'
    
    body = """
    This is a test email from AKIRA AI System.
    
    If you receive this email, Gmail SMTP integration is working correctly!
    
    Test Details:
    - Sent via: Gmail SMTP
    - Server: smtp.gmail.com:587
    - Authentication: App Password
    
    AKIRA AI System
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    print("\n🔄 Connecting to Gmail SMTP server...")
    
    # Connect to Gmail SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.set_debuglevel(1)  # Show debug output
    
    print("\n🔒 Starting TLS encryption...")
    server.starttls()
    
    print("\n🔑 Logging in...")
    server.login(email_address, email_password)
    
    print("\n📤 Sending email...")
    server.send_message(msg)
    
    print("\n✅ Email sent successfully!")
    print(f"   Check your inbox: {email_address}")
    print(f"   Check your Sent folder in Gmail")
    
    server.quit()
    
    print("\n" + "="*60)
    print("✅ SUCCESS! Gmail SMTP is working correctly!")
    print("="*60)
    
except smtplib.SMTPAuthenticationError as e:
    print("\n❌ AUTHENTICATION ERROR!")
    print(f"   Error: {e}")
    print("\n   Possible causes:")
    print("   1. App Password is incorrect")
    print("   2. 2-Step Verification not enabled")
    print("   3. App Password was revoked")
    print("\n   Solution:")
    print("   - Generate a new App Password")
    print("   - Go to: https://myaccount.google.com/apppasswords")
    
except smtplib.SMTPException as e:
    print("\n❌ SMTP ERROR!")
    print(f"   Error: {e}")
    
except Exception as e:
    print("\n❌ ERROR!")
    print(f"   Error: {e}")
    print(f"   Type: {type(e).__name__}")

print("\n")
