# 🚀 Quick Start Guide - Calendar & Email Features

Get started with the new Calendar and Email features in 5 minutes!

---

## 📅 CALENDAR & SCHEDULING - QUICK START

### Step 1: Access Calendar
```
1. Start AKIRA system: python flask_app.py
2. Open browser: http://localhost:5000
3. Click "Calendar & Scheduling" card
```

### Step 2: Schedule Your First Meeting
```
1. Fill in the form:
   - Title: "Team Standup"
   - Date: Select today
   - Time: 09:00
   - Duration: 30 minutes
   - Attendees: John, Sarah, Mike
   - Location: Conference Room A

2. Click "Schedule Meeting"
3. ✅ Done! Automatic reminder created
```

### Step 3: Schedule an Appointment
```
1. Use the right form:
   - Title: "Doctor Appointment"
   - Date: Tomorrow
   - Time: 14:00
   - Duration: 60 minutes
   - With: Dr. Smith
   - Location: Medical Center

2. Click "Schedule Appointment"
3. ✅ Done! Reminder set for 30 minutes before
```

### Step 4: View Your Schedule
```
- Today's Schedule: See all items for today
- Week View: 7-day overview at the bottom
- Statistics: Check the cards at the top
```

---

## 📧 EMAIL MANAGEMENT - QUICK START

### Step 1: Access Email
```
1. From home page: http://localhost:5000
2. Click "Email Management" card
3. Email interface opens
```

### Step 2: Send Your First Email
```
1. In "Compose Email" section:
   - To: [email]
   - Subject: "Test Email from AKIRA"
   - Message: "This is my first email!"

2. Click "Send Email"
3. ✅ Done! Email sent successfully
```

### Step 3: Use Email Template
```
1. Click "Templates" tab
2. Choose a template:
   - Welcome: For new users
   - Notification: General alerts
   - Reminder: Send reminders
   - Alert: Important alerts
   - Report: Daily reports

3. Template loads automatically
4. Customize and send
```

### Step 4: Save a Draft
```
1. Compose your email
2. Click "Save Draft" instead of send
3. Draft saved for later
4. Check statistics to see draft count
```

---

## 🎯 QUICK ACTIONS

### Calendar Quick Actions
```bash
# View today's schedule
curl http://localhost:5000/api/calendar/today

# Get week overview
curl http://localhost:5000/api/calendar/week

# Get statistics
curl http://localhost:5000/api/calendar/statistics
```

### Email Quick Actions
```bash
# Send email via API
curl -X POST http://localhost:5000/api/email/send \
  -H "Content-Type: application/json" \
  -d '{
    "to_email": "[email]",
    "subject": "Test",
    "body": "Hello from AKIRA!"
  }'

# Get inbox
curl http://localhost:5000/api/email/inbox

# Get statistics
curl http://localhost:5000/api/email/statistics
```

---

## 🔗 INTEGRATION EXAMPLES

### Calendar + Notifications
```python
# Schedule meeting with notification
from calendar_scheduler import calendar
from notification_system import NotificationSystem

notifications = NotificationSystem()

# Schedule meeting
meeting = calendar.schedule_meeting(
    title="Important Meeting",
    date="2026-02-20",
    time="10:00",
    duration=60,
    attendees=["John", "Sarah"],
    location="Zoom"
)

# Send notification
notifications.send_system_notification(
    user_id="john@example.com",
    notification_type="reminder",
    message=f"Meeting scheduled: {meeting['title']}"
)
```

### Email + Templates
```python
# Send welcome email using template
from email_service import email_service

result = email_service.send_from_template(
    template_name='welcome',
    to_email='[email]',
    variables={'name': 'John Doe'}
)

print(f"Email sent: {result['success']}")
```

---

## 📊 VIEWING STATISTICS

### Calendar Statistics
```
Navigate to: http://localhost:5000/calendar

Top cards show:
- Total Meetings
- Total Appointments
- Total Events
- Today's Items
```

### Email Statistics
```
Navigate to: http://localhost:5000/email

Top cards show:
- Inbox Count
- Unread Count
- Sent Count
- Drafts Count
```

---

## 🎨 CUSTOMIZATION

### Add Custom Email Template
```python
from email_service import email_service

email_service.add_template(
    name='custom',
    subject='Custom Template',
    body='Hello {name},\n\nYour custom message here.\n\nBest regards'
)
```

### Create Recurring Meeting
```python
from calendar_scheduler import calendar
from datetime import datetime, timedelta

# Schedule weekly meeting for next 4 weeks
for week in range(4):
    date = (datetime.now() + timedelta(weeks=week)).strftime('%Y-%m-%d')
    calendar.schedule_meeting(
        title="Weekly Standup",
        date=date,
        time="09:00",
        duration=30,
        attendees=["Team"],
        location="Conference Room"
    )
```

---

## 🔧 CONFIGURATION

### Email Configuration (Optional)
```bash
# Edit .env file
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
IMAP_SERVER=imap.gmail.com
IMAP_PORT=993
EMAIL_ADDRESS=[email]
EMAIL_PASSWORD=[password]
```

### Calendar Configuration
```python
# Calendar data stored in: calendar_data.json
# Automatic backup on each change
# No configuration needed!
```

---

## 💡 PRO TIPS

### Calendar Tips
1. **Set reminders early**: Meetings get 15-min reminders, appointments get 30-min
2. **Use descriptive titles**: Makes searching easier
3. **Add locations**: Especially for in-person meetings
4. **Check week view**: Plan your week on Mondays
5. **Use notes field**: Add agenda or important details

### Email Tips
1. **Use templates**: Save time with pre-built templates
2. **Save drafts**: For emails that need more thought
3. **Clear subjects**: Make emails easy to find later
4. **Check inbox regularly**: Auto-refreshes every 30 seconds
5. **Star important emails**: Quick access to priority items

---

## 🆘 TROUBLESHOOTING

### Calendar Not Loading?
```bash
# Check if calendar data file exists
ls calendar_data.json

# If missing, it will be created automatically
# Just schedule your first meeting!
```

### Email Not Sending?
```bash
# Check .env file for email settings
cat .env | grep EMAIL

# For testing, system works without real SMTP
# Emails are simulated and logged
```

### Statistics Not Updating?
```bash
# Refresh the page
# Or wait for auto-refresh (30 seconds)
# Or check browser console for errors
```

---

## 🎉 YOU'RE READY!

You now have:
- ✅ Calendar system with meetings, appointments, and events
- ✅ Email system with templates and drafts
- ✅ Automatic reminders
- ✅ Beautiful web interfaces
- ✅ Full REST APIs

### Next Steps
1. Schedule your first meeting
2. Send your first email
3. Explore the templates
4. Check the statistics
5. Integrate with other AKIRA features

---

## 📚 MORE RESOURCES

- **Full Documentation**: `CALENDAR_EMAIL_GUIDE.md`
- **Complete Features**: `COMPLETE_FEATURES_LIST.md`
- **API Reference**: Check Flask app endpoints
- **System Guide**: `COMPLETE_SYSTEM_SUMMARY.md`

---

## 🚀 LAUNCH COMMAND

```bash
# Start AKIRA system
python flask_app.py

# Access in browser
http://localhost:5000

# Click Calendar or Email cards
# Start using immediately!
```

---

**Happy Scheduling & Emailing! 📅📧**

*AKIRA AI System - Your Complete AI Companion*
