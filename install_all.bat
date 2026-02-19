@echo off
echo ========================================
echo AKIRA AI System - Complete Installation
echo ========================================
echo.
echo This will install ALL required libraries for your AKIRA system
echo.
pause

echo.
echo [1/5] Upgrading pip...
python -m pip install --upgrade pip

echo.
echo [2/5] Installing core AI and ML libraries...
pip install numpy scikit-learn nltk

echo.
echo [3/5] Installing computer vision libraries...
pip install opencv-python

echo.
echo [4/5] Installing voice and audio libraries...
pip install pyttsx3 SpeechRecognition pyaudio

echo.
echo [5/5] Installing web framework and utilities...
pip install flask flask-cors requests

echo.
echo ========================================
echo Optional Libraries (Recommended)
echo ========================================
echo.
echo Installing face recognition (may take time)...
pip install cmake dlib face_recognition

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo You can now run:
echo   - python main.py (Original system)
echo   - python flask_app.py (Web interface)
echo   - python akira_complete_system.py (Complete system)
echo.
pause
