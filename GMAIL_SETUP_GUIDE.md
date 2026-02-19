# 📧 Gmail Integration Setup Guide

Complete guide to configure AKIRA to send real emails through your Gmail account.

---

## 🎯 OVERVIEW

AKIRA can send real emails through Gmail using SMTP. You'll see the emails in your Gmail Sent folder and recipients will receive them in their inbox.

---

## 📋 PREREQUISITES

1. A Gmail account
2. 2-Step Verification enabled on your Google account
3. An App Password generated for AKIRA

---

## 🔧 STEP-BY-STEP SETUP

### Step 1: Enable 2-Step Verification

1. Go to your Google Account: https://myaccount.google.com
2. Click on "Security" in the left menu
3. Under "Signing in to Google", click "2-Step Verification"
4. Follow the prompts to enable 2-Step Verification
5. You'll need your phone to receive verification codes

### Step 2: Generate App Password

1. After enabling 2-Step Verification, go back to Security
2. Under "Signing in to Google", click "App passwords"
   - Direct link: https://myaccount.google.com/apppasswords
3. You may need to sign in again
4. Select app: Choose "Mail"
5. Select device: Choose "Other (Custom name)"
6. Enter name: Type "AKIRA AI System"
7. Click "Generate"
8. **IMPORTANT**: Copy the 16-character password (it looks like: `abcd efgh ijkl mnop`)
9. Save this password - you won't see it again!

### Step 3: Configure AKIRA

1. Open your `.env` file in the AKIRA project folder
2. Add or update these lines:

```bash
# Gmail Configuration
EMAIL_ADDRESS=your.email@gmail.com
EMAIL_PASSWORD=abcdefghijklmnop
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

**Replace**:
- `your.email@gmail.com` with your actual Gmail address
- `abcdefghijklmnop` with the 16-character App Password (remove spaces)

### Step 4: Test the Configuration

Run this test script:

```python
from email_service import email_service

# Send test email
result = email_service.send_email(
    to_email='your.email@gmail.com',  # Send to yourself first
    subject='Test Email from AKIRA',
    body='This is a test email. If you receive this, Gmail integration is working!'
)

print(f"Success: {result['success']}")
print(f"Message: {result['message']}")
```

Or use the web interface:
1. Go to http://localhost:5000/email
2. Compose an email to yourself
3. Click "Send Email"
4. Check your Gmail inbox!

---

## ✅ VERIFICATION

After sending a test email, check:

1. **Your Gmail Sent folder**: The email should appear here
2. **Recipient's inbox**: They should receive the email
3. **AKIRA console**: Should show "✅ Email sent successfully"

---

## 🔒 SECURITY NOTES

### App Passwords are Secure
- App passwords are safer than using your main Gmail password
- They only work for the specific app (AKIRA)
- You can revoke them anytime without changing your main password

### Keep Your .env File Private
- Never share your `.env` file
- Add `.env` to `.gitignore` if using Git
- The `.env` file contains sensitive credentials

### Revoke Access Anytime
1. Go to https://myaccount.google.com/apppasswords
2. Find "AKIRA AI System"
3. Click "Remove" to revoke access

---

## 🎨 EXAMPLE .env FILE

```bash
# AKIRA AI System Configuration

# Gmail Settings (for sending emails)
EMAIL_ADDRESS=john.doe@gmail.com
EMAIL_PASSWORD=abcdefghijklmnop
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

# IMAP Settings (for receiving emails - optional)
IMAP_SERVER=imap.gmail.com
IMAP_PORT=993

# AI API Keys
GEMINI_API_KEY=your_gemini_key_here
OPENAI_API_KEY=your_openai_key_here

# Weather API
WEATHER_API_KEY=your_weather_key_here

# Payment Gateways (optional)
STRIPE_API_KEY=your_stripe_key
PAYPAL_CLIENT_ID=your_paypal_id
```

---

## 📧 SENDING EMAILS

### Via Web Interface

1. Navigate to http://localhost:5000/email
2. Fill in the form:
   - To: recipient@example.com
   - Subject: Your subject
   - Message: Your message
3. Click "Send Email"
4. Email will be sent via Gmail!

### Via Python Code

```python
from email_service import email_service

# Simple email
email_service.send_email(
    to_email='recipient@example.com',
    subject='Hello from AKIRA',
    body='This is a test email sent via Gmail!'
)

# Email with HTML
email_service.send_email(
    to_email='recipient@example.com',
    subject='HTML Email',
    body='<h1>Hello!</h1><p>This is <b>HTML</b> email.</p>',
    html=True
)

