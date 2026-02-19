## AKIRA AI System - Complete Installation Guide

## 🚀 Quick Installation (Windows)

### Method 1: Automatic Installation (Recommended)

Simply run the installation script:

```bash
install_all.bat
```

This will install everything automatically!

---

### Method 2: Manual Installation

#### Step 1: Install Core Libraries
```bash
pip install numpy scikit-learn nltk
```

#### Step 2: Install Computer Vision
```bash
pip install opencv-python
```

#### Step 3: Install Voice Libraries
```bash
pip install pyttsx3 SpeechRecognition pyaudio
```

#### Step 4: Install Web Framework
```bash
pip install flask flask-cors requests
```

#### Step 5: Install Face Recognition (Optional but Recommended)
```bash
pip install cmake
pip install dlib
pip install face_recognition
```

---

## 📦 Complete Requirements List

### Essential (Required)
- numpy >= 1.24.0
- scikit-learn >= 1.3.0
- nltk >= 3.8.0
- opencv-python >= 4.8.0
- pyttsx3 >= 2.90
- SpeechRecognition >= 3.10.0
- flask >= 2.3.0
- requests >= 2.31.0

### Recommended
- pyaudio >= 0.2.13 (for voice input)
- face_recognition >= 1.3.0 (for face recognition)
- dlib >= 19.24.0 (required by face_recognition)
- cmake (required for dlib on Windows)

### Optional
- tensorflow >= 2.13.0 (for deep learning)
- torch >= 2.0.0 (PyTorch alternative)
- twilio >= 8.5.0 (for SMS notifications)

---

## 🔧 Troubleshooting Installation Issues

### Issue 1: PyAudio Installation Fails

**Solution for Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Alternative:**
Download the wheel file from:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

Then install:
```bash
pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
```

---

### Issue 2: Face Recognition Installation Fails

**Solution:**

1. Install Visual C++ Build Tools:
   - Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - Install "Desktop development with C++"

2. Install CMake:
```bash
pip install cmake
```

3. Install dlib:
```bash
pip install dlib
```

4. Install face_recognition:
```bash
pip install face_recognition
```

**Alternative (Skip Face Recognition):**
The system will work without face recognition, just with limited features.

---

### Issue 3: NLTK Data Missing

**Solution:**
```python
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

---

### Issue 4: OpenCV Import Error

**Solution:**
```bash
pip uninstall opencv-python
pip install opencv-python-headless
```

---

## ✅ Verify Installation

Run this to check if everything is installed:

```python
python -c "import numpy, sklearn, nltk, cv2, pyttsx3, flask; print('✅ All core libraries installed!')"
```

---

## 🚀 Running Your System

### Option 1: Original System (No Face Recognition Required)
```bash
python main.py
```

### Option 2: Web Interface (Recommended)
```bash
python flask_app.py
```
Then open: http://localhost:5000

### Option 3: Complete System (All Features)
```bash
python akira_complete_system.py
```

### Option 4: AI Engineering (Standalone)
```bash
python ai_engineering_standalone.py
```

---

## 🌐 Web Interface Setup

### Start the Web Server
```bash
python flask_app.py
```

### Access the Application
Open your browser and go to:
- **Main Page**: http://localhost:5000
- **Dashboard**: http://localhost:5000/dashboard
- **IoT Control**: http://localhost:5000/iot
- **Assistant**: http://localhost:5000/assistant

### API Endpoints
- `GET /api/status` - System status
- `POST /api/assistant/command` - Send command to assistant
- `GET /api/iot/devices` - List IoT devices
- `POST /api/iot/control` - Control IoT device
- `GET /api/dashboard/metrics` - Get system metrics

---

## 📱 Testing the Installation

### Test 1: Basic System
```bash
python main.py
```
Choose option 1 for demo

### Test 2: Web Interface
```bash
python flask_app.py
```
Open http://localhost:5000 in browser

### Test 3: AI Engineering
```bash
python ai_engineering_standalone.py
```
Choose option 10 for demo

---

## 🔍 Common Installation Errors

### Error: "No module named 'numpy'"
**Solution:** `pip install numpy`

### Error: "No module named 'sklearn'"
**Solution:** `pip install scikit-learn`

### Error: "No module named 'cv2'"
**Solution:** `pip install opencv-python`

### Error: "No module named 'flask'"
**Solution:** `pip install flask`

### Error: "Microsoft Visual C++ 14.0 is required"
**Solution:** Install Visual C++ Build Tools

---

## 💡 Installation Tips

1. **Use Virtual Environment (Recommended)**
```bash
python -m venv akira_env
akira_env\Scripts\activate
pip install -r requirements.txt
```

2. **Check Python Version**
```bash
python --version
```
Requires Python 3.8 or higher

3. **Update pip First**
```bash
python -m pip install --upgrade pip
```

4. **Install One by One**
If batch installation fails, install packages one by one

5. **Skip Optional Packages**
Face recognition is optional - system works without it

---

## 📊 Installation Progress Checklist

- [ ] Python 3.8+ installed
- [ ] pip upgraded
- [ ] numpy installed
- [ ] scikit-learn installed
- [ ] nltk installed
- [ ] opencv-python installed
- [ ] pyttsx3 installed
- [ ] SpeechRecognition installed
- [ ] flask installed
- [ ] pyaudio installed (optional)
- [ ] face_recognition installed (optional)
- [ ] NLTK data downloaded
- [ ] System tested

---

## 🎯 What Works Without Optional Libraries

### Without Face Recognition:
✅ Virtual Assistant
✅ IoT Control
✅ Marketing
✅ AI Predictions
✅ Database
✅ Notifications
✅ Web Interface
❌ Face Recognition
❌ Surveillance (limited)

### Without PyAudio:
✅ Everything except voice input
✅ Text-to-speech still works
❌ Voice recognition

---

## 🆘 Getting Help

If installation fails:

1. Check error message carefully
2. Google the specific error
3. Try installing packages one by one
4. Skip optional packages if needed
5. Use the system without problematic features

---

## 🎉 Post-Installation

After successful installation:

1. Run `python main.py` to test basic system
2. Run `python flask_app.py` to start web interface
3. Open http://localhost:5000 in browser
4. Explore all features!

---

## 📝 Installation Summary

**Minimum Installation (Works):**
```bash
pip install numpy scikit-learn nltk opencv-python pyttsx3 flask
```

**Recommended Installation (Full Features):**
```bash
pip install numpy scikit-learn nltk opencv-python pyttsx3 SpeechRecognition pyaudio flask face_recognition dlib
```

**Complete Installation (Everything):**
```bash
install_all.bat
```

---

**Installation Time:**
- Minimum: 2-5 minutes
- Recommended: 5-10 minutes
- Complete: 10-20 minutes (depending on internet speed)

**Disk Space Required:**
- Minimum: ~500 MB
- Recommended: ~1 GB
- Complete: ~2 GB

---

🎉 **You're ready to use AKIRA AI System!**
