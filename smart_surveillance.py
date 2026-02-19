"""
Smart Surveillance System with Object Detection and Anomaly Detection
"""
import time
from datetime import datetime
import threading

try:
    import cv2
    import numpy as np
    CV_AVAILABLE = True
except ImportError:
    CV_AVAILABLE = False
    print("⚠️  OpenCV not available. Install opencv-python for surveillance features.")


class SmartSurveillance:
    """Smart Surveillance System with AI capabilities"""
    
    def __init__(self):
        self.is_monitoring = False
        self.detected_objects = []
        self.access_log = []
        self.alerts = []
        self.authorized_persons = []
        
        # Load pre-trained models
        if CV_AVAILABLE:
            try:
                # YOLO or Haar Cascade for object detection
                self.face_cascade = cv2.CascadeClassifier(
                    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
                )
                self.body_cascade = cv2.CascadeClassifier(
                    cv2.data.haarcascades + 'haarcascade_fullbody.xml'
                )
            except:
                print("⚠️  Could not load detection models")
    
    def start_monitoring(self, camera_id=0):
        """Start surveillance monitoring"""
        if not CV_AVAILABLE:
            print("❌ OpenCV not available")
            return
        
        self.is_monitoring = True
        print("🎥 Starting smart surveillance...")
        
        try:
            camera = cv2.VideoCapture(camera_id)
            
            if not camera.isOpened():
                print("❌ Could not access camera")
                return
            
            frame_count = 0
            
            while self.is_monitoring:
                ret, frame = camera.read()
                
                if not ret:
                    break
                
                frame_count += 1
                
                # Process every 5th frame for efficiency
                if frame_count % 5 == 0:
                    # Detect objects
                    detections = self.detect_objects(frame)
                    
                    # Check for anomalies
                    if self.detect_anomaly(detections):
                        self.trigger_alert("Anomaly detected!", detections)
                    
                    # Draw detections
                    frame = self.draw_detections(frame, detections)
                
                # Display frame
                cv2.imshow('Smart Surveillance', frame)
                
                # Break on 'q' key
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.is_monitoring = False
                    break
            
            camera.release()
            cv2.destroyAllWindows()
            
        except Exception as e:
            print(f"❌ Surveillance error: {e}")
    
    def detect_objects(self, frame):
        """Detect objects in frame"""
        detections = []
        
        if not CV_AVAILABLE:
            return detections
        
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                detections.append({
                    'type': 'face',
                    'bbox': (x, y, w, h),
                    'confidence': 0.9,
                    'timestamp': datetime.now()
                })
            
            # Detect bodies
            bodies = self.body_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in bodies:
                detections.append({
                    'type': 'person',
                    'bbox': (x, y, w, h),
                    'confidence': 0.85,
                    'timestamp': datetime.now()
                })
        
        except Exception as e:
            print(f"Detection error: {e}")
        
        return detections
    
    def draw_detections(self, frame, detections):
        """Draw bounding boxes on frame"""
        for det in detections:
            x, y, w, h = det['bbox']
            color = (0, 255, 0) if det['type'] == 'face' else (255, 0, 0)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            
            label = f"{det['type']} ({det['confidence']:.2f})"
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 
                       0.5, color, 2)
        
        return frame
    
    def detect_anomaly(self, detections):
        """Detect anomalies in surveillance data"""
        # Anomaly rules
        
        # Rule 1: Too many people detected
        person_count = sum(1 for d in detections if d['type'] in ['face', 'person'])
        if person_count > 5:
            return True
        
        # Rule 2: Detection at unusual hours
        hour = datetime.now().hour
        if (hour < 6 or hour > 22) and person_count > 0:
            return True
        
        # Rule 3: Rapid movement detection (future enhancement)
        
        return False
    
    def trigger_alert(self, message, detections):
        """Trigger security alert"""
        alert = {
            'message': message,
            'timestamp': datetime.now(),
            'detections': len(detections),
            'severity': 'high'
        }
        
        self.alerts.append(alert)
        print(f"\n🚨 ALERT: {message}")
        print(f"   Time: {alert['timestamp'].strftime('%H:%M:%S')}")
        print(f"   Detections: {len(detections)}")
    
    def check_access_control(self, person_id):
        """Check if person is authorized"""
        if person_id in self.authorized_persons:
            self.log_access(person_id, "granted")
            return True
        else:
            self.log_access(person_id, "denied")
            self.trigger_alert(f"Unauthorized access attempt by {person_id}", [])
            return False
    
    def log_access(self, person_id, status):
        """Log access attempts"""
        log_entry = {
            'person_id': person_id,
            'status': status,
            'timestamp': datetime.now()
        }
        self.access_log.append(log_entry)
    
    def add_authorized_person(self, person_id):
        """Add person to authorized list"""
        self.authorized_persons.append(person_id)
        print(f"✅ Added {person_id} to authorized persons")
    
    def get_alerts(self):
        """Get all alerts"""
        if not self.alerts:
            return "No alerts"
        
        alert_list = "\n".join([
            f"- {a['message']} at {a['timestamp'].strftime('%H:%M:%S')}"
            for a in self.alerts[-10:]  # Last 10 alerts
        ])
        return f"🚨 Recent Alerts:\n{alert_list}"
    
    def get_access_log(self):
        """Get access log"""
        if not self.access_log:
            return "No access logs"
        
        log_list = "\n".join([
            f"- {l['person_id']}: {l['status']} at {l['timestamp'].strftime('%H:%M:%S')}"
            for l in self.access_log[-10:]  # Last 10 entries
        ])
        return f"📋 Access Log:\n{log_list}"
    
    def analyze_patterns(self):
        """Analyze surveillance patterns using ML"""
        # Basic pattern analysis
        if len(self.detected_objects) < 10:
            return "Not enough data for pattern analysis"
        
        # Analyze peak hours
        hours = [d['timestamp'].hour for d in self.detected_objects if 'timestamp' in d]
        if hours:
            from collections import Counter
            hour_counts = Counter(hours)
            peak_hour = hour_counts.most_common(1)[0][0]
            return f"📊 Peak activity hour: {peak_hour}:00"
        
        return "Pattern analysis complete"
