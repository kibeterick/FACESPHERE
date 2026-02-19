@echo off
echo ================================================================================
echo                    AKIRA System Diagnostics
echo ================================================================================
echo.
echo This script will check your system and diagnose any issues.
echo.
pause

echo.
echo ================================================================================
echo                    System Information
echo ================================================================================
echo.

echo Operating System:
ver

echo.
echo Python Version:
python --version 2>nul || echo ❌ Python not found!

echo.
echo Pip Version:
pip --version 2>nul || echo ❌ pip not found!

echo.
echo CMake Status:
cmake --version 2>nul || echo ⚠️  CMake not installed (needed for face_recognition only)

echo.
echo ================================================================================
echo                    Python Package Status
echo ================================================================================
echo.

echo Checking installed packages...
echo.

echo Core AI/ML Libraries:
python -c "import numpy; print('  ✅ numpy version:', numpy.__version__)" 2>nul || echo   ❌ numpy - NOT INSTALLED
python -c "import sklearn; print('  ✅ scikit-learn version:', sklearn.__version__)" 2>nul || echo   ❌ scikit-learn - NOT INSTALLED
python -c "import nltk; print('  ✅ nltk version:', nltk.__version__)" 2>nul || echo   ❌ nltk - NOT INSTALLED

echo.
echo Computer Vision:
python -c "import cv2; print('  ✅ opencv-python version:', cv2.__version__)" 2>nul || echo   ❌ opencv-python - NOT INSTALLED

echo.
echo Web Framework:
python -c "import flask; print('  ✅ flask version:', flask.__version__)" 2>nul || echo   ❌ flask - NOT INSTALLED
python -c "import flask_cors; print('  ✅ flask-cors installed')" 2>nul || echo   ❌ flask-cors - NOT INSTALLED
python -c "import requests; print('  ✅ requests version:', requests.__version__)" 2>nul || echo   ❌ requests - NOT INSTALLED

