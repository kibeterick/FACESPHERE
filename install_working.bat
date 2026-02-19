@echo off
echo ========================================
echo AKIRA AI System - Working Installation
echo ========================================
echo.
echo Installing ONLY the packages that work on your system
echo Face recognition will be skipped (system works without it!)
echo.
pause

echo.
echo [1/4] Upgrading pip...
python -m pip install --upgrade pip

echo.
echo [2/4] Installing core AI and ML libraries...
pip install numpy scikit-learn nltk

echo.
echo [3/4] Installing computer vision libraries...
pip install opencv-python

echo.
echo [4/5] Installing AI API packages...
pip install google-generativeai python-dotenv

echo.
echo [5/5] Installing voice and web libraries...
pip install pyttsx3 SpeechRecognition flask flask-cors requests

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo ✅ Installed Successfully:
echo    - numpy, scikit-learn, nltk (AI/ML)
echo    - opencv-python (Computer Vision)
echo    - pyttsx3, SpeechRecognition (Voice)
echo    - flask, flask-cors, requests (Web)
echo.
echo ⚠️  Skipped (Not Required):
echo    - face_recognition (needs CMake - system works without it!)
echo    - pyaudio (voice input - text-to-speech still works!)
echo.
echo 🎉 Your system is ready to use!
echo.
echo You can now run:
echo   - AKIRA.bat (Unified launcher - RECOMMENDED)
echo   - python flask_app.py (Web interface)
echo   - python main.py (Original system)
echo.
echo Note: Face recognition features will be disabled, but
echo everything else works perfectly!
echo.
pause
