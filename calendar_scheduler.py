"""
Calendar & Scheduling System
Meeting scheduler, appointments, reminders, and event notifications
"""
import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class CalendarScheduler:
    """Complete calendar and scheduling system"""
    
    def __init__(self, data_file='calendar_data.json'):
        self.data_file = data_file
        self.events = []
        self.meetings = []
        self.appointments = []
        self.reminders = []
        self._load_data()
    
    def _load_data(self):
        """Load calendar data from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.events = data.get('events', [])
                    self.meetings = data.get('meetings', [])
                    self.appointments = data.get('appointments', [])
                    self.reminders = data.get('reminders', [])
            except:
                pass
    
    def _save_data(self):
        """Save calendar data to file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump({
                    'events': self.events,
                    'meetings': self.meetings,
                    'appointments': self.appointments,
                    'reminders': self.reminders
                }, f, indent=2)
        except Exception as e:
            print(f"Error saving calendar data: {e}")
    
    def schedule_meeting(self, title: str, date: str, time: str, 
                        duration: int, attendees: List[str], 
                        location: str = "", notes: str = "") -> Dict:
        """Schedule a new meeting"""
        meeting = {
            'id': len(self.meetings) + 1,
            'type': 'meeting',
            'title': title,
            'date': date,
            'time': time,
            'duration': duration,  # in minutes
            'attendees': attendees,
            'location': location,
            'notes': notes,
            'status': 'scheduled',
            'created_at': datetime.now().isoformat(),
            'reminders_sent': False
        }
        
        self.meetings.append(meeting)
        self._save_data()
        
        # Create automatic reminder 15 minutes before
        self.create_reminder(
            f"Meeting: {title}",
            f"{date} {time}",
            15  # minutes before
        )
        
        return meeting
    
    def schedule_appointment(self, title: str, date: str, time: str,
                           duration: int, with_person: str = "",
                           location: str = "", notes: str = "") -> Dict:
        """Schedule a new appointment"""
        appointment = {
            'id': len(self.appointments) + 1,
            'type': 'appointment',
            'title': title,
            'date': date,
            'time': time,
            'duration': duration,
            'with': with_person,
            'location': location,
            'notes': notes,
            'status': 'scheduled',
            'created_at': datetime.now().isoformat(),
            'reminders_sent': False
        }
        
        self.appointments.append(appointment)
        self._save_data()
        
        # Create automatic reminder
        self.create_reminder(
            f"Appointment: {title}",
            f"{date} {time}",
            30  # minutes before
        )
        
        return appointment
    
    def create_event(self, title: str, date: str, time: str = "",
                    all_day: bool = False, location: str = "",
                    description: str = "", category: str = "general") -> Dict:
        """Create a new event"""
        event = {
            'id': len(self.events) + 1,
            'type': 'event',
            'title': title,
            'date': date,
            'time': time if not all_day else "All Day",
            'all_day': all_day,
            'location': location,
            'description': description,
            'category': category,
            'status': 'active',
            'created_at': datetime.now().isoformat()
        }
        
        self.events.append(event)
        self._save_data()
        
        return event
    
    def create_reminder(self, title: str, datetime_str: str, 
                       minutes_before: int = 15) -> Dict:
        """Create a reminder"""
        reminder = {
            'id': len(self.reminders) + 1,
            'title': title,
            'datetime': datetime_str,
            'minutes_before': minutes_before,
            'status': 'pending',
            'sent': False,
            'created_at': datetime.now().isoformat()
        }
        
        self.reminders.append(reminder)
        self._save_data()
        
        return reminder
    
    def get_today_schedule(self) -> Dict:
        """Get today's schedule"""
        today = datetime.now().strftime('%Y-%m-%d')
        
        today_meetings = [m for m in self.meetings if m['date'] == today and m['status'] != 'cancelled']
        today_appointments = [a for a in self.appointments if a['date'] == today and a['status'] != 'cancelled']
        today_events = [e for e in self.events if e['date'] == today and e['status'] == 'active']
        
        return {
            'date': today,
            'meetings': sorted(today_meetings, key=lambda x: x['time']),
            'appointments': sorted(today_appointments, key=lambda x: x['time']),
            'events': sorted(today_events, key=lambda x: x.get('time', '')),
            'total_items': len(today_meetings) + len(today_appointments) + len(today_events)
        }
    
    def get_week_schedule(self) -> List[Dict]:
        """Get this week's schedule"""
        today = datetime.now()
        week_schedule = []
        
        for i in range(7):
            date = (today + timedelta(days=i)).strftime('%Y-%m-%d')
            day_meetings = [m for m in self.meetings if m['date'] == date and m['status'] != 'cancelled']
            day_appointments = [a for a in self.appointments if a['date'] == date and a['status'] != 'cancelled']
            day_events = [e for e in self.events if e['date'] == date and e['status'] == 'active']
            
            week_schedule.append({
                'date': date,
                'day_name': (today + timedelta(days=i)).strftime('%A'),
                'meetings': len(day_meetings),
                'appointments': len(day_appointments),
                'events': len(day_events),
                'total': len(day_meetings) + len(day_appointments) + len(day_events)
            })
        
        return week_schedule
    
    def get_upcoming_reminders(self, hours: int = 24) -> List[Dict]:
        """Get upcoming reminders"""
        now = datetime.now()
        upcoming = []
        
        for reminder in self.reminders:
            if reminder['status'] == 'pending' and not reminder['sent']:
                # Parse reminder datetime
                try:
                    reminder_time = datetime.strptime(reminder['datetime'], '%Y-%m-%d %H:%M')
                    reminder_time -= timedelta(minutes=reminder['minutes_before'])
                    
                    if now <= reminder_time <= now + timedelta(hours=hours):
                        upcoming.append(reminder)
                except:
                    pass
        
        return upcoming
    
    def cancel_meeting(self, meeting_id: int) -> bool:
        """Cancel a meeting"""
        for meeting in self.meetings:
            if meeting['id'] == meeting_id:
                meeting['status'] = 'cancelled'
                self._save_data()
                return True
        return False
    
    def reschedule_meeting(self, meeting_id: int, new_date: str, new_time: str) -> bool:
        """Reschedule a meeting"""
        for meeting in self.meetings:
            if meeting['id'] == meeting_id:
                meeting['date'] = new_date
                meeting['time'] = new_time
                meeting['status'] = 'rescheduled'
                self._save_data()
                return True
        return False
    
    def search_schedule(self, query: str) -> Dict:
        """Search in schedule"""
        query_lower = query.lower()
        results = {
            'meetings': [],
            'appointments': [],
            'events': []
        }
        
        for meeting in self.meetings:
            if (query_lower in meeting['title'].lower() or 
                query_lower in meeting.get('notes', '').lower()):
                results['meetings'].append(meeting)
        
        for appointment in self.appointments:
            if (query_lower in appointment['title'].lower() or 
                query_lower in appointment.get('notes', '').lower()):
                results['appointments'].append(appointment)
        
        for event in self.events:
            if (query_lower in event['title'].lower() or 
                query_lower in event.get('description', '').lower()):
                results['events'].append(event)
        
        return results
    
    def get_statistics(self) -> Dict:
        """Get calendar statistics"""
        total_meetings = len([m for m in self.meetings if m['status'] != 'cancelled'])
        total_appointments = len([a for a in self.appointments if a['status'] != 'cancelled'])
        total_events = len([e for e in self.events if e['status'] == 'active'])
        
        return {
            'total_meetings': total_meetings,
            'total_appointments': total_appointments,
            'total_events': total_events,
            'total_reminders': len(self.reminders),
            'pending_reminders': len([r for r in self.reminders if r['status'] == 'pending']),
            'today_items': self.get_today_schedule()['total_items']
        }


