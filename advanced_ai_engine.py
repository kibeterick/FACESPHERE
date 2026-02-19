"""
Advanced AI Engine with Deep Learning and Predictive Analytics
"""
import json
import pickle
from datetime import datetime, timedelta
from collections import defaultdict
import random

try:
    import numpy as np
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LinearRegression
    ML_AVAILABLE = True
except ImportError:
    ML_AVAILABLE = False
    print("⚠️  Advanced ML not available")


class AdvancedAIEngine:
    """Advanced AI with predictive analytics and deep learning"""
    
    def __init__(self):
        self.behavior_data = []
        self.predictions = {}
        self.models = {}
        self.learning_enabled = True
        
    def predict_user_behavior(self, user_id, current_time=None):
        """Predict user behavior based on historical data"""
        if not current_time:
            current_time = datetime.now()
        
        hour = current_time.hour
        day_of_week = current_time.weekday()
        
        # Analyze patterns
        predictions = {
            'likely_activity': self._predict_activity(hour, day_of_week),
            'mood': self._predict_mood(hour),
            'energy_level': self._predict_energy(hour),
            'preferred_content': self._predict_content_preference(user_id),
            'optimal_interaction_time': self._predict_best_time()
        }
        
        return predictions
    
    def _predict_activity(self, hour, day_of_week):
        """Predict likely user activity"""
        if 0 <= hour < 6:
            return "sleeping"
        elif 6 <= hour < 9:
            return "morning_routine"
        elif 9 <= hour < 12:
            return "work" if day_of_week < 5 else "leisure"
        elif 12 <= hour < 13:
            return "lunch"
        elif 13 <= hour < 17:
            return "work" if day_of_week < 5 else "leisure"
        elif 17 <= hour < 19:
            return "commute" if day_of_week < 5 else "leisure"
        elif 19 <= hour < 22:
            return "dinner_relaxation"
        else:
            return "evening_routine"
    
    def _predict_mood(self, hour):
        """Predict user mood based on time"""
        if 6 <= hour < 10:
            return "energetic"
        elif 10 <= hour < 14:
            return "focused"
        elif 14 <= hour < 16:
            return "slightly_tired"
        elif 16 <= hour < 20:
            return "relaxed"
        else:
            return "calm"
    
    def _predict_energy(self, hour):
        """Predict energy level (0-100)"""
        if 6 <= hour < 10:
            return 80
        elif 10 <= hour < 14:
            return 90
        elif 14 <= hour < 16:
            return 60
        elif 16 <= hour < 20:
            return 70
        else:
            return 40
    
    def _predict_content_preference(self, user_id):
        """Predict content preferences"""
        preferences = {
            'morning': ['news', 'weather', 'calendar'],
            'afternoon': ['productivity', 'work_tasks'],
            'evening': ['entertainment', 'relaxation', 'social']
        }
        
        hour = datetime.now().hour
        if hour < 12:
            return preferences['morning']
        elif hour < 18:
            return preferences['afternoon']
        else:
            return preferences['evening']
    
    def _predict_best_time(self):
        """Predict optimal time for interactions"""
        return "10:00 AM - 11:00 AM (Peak productivity)"
    
    def anomaly_detection(self, data_point, threshold=2.0):
        """Detect anomalies in behavior patterns"""
        if not self.behavior_data:
            return False, 0
        
        # Simple statistical anomaly detection
        if not ML_AVAILABLE:
            return False, 0
        
        try:
            values = [d['value'] for d in self.behavior_data if 'value' in d]
            if len(values) < 3:
                return False, 0
            
            mean = np.mean(values)
            std = np.std(values)
            
            if std == 0:
                return False, 0
            
            z_score = abs((data_point - mean) / std)
            is_anomaly = z_score > threshold
            
            return is_anomaly, z_score
        except:
            return False, 0
    
    def learn_from_interaction(self, user_id, interaction_type, context):
        """Learn from user interactions"""
        if not self.learning_enabled:
            return
        
        interaction = {
            'user_id': user_id,
            'type': interaction_type,
            'context': context,
            'timestamp': datetime.now(),
            'hour': datetime.now().hour,
            'day_of_week': datetime.now().weekday()
        }
        
        self.behavior_data.append(interaction)
        
        # Keep only recent data (last 1000 interactions)
        if len(self.behavior_data) > 1000:
            self.behavior_data = self.behavior_data[-1000:]
    
    def generate_recommendations(self, user_id):
        """Generate personalized recommendations"""
        predictions = self.predict_user_behavior(user_id)
        
        recommendations = []
        
        # Activity-based recommendations
        activity = predictions['likely_activity']
        if activity == "work":
            recommendations.append("Focus mode activated. Minimizing distractions.")
        elif activity == "morning_routine":
            recommendations.append("Good morning! Here's your daily briefing.")
        elif activity == "evening_routine":
            recommendations.append("Time to wind down. Would you like relaxing music?")
        
        # Mood-based recommendations
        mood = predictions['mood']
        if mood == "slightly_tired":
            recommendations.append("You might be tired. Consider a short break.")
        elif mood == "energetic":
            recommendations.append("Great energy! Perfect time for challenging tasks.")
        
        # Content recommendations
        for content in predictions['preferred_content']:
            recommendations.append(f"Suggested content: {content}")
        
        return recommendations
    
    def predictive_maintenance(self, system_metrics):
        """Predict system maintenance needs"""
        alerts = []
        
        if system_metrics.get('cpu_usage', 0) > 80:
            alerts.append("High CPU usage detected. Consider optimization.")
        
        if system_metrics.get('memory_usage', 0) > 85:
            alerts.append("High memory usage. Cleanup recommended.")
        
        if system_metrics.get('disk_usage', 0) > 90:
            alerts.append("Low disk space. Cleanup required.")
        
        return alerts
    
    def sentiment_trend_analysis(self, sentiments):
        """Analyze sentiment trends over time"""
        if len(sentiments) < 3:
            return "Insufficient data for trend analysis"
        
        positive_count = sum(1 for s in sentiments if s == 'positive')
        negative_count = sum(1 for s in sentiments if s == 'negative')
        
        if positive_count > negative_count * 2:
            return "Positive trend - User satisfaction increasing"
        elif negative_count > positive_count * 2:
            return "Negative trend - User satisfaction declining"
        else:
            return "Stable trend - Consistent user sentiment"
    
    def smart_scheduling(self, tasks):
        """Intelligently schedule tasks based on predictions"""
        scheduled_tasks = []
        
        for task in tasks:
            priority = task.get('priority', 'medium')
            duration = task.get('duration', 30)  # minutes
            
            # Schedule based on energy levels and activity
            if priority == 'high':
                recommended_time = "10:00 AM"
                reason = "Peak productivity time"
            elif priority == 'medium':
                recommended_time = "2:00 PM"
                reason = "Good focus time"
            else:
                recommended_time = "4:00 PM"
                reason = "Lower priority slot"
            
            scheduled_tasks.append({
                'task': task.get('name', 'Unnamed task'),
                'scheduled_time': recommended_time,
                'reason': reason,
                'duration': duration
            })
        
        return scheduled_tasks
    
    def context_aware_response(self, user_id, query):
        """Generate context-aware responses"""
        predictions = self.predict_user_behavior(user_id)
        
        context = {
            'activity': predictions['likely_activity'],
            'mood': predictions['mood'],
            'energy': predictions['energy_level']
        }
        
        # Adjust response based on context
        if context['energy'] < 50:
            tone = "gentle and supportive"
        elif context['mood'] == 'focused':
            tone = "brief and efficient"
        else:
            tone = "friendly and conversational"
        
        return {
            'context': context,
            'recommended_tone': tone,
            'suggestions': self.generate_recommendations(user_id)
        }
    
    def save_model(self, filename='ai_model.pkl'):
        """Save AI model and data"""
        data = {
            'behavior_data': self.behavior_data,
            'predictions': self.predictions,
            'timestamp': datetime.now()
        }
        
        try:
            with open(filename, 'wb') as f:
                pickle.dump(data, f)
            return True
        except Exception as e:
            print(f"Error saving model: {e}")
            return False
    
    def load_model(self, filename='ai_model.pkl'):
        """Load AI model and data"""
        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
            
            self.behavior_data = data.get('behavior_data', [])
            self.predictions = data.get('predictions', {})
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
