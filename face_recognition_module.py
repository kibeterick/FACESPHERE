import os
import pickle
from datetime import datetime

# Face recognition capabilities
try:
    import cv2
    import face_recognition
    FACE_RECOGNITION_AVAILABLE = True
except ImportError:
    FACE_RECOGNITION_AVAILABLE = False
    print("⚠️  Face recognition not available. Install opencv-python and face_recognition.")


class FaceConnect:
    """FaceConnect - Facial Recognition System"""
    
    def __init__(self, data_dir="face_data"):
        self.data_dir = data_dir
        self.known_faces = {}
        self.known_encodings = []
        self.known_names = []
        self.camera = None
        
        # Create data directory if it doesn't exist
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            
        # Load existing face data
        self.load_face_data()
        
    def load_face_data(self):
        """Load saved face encodings"""
        face_data_file = os.path.join(self.data_dir, "face_encodings.pkl")
        
        if os.path.exists(face_data_file):
            try:
                with open(face_data_file, 'rb') as f:
                    data = pickle.load(f)
                    self.known_encodings = data['encodings']
                    self.known_names = data['names']
                    print(f"✅ Loaded {len(self.known_names)} known faces")
            except Exception as e:
                print(f"⚠️  Could not load face data: {e}")
        else:
            print("ℹ️  No existing face data found. Starting fresh.")
            
    def save_face_data(self):
        """Save face encodings to file"""
        face_data_file = os.path.join(self.data_dir, "face_encodings.pkl")
        
        try:
            data = {
                'encodings': self.known_encodings,
                'names': self.known_names
            }
            with open(face_data_file, 'wb') as f:
                pickle.dump(data, f)
            print("✅ Face data saved successfully")
        except Exception as e:
            print(f"❌ Error saving face data: {e}")
            
    def register_face(self, name, image_path=None):
        """Register a new face"""
        if not FACE_RECOGNITION_AVAILABLE:
            print("❌ Face recognition libraries not installed")
            return False
            
        try:
            if image_path:
                # Load image from file
                image = face_recognition.load_image_file(image_path)
            else:
                # Capture from camera
                print("📸 Please look at the camera...")
                image = self.capture_from_camera()
                
                if image is None:
                    return False
                    
            # Find face encodings
            face_encodings = face_recognition.face_encodings(image)
            
            if len(face_encodings) == 0:
                print("❌ No face detected in the image")
                return False
                
            if len(face_encodings) > 1:
                print("⚠️  Multiple faces detected. Using the first one.")
                
            # Add to known faces
            self.known_encodings.append(face_encodings[0])
            self.known_names.append(name)
            
            # Save to file
            self.save_face_data()
            
            print(f"✅ Successfully registered face for {name}")
            return True
            
        except Exception as e:
            print(f"❌ Error registering face: {e}")
            return False
            
    def capture_from_camera(self):
        """Capture image from camera"""
        if not FACE_RECOGNITION_AVAILABLE:
            return None
            
        try:
            camera = cv2.VideoCapture(0)
            
            if not camera.isOpened():
                print("❌ Could not access camera")
                return None
                
            print("📸 Capturing in 3 seconds...")
            import time
            time.sleep(3)
            
            ret, frame = camera.read()
            camera.release()
            
            if ret:
                # Convert BGR to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                return rgb_frame
            else:
                print("❌ Failed to capture image")
                return None
                
        except Exception as e:
            print(f"❌ Camera error: {e}")
            return None
            
    def recognize_face(self, image_path=None):
        """Recognize face from image or camera"""
        if not FACE_RECOGNITION_AVAILABLE:
            print("❌ Face recognition libraries not installed")
            return None
            
        if len(self.known_encodings) == 0:
            print("⚠️  No registered faces. Please register a face first.")
            return None
            
        try:
            if image_path:
                image = face_recognition.load_image_file(image_path)
            else:
                print("📸 Looking at camera...")
                image = self.capture_from_camera()
                
                if image is None:
                    return None
                    
            # Find faces in the image
            face_locations = face_recognition.face_locations(image)
            face_encodings = face_recognition.face_encodings(image, face_locations)
            
            if len(face_encodings) == 0:
                print("❌ No face detected")
                return None
                
            # Compare with known faces
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
                name = "Unknown"
                
                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.known_names[first_match_index]
                    
                return name
                
            return "Unknown"
            
        except Exception as e:
            print(f"❌ Error recognizing face: {e}")
            return None
            
    def start_continuous_recognition(self, callback=None):
        """Start continuous face recognition from camera"""
        if not FACE_RECOGNITION_AVAILABLE:
            print("❌ Face recognition libraries not installed")
            return
            
        try:
            camera = cv2.VideoCapture(0)
            
            if not camera.isOpened():
                print("❌ Could not access camera")
                return
                
            print("🎥 Starting continuous face recognition...")
            print("Press 'q' to quit")
            
            while True:
                ret, frame = camera.read()
                
                if not ret:
                    break
                    
                # Convert BGR to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Find faces
                face_locations = face_recognition.face_locations(rgb_frame)
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                
                # Recognize faces
                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                    matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
                    name = "Unknown"
                    
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = self.known_names[first_match_index]
                        
                    # Draw rectangle and name
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)
                    
                    # Call callback if provided
                    if callback and name != "Unknown":
                        callback(name)
                        
                # Display the frame
                cv2.imshow('FaceConnect - Face Recognition', frame)
                
                # Break on 'q' key
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
            camera.release()
            cv2.destroyAllWindows()
            
        except Exception as e:
            print(f"❌ Error in continuous recognition: {e}")
            
    def detect_stranger(self):
        """Detect if an unknown person is present"""
        name = self.recognize_face()
        
        if name == "Unknown":
            print("⚠️  STRANGER DETECTED!")
            return True
        elif name:
            print(f"✅ Recognized: {name}")
            return False
        else:
            return None
            
    def get_registered_users(self):
        """Get list of registered users"""
        return self.known_names.copy()
