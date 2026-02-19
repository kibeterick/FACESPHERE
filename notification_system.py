"""
Advanced Notification System - Email, SMS, Push Notifications
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json


class NotificationSystem:
    """Multi-channel notification system"""
    
    def __init__(self):
        self.notification_queue = []
        self.notification_history = []
        self.preferences = {}
        
        # Email configuration (placeholder - configure with real credentials)
        self.email_config = {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'sender_email': '[email]',
            'sender_password': '[password]'
        }
        
        # SMS configuration (placeholder - use Twilio or similar)
        self.sms_config = {
            'account_sid': '[account_sid]',
            'auth_token': '[auth_token]',
            'from_number': '[phone_number]'
        }
    
    def send_email(self, to_email, subject, body, html=False):
        """Send email notification"""
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['From'] = self.email_config['sender_email']
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Add body
            if html:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))
            
            # Note: This is a simulation - real implementation needs valid credentials
            print(f"📧 Email sent to {to_email}")
            print(f"   Subject: {subject}")
            print(f"   Body: {body[:100]}...")
            
            # Log notification
            self._log_notification('email', to_email, subject, 'sent')
            
            return True
            
        except Exception as e:
            print(f"❌ Email error: {e}")
            self._log_notification('email', to_email, subject, 'failed')
            return False
    
    def send_sms(self, to_phone, message):
        """Send SMS notification"""
        try:
            # Note: This is a simulation - real implementation needs Twilio or similar
            print(f"📱 SMS sent to {to_phone}")
            print(f"   Message: {message}")
            
            # Log notification
            self._log_notification('sms', to_phone, message, 'sent')
            
            return True
            
        except Exception as e:
            print(f"❌ SMS error: {e}")
            self._log_notification('sms', to_phone, message, 'failed')
            return False
    
    def send_push_notification(self, user_id, title, body, data=None):
        """Send push notification"""
        try:
            notification = {
                'user_id': user_id,
                'title': title,
                'body': body,
                'data': data or {},
                'timestamp': datetime.now()
            }
            
            print(f"🔔 Push notification sent to {user_id}")
            print(f"   Title: {title}")
            print(f"   Body: {body}")
            
            # Log notification
            self._log_notification('push', user_id, title, 'sent')
            
            return True
            
        except Exception as e:
            print(f"❌ Push notification error: {e}")
            self._log_notification('push', user_id, title, 'failed')
            return False
    
    def send_emergency_alert(self, contacts, message, location=None):
        """Send emergency alert to multiple contacts"""
        results = []
        
        emergency_message = f"🚨 EMERGENCY ALERT\n\n{message}"
        if location:
            emergency_message += f"\n\nLocation: {location}"
        emergency_message += f"\n\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        for contact in contacts:
            # Send via multiple channels for redundancy
            if 'email' in contact:
                self.send_email(
                    contact['email'],
                    "🚨 EMERGENCY ALERT",
                    emergency_message
                )
            
            if 'phone' in contact:
                self.send_sms(
                    contact['phone'],
                    emergency_message
                )
            
            results.append(f"Alert sent to {contact.get('name', 'Unknown')}")
        
        return results
    
    def send_security_alert(self, alert_type, details):
        """Send security-related alert"""
        subject = f"🔒 Security Alert: {alert_type}"
        
        body = f"""
Security Alert Detected

Type: {alert_type}
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Details:
{details}

This is an automated security notification from AKIRA AI System.
        """
        
        print(f"\n{subject}")
        print(body)
        
        self._log_notification('security', 'system', subject, 'sent')
        return True
    
    def send_marketing_notification(self, customer_id, campaign_name, offer):
        """Send marketing notification"""
        subject = f"Special Offer: {campaign_name}"
        
        body = f"""
Hello!

We have a special offer just for you:

{offer}

This offer is personalized based on your preferences.

Thank you for being a valued customer!

