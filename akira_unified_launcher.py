"""
AKIRA Unified System Launcher
Single entry point for the entire AI ecosystem
"""
import os
import sys
import subprocess
import webbrowser
from datetime import datetime

# ASCII Art Logo for AI Engineering
AKIRA_LOGO = """
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║     █████╗ ██╗  ██╗██╗██████╗  █████╗     ███████╗██╗   ██╗███████╗     ║
║    ██╔══██╗██║ ██╔╝██║██╔══██╗██╔══██╗    ██╔════╝╚██╗ ██╔╝██╔════╝     ║
║    ███████║█████╔╝ ██║██████╔╝███████║    ███████╗ ╚████╔╝ ███████╗     ║
║    ██╔══██║██╔═██╗ ██║██╔══██╗██╔══██║    ╚════██║  ╚██╔╝  ╚════██║     ║
║    ██║  ██║██║  ██╗██║██║  ██║██║  ██║    ███████║   ██║   ███████║     ║
║    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝   ╚═╝   ╚══════╝     ║
║                                                                           ║
║              🤖 Complete AI Engineering Ecosystem 🤖                      ║
║                                                                           ║
║  ┌─────────────────────────────────────────────────────────────────┐    ║
║  │  Virtual Assistant  │  Smart Surveillance  │  IoT Control       │    ║
║  │  AI Predictions     │  Marketing AI        │  Face Recognition  │    ║
║  │  ML Engineering     │  Web Dashboard       │  Voice Assistant   │    ║
║  └─────────────────────────────────────────────────────────────────┘    ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

AI_ENGINEERING_BANNER = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║        🧠 AI ENGINEERING POWERED SYSTEM 🧠                   ║
    ║                                                              ║
    ║    ┌──────────┐  ┌──────────┐  ┌──────────┐                ║
    ║    │   NLP    │  │    CV    │  │    ML    │                ║
    ║    │ Natural  │  │ Computer │  │ Machine  │                ║
    ║    │ Language │  │  Vision  │  │ Learning │                ║
    ║    └──────────┘  └──────────┘  └──────────┘                ║
    ║           │            │            │                       ║
    ║           └────────────┴────────────┘                       ║
    ║                      │                                      ║
    ║              ┌───────▼───────┐                              ║
    ║              │  AKIRA CORE   │                              ║
    ║              │   AI ENGINE   │                              ║
    ║              └───────┬───────┘                              ║
    ║                      │                                      ║
    ║         ┌────────────┼────────────┐                         ║
    ║         │            │            │                         ║
    ║    ┌────▼────┐  ┌───▼────┐  ┌───▼────┐                    ║
    ║    │   IoT   │  │  Web   │  │  API   │                    ║
    ║    │ Control │  │  UI    │  │ Access │                    ║
    ║    └─────────┘  └────────┘  └────────┘                    ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
"""


