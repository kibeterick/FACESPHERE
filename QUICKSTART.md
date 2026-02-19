# AKIRA Quick Start Guide

Get up and running with AKIRA in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install numpy scikit-learn nltk pyttsx3 SpeechRecognition pyaudio opencv-python face_recognition dlib
```

## Step 2: Download NLTK Data (First Time Only)

```python
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

## Step 3: Run the System

### Option A: Complete AKIRA System (Recommended)
```bash
python akira_integrated_system.py
```

Choose mode 1 for a complete demo of all features!

### Option B: Original FaceConnect System
```bash
python main.py
```

## What to Try First

### 1. Virtual Assistant Demo (Mode 2)
See Akira handle:
- Task scheduling
- Weather queries
- Calculations
- Sentiment analysis

### 2. Smart Surveillance Demo (Mode 3)
Watch the system:
- Control access
- Log activities
- Detect anomalies
- Analyze patterns

### 3. Personalized Marketing Demo (Mode 4)
Experience:
- Customer segmentation with ML
- Targeted campaigns
- Sentiment analysis
- Product recommendations

### 4. Live Surveillance (Mode 5)
Real-time monitoring:
- Face detection
- Object tracking
- Security alerts

## Quick Examples

### Virtual Assistant
```python
from akira_assistant import Akira

akira = Akira()
print(akira.greet_user("Erick"))
print(akira.process_command("Schedule meeting tomorrow at 3 PM"))
print(akira.process_command("Calculate 50 plus 25"))
```

### Smart Surveillance
```python
from smart_surveillance import SmartSurveillance

surveillance = SmartSurveillance()
surveillance.add_authorized_person("Erick")
result = surveillance.check_access_control("Erick")
print("Access granted!" if result else "Access denied!")
```

### Personalized Marketing
```python
from personalized_marketing import PersonalizedMarketing

marketing = PersonalizedMarketing()
marketing.add_customer("CUST001", {'name': 'Alice', 'age': 28})
marketing.customers['CUST001']['lifetime_value'] = 1200
marketing.segment_customers()
print(marketing.profile_customer("CUST001"))
```

## Troubleshooting

### Camera Not Working
- Check camera permissions
- Try different camera_id (0, 1, 2)
- Ensure no other app is using the camera

### Voice Recognition Issues
- Check microphone permissions
- Speak clearly and wait for the beep
- Ensure internet connection (Google Speech API)

### Face Recognition Errors
- Ensure good lighting
- Face the camera directly
- Install dlib properly (may need Visual C++ on Windows)

### Import Errors
- Install missing packages: `pip install <package_name>`
- Check Python version (3.8+ recommended)

## Next Steps

1. Register your face for personalized experience
2. Add emergency contacts
3. Set up customer profiles for marketing
4. Configure surveillance zones
5. Customize voice responses

## Tips

- Use Mode 1 for a complete walkthrough
- Press Ctrl+C to stop any running process
- Press 'q' in camera windows to quit
- Check README.md for detailed documentation

Enjoy AKIRA! 🚀
