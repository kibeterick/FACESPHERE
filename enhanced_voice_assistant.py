"""
Enhanced Voice Assistant with Wake Word Detection and Multi-language Support
"""
import random
from datetime import datetime


class EnhancedVoiceAssistant:
    """Advanced voice assistant with wake word and multi-language"""
    
    def __init__(self):
        self.wake_words = ['akira', 'hey akira', 'ok akira']
        self.is_listening = False
        self.current_language = 'en'
        self.conversation_context = []
        self.voice_profiles = {}
        
        # Multi-language responses
        self.responses = {
            'en': {
                'greeting': "Hello! How can I help you?",
                'goodbye': "Goodbye! Have a great day!",
                'understood': "I understand. Let me help with that.",
                'error': "Sorry, I didn't catch that. Could you repeat?"
            },
            'es': {
                'greeting': "¡Hola! ¿Cómo puedo ayudarte?",
                'goodbye': "¡Adiós! ¡Que tengas un gran día!",
                'understood': "Entiendo. Déjame ayudarte con eso.",
                'error': "Lo siento, no entendí. ¿Puedes repetir?"
            },
            'fr': {
                'greeting': "Bonjour! Comment puis-je vous aider?",
                'goodbye': "Au revoir! Passez une excellente journée!",
                'understood': "Je comprends. Laissez-moi vous aider.",
                'error': "Désolé, je n'ai pas compris. Pouvez-vous répéter?"
            }
        }
    
    def detect_wake_word(self, audio_text):
        """Detect wake word in audio"""
        audio_lower = audio_text.lower()
        
        for wake_word in self.wake_words:
            if wake_word in audio_lower:
                self.is_listening = True
                return True
        
        return False
    
    def process_voice_command(self, command, user_id=None):
        """Process voice command with context awareness"""
        command_lower = command.lower()
        
        # Check for wake word
        if not self.is_listening:
            if self.detect_wake_word(command):
                return self.get_response('greeting')
            return None
        
        # Add to conversation context
        self.conversation_context.append({
            'command': command,
            'timestamp': datetime.now(),
            'user_id': user_id
        })
        
        # Keep only last 10 interactions for context
        if len(self.conversation_context) > 10:
            self.conversation_context = self.conversation_context[-10:]
        
        # Process command
        response = self._process_command_with_context(command_lower)
        
        # Check for goodbye
        if any(word in command_lower for word in ['goodbye', 'bye', 'see you']):
            self.is_listening = False
        
        return response
    
    def _process_command_with_context(self, command):
        """Process command with conversation context"""
        # Smart home controls
        if 'turn on' in command or 'turn off' in command:
            return self._handle_smart_home_command(command)
        
        # Information queries
        elif any(word in command for word in ['what', 'when', 'where', 'who', 'how']):
            return self._handle_information_query(command)
        
        # Task management
        elif any(word in command for word in ['remind', 'schedule', 'add task']):
            return self._handle_task_command(command)
        
        # Entertainment
        elif any(word in command for word in ['play', 'music', 'video']):
            return self._handle_entertainment_command(command)
        
        # Context-based responses
        elif self._has_context():
            return self._handle_contextual_command(command)
        
        else:
            return self.get_response('understood')
    
    def _handle_smart_home_command(self, command):
        """Handle smart home control commands"""
        if 'light' in command:
            action = 'on' if 'turn on' in command else 'off'
            return f"Turning {action} the lights"
        elif 'temperature' in command or 'thermostat' in command:
            return "Adjusting the temperature"
        elif 'lock' in command:
            return "Locking the door"
        else:
            return "Controlling smart home device"
    
    def _handle_information_query(self, command):
        """Handle information queries"""
        if 'weather' in command:
            return "The weather is pleasant today, around 72°F with clear skies"
        elif 'time' in command:
            return f"The time is {datetime.now().strftime('%I:%M %p')}"
        elif 'date' in command:
            return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}"
        else:
            return "Let me look that up for you"
    
    def _handle_task_command(self, command):
        """Handle task management commands"""
        if 'remind' in command:
            return "I'll remind you about that"
        elif 'schedule' in command:
            return "I've added that to your schedule"
        else:
            return "Task added to your list"
    
    def _handle_entertainment_command(self, command):
        """Handle entertainment commands"""
        if 'music' in command:
            return "Playing your favorite music"
        elif 'video' in command:
            return "Starting video playback"
        else:
            return "Starting entertainment"
    
    def _has_context(self):
        """Check if there's conversation context"""
        return len(self.conversation_context) > 0
    
    def _handle_contextual_command(self, command):
        """Handle commands based on conversation context"""
        # Get last interaction
        last_interaction = self.conversation_context[-1]
        
        # Handle follow-up questions
        if any(word in command for word in ['yes', 'yeah', 'sure', 'okay']):
            return "Great! I'll proceed with that"
        elif any(word in command for word in ['no', 'nope', 'cancel']):
            return "Okay, I won't do that"
        else:
            return "Based on our conversation, let me help with that"
    
    def get_response(self, response_type):
        """Get response in current language"""
        lang_responses = self.responses.get(self.current_language, self.responses['en'])
        return lang_responses.get(response_type, "I'm here to help")
    
    def set_language(self, language_code):
        """Set assistant language"""
        if language_code in self.responses:
            self.current_language = language_code
            return f"Language set to {language_code}"
        return "Language not supported"
    
    def register_voice_profile(self, user_id, voice_characteristics):
        """Register user voice profile for speaker recognition"""
        self.voice_profiles[user_id] = {
            'characteristics': voice_characteristics,
            'registered_at': datetime.now()
        }
        return f"Voice profile registered for {user_id}"
    
    def identify_speaker(self, voice_sample):
        """Identify speaker from voice sample"""
        # Placeholder for voice recognition
        # In production, use speaker recognition ML model
        if self.voice_profiles:
            return list(self.voice_profiles.keys())[0]
        return "Unknown"
    
    def natural_language_understanding(self, text):
        """Advanced NLU for intent and entity extraction"""
        intent = self._extract_intent(text)
        entities = self._extract_entities(text)
        
        return {
            'intent': intent,
            'entities': entities,
            'confidence': 0.85
        }
    
    def _extract_intent(self, text):
        """Extract intent from text"""
        text_lower = text.lower()
        
        intents = {
            'control_device': ['turn on', 'turn off', 'set', 'adjust'],
            'query_info': ['what', 'when', 'where', 'who', 'how'],
            'task_management': ['remind', 'schedule', 'add', 'create'],
            'entertainment': ['play', 'show', 'watch'],
            'greeting': ['hello', 'hi', 'hey'],
            'goodbye': ['bye', 'goodbye', 'see you']
        }
        
        for intent, keywords in intents.items():
            if any(keyword in text_lower for keyword in keywords):
                return intent
        
        return 'unknown'
    
    def _extract_entities(self, text):
        """Extract entities from text"""
        entities = {}
        
        # Extract time
        if 'tomorrow' in text.lower():
            entities['time'] = 'tomorrow'
        elif 'today' in text.lower():
            entities['time'] = 'today'
        
        # Extract devices
        devices = ['light', 'thermostat', 'lock', 'camera', 'speaker']
        for device in devices:
            if device in text.lower():
                entities['device'] = device
        
        # Extract numbers
        import re
        numbers = re.findall(r'\d+', text)
        if numbers:
            entities['number'] = numbers[0]
        
        return entities
    
    def generate_smart_response(self, user_input, user_context):
        """Generate contextually appropriate response"""
        # Analyze user context
        time_of_day = datetime.now().hour
        user_mood = user_context.get('mood', 'neutral')
        
        # Adjust response based on context
        if time_of_day < 12:
            greeting = "Good morning"
        elif time_of_day < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        
        # Adjust tone based on mood
        if user_mood == 'tired':
            tone = "gentle"
            response = f"{greeting}. You sound tired. How can I help you relax?"
        elif user_mood == 'energetic':
            tone = "enthusiastic"
            response = f"{greeting}! You're full of energy! What can I do for you?"
        else:
            tone = "friendly"
            response = f"{greeting}! How can I assist you?"
        
        return response
    
    def continuous_learning(self, user_feedback):
        """Learn from user feedback"""
        # Store feedback for model improvement
        feedback_entry = {
            'feedback': user_feedback,
            'timestamp': datetime.now(),
            'context': self.conversation_context[-1] if self.conversation_context else None
        }
        
        # In production, use this to retrain models
        return "Thank you for your feedback! I'm learning to serve you better."
    
    def get_conversation_summary(self):
        """Get summary of conversation"""
        if not self.conversation_context:
            return "No conversation history"
        
        total_interactions = len(self.conversation_context)
        first_interaction = self.conversation_context[0]['timestamp']
        last_interaction = self.conversation_context[-1]['timestamp']
        
        return {
            'total_interactions': total_interactions,
            'duration': str(last_interaction - first_interaction),
            'first_command': self.conversation_context[0]['command'],
            'last_command': self.conversation_context[-1]['command']
        }
