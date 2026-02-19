# Email Sending Solutions for AKIRA

## Problem
Emails show "success" but recipients don't receive them.

## Root Cause
Your network/firewall is blocking SMTP ports (587, 465, 25).

## Solutions (Try in Order)

### Solution 1: Check Firewall Settings ⭐ RECOMMENDED
1. Open Windows Defender Firewall
2. Click "Allow an app through firewall"
3. Allow Python through both Private and Public networks
4. Try sending email again

### Solution 2: Try Different SMTP Port
Gmail supports multiple ports:
- Port 587 (TLS) - Currently trying
- Port 465 (SSL) - Alternative
- Port 25 (Plain) - Last resort

Update `.env`:
```
SMTP_PORT=465
```

### Solution 3: Use Gmail API (No SMTP needed)
Gmail API works even when SMTP is blocked.

#### Setup Steps:
1. Go to: https://console.cloud.google.com/
2. Create new project: "AKIRA Email"
3. Enable Gmail API
4. Create OAuth 2.0 credentials
5. Download as `credentials.json`
6. Place in project folder
7. Install: `pip install google-auth google-auth-oauthlib google-api-python-client`
8. Run: `python setup_gmail_api.py`

### Solution 4: Use Email Service Provider
Services like SendGrid, Mailgun work without SMTP:
- SendGrid: Free 100 emails/day
- Mailgun: Free 5,000 emails/month

### Solution 5: Contact Network Admin
If on corporate/school network, ask admin to unblock:
- smtp.gmail.com:587
- smtp.gmail.com:465

## Quick Test
Run this to check which ports are open:
```
python check_smtp_port.py
```

## Current Status
- Gmail configured: ✅ kibeterick57@gmail.com
- App Password: ✅ Set
- SMTP Port 587: ❌ Blocked by firewall
- Need: Firewall fix OR Gmail API

