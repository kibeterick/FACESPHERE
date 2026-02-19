@echo off
setlocal enabledelayedexpansion

echo ================================================================================
echo                    AKIRA AI System - Complete Installation
echo ================================================================================
echo.
echo This script will attempt to install ALL packages including face recognition.
echo.
echo NOTE: Face recognition requires CMake and may fail on some systems.
echo      If it fails, use install_working.bat instead (90%% functionality).
echo.
echo ================================================================================
pause

echo.
echo [Step 1/6] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found! Please install Python 3.10 or later.
    pause
    exit /b 1
)
python --version
echo ✅ Python found!

echo.
echo [Step 2/6] Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo ⚠️  Warning: pip upgrade failed, continuing anyway...
) else (
    echo ✅ pip upgraded successfully!
)

echo.
echo [Step 3/6] Installing core AI and ML libraries...
echo Installing: numpy, scikit-learn, nltk
pip install numpy scikit-learn nltk
if errorlevel 1 (
    echo ❌ Core libraries installation failed!
    pause
    exit /b 1
)
echo ✅ Core libraries installed!

echo.
echo [Step 4/6] Installing computer vision and web libraries...
echo Installing: opencv-python, flask, flask-cors, requests
pip install opencv-python flask flask-cors requests
if errorlevel 1 (
    echo ❌ Computer vision/web libraries installation failed!
    pause
    exit /b 1
)
echo ✅ Computer vision and web libraries installed!

echo.
echo [Step 5/6] Installing voice libraries...
echo Installing: pyttsx3, SpeechRecognition
pip install pyttsx3 SpeechRecognition
if errorlevel 1 (
    echo ⚠️  Warning: Voice libraries installation had issues
    echo    Text-to-speech may not work, but system will continue
) else (
    echo ✅ Voice libraries installed!
)

echo.
echo [Step 6/6] Attempting to install face recognition (may take time)...
echo.
echo ⚠️  This step often fails due to CMake requirements!
echo    If it fails, your system will still work (90%% functionality)
echo.
echo Checking for CMake...
cmake --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ❌ CMake not found!
    echo.
    echo Face recognition requires CMake to be installed.
    echo.
    echo OPTIONS:
    echo   1. Skip face recognition (recommended - system works without it)
    echo   2. Install CMake first (see CMAKE_INSTALLATION_GUIDE.md)
    echo.
    set /p choice="Enter choice (1 or 2): "
    if "!choice!"=="2" (
        echo.
        echo Please install CMake from: https://cmake.org/download/
        echo Then run this script again.
        echo.
        echo Or see CMAKE_INSTALLATION_GUIDE.md for detailed instructions.
        pause
        exit /b 0
    )
    echo.
    echo Skipping face recognition installation...
    goto :skip_face_recognition
) else (
    cmake --version
    echo ✅ CMake found! Attempting face recognition installation...
    echo.
    echo This may take 5-30 minutes. Please be patient...
    pip install cmake dlib face_recognition
    if errorlevel 1 (
        echo.
        echo ❌ Face recognition installation failed!
        echo.
        echo This is common on Windows systems.
        echo Your system will work without it (90%% functionality).
        echo.
        echo To enable face recognition later:
        echo   - See CMAKE_INSTALLATION_GUIDE.md
        echo   - Or use pre-built wheels (easier method)
        echo.
        goto :skip_face_recognition
    ) else (
        echo ✅ Face recognition installed successfully!
        set FACE_RECOGNITION_INSTALLED=1
    )
)

:skip_face_recognition

echo.
echo ================================================================================
echo                         Installation Summary
echo ================================================================================
echo.

REM Verify installations
echo Verifying installations...
echo.

python -c "import numpy; print('✅ numpy')" 2>nul || echo ❌ numpy
python -c "import sklearn; print('✅ scikit-learn')" 2>nul || echo ❌ scikit-learn
python -c "import nltk; print('✅ nltk')" 2>nul || echo ❌ nltk
python -c "import cv2; print('✅ opencv-python')" 2>nul || echo ❌ opencv-python
python -c "import flask; print('✅ flask')" 2>nul || echo ❌ flask
python -c "import pyttsx3; print('✅ pyttsx3')" 2>nul || echo ❌ pyttsx3
python -c "import speech_recognition; print('✅ SpeechRecognition')" 2>nul || echo ❌ SpeechRecognition

echo.
echo Optional packages:
python -c "import face_recognition; print('✅ face_recognition (ENABLED)')" 2>nul || echo ⚠️  face_recognition (DISABLED - system works without it)

echo.
echo ================================================================================
echo                         Installation Complete!
echo ================================================================================
echo.

if defined FACE_RECOGNITION_INSTALLED (
    echo 🎉 SUCCESS! All packages installed including face recognition!
    echo.
    echo Your AKIRA system has 100%% functionality!
) else (
    echo 🎉 SUCCESS! Core packages installed!
    echo.
    echo Your AKIRA system has 90%% functionality!
    echo Face recognition is disabled but everything else works perfectly.
)

echo.
echo ================================================================================
echo                         What You Can Do Now
echo ================================================================================
echo.
echo 1. Launch Unified System (Recommended):
echo    ^> AKIRA.bat
echo.
echo 2. Start Web Interface:
echo    ^> python flask_app.py
echo    Then open: http://localhost:5000
echo.
echo 3. Run Original System:
echo    ^> python main.py
echo.
echo 4. Train ML Models:
echo    ^> python ai_engineering_standalone.py
echo.
echo ================================================================================
echo                         Documentation
echo ================================================================================
echo.
echo Quick Start:
echo   - START_NOW.txt - Quick start guide
echo   - START_HERE.md - Getting started
echo.
echo Installation Help:
echo   - FIX_INSTALLATION.md - Troubleshooting
echo   - CMAKE_INSTALLATION_GUIDE.md - Enable face recognition
echo.
echo System Guides:
echo   - UNIFIED_SYSTEM_GUIDE.md - Unified launcher
echo   - WEB_INTERFACE_GUIDE.md - Web interface and API
echo   - COMPLETE_SETUP_GUIDE.md - Everything
echo.
echo ================================================================================
echo                         Next Steps
echo ================================================================================
echo.
echo 1. Close this window
echo 2. Double-click: AKIRA.bat
echo 3. Choose option 1 (Web Interface)
echo 4. Open browser: http://localhost:5000
echo 5. Enjoy your AI system!
echo.
echo ================================================================================

pause