echo.
echo Voice Libraries:
python -c "import pyttsx3; print('  ✅ pyttsx3 installed')" 2>nul || echo   ⚠️  pyttsx3 - NOT INSTALLED (text-to-speech won't work)
python -c "import speech_recognition; print('  ✅ SpeechRecognition version:', speech_recognition.__version__)" 2>nul || echo   ⚠️  SpeechRecognition - NOT INSTALLED (voice input won't work)

echo.
echo Optional Libraries:
python -c "import face_recognition; print('  ✅ face_recognition installed')" 2>nul || echo   ⚠️  face_recognition - NOT INSTALLED (face features disabled)
python -c "import dlib; print('  ✅ dlib installed')" 2>nul || echo   ⚠️  dlib - NOT INSTALLED (needed for face_recognition)

echo.
echo ================================================================================
echo                    AKIRA System Files
echo ================================================================================
echo.

echo Checking for required files...
echo.

if exist "main.py" (echo ✅ main.py) else (echo ❌ main.py - MISSING!)
if exist "flask_app.py" (echo ✅ flask_app.py) else (echo ❌ flask_app.py - MISSING!)
if exist "akira_unified_launcher.py" (echo ✅ akira_unified_launcher.py) else (echo ❌ akira_unified_launcher.py - MISSING!)
if exist "AKIRA.bat" (echo ✅ AKIRA.bat) else (echo ❌ AKIRA.bat - MISSING!)

echo.
echo Module Files:
if exist "akira_assistant.py" (echo ✅ akira_assistant.py) else (echo ❌ akira_assistant.py - MISSING!)
if exist "smart_surveillance.py" (echo ✅ smart_surveillance.py) else (echo ❌ smart_surveillance.py - MISSING!)
if exist "personalized_marketing.py" (echo ✅ personalized_marketing.py) else (echo ❌ personalized_marketing.py - MISSING!)
if exist "advanced_ai_engine.py" (echo ✅ advanced_ai_engine.py) else (echo ❌ advanced_ai_engine.py - MISSING!)
if exist "iot_integration.py" (echo ✅ iot_integration.py) else (echo ❌ iot_integration.py - MISSING!)
if exist "database_manager.py" (echo ✅ database_manager.py) else (echo ❌ database_manager.py - MISSING!)
if exist "notification_system.py" (echo ✅ notification_system.py) else (echo ❌ notification_system.py - MISSING!)
if exist "enhanced_voice_assistant.py" (echo ✅ enhanced_voice_assistant.py) else (echo ❌ enhanced_voice_assistant.py - MISSING!)
if exist "web_dashboard.py" (echo ✅ web_dashboard.py) else (echo ❌ web_dashboard.py - MISSING!)
if exist "face_recognition_module.py" (echo ✅ face_recognition_module.py) else (echo ❌ face_recognition_module.py - MISSING!)
if exist "ai_engineering_module.py" (echo ✅ ai_engineering_module.py) else (echo ❌ ai_engineering_module.py - MISSING!)

echo.
echo Templates:
if exist "templates\index.html" (echo ✅ templates\index.html) else (echo ❌ templates\index.html - MISSING!)
if exist "templates\dashboard.html" (echo ✅ templates\dashboard.html) else (echo ❌ templates\dashboard.html - MISSING!)

echo.
echo ================================================================================
echo                    Port Availability
echo ================================================================================
echo.

echo Checking if port 5000 is available...
netstat -an | find ":5000" >nul
if errorlevel 1 (
    echo ✅ Port 5000 is available
) else (
    echo ⚠️  Port 5000 is in use - web interface may not start
    echo    Solution: Edit flask_app.py and change port to 8080
)

echo.
echo ================================================================================
echo                    Diagnostic Summary
echo ================================================================================
echo.

REM Count issues
set CRITICAL_ISSUES=0
set WARNINGS=0

python --version >nul 2>&1 || set /a CRITICAL_ISSUES+=1
python -c "import numpy" 2>nul || set /a CRITICAL_ISSUES+=1
python -c "import sklearn" 2>nul || set /a CRITICAL_ISSUES+=1
python -c "import flask" 2>nul || set /a CRITICAL_ISSUES+=1

python -c "import face_recognition" 2>nul || set /a WARNINGS+=1
python -c "import pyttsx3" 2>nul || set /a WARNINGS+=1

if %CRITICAL_ISSUES% EQU 0 (
    echo ✅ System Status: READY TO USE
    echo.
    echo Your AKIRA system is properly configured!
    echo.
    if %WARNINGS% GTR 0 (
        echo ⚠️  %WARNINGS% optional feature(s) disabled
        echo    System will work with reduced functionality
    )
) else (
    echo ❌ System Status: NEEDS ATTENTION
    echo.
    echo Found %CRITICAL_ISSUES% critical issue(s)
    echo.
    echo Please run one of these installation scripts:
    echo   - install_working.bat (recommended)
    echo   - install_complete.bat (tries everything)
)

echo.
echo ================================================================================
echo                    Recommendations
echo ================================================================================
echo.

python -c "import numpy, sklearn, flask" 2>nul
if errorlevel 1 (
    echo 🔧 ACTION REQUIRED:
    echo    Run: install_working.bat
    echo    This will install all required packages
    echo.
) else (
    python -c "import face_recognition" 2>nul
    if errorlevel 1 (
        echo 💡 OPTIONAL:
        echo    Face recognition is disabled
        echo    To enable: See CMAKE_INSTALLATION_GUIDE.md
        echo    Or just use the system without it (90%% functionality)
        echo.
    )
    
    echo ✅ READY TO LAUNCH:
    echo    Run: AKIRA.bat
    echo    Then choose option 1 for web interface
    echo.
)

echo ================================================================================
echo                    Quick Fixes
echo ================================================================================
echo.
echo If you see issues above, try these:
echo.
echo 1. Missing Python packages:
echo    ^> install_working.bat
echo.
echo 2. Want face recognition:
echo    ^> See CMAKE_INSTALLATION_GUIDE.md
echo.
echo 3. Port 5000 in use:
echo    ^> Edit flask_app.py, change port to 8080
echo.
echo 4. Module not found errors:
echo    ^> Run install_working.bat again
echo.
echo 5. System won't start:
echo    ^> Check if Python is in PATH
echo    ^> Reinstall Python if needed
echo.
echo ================================================================================
echo                    Documentation
echo ================================================================================
echo.
echo For more help, see:
echo   - FIX_INSTALLATION.md - Installation troubleshooting
echo   - CMAKE_INSTALLATION_GUIDE.md - Enable face recognition
echo   - START_NOW.txt - Quick start guide
echo   - UNIFIED_SYSTEM_GUIDE.md - System documentation
echo.
echo ================================================================================

pause
