"""
Video Calling System
Video conferencing, screen sharing, recording, and chat
"""
import json
import os
from datetime import datetime
from typing import List, Dict, Optional
import uuid


class VideoCallSystem:
    """Complete video calling and conferencing system"""
    
    def __init__(self, data_file='video_calls_data.json'):
        self.data_file = data_file
        self.active_calls = []
        self.call_history = []
        self.recordings = []
        self.participants = {}
        self._load_data()
    
    def _load_data(self):
        """Load video call data from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.call_history = data.get('call_history', [])
                    self.recordings = data.get('recordings', [])
            except:
                pass
    
    def _save_data(self):
        """Save video call data to file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump({
                    'call_history': self.call_history,
                    'recordings': self.recordings
                }, f, indent=2)
        except Exception as e:
            print(f"Error saving video call data: {e}")
    
    def create_call(self, host_id: str, title: str, 
                   participants: List[str] = None,
                   scheduled_time: str = None) -> Dict:
        """Create a new video call"""
        call_id = str(uuid.uuid4())[:8]
        
        call = {
            'call_id': call_id,
            'host_id': host_id,
            'title': title,
            'participants': participants or [],
            'scheduled_time': scheduled_time,
            'status': 'scheduled' if scheduled_time else 'ready',
            'created_at': datetime.now().isoformat(),
            'room_url': f'https://akira-video.com/room/{call_id}',
            'settings': {
                'video_enabled': True,
                'audio_enabled': True,
                'screen_share_enabled': True,
                'recording_enabled': False,
                'chat_enabled': True,
                'max_participants': 50
            }
        }
        
        print(f"📹 Video call created: {title}")
        print(f"   Call ID: {call_id}")
        print(f"   Room URL: {call['room_url']}")
        
        return call
    
    def start_call(self, call_id: str, host_id: str) -> Dict:
        """Start a video call"""
        call = {
            'call_id': call_id,
            'host_id': host_id,
            'status': 'active',
            'started_at': datetime.now().isoformat(),
            'participants_count': 1,
            'duration': 0,
            'video_quality': 'HD',
            'audio_quality': 'High',
            'screen_sharing': False,
            'recording': False
        }
        
        self.active_calls.append(call)
        
        print(f"🎥 Call started: {call_id}")
        print(f"   Host: {host_id}")
        print(f"   Status: Active")
        
        return call
    
    def join_call(self, call_id: str, participant_id: str, 
                 participant_name: str) -> Dict:
        """Join an existing video call"""
        # Find active call
        call = None
        for c in self.active_calls:
            if c['call_id'] == call_id:
                call = c
                break
        
        if not call:
            return {
                'success': False,
                'message': 'Call not found or not active'
            }
        
        # Add participant
        participant = {
            'id': participant_id,
            'name': participant_name,
            'joined_at': datetime.now().isoformat(),
            'video_enabled': True,
            'audio_enabled': True,
            'screen_sharing': False
        }
        
        if call_id not in self.participants:
            self.participants[call_id] = []
        
        self.participants[call_id].append(participant)
        call['participants_count'] += 1
        
        print(f"👤 {participant_name} joined call {call_id}")
        
        return {
            'success': True,
            'call': call,
            'participant': participant
        }
    
    def leave_call(self, call_id: str, participant_id: str) -> bool:
        """Leave a video call"""
        if call_id in self.participants:
            self.participants[call_id] = [
                p for p in self.participants[call_id] 
                if p['id'] != participant_id
            ]
            
            # Update participant count
            for call in self.active_calls:
                if call['call_id'] == call_id:
                    call['participants_count'] -= 1
                    break
            
            print(f"👋 Participant {participant_id} left call {call_id}")
            return True
        
        return False
    
    def end_call(self, call_id: str, host_id: str) -> Dict:
        """End a video call"""
        call = None
        for c in self.active_calls:
            if c['call_id'] == call_id and c['host_id'] == host_id:
                call = c
                break
        
        if not call:
            return {
                'success': False,
                'message': 'Call not found or unauthorized'
            }
        
        # Calculate duration
        started_at = datetime.fromisoformat(call['started_at'])
        ended_at = datetime.now()
        duration = int((ended_at - started_at).total_seconds() / 60)
        
        # Create call history entry
        history_entry = {
            'call_id': call_id,
            'host_id': host_id,
            'started_at': call['started_at'],
            'ended_at': ended_at.isoformat(),
            'duration_minutes': duration,
            'participants_count': call['participants_count'],
            'recording_available': call.get('recording', False)
        }
        
        self.call_history.append(history_entry)
        self.active_calls.remove(call)
        
        # Clear participants
        if call_id in self.participants:
            del self.participants[call_id]
        
        self._save_data()
        
        print(f"🛑 Call ended: {call_id}")
        print(f"   Duration: {duration} minutes")
        print(f"   Participants: {call['participants_count']}")
        
        return {
            'success': True,
            'duration': duration,
            'participants': call['participants_count']
        }
    
    def toggle_video(self, call_id: str, participant_id: str) -> bool:
        """Toggle video on/off"""
        if call_id in self.participants:
            for p in self.participants[call_id]:
                if p['id'] == participant_id:
                    p['video_enabled'] = not p['video_enabled']
                    status = "enabled" if p['video_enabled'] else "disabled"
                    print(f"📹 Video {status} for {p['name']}")
                    return p['video_enabled']
        return False
    
    def toggle_audio(self, call_id: str, participant_id: str) -> bool:
        """Toggle audio on/off"""
        if call_id in self.participants:
            for p in self.participants[call_id]:
                if p['id'] == participant_id:
                    p['audio_enabled'] = not p['audio_enabled']
                    status = "enabled" if p['audio_enabled'] else "disabled"
                    print(f"🎤 Audio {status} for {p['name']}")
                    return p['audio_enabled']
        return False
    
    def start_screen_share(self, call_id: str, participant_id: str) -> bool:
        """Start screen sharing"""
        if call_id in self.participants:
            for p in self.participants[call_id]:
                if p['id'] == participant_id:
                    p['screen_sharing'] = True
                    print(f"🖥️ {p['name']} started screen sharing")
                    return True
        return False
    
    def stop_screen_share(self, call_id: str, participant_id: str) -> bool:
        """Stop screen sharing"""
        if call_id in self.participants:
            for p in self.participants[call_id]:
                if p['id'] == participant_id:
                    p['screen_sharing'] = False
                    print(f"🖥️ {p['name']} stopped screen sharing")
                    return True
        return False
    
    def start_recording(self, call_id: str, host_id: str) -> Dict:
        """Start recording the call"""
        for call in self.active_calls:
            if call['call_id'] == call_id and call['host_id'] == host_id:
                call['recording'] = True
                
                recording = {
                    'recording_id': str(uuid.uuid4())[:8],
                    'call_id': call_id,
                    'started_at': datetime.now().isoformat(),
                    'status': 'recording',
                    'file_size': 0
                }
                
                print(f"🔴 Recording started for call {call_id}")
                
                return recording
        
        return {'success': False, 'message': 'Call not found or unauthorized'}
    
    def stop_recording(self, call_id: str, recording_id: str) -> Dict:
        """Stop recording the call"""
        for call in self.active_calls:
            if call['call_id'] == call_id:
                call['recording'] = False
                
                recording = {
                    'recording_id': recording_id,
                    'call_id': call_id,
                    'stopped_at': datetime.now().isoformat(),
                    'status': 'completed',
                    'file_size': 125.5,  # MB (simulated)
                    'duration': 45,  # minutes (simulated)
                    'download_url': f'https://akira-video.com/recordings/{recording_id}.mp4'
                }
                
                self.recordings.append(recording)
                self._save_data()
                
                print(f"⏹️ Recording stopped for call {call_id}")
                print(f"   File size: {recording['file_size']} MB")
                
                return recording
        
        return {'success': False, 'message': 'Call not found'}
    
    def send_chat_message(self, call_id: str, sender_id: str, 
                         sender_name: str, message: str) -> Dict:
        """Send chat message during call"""
        chat_message = {
            'message_id': str(uuid.uuid4())[:8],
            'call_id': call_id,
            'sender_id': sender_id,
            'sender_name': sender_name,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"💬 {sender_name}: {message}")
        
        return chat_message
    
    def get_active_calls(self) -> List[Dict]:
        """Get all active calls"""
        return self.active_calls
    
    def get_call_participants(self, call_id: str) -> List[Dict]:
        """Get participants in a call"""
        return self.participants.get(call_id, [])
    
    def get_call_history(self, user_id: str = None, limit: int = 50) -> List[Dict]:
        """Get call history"""
        if user_id:
            history = [c for c in self.call_history if c['host_id'] == user_id]
        else:
            history = self.call_history
        
        return history[-limit:]
    
    def get_recordings(self, call_id: str = None) -> List[Dict]:
        """Get call recordings"""
        if call_id:
            return [r for r in self.recordings if r['call_id'] == call_id]
        return self.recordings
    
    def get_statistics(self) -> Dict:
        """Get video call statistics"""
        total_calls = len(self.call_history)
        active_calls = len(self.active_calls)
        total_recordings = len(self.recordings)
        
        total_duration = sum(c.get('duration_minutes', 0) for c in self.call_history)
        total_participants = sum(c.get('participants_count', 0) for c in self.call_history)
        
        avg_duration = total_duration / total_calls if total_calls > 0 else 0
        avg_participants = total_participants / total_calls if total_calls > 0 else 0
        
        return {
            'total_calls': total_calls,
            'active_calls': active_calls,
            'total_recordings': total_recordings,
            'total_duration_minutes': total_duration,
            'average_duration_minutes': round(avg_duration, 1),
            'average_participants': round(avg_participants, 1)
        }


# Global instance
video_call_system = VideoCallSystem()


if __name__ == '__main__':
    print("="*60)
    print("📹 Video Calling System - Test")
    print("="*60)
    
    # Create call
    call = video_call_system.create_call(
        host_id='user123',
        title='Team Meeting',
        participants=['john@example.com', 'sarah@example.com']
    )
    print(f"\n✅ Call created: {call['call_id']}")
    
    # Start call
    active_call = video_call_system.start_call(call['call_id'], 'user123')
    print(f"✅ Call started")
    
    # Join call
    result = video_call_system.join_call(call['call_id'], 'user456', 'John Doe')
    print(f"✅ Participant joined: {result['success']}")
    
    # Toggle video
    video_call_system.toggle_video(call['call_id'], 'user456')
    
    # Start screen share
    video_call_system.start_screen_share(call['call_id'], 'user456')
    
    # Send chat message
    video_call_system.send_chat_message(
        call['call_id'], 'user456', 'John Doe', 'Hello everyone!'
    )
    
    # Get statistics
    stats = video_call_system.get_statistics()
    print(f"\n📊 Statistics:")
    print(f"   Active calls: {stats['active_calls']}")
    print(f"   Total calls: {stats['total_calls']}")
    
    print("\n✅ Video call system tested!")