# Using template
email_service.send_from_template(
    template_name='welcome',
    to_email='newuser@example.com',
    variables={'name': 'John Doe'}
)
```

### Via API

```bash
curl -X POST http://localhost:5000/api/email/send \
  -H "Content-Type: application/json" \
  -d '{
    "to_email": "recipient@example.com",
    "subject": "Test Email",
    "body": "Hello from AKIRA API!"
  }'
```

---

## 🆘 TROUBLESHOOTING

### Error: "SMTPAuthenticationError"

**Problem**: Gmail authentication failed

**Solutions**:
1. Verify 2-Step Verification is enabled
2. Check App Password is correct (16 characters, no spaces)
3. Make sure EMAIL_ADDRESS matches the Gmail account
4. Try generating a new App Password

### Error: "SMTPServerDisconnected"

**Problem**: Connection to Gmail server failed

**Solutions**:
1. Check internet connection
2. Verify SMTP_SERVER is `smtp.gmail.com`
3. Verify SMTP_PORT is `587`
4. Check firewall settings

### Emails Not Appearing in Sent Folder

**Problem**: Email sent but not in Gmail Sent folder

**Solutions**:
1. Check Gmail's "All Mail" folder
2. Wait a few seconds and refresh
3. Check if email went to Spam
4. Verify you're checking the correct Gmail account

### "Less Secure App Access" Message

**Problem**: Gmail blocks the login

**Solution**:
- This is why we use App Passwords!
- App Passwords bypass "less secure app" restrictions
- Make sure you're using an App Password, not your regular password

---

## 💡 PRO TIPS

### 1. Test with Yourself First
Always send the first test email to your own address to verify it works.

### 2. Check Spam Folder
If recipients don't receive emails, ask them to check their Spam folder.

### 3. Use Templates
Create email templates for common messages to save time.

### 4. Monitor Sending Limits
Gmail has sending limits:
- Free accounts: 500 emails/day
- Google Workspace: 2,000 emails/day

### 5. Add Signature
Customize email templates to include your signature.

---

## 🔄 SWITCHING GMAIL ACCOUNTS

To use a different Gmail account:

1. Generate App Password for the new account
2. Update `.env` file with new credentials:
   ```bash
   EMAIL_ADDRESS=newemail@gmail.com
   EMAIL_PASSWORD=new_app_password
   ```
3. Restart AKIRA
4. Test with new account

---

## 📊 MONITORING

### Check Sent Emails

```python
from email_service import email_service

# Get sent emails
sent = email_service.get_sent_emails(limit=10)

for email in sent:
    print(f"To: {email['to']}")
    print(f"Subject: {email['subject']}")
    print(f"Status: {email['status']}")
    print("---")
```

### View Statistics

```python
stats = email_service.get_email_statistics()

print(f"Total sent: {stats['sent']}")
print(f"Total drafts: {stats['drafts']}")
```

---

## 🎯 WHAT YOU CAN DO NOW

With Gmail integration, you can:

✅ Send real emails to anyone  
✅ See emails in your Gmail Sent folder  
✅ Recipients receive emails in their inbox  
✅ Use email templates  
✅ Send HTML emails  
✅ Attach files (coming soon)  
✅ Track sent emails  
✅ Integrate with other AKIRA features  

---

## 🔗 USEFUL LINKS

- Google Account Security: https://myaccount.google.com/security
- App Passwords: https://myaccount.google.com/apppasswords
- 2-Step Verification: https://myaccount.google.com/signinoptions/two-step-verification
- Gmail Help: https://support.google.com/mail

---

## 📞 NEED HELP?

If you're still having issues:

1. Double-check all steps above
2. Try generating a new App Password
3. Restart AKIRA after updating `.env`
4. Check the console for error messages
5. Verify your Gmail account is active

---

## ✨ EXAMPLE: COMPLETE WORKFLOW

```python
# 1. Configure in .env
# EMAIL_ADDRESS=myemail@gmail.com
# EMAIL_PASSWORD=abcdefghijklmnop

# 2. Import service
from email_service import email_service

# 3. Send welcome email
result = email_service.send_from_template(
    template_name='welcome',
    to_email='newuser@example.com',
    variables={'name': 'John Doe'}
)

# 4. Check result
if result['success']:
    print("✅ Email sent! Check your Gmail Sent folder!")
else:
    print(f"❌ Error: {result['message']}")

# 5. View in Gmail
# - Open Gmail
# - Go to Sent folder
# - See your email!
```

---

**Last Updated**: February 19, 2026  
**Version**: 1.0.0  
**Status**: ✅ Ready to Use

**Happy Emailing! 📧**
