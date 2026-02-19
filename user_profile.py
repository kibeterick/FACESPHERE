"""
User Profile System - Stores and manages user information
Allows Akira to remember and personalize conversations
"""
import json
import os
from datetime import datetime


class UserProfile:
    """Manages user profiles and preferences"""
    
    def __init__(self, profile_file='user_profiles.json'):
        self.profile_file = profile_file
        self.profiles = self._load_profiles()
    
    def _load_profiles(self):
        """Load user profiles from file"""
        if os.path.exists(self.profile_file):
            try:
                with open(self.profile_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save_profiles(self):
        """Save user profiles to file"""
        try:
            with open(self.profile_file, 'w') as f:
                json.dump(self.profiles, f, indent=2)
        except Exception as e:
            print(f"Error saving profiles: {e}")
    
    def create_profile(self, user_name):
        """Create a new user profile"""
        if user_name not in self.profiles:
            self.profiles[user_name] = {
                'name': user_name,
                'created_at': datetime.now().isoformat(),
                'last_seen': datetime.now().isoformat(),
                'preferences': {
                    'favorite_music': None,
                    'usual_wake_time': None,
                    'usual_sleep_time': None,
                    'preferred_temperature': 72
                },
                'interactions': {
                    'total_conversations': 0,
                    'music_played': 0,
                    'emergencies_triggered': 0,
                    'person_detections': 0
                },
                'favorites': {
                    'songs': [],
                    'activities': []
                },
                'notes': [],
                'mood_history': [],
                'last_activities': []
            }
            self._save_profiles()
        return self.profiles[user_name]
    
    def get_profile(self, user_name):
        """Get user profile"""
        if user_name not in self.profiles:
            return self.create_profile(user_name)
        
        # Update last seen
        self.profiles[user_name]['last_seen'] = datetime.now().isoformat()
        self._save_profiles()
        
        return self.profiles[user_name]
    
    def update_preference(self, user_name, key, value):
        """Update user preference"""
        profile = self.get_profile(user_name)
        profile['preferences'][key] = value
        self._save_profiles()
    
    def add_interaction(self, user_name, interaction_type):
        """Record an interaction"""
        profile = self.get_profile(user_name)
        profile['interactions']['total_conversations'] += 1
        
        if interaction_type in profile['interactions']:
            profile['interactions'][interaction_type] += 1
        
        self._save_profiles()
    
    def add_note(self, user_name, note):
        """Add a note about the user"""
        profile = self.get_profile(user_name)
        profile['notes'].append({
            'note': note,
            'timestamp': datetime.now().isoformat()
        })
        self._save_profiles()
    
    def add_mood(self, user_name, mood):
        """Record user's mood"""
        profile = self.get_profile(user_name)
        profile['mood_history'].append({
            'mood': mood,
            'timestamp': datetime.now().isoformat()
        })
        # Keep only last 10 moods
        profile['mood_history'] = profile['mood_history'][-10:]
        self._save_profiles()
    
    def add_activity(self, user_name, activity):
        """Record user activity"""
        profile = self.get_profile(user_name)
        profile['last_activities'].append({
            'activity': activity,
            'timestamp': datetime.now().isoformat()
        })
        # Keep only last 20 activities
        profile['last_activities'] = profile['last_activities'][-20:]
        self._save_profiles()
    
    def get_personalized_greeting(self, user_name):
        """Generate personalized greeting based on user profile"""
        profile = self.get_profile(user_name)
        
        hour = datetime.now().hour
        if hour < 12:
            time_greeting = "Good morning"
        elif hour < 18:
            time_greeting = "Good afternoon"
        else:
            time_greeting = "Good evening"
        
        # Build personalized message
        messages = [f"{time_greeting}, {user_name}!"]
        
        # Add interaction count
        total = profile['interactions']['total_conversations']
        if total == 0:
            messages.append("It's great to meet you for the first time!")
        elif total < 5:
            messages.append(f"Nice to see you again! This is our conversation number {total + 1}.")
        else:
            messages.append(f"Welcome back! We've had {total} great conversations together.")
        
        # Add favorite music if known
        fav_music = profile['preferences'].get('favorite_music')
        if fav_music:
            messages.append(f"I remember you love {fav_music} music.")
        
        # Add recent mood
        if profile['mood_history']:
            last_mood = profile['mood_history'][-1]['mood']
            messages.append(f"Last time you were feeling {last_mood}.")
        
        # Add recent activity
        if profile['last_activities']:
            last_activity = profile['last_activities'][-1]['activity']
            messages.append(f"Last time we {last_activity}.")
        
        # Add notes
        if profile['notes']:
            latest_note = profile['notes'][-1]['note']
            messages.append(f"I remember: {latest_note}")
        
        return " ".join(messages)
    
    def get_user_summary(self, user_name):
        """Get summary of what we know about the user"""
        profile = self.get_profile(user_name)
        
        summary = {
            'name': user_name,
            'member_since': profile['created_at'],
            'total_conversations': profile['interactions']['total_conversations'],
            'favorite_music': profile['preferences'].get('favorite_music', 'Not set'),
            'music_played': profile['interactions'].get('music_played', 0),
            'recent_moods': [m['mood'] for m in profile['mood_history'][-3:]],
            'recent_activities': [a['activity'] for a in profile['last_activities'][-3:]],
            'notes_count': len(profile['notes']),
            'last_seen': profile['last_seen']
        }
        
        return summary


# Global instance
user_profile_manager = UserProfile()


if __name__ == '__main__':
    # Test the profile system
    print("="*60)
    print("User Profile System - Test")
    print("="*60)
    
    # Create profile
    profile = user_profile_manager.create_profile("Erick Too")
    print(f"\n✅ Profile created for: {profile['name']}")
    
    # Add some data
    user_profile_manager.update_preference("Erick Too", "favorite_music", "relaxing")
    user_profile_manager.add_note("Erick Too", "Loves technology and AI systems")
    user_profile_manager.add_mood("Erick Too", "excited")
    user_profile_manager.add_activity("Erick Too", "played relaxing music")
    user_profile_manager.add_interaction("Erick Too", "music_played")
    
    # Get personalized greeting
    greeting = user_profile_manager.get_personalized_greeting("Erick Too")
    print(f"\n🗣️ Personalized Greeting:\n{greeting}")
    
    # Get summary
    summary = user_profile_manager.get_user_summary("Erick Too")
    print(f"\n📊 User Summary:")
    for key, value in summary.items():
        print(f"   {key}: {value}")
