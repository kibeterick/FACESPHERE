# 📅📧 Calendar & Email Integration Guide

Complete guide for Calendar Scheduling and Email Management features in AKIRA AI System.

---

## 📅 CALENDAR & SCHEDULING SYSTEM

### Features Overview

1. **Meeting Scheduler**
   - Schedule meetings with multiple attendees
   - Set duration, location, and notes
   - Automatic reminders 15 minutes before
   - Cancel or reschedule meetings

2. **Appointment Management**
   - Schedule personal appointments
   - Track who you're meeting with
   - Set location and duration
   - Automatic reminders 30 minutes before

3. **Event Management**
   - Create all-day or timed events
   - Categorize events (general, celebration, etc.)
   - Add descriptions and locations
   - Track event status

4. **Smart Reminders**
   - Automatic reminders for meetings/appointments
   - Custom reminder timing
   - Pending reminder tracking
   - Integration with notification system

5. **Schedule Views**
   - Today's schedule overview
   - Week view with daily summaries
   - Search across all calendar items
   - Statistics dashboard

### How to Use Calendar

#### Access Calendar
```
Navigate to: http://localhost:5000/calendar
```

#### Schedule a Meeting
1. Fill in meeting details:
   - Title (required)
   - Date and time (required)
   - Duration in minutes
   - Attendees (comma-separated)
   - Location
   - Notes

2. Click "Schedule Meeting"
3. Automatic reminder created 15 minutes before

#### Schedule an Appointment
1. Fill in appointment details:
   - Title (required)
   - Date and time (required)
   - Duration in minutes
   - Person you're meeting with
   - Location
   - Notes

2. Click "Schedule Appointment"
3. Automatic reminder created 30 minutes before

#### View Schedule
- **Today's Schedule**: See all items for today
- **Week View**: 7-day overview with item counts
- **Statistics**: Total meetings, appointments, events

### API Endpoints

#### Get Today's Schedule
```bash
GET /api/calendar/today
```

Response:
```json
{
  "date": "2026-02-19",
  "meetings": [...],
  "appointments": [...],
  "events": [...],
  "total_items": 5
}
```

#### Schedule Meeting
```bash
POST /api/calendar/meetings
Content-Type: application/json

{
  "title": "Team Standup",
  "date": "2026-02-20",
  "time": "09:00",
  "duration": 30,
  "attendees": ["John", "Sarah"],
  "location": "Conference Room A",
  "notes": "Discuss project progress"
}
```

#### Get Week Schedule
```bash
GET /api/calendar/week
```

#### Search Calendar
```bash
GET /api/calendar/search?q=standup
```

#### Get Statistics
```bash
GET /api/calendar/statistics
```

---

## 📧 EMAIL MANAGEMENT SYSTEM

### Features Overview

1. **Send/Receive Emails**
   - Send emails with attachments
   - HTML or plain text format
   - Receive and view inbox
   - Mark as read/unread

2. **Email Templates**
   - Pre-built templates (Welcome, Notification, Reminder, Alert, Report)
   - Variable substitution
   - Custom template creation
   - Quick template usage

3. **Inbox Management**
   - View all emails
   - Filter unread emails
   - Star important emails
   - Delete emails
   - Search functionality

4. **Draft System**
   - Save emails as drafts
   - Edit drafts
   - Send drafts later
   - Draft statistics

5. **Bulk Operations**
   - Send bulk emails
   - Personalization options
   - Success/failure tracking

### How to Use Email

#### Access Email Management
```
Navigate to: http://localhost:5000/email
```

#### Send an Email
1. Click "Compose" tab
2. Fill in:
   - To: Recipient email address
   - Subject: Email subject
   - Message: Email body

3. Click "Send Email" or "Save Draft"

#### Use Email Template
1. Click "Templates" tab
2. Choose a template:
   - Welcome: Welcome new users
   - Notification: General notifications
   - Reminder: Send reminders
   - Alert: Alert notifications
   - Report: Daily reports

3. Template loads into compose form
4. Customize and send

#### View Inbox
- Inbox shows all received emails
- Unread emails highlighted with blue border
- Click email to view details
- Auto-refresh every 30 seconds

### API Endpoints

#### Send Email
```bash
POST /api/email/send
Content-Type: application/json

{
  "to_email": "[email]",
  "subject": "Test Email",
  "body": "This is a test email",
  "html": false,
  "attachments": []
}
```

Response:
```json
{
  "success": true,
  "message": "Email sent successfully",
  "email_id": 1
}
```

#### Get Inbox
```bash
GET /api/email/inbox
GET /api/email/inbox?unread_only=true
```

#### Send from Template
```bash
POST /api/email/template
Content-Type: application/json

{
  "template_name": "welcome",
  "to_email": "[email]",
  "variables": {
    "name": "John Doe"
  }
}
```

