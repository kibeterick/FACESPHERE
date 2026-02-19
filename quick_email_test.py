"""Quick Gmail SMTP Test"""
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')

print(f"Testing: {email}")
print(f"Password length: {len(password) if password else 0}")

try:
    print("Connecting...")
    server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
    print("Starting TLS...")
    server.starttls()
    print("Logging in...")
    server.login(email, password)
    print("✅ SUCCESS! Gmail SMTP works!")
    server.quit()
except Exception as e:
    print(f"❌ ERROR: {e}")
