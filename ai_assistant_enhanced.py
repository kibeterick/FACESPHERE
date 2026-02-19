"""
Enhanced Akira AI Assistant with Google Gemini Integration
Provides intelligent, context-aware responses using real AI
"""
import os
import random
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Try to import Google Gemini
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("⚠️  Google Gemini not available. Install: pip install google-generativeai")

# Try to import OpenAI (fallback)
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# NLP capabilities
try:
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    NLP_AVAILABLE = True
except ImportError:
    NLP_AVAILABLE = False


class EnhancedAkira:
    """Enhanced Akira - AI-Powered Virtual Assistant"""
    
    def __init__(self):
        self.name = "Akira"
        self.user_preferences = {}
        self.conversation_history = []
        self.tasks = []
        self.ai_enabled = False
        
        # Initialize AI APIs
        self._initialize_ai()
        
        # Initialize NLP
        if NLP_AVAILABLE:
            try:
                self.stop_words = set(stopwords.words('english'))
            except:
                nltk.download('punkt', quiet=True)
                nltk.download('stopwords', quiet=True)
                self.stop_words = set(stopwords.words('english'))
    
    def _initialize_ai(self):
        """Initialize AI APIs (Gemini, OpenAI)"""
        # Try Gemini first
        gemini_key = os.getenv('GEMINI_API_KEY')
        if GEMINI_AVAILABLE and gemini_key and gemini_key != 'your_gemini_api_key_here':
            try:
                genai.configure(api_key=gemini_key)
                self.gemini_model = genai.GenerativeModel('gemini-pro')
                self.ai_enabled = True
                self.ai_provider = 'gemini'
                print("✅ Google Gemini AI enabled")
                return
            except Exception as e:
                print(f"⚠️  Gemini initialization failed: {e}")
        
        # Try OpenAI as fallback
        openai_key = os.getenv('OPENAI_API_KEY')
        if OPENAI_AVAILABLE and openai_key and openai_key != 'your_openai_api_key_here':
            try:
                openai.api_key = openai_key
                self.ai_enabled = True
                self.ai_provider = 'openai'
                print("✅ OpenAI enabled")
                return
            except Exception as e:
                print(f"⚠️  OpenAI initialization failed: {e}")
        
        print("ℹ️  AI APIs not configured. Using rule-based responses.")
        print("   Add GEMINI_API_KEY to .env file to enable AI responses.")
    
    def greet_user(self, user_name):
        """Personalized greeting"""
        hour = datetime.now().hour
        
        if hour < 12:
            greeting = f"Good morning, {user_name}!"
        elif hour < 18:
            greeting = f"Good afternoon, {user_name}!"
        else:
            greeting = f"Good evening, {user_name}!"
            
        return f"{greeting} I'm Akira, your AI-powered assistant. How can I help you today?"
    
    def process_command(self, command, user_name="User"):
        """Process command with AI or rule-based logic"""
        # Add to conversation history
        self.conversation_history.append({
            'role': 'user',
            'content': command,
            'timestamp': datetime.now()
        })
        
        # Try AI response first
        if self.ai_enabled:
            response = self._get_ai_response(command, user_name)
            if response:
                self.conversation_history.append({
                    'role': 'assistant',
                    'content': response,
                    'timestamp': datetime.now()
                })
                return response
        
        # Fallback to rule-based responses
        response = self._get_rule_based_response(command)
        self.conversation_history.append({
            'role': 'assistant',
            'content': response,
            'timestamp': datetime.now()
        })
        return response
    
    def _get_ai_response(self, command, user_name):
        """Get response from AI (Gemini or OpenAI)"""
        try:
            if self.ai_provider == 'gemini':
                return self._get_gemini_response(command, user_name)
            elif self.ai_provider == 'openai':
                return self._get_openai_response(command, user_name)
        except Exception as e:
            print(f"⚠️  AI response failed: {e}")
            return None
    
    def _get_gemini_response(self, command, user_name):
        """Get response from Google Gemini"""
        # Build context-aware prompt
        system_context = f"""You are Akira, an intelligent AI assistant helping {user_name}. 
You are part of a smart home system with IoT capabilities, task management, and information services.
Be helpful, concise, and friendly. Keep responses under 150 words unless asked for details.
Current time: {datetime.now().strftime('%I:%M %p, %A, %B %d, %Y')}"""
        
        # Include recent conversation history for context
        context = system_context
        if len(self.conversation_history) > 0:
            recent = self.conversation_history[-4:]  # Last 2 exchanges
            for msg in recent:
                if msg['role'] == 'user':
                    context += f"\nUser: {msg['content']}"
                else:
                    context += f"\nAkira: {msg['content']}"
        
        context += f"\nUser: {command}\nAkira:"
        
        # Generate response
        response = self.gemini_model.generate_content(context)
        return response.text.strip()
    
    def _get_openai_response(self, command, user_name):
        """Get response from OpenAI"""
        messages = [
            {
                "role": "system",
                "content": f"""You are Akira, an intelligent AI assistant helping {user_name}. 
You are part of a smart home system with IoT capabilities, task management, and information services.
Be helpful, concise, and friendly. Keep responses under 150 words unless asked for details.
Current time: {datetime.now().strftime('%I:%M %p, %A, %B %d, %Y')}"""
            }
        ]
        
        # Add recent conversation history
        if len(self.conversation_history) > 0:
            recent = self.conversation_history[-4:]
            for msg in recent:
                messages.append({
                    "role": msg['role'],
                    "content": msg['content']
                })
        
        messages.append({"role": "user", "content": command})
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=200,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()
    
    def _get_rule_based_response(self, command):
        """Fallback rule-based responses"""
        command_lower = command.lower()
        
        # Time queries
        if any(word in command_lower for word in ['time', 'clock']):
            return f"⏰ The current time is {datetime.now().strftime('%I:%M %p')}."
        
        # Date queries
        if any(word in command_lower for word in ['date', 'today', 'day']):
            return f"📅 Today is {datetime.now().strftime('%A, %B %d, %Y')}."
        
        # Greetings
        if any(word in command_lower for word in ['hello', 'hi', 'hey']):
            return "👋 Hello! I'm Akira, your AI assistant. How can I help you today?"
        
        # Name introduction
        if 'my name is' in command_lower or 'i am' in command_lower or "i'm" in command_lower:
            # Extract name
            parts = command_lower.replace('my name is', '').replace('i am', '').replace("i'm", '').strip().split()
            if parts:
                name = ' '.join(parts).title()
                return f"😊 Nice to meet you, {name}! I'm Akira. How can I assist you today?"
        
        # How are you
        if 'how are you' in command_lower:
            return "😊 I'm functioning perfectly, thank you! How can I help you today?"
        
        # Thank you
        if any(word in command_lower for word in ['thank', 'thanks']):
            return "😊 You're welcome! Happy to help anytime!"
        
        # Help
        if 'help' in command_lower:
            return """🤖 I can help you with:
• Answering questions
• Managing tasks
• Controlling IoT devices
• Weather and news
• Calculations
• And much more!

💡 Tip: Add your GEMINI_API_KEY to .env for AI-powered responses!"""
        
        # Who are you
        if any(phrase in command_lower for phrase in ['who are you', 'what are you']):
            ai_status = "with AI-powered intelligence" if self.ai_enabled else "(AI can be enabled with API key)"
            return f"🤖 I'm Akira, your intelligent assistant {ai_status}! I can help with tasks, answer questions, control smart devices, and more!"
        
        # Tasks
        if any(word in command_lower for word in ['task', 'todo', 'remind', 'schedule']):
            task = command.replace('task', '').replace('todo', '').replace('remind', '').replace('schedule', '').strip()
            if task:
                self.tasks.append({'task': task, 'created': datetime.now(), 'status': 'pending'})
                return f"✅ Task added: {task}"
            return "📋 What task would you like to add?"
        
        # Weather
        if 'weather' in command_lower:
            return "🌤️ Current weather: Pleasant and clear, 72°F. (Add WEATHER_API_KEY for real data)"
        
        # News
        if 'news' in command_lower:
            return "📰 Top headlines: Tech sector growth continues. (Add NEWS_API_KEY for real news)"
        
        # Calculations
        if any(word in command_lower for word in ['calculate', 'compute', 'plus', 'minus', 'times', 'divided']):
            import re
            numbers = re.findall(r'\d+', command)
            if len(numbers) >= 2:
                a, b = int(numbers[0]), int(numbers[1])
                if 'plus' in command_lower or '+' in command:
                    return f"🔢 {a} + {b} = {a + b}"
                elif 'minus' in command_lower or '-' in command:
                    return f"🔢 {a} - {b} = {a - b}"
                elif 'times' in command_lower or '*' in command or 'multiply' in command_lower:
                    return f"🔢 {a} × {b} = {a * b}"
                elif 'divided' in command_lower or '/' in command:
                    return f"🔢 {a} ÷ {b} = {a / b:.2f}"
        
        # Default response
        return f"🤔 I understand you're asking about: '{command}'. I can help with tasks, questions, IoT control, and more. Could you be more specific?\n\n💡 Tip: Enable AI responses by adding GEMINI_API_KEY to your .env file!"
    
    def get_tasks(self):
        """Get all tasks"""
        if not self.tasks:
            return "You have no pending tasks."
        
        task_list = "\n".join([f"- {t['task']} ({t['status']})" for t in self.tasks])
        return f"📋 Your tasks:\n{task_list}"
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        return "🗑️ Conversation history cleared."
    
    def get_status(self):
        """Get assistant status"""
        status = {
            'ai_enabled': self.ai_enabled,
            'ai_provider': self.ai_provider if self.ai_enabled else 'none',
            'conversation_length': len(self.conversation_history),
            'tasks_count': len(self.tasks),
            'nlp_available': NLP_AVAILABLE
        }
        return status


# Backward compatibility - create instance with old class name
class Akira(EnhancedAkira):
    """Alias for backward compatibility"""
    pass


if __name__ == '__main__':
    # Test the assistant
    print("="*70)
    print("🤖 Enhanced Akira AI Assistant - Test Mode")
    print("="*70)
    
    assistant = EnhancedAkira()
    print(f"\nAI Status: {'✅ Enabled' if assistant.ai_enabled else '❌ Disabled (add API key to .env)'}")
    
    if assistant.ai_enabled:
        print(f"AI Provider: {assistant.ai_provider}")
    
    print("\n" + assistant.greet_user("Test User"))
    print("\nTry asking questions!")
    print("Type 'exit' to quit\n")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Akira: Goodbye! 👋")
                break
            
            response = assistant.process_command(user_input, "Test User")
            print(f"Akira: {response}\n")
        except KeyboardInterrupt:
            print("\n\nAkira: Goodbye! 👋")
            break
        except Exception as e:
            print(f"Error: {e}")
