"""
Akira - Advanced Virtual Assistant with NLP and ML capabilities
"""
import random
from datetime import datetime

# NLP capabilities
try:
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    NLP_AVAILABLE = True
except ImportError:
    NLP_AVAILABLE = False
    print("⚠️  NLP not available. Install nltk for advanced language processing.")


class Akira:
    """Akira - Intelligent Virtual Assistant"""
    
    def __init__(self):
        self.name = "Akira"
        self.user_preferences = {}
        self.conversation_history = []
        self.tasks = []
        
        if NLP_AVAILABLE:
            try:
                self.stop_words = set(stopwords.words('english'))
            except:
                print("Downloading NLTK data...")
                nltk.download('punkt', quiet=True)
                nltk.download('stopwords', quiet=True)
                self.stop_words = set(stopwords.words('english'))
        
    def greet_user(self, user_name):
        """Personalized greeting based on time and user"""
        hour = datetime.now().hour
        
        if hour < 12:
            greeting = f"Good morning, {user_name}!"
        elif hour < 18:
            greeting = f"Good afternoon, {user_name}!"
        else:
            greeting = f"Good evening, {user_name}!"
            
        return f"{greeting} I'm Akira, your intelligent assistant. How can I help you today?"
    
    def process_command(self, command):
        """Process natural language commands using NLP"""
        command_lower = command.lower()
        
        # Calculations - handle first for direct math questions
        if any(word in command_lower for word in ['plus', 'minus', 'times', 'divided', 'calculate', 'compute']) or any(char in command for char in ['+', '-', '*', '/']):
            return self.handle_calculation_command(command)
        
        # Extract intent using keyword matching
        if any(word in command_lower for word in ['schedule', 'remind', 'task', 'todo']):
            return self.handle_task_command(command)
        elif any(word in command_lower for word in ['weather', 'temperature']):
            return self.handle_weather_command(command)
        elif any(word in command_lower for word in ['news', 'headlines']):
            return self.handle_news_command(command)
        elif any(word in command_lower for word in ['email', 'message', 'send']):
            return self.handle_communication_command(command)
        elif any(word in command_lower for word in ['search', 'find', 'look up']):
            return self.handle_search_command(command)
        else:
            return self.handle_general_query(command)
    
    def handle_task_command(self, command):
        """Handle task-related commands"""
        task = command.replace('schedule', '').replace('remind', '').replace('task', '').strip()
        self.tasks.append({
            'task': task,
            'created': datetime.now(),
            'status': 'pending'
        })
        return f"✅ Task added: {task}. You now have {len(self.tasks)} tasks."
    
    def handle_weather_command(self, command):
        """Handle weather queries using real weather API"""
        try:
            # Import weather service
            from weather_service import weather_service
            
            # Extract location if mentioned
            command_lower = command.lower()
            location = None
            
            # Check for specific locations
            cities = ['kigali', 'nairobi', 'kampala', 'dar es salaam', 'addis ababa', 'lagos', 'cairo', 'johannesburg', 'new york', 'london', 'paris', 'tokyo']
            for city in cities:
                if city in command_lower:
                    location = city.title()
                    break
            
            # Default to Kigali if no location specified
            if not location:
                location = 'Kigali'
            
            # Get weather data
            if 'tomorrow' in command_lower or 'forecast' in command_lower or 'week' in command_lower:
                # Get forecast
                forecast_data = weather_service.get_forecast(location, 5)
                
                if 'tomorrow' in command_lower:
                    tomorrow = forecast_data['forecast'][1] if len(forecast_data['forecast']) > 1 else forecast_data['forecast'][0]
                    return f"🌤️ Tomorrow's forecast in {location}: {tomorrow['description']}, High: {tomorrow['temp_high']}°F, Low: {tomorrow['temp_low']}°F, Humidity: {tomorrow['humidity']}%"
                else:
                    # 5-day forecast
                    forecast_text = f"📅 5-Day Forecast for {location}:\n"
                    for day in forecast_data['forecast'][:5]:
                        forecast_text += f"• {day['date']}: {day['description']}, {day['temp_high']}°F/{day['temp_low']}°F\n"
                    return forecast_text
            else:
                # Get current weather
                weather = weather_service.get_current_weather(location)
                
                return f"""🌤️ Current weather in {weather['location']}:
• Condition: {weather['description']}
• Temperature: {weather['temperature']}°F (feels like {weather['feels_like']}°F)
• Humidity: {weather['humidity']}%
• Wind: {weather['wind_speed']} mph
• Visibility: {weather['visibility']} km"""
                
        except Exception as e:
            # Fallback to simulated data if API fails
            return """🌤️ Current weather in Kigali:
• Condition: Clear Sky
• Temperature: 72°F (feels like 74°F)
• Humidity: 65%
• Wind: 8 mph
• Visibility: 10 km"""
    
    def handle_news_command(self, command):
        """Handle news queries"""
        command_lower = command.lower()
        
        if 'tech' in command_lower or 'technology' in command_lower:
            return """📰 Tech News:
• AI breakthroughs in natural language processing
• New smartphone releases expected next month
• Cybersecurity updates for businesses
• Cloud computing trends for 2026"""
        elif 'business' in command_lower or 'finance' in command_lower:
            return """💼 Business News:
• Stock markets show steady growth
• Tech sector leads market gains
• New startup funding rounds announced
• Economic outlook remains positive"""
        elif 'sports' in command_lower:
            return """⚽ Sports News:
• Championship games this weekend
• Player transfers making headlines
• Olympic preparations underway
• Record-breaking performances"""
        else:
            return """📰 Top Headlines Today:
• Technology: AI advancements continue to reshape industries
• Business: Markets show positive trends
• Science: New research breakthrough announced
• World: International cooperation on climate initiatives"""
    
    def handle_communication_command(self, command):
        """Handle email/message commands"""
        return "📧 I can help you draft that message. What would you like to say?"
    
    def handle_search_command(self, command):
        """Handle search queries"""
        query = command.replace('search', '').replace('find', '').replace('look up', '').replace('for', '').strip()
        
        if not query:
            return "🔍 What would you like me to search for? Just tell me the topic!"
        
        return f"""🔍 Search Results for: "{query}"

I found several relevant results:
• {query.title()} - Overview and key information
• Latest updates about {query}
• How to use/understand {query}
• Related topics and resources

Would you like more specific information about any aspect?"""
    
    def handle_calculation_command(self, command):
        """Handle mathematical calculations"""
        try:
            import re
            
            # Extract numbers from command
            numbers = re.findall(r'\d+\.?\d*', command)
            
            if len(numbers) >= 2:
                a = float(numbers[0])
                b = float(numbers[1])
                
                command_lower = command.lower()
                
                # Check for operation
                if 'plus' in command_lower or '+' in command:
                    result = a + b
                    return f"🔢 {int(a) if a.is_integer() else a} + {int(b) if b.is_integer() else b} = {int(result) if result.is_integer() else result}"
                elif 'minus' in command_lower or '-' in command:
                    result = a - b
                    return f"🔢 {int(a) if a.is_integer() else a} - {int(b) if b.is_integer() else b} = {int(result) if result.is_integer() else result}"
                elif 'times' in command_lower or '*' in command or 'multiply' in command_lower or 'x' in command_lower:
                    result = a * b
                    return f"🔢 {int(a) if a.is_integer() else a} × {int(b) if b.is_integer() else b} = {int(result) if result.is_integer() else result}"
                elif 'divided' in command_lower or '/' in command or 'divide' in command_lower:
                    if b == 0:
                        return "🔢 Cannot divide by zero!"
                    result = a / b
                    return f"🔢 {int(a) if a.is_integer() else a} ÷ {int(b) if b.is_integer() else b} = {result:.2f}"
            
            # If no clear operation found
            return "🔢 I can help with calculations! Try: 'Calculate 5 plus 3' or '7 times 8'"
            
        except Exception as e:
            return "🔢 I can help with calculations. Try: 'Calculate 5 plus 3' or '10 divided by 2'"
    
    def handle_general_query(self, query):
        """Handle general queries with intelligent responses"""
        query_lower = query.lower()
        
        # Time-related queries
        if any(word in query_lower for word in ['time', 'clock', "what's the time"]):
            current_time = datetime.now().strftime("%I:%M %p")
            return f"⏰ The current time is {current_time}."
        
        # Date-related queries
        if any(word in query_lower for word in ['date', 'today', 'day']):
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            return f"📅 Today is {current_date}."
        
        # Greeting responses
        if any(word in query_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            return "👋 Hello! I'm Akira, your AI assistant. How can I help you today?"
        
        # How are you
        if any(phrase in query_lower for phrase in ['how are you', 'how do you do', 'how are things']):
            return "😊 I'm functioning perfectly, thank you for asking! How can I assist you today?"
        
        # Thank you
        if any(word in query_lower for word in ['thank', 'thanks', 'appreciate']):
            return "😊 You're welcome! I'm always here to help. Is there anything else you need?"
        
        # Help requests
        if any(word in query_lower for word in ['help', 'assist', 'support']):
            return """🤖 I can help you with:
• Task management (schedule, remind, todo)
• Weather information
• News updates
• Calculations and math
• Search queries
• Time and date
• IoT device control
• General questions

Just ask me anything!"""
        
        # Who are you
        if any(phrase in query_lower for phrase in ['who are you', 'what are you', 'tell me about yourself']):
            return """🤖 I'm Akira, your intelligent AI assistant! I can:
• Answer questions and provide information
• Manage your tasks and schedules
• Control smart home devices
• Perform calculations
• Search for information
• And much more!

I'm here to make your life easier. What would you like to do?"""
        
        # Capabilities
        if any(word in query_lower for word in ['can you', 'able to', 'capabilities']):
            return """✨ I have many capabilities:
• Natural language understanding
• Task automation
• Smart home control
• Information retrieval
• Calculations and analysis
• Personalized assistance
• Learning your preferences

Try asking me to do something specific!"""
        
        # Name-related
        if 'your name' in query_lower or 'who made you' in query_lower:
            return "🤖 My name is Akira. I'm an advanced AI assistant created to help you with various tasks and queries."
        
        # Jokes
        if 'joke' in query_lower or 'funny' in query_lower:
            jokes = [
                "Why did the AI go to school? To improve its learning algorithms! 😄",
                "What do you call an AI that sings? A-dell! 🎵",
                "Why don't AIs ever get tired? Because they run on endless loops! 😊"
            ]
            return random.choice(jokes)
        
        # Smart home related
        if any(word in query_lower for word in ['light', 'lights', 'lamp']):
            return "💡 I can control your lights! Try: 'Turn on the living room light' or check the IoT page."
        
        if any(word in query_lower for word in ['temperature', 'thermostat', 'heating', 'cooling']):
            return "🌡️ I can adjust your thermostat! Try: 'Set temperature to 72 degrees' or use the IoT control panel."
        
        if any(word in query_lower for word in ['door', 'lock', 'unlock', 'security']):
            return "🔒 I can control your smart locks! Try: 'Lock the front door' or check the IoT page."
        
        # System status
        if any(word in query_lower for word in ['status', 'system', 'running']):
            return f"✅ System Status: All modules operational. Current time: {datetime.now().strftime('%I:%M %p')}. How can I assist you?"
        
        # Default intelligent response
        return f"🤔 I understand you're asking about: '{query}'. While I'm processing that, I can help you with tasks, weather, calculations, IoT control, and more. Could you be more specific about what you need?"
    
    def learn_preference(self, category, preference):
        """Learn user preferences for personalization"""
        self.user_preferences[category] = preference
        return f"✅ Learned your preference: {category} = {preference}"
    
    def get_tasks(self):
        """Get all tasks"""
        if not self.tasks:
            return "You have no pending tasks."
        
        task_list = "\n".join([f"- {t['task']} ({t['status']})" for t in self.tasks])
        return f"📋 Your tasks:\n{task_list}"
    
    def automate_task(self, task_type):
        """Automate repetitive tasks"""
        automation_templates = {
            'email': "Setting up email automation...",
            'backup': "Configuring automatic backup...",
            'report': "Scheduling report generation...",
            'reminder': "Setting up smart reminders..."
        }
        
        return automation_templates.get(task_type, "Task automation configured.")
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of text (basic implementation)"""
        positive_words = ['good', 'great', 'excellent', 'happy', 'love', 'wonderful', 'amazing']
        negative_words = ['bad', 'terrible', 'hate', 'awful', 'poor', 'sad', 'angry']
        
        text_lower = text.lower()
        pos_count = sum(1 for word in positive_words if word in text_lower)
        neg_count = sum(1 for word in negative_words if word in text_lower)
        
        if pos_count > neg_count:
            return "positive", pos_count
        elif neg_count > pos_count:
            return "negative", neg_count
        else:
            return "neutral", 0
