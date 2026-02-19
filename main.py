import time
import threading
from datetime import datetime
import random
from face_recognition_module import FaceConnect
from akira_assistant import Akira
from smart_surveillance import SmartSurveillance
from personalized_marketing import PersonalizedMarketing

# Voice capabilities (will work with or without libraries installed)
try:
    import pyttsx3
    VOICE_AVAILABLE = True
except ImportError:
    VOICE_AVAILABLE = False
    print("⚠️  Voice output not available. Install pyttsx3 for speech.")

try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False
    print("⚠️  Speech recognition not available. Install SpeechRecognition for voice input.")

class PersonalAssistant:
    def __init__(self):
        self.user_name = "User"
        self.is_running = False
        self.emergency_contacts = []
        self.conversation_mode = False
        self.face_system = FaceConnect()
        self.recognized_user = None
        
        # Initialize Akira AI Assistant
        self.akira = Akira()
        
        # Initialize Smart Surveillance
        self.surveillance = SmartSurveillance()
        
        # Initialize Personalized Marketing
        self.marketing = PersonalizedMarketing()
        
        # Initialize voice engine
        if VOICE_AVAILABLE:
            self.voice_engine = pyttsx3.init()
            self.voice_engine.setProperty('rate', 150)  # Speed of speech
            self.voice_engine.setProperty('volume', 0.9)  # Volume level
        else:
            self.voice_engine = None
            
        # Initialize speech recognizer
        if SPEECH_RECOGNITION_AVAILABLE:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
        else:
            self.recognizer = None
            self.microphone = None
        
    def start(self):
        """Start the assistant system"""
        self.is_running = True
        
        # Try to recognize user
        print("🔍 Checking for registered user...")
        recognized = self.face_system.recognize_face()
        
        if recognized and recognized != "Unknown":
            self.user_name = recognized
            self.recognized_user = recognized
            message = f"Welcome back, {self.user_name}! I recognized you. How can I help you today?"
        elif recognized == "Unknown":
            message = "I don't recognize you. Please identify yourself or register your face."
            self.speak("I don't recognize you. What's your name?")
            # In a real scenario, you might want to register them here
        else:
            message = f"Hello {self.user_name}! I'm here to help you."
            
        print(f"🤖 FaceConnect Assistant activated at {datetime.now().strftime('%H:%M:%S')}")
        print(message)
        self.speak(message)
        
    def speak(self, text):
        """Convert text to speech"""
        print(f"🗣️  Assistant: {text}")
        if self.voice_engine:
            self.voice_engine.say(text)
            self.voice_engine.runAndWait()
            
    def listen(self):
        """Listen to user voice input"""
        if not self.recognizer or not self.microphone:
            print("⚠️  Voice input not available. Using text input instead.")
            return input("You: ")
            
        try:
            with self.microphone as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5)
                
            print("🔄 Processing...")
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
            
        except sr.WaitTimeoutError:
            print("⏱️  No speech detected")
            return ""
        except sr.UnknownValueError:
            print("❓ Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"❌ Error: {e}")
            return ""
            
    def start_conversation(self):
        """Start natural conversation mode"""
        self.conversation_mode = True
        greeting = "I'm listening. You can talk to me naturally. Say 'goodbye' to end our conversation."
        self.speak(greeting)
        
        while self.conversation_mode:
            user_input = self.listen()
            
            if not user_input:
                continue
                
            # Process the conversation
            response = self.process_conversation(user_input)
            self.speak(response)
            
            if "goodbye" in user_input or "bye" in user_input:
                self.conversation_mode = False
                
    def process_conversation(self, user_input):
        """Process user input and generate appropriate response"""
        user_input = user_input.lower()
        
        # Check for face registration
        if any(word in user_input for word in ["register face", "add face", "register me"]):
            name = self.user_name
            if "my name is" in user_input:
                name = user_input.split("my name is")[-1].strip()
            self.speak(f"Registering your face as {name}. Please look at the camera.")
            success = self.face_system.register_face(name)
            if success:
                return f"Successfully registered your face, {name}!"
            else:
                return "Sorry, I couldn't register your face. Please try again."
                
        # Check for face recognition
        elif any(word in user_input for word in ["who am i", "recognize me", "do you know me"]):
            self.speak("Let me look at you.")
            recognized = self.face_system.recognize_face()
            if recognized and recognized != "Unknown":
                self.recognized_user = recognized
                self.user_name = recognized
                return f"Yes! You are {recognized}. Nice to see you!"
            elif recognized == "Unknown":
                return "I don't recognize you. Would you like to register your face?"
            else:
                return "I couldn't see your face clearly. Please try again."
                
        # Check for stranger detection
        elif any(word in user_input for word in ["who is there", "stranger", "intruder", "check person"]):
            self.speak("Checking for unknown persons...")
            is_stranger = self.face_system.detect_stranger()
            if is_stranger:
                self.detect_danger(True)
                return "Warning! Unknown person detected. Sending emergency alert!"
            elif is_stranger is False:
                return f"It's just {self.recognized_user}. No strangers detected."
            else:
                return "I couldn't detect anyone."
                
        # Check for registered users list
        elif any(word in user_input for word in ["who do you know", "registered users", "known faces"]):
            users = self.face_system.get_registered_users()
            if users:
                user_list = ", ".join(users)
                return f"I know these people: {user_list}"
            else:
                return "I don't have any registered faces yet."
        
        # Check for tiredness
        elif any(word in user_input for word in ["tired", "exhausted", "sleepy", "fatigue"]):
            self.check_tiredness(8)
            return "You sound tired. Let me play some relaxing music and tell you a story."
            
        # Check for music request
        elif any(word in user_input for word in ["music", "song", "play"]):
            if "energetic" in user_input or "upbeat" in user_input:
                self.play_music("energetic")
                return "Playing energetic music for you!"
            elif "calm" in user_input or "relaxing" in user_input:
                self.play_music("relaxing")
                return "Playing calming music to help you relax."
            else:
                self.play_music("calm")
                return "Playing some nice music for you."
                
        # Check for story request
        elif any(word in user_input for word in ["story", "tale"]):
            self.tell_story()
            return "Here's a story for you."
            
        # Check for emergency keywords
        elif any(word in user_input for word in ["help", "emergency", "danger", "scared"]):
            self.detect_danger(True)
            return "Emergency detected! Sending alerts now!"
            
        # Check for greeting
        elif any(word in user_input for word in ["hello", "hi", "hey"]):
            if self.recognized_user:
                return f"Hello {self.recognized_user}! How can I help you today?"
            else:
                return f"Hello {self.user_name}! How can I help you today?"
            
        # Check for how are you
        elif "how are you" in user_input:
            return "I'm functioning perfectly and ready to assist you!"
            
        # Check for time
        elif "time" in user_input:
            current_time = datetime.now().strftime('%I:%M %p')
            return f"The current time is {current_time}."
            
        # Check for goodbye
        elif any(word in user_input for word in ["goodbye", "bye", "see you"]):
            return "Goodbye! Take care. I'll be here if you need me."
            
        # Default response
        else:
            responses = [
                "I'm here for you. Tell me more.",
                "I understand. How can I help?",
                "I'm listening. What would you like me to do?",
                "Got it. Anything else you need?"
            ]
            return random.choice(responses)
        
    def check_tiredness(self, tiredness_level):
        """Check if user is tired and respond accordingly"""
        if tiredness_level >= 7:
            message = "You seem very tired! Let me help you relax."
            print(f"\n💤 {message}")
            self.play_music("relaxing")
            self.tell_story()
        elif tiredness_level >= 5:
            message = "You're getting tired. Would you like some calming music?"
            print(f"\n😌 {message}")
            self.play_music("calm")
            
    def play_music(self, mood="relaxing"):
        """Play music based on mood"""
        music_library = {
            "relaxing": ["Ocean Waves", "Soft Piano", "Rain Sounds"],
            "calm": ["Acoustic Guitar", "Nature Sounds", "Meditation Music"],
            "energetic": ["Upbeat Pop", "Rock", "Electronic"]
        }
        
        playlist = music_library.get(mood, music_library["relaxing"])
        print(f"\n🎵 Playing {mood} music: {', '.join(playlist)}")
        
    def tell_story(self):
        """Tell a calming story"""
        stories = [
            "Once upon a time, in a peaceful forest, a gentle deer found a magical stream...",
            "Under the starlit sky, a wise owl shared tales of ancient wisdom...",
            "In a cozy cottage by the sea, an old sailor reminisced about calm waters..."
        ]
        
        import random
        story = random.choice(stories)
        print(f"\n📖 Story time: {story}")
        
    def detect_danger(self, danger_signal):
        """Detect danger and send emergency alerts"""
        if danger_signal:
            print("\n🚨 DANGER DETECTED!")
            self.send_emergency_alert()
            
    def send_emergency_alert(self):
        """Send emergency signals to contacts"""
        print("📱 Sending emergency alerts...")
        
        if not self.emergency_contacts:
            print("⚠️  No emergency contacts configured!")
            print("📞 Calling emergency services: 911")
        else:
            for contact in self.emergency_contacts:
                print(f"📞 Alerting {contact['name']}: {contact['phone']}")
                
        print("📍 Sharing current location with emergency services")
        print("🔔 Emergency alert sent successfully!")
        
    def add_emergency_contact(self, name, phone):
        """Add emergency contact"""
        self.emergency_contacts.append({"name": name, "phone": phone})
        print(f"✅ Added emergency contact: {name}")
        
    def set_user_name(self, name):
        """Set user name"""
        self.user_name = name
        print(f"✅ User name set to: {name}")
        
    def register_user_face(self, name):
        """Register a user's face"""
        print(f"📸 Registering face for {name}...")
        success = self.face_system.register_face(name)
        if success:
            self.user_name = name
            self.recognized_user = name
        return success
        
    def start_face_monitoring(self):
        """Start continuous face monitoring for security"""
        def on_face_detected(name):
            if name not in self.face_system.get_registered_users():
                print(f"⚠️  ALERT: Unknown person detected!")
                self.detect_danger(True)
            else:
                print(f"✅ Recognized: {name}")
                
        self.face_system.start_continuous_recognition(callback=on_face_detected)


def main():
    assistant = PersonalAssistant()
    
    print("\n" + "="*50)
    print("🔷 FACECONNECT - Smart Personal Assistant 🔷")
    print("="*50)
    
    print("\nWelcome! Let me help you set up.")
    
    # Setup
    name = input("What's your name? ").strip() or "Friend"
    assistant.set_user_name(name)
    
    # Ask if user wants to register face
    register = input("\nWould you like to register your face for recognition? (yes/no): ").strip().lower()
    if register in ['yes', 'y']:
        assistant.register_user_face(name)
    
    # Add emergency contacts
    print("\n📱 Setting up emergency contacts...")
    assistant.add_emergency_contact("Emergency Contact 1", "[phone_number]")
    assistant.add_emergency_contact("Emergency Contact 2", "[phone_number]")
    
    # Start the assistant
    assistant.start()
    
    print("\n" + "="*50)
    print("Choose mode:")
    print("="*50)
    print("1. Demo scenarios (automated)")
    print("2. Voice conversation mode (interactive)")
    print("3. Face monitoring mode (security)")
    print("4. Test face recognition")
    
    try:
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "2":
            print("\n🎙️  Starting voice conversation mode...")
            print("Tip: Speak clearly and wait for the beep sound")
            print("\nVoice commands you can try:")
            print("- 'Register my face' or 'Register me'")
            print("- 'Who am I?' or 'Recognize me'")
            print("- 'Who is there?' or 'Check for strangers'")
            print("- 'Who do you know?' (list registered users)")
            print("- 'I'm tired' / 'Play music' / 'Tell me a story'")
            print("- 'Help! Emergency!'")
            assistant.start_conversation()
            
        elif choice == "3":
            print("\n🎥 Starting face monitoring mode...")
            print("The system will continuously monitor for faces")
            print("Unknown faces will trigger emergency alerts")
            print("Press 'q' in the camera window to quit")
            assistant.start_face_monitoring()
            
        elif choice == "4":
            print("\n🔍 Testing face recognition...")
            recognized = assistant.face_system.recognize_face()
            if recognized:
                print(f"\n✅ Recognition result: {recognized}")
            else:
                print("\n❌ Could not recognize face")
                
        else:
            # Run demo scenarios
            print("\n--- Scenario 1: Face Recognition ---")
            print("Attempting to recognize user...")
            recognized = assistant.face_system.recognize_face()
            if recognized:
                print(f"Recognized: {recognized}")
            
            time.sleep(2)
            
            print("\n--- Scenario 2: Checking tiredness level ---")
            assistant.check_tiredness(8)
            
            time.sleep(2)
            
            print("\n--- Scenario 3: Playing energetic music ---")
            assistant.play_music("energetic")
            
            time.sleep(2)
            
            print("\n--- Scenario 4: Emergency situation ---")
            assistant.detect_danger(True)
            
            print("\n✨ Demo completed!")
            
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down FaceConnect assistant...")


if __name__ == "__main__":
    main()
