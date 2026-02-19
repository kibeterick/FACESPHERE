@echo off
echo ================================================================================
echo                    Restarting AKIRA Web Server
echo ================================================================================
echo.
echo Stopping any running Flask servers...
echo.

REM Kill any Python processes running flask_app.py
for /f "tokens=2" %%a in ('tasklist ^| findstr /i "python.exe"') do (
    taskkill /F /PID %%a >nul 2>&1
)

echo Server stopped.
echo.
echo Starting fresh server...
echo.

REM Start the Flask server
start "AKIRA Web Server" python flask_app.py

echo.
echo ================================================================================
echo Server restarted!
echo ================================================================================
echo.
echo Open your browser to: http://localhost:5000
echo.
echo Press any key to close this window...
pause >nul