# Global instance
calendar = CalendarScheduler()


if __name__ == '__main__':
    print("="*60)
    print("📅 Calendar & Scheduling System - Test")
    print("="*60)
    
    # Test meeting
    meeting = calendar.schedule_meeting(
        title="Team Standup",
        date="2026-02-20",
        time="09:00",
        duration=30,
        attendees=["John", "Sarah", "Mike"],
        location="Conference Room A",
        notes="Discuss project progress"
    )
    print(f"\n✅ Meeting scheduled: {meeting['title']}")
    
    # Test appointment
    appointment = calendar.schedule_appointment(
        title="Doctor Appointment",
        date="2026-02-21",
        time="14:00",
        duration=60,
        with_person="Dr. Smith",
        location="Medical Center"
    )
    print(f"✅ Appointment scheduled: {appointment['title']}")
    
    # Test event
    event = calendar.create_event(
        title="Company Anniversary",
        date="2026-02-25",
        all_day=True,
        category="celebration"
    )
    print(f"✅ Event created: {event['title']}")
    
    # Get today's schedule
    today = calendar.get_today_schedule()
    print(f"\n📅 Today's Schedule: {today['total_items']} items")
    
    # Get statistics
    stats = calendar.get_statistics()
    print(f"\n📊 Statistics:")
    print(f"   Meetings: {stats['total_meetings']}")
    print(f"   Appointments: {stats['total_appointments']}")
    print(f"   Events: {stats['total_events']}")
    print(f"   Reminders: {stats['total_reminders']}")
    
    print("\n✅ Calendar system tested!")