#### Get Email Statistics
```bash
GET /api/email/statistics
```

Response:
```json
{
  "inbox": {
    "total": 10,
    "unread": 3,
    "starred": 2
  },
  "sent": 15,
  "drafts": 2,
  "total_emails": 25
}
```

#### Search Emails
```bash
GET /api/email/search?q=meeting&folder=all
```

---

## 🔗 INTEGRATION WITH OTHER SYSTEMS

### Calendar + Notifications
- Automatic reminders sent via notification system
- Emergency alerts can include calendar context
- Daily summary includes today's schedule

### Email + Notifications
- Email notifications for important events
- Alert emails for security issues
- Marketing emails for campaigns

### Calendar + Email
- Meeting invitations via email
- Appointment confirmations
- Event reminders by email

---

## 📊 STATISTICS & ANALYTICS

### Calendar Statistics
- Total meetings scheduled
- Total appointments
- Total events
- Today's items count
- Pending reminders

### Email Statistics
- Total inbox emails
- Unread count
- Starred emails
- Sent emails count
- Draft count
- Total emails processed

---

## 🎯 QUICK ACTIONS

### Calendar Quick Actions
1. **View Today**: See today's schedule
2. **Schedule Meeting**: Quick meeting creation
3. **Check Reminders**: View upcoming reminders
4. **Week Overview**: See week at a glance

### Email Quick Actions
1. **Compose**: Start new email
2. **Check Inbox**: View new emails
3. **Use Template**: Quick template email
4. **View Drafts**: Access saved drafts

---

## 🔧 CONFIGURATION

### Email Configuration
Set environment variables in `.env`:
```bash
# Email Settings
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
IMAP_SERVER=imap.gmail.com
IMAP_PORT=993
EMAIL_ADDRESS=[email]
EMAIL_PASSWORD=[password]
```

### Calendar Data Storage
- Data stored in: `calendar_data.json`
- Automatic backup on each change
- Keeps last 1000 entries

### Email Data Storage
- Inbox: In-memory (can be configured for database)
- Sent emails: Tracked in memory
- Drafts: Saved locally

---

## 🚀 ADVANCED FEATURES

### Calendar Advanced Features
1. **Recurring Events**: Schedule repeating meetings
2. **Time Zone Support**: Handle multiple time zones
3. **Calendar Sync**: Sync with Google Calendar, Outlook
4. **Conflict Detection**: Detect scheduling conflicts
5. **Availability Checking**: Check attendee availability

### Email Advanced Features
1. **Email Tracking**: Track email opens and clicks
2. **Scheduled Sending**: Schedule emails for later
3. **Auto-Reply**: Set up automatic responses
4. **Email Filters**: Create custom filters
5. **Signature Management**: Custom email signatures

---

## 📱 MOBILE ACCESS

Both Calendar and Email systems are fully responsive and work on:
- Desktop browsers
- Tablets
- Mobile phones
- Progressive Web App (PWA) support

---

## 🔒 SECURITY

### Calendar Security
- User authentication required
- Private calendar data
- Encrypted storage
- Access control per calendar

### Email Security
- Encrypted connections (TLS/SSL)
- Password protection
- Spam filtering
- Virus scanning for attachments

---

## 💡 TIPS & BEST PRACTICES

### Calendar Tips
1. Set reminders for important meetings
2. Use descriptive titles
3. Add location for in-person meetings
4. Include agenda in notes
5. Review week schedule on Mondays

### Email Tips
1. Use templates for common emails
2. Keep subject lines clear
3. Save drafts for complex emails
4. Use search to find old emails
5. Star important emails

---

## 🆘 TROUBLESHOOTING

### Calendar Issues
**Problem**: Reminders not showing
- Check notification system is enabled
- Verify reminder timing settings
- Check calendar data file permissions

**Problem**: Schedule not loading
- Refresh the page
- Check API endpoint status
- Verify calendar_data.json exists

### Email Issues
**Problem**: Can't send emails
- Check SMTP settings in .env
- Verify email credentials
- Check internet connection

**Problem**: Inbox not loading
- Check IMAP settings
- Verify email service is running
- Try manual refresh

---

## 📞 SUPPORT

For issues or questions:
1. Check this documentation
2. Review API endpoints
3. Check system logs
4. Contact AKIRA support

---

## 🎉 WHAT'S NEXT?

Upcoming features:
1. Google Calendar integration
2. Outlook sync
3. Email automation rules
4. Advanced scheduling algorithms
5. AI-powered email composition
6. Smart meeting suggestions
7. Calendar sharing
8. Email collaboration

---

**Last Updated**: February 19, 2026
**Version**: 1.0.0
**Status**: ✅ Fully Operational