Best regards,
AKIRA Marketing Team
        """
        
        print(f"📊 Marketing notification sent to {customer_id}")
        print(f"   Campaign: {campaign_name}")
        
        self._log_notification('marketing', customer_id, campaign_name, 'sent')
        return True
    
    def send_system_notification(self, user_id, notification_type, message):
        """Send system notification"""
        icons = {
            'info': 'ℹ️',
            'warning': '⚠️',
            'error': '❌',
            'success': '✅',
            'reminder': '⏰'
        }
        
        icon = icons.get(notification_type, '📢')
        
        print(f"{icon} System notification to {user_id}: {message}")
        
        self._log_notification('system', user_id, message, 'sent')
        return True
    
    def schedule_notification(self, notification_type, recipient, message, scheduled_time):
        """Schedule a notification for later"""
        scheduled = {
            'type': notification_type,
            'recipient': recipient,
            'message': message,
            'scheduled_time': scheduled_time,
            'status': 'pending'
        }
        
        self.notification_queue.append(scheduled)
        print(f"📅 Notification scheduled for {scheduled_time}")
        return True
    
    def send_daily_summary(self, user_id, summary_data):
        """Send daily summary notification"""
        subject = f"Daily Summary - {datetime.now().strftime('%B %d, %Y')}"
        
        body = f"""
Good evening!

Here's your daily summary:

📊 Activity Summary:
- Interactions: {summary_data.get('interactions', 0)}
- Tasks Completed: {summary_data.get('tasks_completed', 0)}
- Alerts: {summary_data.get('alerts', 0)}

🎯 Highlights:
{chr(10).join(f"- {h}" for h in summary_data.get('highlights', ['No highlights today']))}

💡 Recommendations:
{chr(10).join(f"- {r}" for r in summary_data.get('recommendations', ['Keep up the good work!']))}

Have a great evening!

AKIRA AI System
        """
        
        print(f"\n📊 Daily Summary for {user_id}")
        print(body)
        
        self._log_notification('summary', user_id, subject, 'sent')
        return True
    
    def send_reminder(self, user_id, reminder_text, priority='normal'):
        """Send reminder notification"""
        priority_icons = {
            'low': '📝',
            'normal': '⏰',
            'high': '🔔',
            'urgent': '🚨'
        }
        
        icon = priority_icons.get(priority, '⏰')
        
        print(f"{icon} Reminder for {user_id}: {reminder_text}")
        
        self._log_notification('reminder', user_id, reminder_text, 'sent')
        return True
    
    def set_notification_preferences(self, user_id, preferences):
        """Set user notification preferences"""
        self.preferences[user_id] = preferences
        print(f"✅ Notification preferences updated for {user_id}")
        return True
    
    def get_notification_preferences(self, user_id):
        """Get user notification preferences"""
        return self.preferences.get(user_id, {
            'email': True,
            'sms': True,
            'push': True,
            'quiet_hours': {'start': 22, 'end': 7}
        })
    
    def _log_notification(self, notification_type, recipient, content, status):
        """Log notification to history"""
        log_entry = {
            'type': notification_type,
            'recipient': recipient,
            'content': content,
            'status': status,
            'timestamp': datetime.now()
        }
        
        self.notification_history.append(log_entry)
        
        # Keep only last 1000 notifications
        if len(self.notification_history) > 1000:
            self.notification_history = self.notification_history[-1000:]
    
    def get_notification_history(self, user_id=None, limit=50):
        """Get notification history"""
        if user_id:
            history = [n for n in self.notification_history if n['recipient'] == user_id]
        else:
            history = self.notification_history
        
        return history[-limit:]
    
    def get_notification_statistics(self):
        """Get notification statistics"""
        total = len(self.notification_history)
        
        by_type = {}
        by_status = {}
        
        for notif in self.notification_history:
            notif_type = notif['type']
            status = notif['status']
            
            by_type[notif_type] = by_type.get(notif_type, 0) + 1
            by_status[status] = by_status.get(status, 0) + 1
        
        return {
            'total_notifications': total,
            'by_type': by_type,
            'by_status': by_status
        }
    
    def clear_notification_queue(self):
        """Clear pending notifications"""
        cleared = len(self.notification_queue)
        self.notification_queue = []
        print(f"✅ Cleared {cleared} pending notifications")
        return cleared