class AkiraUnifiedLauncher:
    """Unified launcher for the entire AKIRA ecosystem"""
    
    def __init__(self):
        self.system_name = "AKIRA AI Engineering System"
        self.version = "2.0 Enterprise Edition"
        self.modules_available = self.check_modules()
    
    def check_modules(self):
        """Check which modules are available"""
        modules = {
            'main': os.path.exists('main.py'),
            'complete': os.path.exists('akira_complete_system.py'),
            'flask': os.path.exists('flask_app.py'),
            'ai_engineering': os.path.exists('ai_engineering_standalone.py'),
            'integrated': os.path.exists('akira_integrated_system.py')
        }
        return modules
    
    def display_header(self):
        """Display the main header with AI engineering theme"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(AKIRA_LOGO)
        print(f"\n{'='*79}")
        print(f"  System: {self.system_name}")
        print(f"  Version: {self.version}")
        print(f"  Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*79}\n")
    
    def display_ai_architecture(self):
        """Display AI engineering architecture"""
        print(AI_ENGINEERING_BANNER)
        print("\n" + "="*79)
        print("  🎯 UNIFIED AI ECOSYSTEM")
        print("="*79)
        print("""
  This system integrates multiple AI technologies:
  
  🧠 Natural Language Processing (NLP)
     └─ Voice commands, text understanding, sentiment analysis
  
  👁️  Computer Vision (CV)
     └─ Face recognition, object detection, surveillance
  
  🤖 Machine Learning (ML)
     └─ Predictions, clustering, classification, recommendations
  
  🏠 IoT Integration
     └─ Smart home control, automation, energy monitoring
  
  🌐 Web Interface
     └─ Dashboard, API, real-time monitoring
  
  💾 Data Management
     └─ Database, logging, analytics
        """)
        print("="*79 + "\n")
    
    def main_menu(self):
        """Display main menu"""
        print("\n" + "="*79)
        print("  🚀 LAUNCH OPTIONS")
        print("="*79)
        print("""
  ┌─────────────────────────────────────────────────────────────────────┐
  │  INTEGRATED SYSTEMS (All-in-One)                                    │
  ├─────────────────────────────────────────────────────────────────────┤
  │  1. 🌐 Web Interface (Recommended)                                  │
  │     → Full system with browser-based control panel                  │
  │     → Access: http://localhost:5000                                 │
  │                                                                      │
  │  2. 🎯 Complete AI System                                           │
  │     → All 10 modules integrated                                     │
  │     → Interactive demos and full features                           │
  │                                                                      │
  │  3. 🔷 Original FaceConnect System                                  │
  │     → Face recognition + Voice + Basic AI                           │
  │     → Your original project                                         │
  └─────────────────────────────────────────────────────────────────────┘
  
  ┌─────────────────────────────────────────────────────────────────────┐
  │  SPECIALIZED MODULES (Standalone)                                   │
  ├─────────────────────────────────────────────────────────────────────┤
  │  4. 🔧 AI Engineering Module                                        │
  │     → Train custom ML models                                        │
  │     → Model deployment and management                               │
  │                                                                      │
  │  5. 📊 System Dashboard Only                                        │
  │     → View metrics and status                                       │
  │     → Generate reports                                              │
  └─────────────────────────────────────────────────────────────────────┘
  
  ┌─────────────────────────────────────────────────────────────────────┐
  │  UTILITIES                                                           │
  ├─────────────────────────────────────────────────────────────────────┤
  │  6. 📚 Open Documentation                                           │
  │  7. 🔍 System Status Check                                          │
  │  8. ⚙️  Installation Guide                                          │
  │  0. 🚪 Exit                                                          │
  └─────────────────────────────────────────────────────────────────────┘
        """)
        print("="*79)
    
    def launch_web_interface(self):
        """Launch Flask web interface"""
        print("\n🌐 Launching Web Interface...")
        print("="*79)
        print("  Starting Flask web server...")
        print("  Access the system at: http://localhost:5000")
        print("  Press Ctrl+C to stop the server")
        print("="*79 + "\n")
        
        try:
            # Open browser automatically
            import threading
            def open_browser():
                import time
                time.sleep(2)
                webbrowser.open('http://localhost:5000')
            
            threading.Thread(target=open_browser, daemon=True).start()
            
            # Run Flask app
            subprocess.run([sys.executable, 'flask_app.py'])
        except KeyboardInterrupt:
            print("\n\n✅ Web server stopped")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Make sure Flask is installed: pip install flask")
    
    def launch_complete_system(self):
        """Launch complete AKIRA system"""
        print("\n🎯 Launching Complete AI System...")
        print("="*79 + "\n")
        
        try:
            subprocess.run([sys.executable, 'akira_complete_system.py'])
        except Exception as e:
            print(f"\n❌ Error: {e}")
    
    def launch_original_system(self):
        """Launch original FaceConnect system"""
        print("\n🔷 Launching Original FaceConnect System...")
        print("="*79 + "\n")
        
        try:
            subprocess.run([sys.executable, 'main.py'])
        except Exception as e:
            print(f"\n❌ Error: {e}")
    
    def launch_ai_engineering(self):
        """Launch AI Engineering module"""
        print("\n🔧 Launching AI Engineering Module...")
        print("="*79 + "\n")
        
        try:
            subprocess.run([sys.executable, 'ai_engineering_standalone.py'])
        except Exception as e:
            print(f"\n❌ Error: {e}")
    
    def show_dashboard(self):
        """Show system dashboard"""
        print("\n📊 System Dashboard")
        print("="*79)
        
        # Check module availability
        print("\n  Module Status:")
        print("  " + "-"*75)
        
        modules = {
            'Virtual Assistant': 'akira_assistant.py',
            'Smart Surveillance': 'smart_surveillance.py',
            'Marketing AI': 'personalized_marketing.py',
            'Face Recognition': 'face_recognition_module.py',
            'Advanced AI Engine': 'advanced_ai_engine.py',
            'IoT Integration': 'iot_integration.py',
            'Database Manager': 'database_manager.py',
            'Notification System': 'notification_system.py',
            'Voice Assistant': 'enhanced_voice_assistant.py',
            'Web Dashboard': 'web_dashboard.py',
            'AI Engineering': 'ai_engineering_module.py'
        }
        
        for name, file in modules.items():
            status = "✅ Available" if os.path.exists(file) else "❌ Missing"
            print(f"  {name:.<50} {status}")
        
        print("\n  System Files:")
        print("  " + "-"*75)
        
        files = {
            'Main Application': 'main.py',
            'Complete System': 'akira_complete_system.py',
            'Web Interface': 'flask_app.py',
            'AI Engineering': 'ai_engineering_standalone.py'
        }
        
        for name, file in files.items():
            status = "✅ Ready" if os.path.exists(file) else "❌ Missing"
            print(f"  {name:.<50} {status}")
        
        print("\n  " + "="*75)
        print(f"  Total Modules: {len([f for f in modules.values() if os.path.exists(f)])}/11")
        print(f"  System Status: {'🟢 Operational' if len([f for f in modules.values() if os.path.exists(f)]) > 5 else '🟡 Partial'}")
        print("  " + "="*75)
    
    def open_documentation(self):
        """Open documentation"""
        print("\n📚 Documentation")
        print("="*79)
        print("""
  Available Documentation:
  
  1. START_HERE.md - Quick start guide
  2. INSTALLATION_GUIDE.md - Installation instructions
  3. WEB_INTERFACE_GUIDE.md - Web and API documentation
  4. AI_ENGINEERING_GUIDE.md - ML model training guide
  5. COMPLETE_SETUP_GUIDE.md - Complete setup instructions
  6. FEATURES.md - All features listed
  7. README.md - Main documentation
  8. INSTRUCTIONS.txt - Simple text instructions
        """)
        
        choice = input("\n  Enter number to open (or press Enter to skip): ").strip()
        
        docs = {
            '1': 'START_HERE.md',
            '2': 'INSTALLATION_GUIDE.md',
            '3': 'WEB_INTERFACE_GUIDE.md',
            '4': 'AI_ENGINEERING_GUIDE.md',
            '5': 'COMPLETE_SETUP_GUIDE.md',
            '6': 'FEATURES.md',
            '7': 'README.md',
            '8': 'INSTRUCTIONS.txt'
        }
        
        if choice in docs:
            try:
                if os.name == 'nt':  # Windows
                    os.startfile(docs[choice])
                else:  # Linux/Mac
                    subprocess.run(['xdg-open', docs[choice]])
                print(f"\n  ✅ Opened {docs[choice]}")
            except Exception as e:
                print(f"\n  ❌ Error opening file: {e}")
    
    def system_status_check(self):
        """Check system status"""
        print("\n🔍 System Status Check")
        print("="*79)
        
        print("\n  Checking Python packages...")
        print("  " + "-"*75)
        
        packages = {
            'numpy': 'Core numerical computing',
            'sklearn': 'Machine learning',
            'nltk': 'Natural language processing',
            'cv2': 'Computer vision',
            'pyttsx3': 'Text-to-speech',
            'flask': 'Web framework',
            'speech_recognition': 'Voice recognition'
        }
        
        for package, description in packages.items():
            try:
                __import__(package)
                print(f"  ✅ {package:.<30} {description}")
            except ImportError:
                print(f"  ❌ {package:.<30} {description} (Not installed)")
        
        print("\n  " + "="*75)
        print("  Run 'install_all.bat' to install missing packages")
        print("  " + "="*75)
    
    def installation_guide(self):
        """Show installation guide"""
        print("\n⚙️  Installation Guide")
        print("="*79)
        print("""
  QUICK INSTALLATION:
  
  Step 1: Run the installation script
          → Double-click: install_all.bat
          → Or run: pip install -r requirements.txt
  
  Step 2: Wait for installation to complete (5-15 minutes)
  
  Step 3: Launch the system
          → Use this launcher (recommended)
          → Or run: start_web.bat
  
  WHAT GETS INSTALLED:
  
  ✓ numpy, scikit-learn, nltk (AI/ML)
  ✓ opencv-python (Computer Vision)
  ✓ pyttsx3, SpeechRecognition (Voice)
  ✓ flask, requests (Web)
  ✓ face_recognition, dlib (Optional)
  
  TROUBLESHOOTING:
  
  • If face_recognition fails: Skip it, system works without it
  • If pyaudio fails: Voice input won't work, but everything else will
  • If any package fails: Install what works, skip what fails
  
  For detailed help, see: INSTALLATION_GUIDE.md
        """)
        print("="*79)
    
    def run(self):
        """Main run loop"""
        while True:
            self.display_header()
            self.display_ai_architecture()
            self.main_menu()
            
            choice = input("\n  Enter your choice: ").strip()
            
            if choice == '1':
                if self.modules_available['flask']:
                    self.launch_web_interface()
                else:
                    print("\n  ❌ Flask app not found. Please check installation.")
                    input("\n  Press Enter to continue...")
            
            elif choice == '2':
                if self.modules_available['complete']:
                    self.launch_complete_system()
                else:
                    print("\n  ❌ Complete system not found. Please check installation.")
                    input("\n  Press Enter to continue...")
            
            elif choice == '3':
                if self.modules_available['main']:
                    self.launch_original_system()
                else:
                    print("\n  ❌ Main system not found. Please check installation.")
                    input("\n  Press Enter to continue...")
            
            elif choice == '4':
                if self.modules_available['ai_engineering']:
                    self.launch_ai_engineering()
                else:
                    print("\n  ❌ AI Engineering module not found. Please check installation.")
                    input("\n  Press Enter to continue...")
            
            elif choice == '5':
                self.show_dashboard()
                input("\n  Press Enter to continue...")
            
            elif choice == '6':
                self.open_documentation()
                input("\n  Press Enter to continue...")
            
            elif choice == '7':
                self.system_status_check()
                input("\n  Press Enter to continue...")
            
            elif choice == '8':
                self.installation_guide()
                input("\n  Press Enter to continue...")
            
            elif choice == '0':
                print("\n  👋 Thank you for using AKIRA AI System!")
                print("  " + "="*75)
                break
            
            else:
                print("\n  ❌ Invalid choice. Please try again.")
                input("\n  Press Enter to continue...")


def main():
    """Main entry point"""
    try:
        launcher = AkiraUnifiedLauncher()
        launcher.run()
    except KeyboardInterrupt:
        print("\n\n  👋 System interrupted. Goodbye!")
    except Exception as e:
        print(f"\n  ❌ Error: {e}")
        input("\n  Press Enter to exit...")


if __name__ == "__main__":
    main()
