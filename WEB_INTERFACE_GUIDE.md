# AKIRA Web Interface Guide

## 🌐 Overview

The AKIRA Web Interface provides a modern, browser-based control panel for your AI system. Access all features through an intuitive web dashboard.

## 🚀 Quick Start

### Method 1: Using the Start Script (Easiest)
```bash
start_web.bat
```

### Method 2: Manual Start
```bash
python flask_app.py
```

### Access the Application
Open your browser and navigate to:
```
http://localhost:5000
```

## 📱 Available Pages

### 1. Home Page
**URL:** `http://localhost:5000`

Main landing page with quick access to all modules:
- Dashboard
- Virtual Assistant
- IoT Control
- Surveillance
- Marketing
- Notifications

### 2. Dashboard
**URL:** `http://localhost:5000/dashboard`

Real-time system monitoring:
- System metrics (CPU, Memory, Users)
- Module status
- Performance indicators
- Quick actions

### 3. Virtual Assistant
**URL:** `http://localhost:5000/assistant`

Interact with Akira AI:
- Send commands
- View task list
- Get AI responses
- Task automation

### 4. IoT Control
**URL:** `http://localhost:5000/iot`

Control smart home devices:
- Lights (on/off/dim)
- Thermostat (temperature control)
- Locks (lock/unlock)
- Cameras
- Speakers

### 5. Surveillance
**URL:** `http://localhost:5000/surveillance`

Security monitoring:
- View alerts
- Access logs
- Authorized persons
- Security status

### 6. Marketing
**URL:** `http://localhost:5000/marketing`

Customer management:
- Customer insights
- Campaign creation
- Analytics
- Segmentation

## 🔌 API Endpoints

### System Status
```
GET /api/status
```
Returns system status and availability

**Response:**
```json
{
  "status": "online",
  "timestamp": "2024-01-01T12:00:00",
  "modules_available": true
}
```

### Virtual Assistant

**Send Command**
```
POST /api/assistant/command
Content-Type: application/json

{
  "command": "Schedule meeting tomorrow at 3 PM"
}
```

**Get Tasks**
```
GET /api/assistant/tasks
```

### IoT Control

**List Devices**
```
GET /api/iot/devices
```

**Control Device**
```
POST /api/iot/control
Content-Type: application/json

{
  "device_id": "light_001",
  "action": "on",
  "params": {
    "brightness": 80
  }
}
```

**Voice Control**
```
POST /api/iot/voice
Content-Type: application/json

{
  "command": "Turn on the lights"
}
```

**Energy Monitoring**
```
GET /api/iot/energy
```

### Surveillance

**Get Status**
```
GET /api/surveillance/status
```

**Get Alerts**
```
GET /api/surveillance/alerts
```

### Marketing

**Get Customer Insights**
```
GET /api/marketing/customers
```

**Create Campaign**
```
POST /api/marketing/campaign
Content-Type: application/json

{
  "segment": "High-Value",
  "offer_type": "VIP Discount"
}
```

### AI Predictions

**Get Predictions**
```
POST /api/ai/predict
Content-Type: application/json

{
  "user_id": "user_001"
}
```

### Notifications

**Send Notification**
```
POST /api/notifications/send
Content-Type: application/json

{
  "type": "email",
  "recipient": "user@example.com",
  "message": "Your notification message"
}
```

### Dashboard

**Get Metrics**
```
GET /api/dashboard/metrics
```

**Generate Report**
```
GET /api/dashboard/report?type=daily
```

## 💻 Using the API with Code

### Python Example
```python
import requests

# Base URL
base_url = "http://localhost:5000"

# Send command to assistant
response = requests.post(
    f"{base_url}/api/assistant/command",
    json={"command": "What's the weather?"}
)
print(response.json())

# Control IoT device
response = requests.post(
    f"{base_url}/api/iot/control",
    json={
        "device_id": "light_001",
        "action": "on",
        "params": {"brightness": 80}
    }
)
print(response.json())

# Get system metrics
response = requests.get(f"{base_url}/api/dashboard/metrics")
print(response.json())
```

### JavaScript Example
```javascript
// Send command to assistant
fetch('http://localhost:5000/api/assistant/command', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        command: "Schedule meeting tomorrow"
    })
})
.then(response => response.json())
.then(data => console.log(data));

// Control IoT device
fetch('http://localhost:5000/api/iot/control', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        device_id: 'light_001',
        action: 'on',
        params: { brightness: 80 }
    })
})
.then(response => response.json())
.then(data => console.log(data));
```

### cURL Example
```bash
# Get system status
curl http://localhost:5000/api/status

# Send assistant command
curl -X POST http://localhost:5000/api/assistant/command \
  -H "Content-Type: application/json" \
  -d '{"command": "What time is it?"}'

# Control IoT device
curl -X POST http://localhost:5000/api/iot/control \
  -H "Content-Type: application/json" \
  -d '{"device_id": "light_001", "action": "on", "params": {"brightness": 80}}'
```

## 🔧 Configuration

### Change Port
Edit `flask_app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Change 5000 to 8080
```

### Enable HTTPS
Install flask-tls:
```bash
pip install flask-tls
```

Update `flask_app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000, ssl_context='adhoc')
```

### Allow External Access
By default, the server is accessible from any device on your network.

To restrict to localhost only:
```python
app.run(debug=True, host='127.0.0.1', port=5000)
```

## 🎨 Customization

### Add Custom Pages
Create new HTML templates in `templates/` folder:

```html
<!-- templates/custom_page.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Custom Page</title>
</head>
<body>
    <h1>My Custom Page</h1>
</body>
</html>
```

Add route in `flask_app.py`:
```python
@app.route('/custom')
def custom_page():
    return render_template('custom_page.html')
```

### Add Custom API Endpoints
```python
@app.route('/api/custom/endpoint', methods=['POST'])
def custom_endpoint():
    data = request.get_json()
    # Your custom logic here
    return jsonify({'result': 'success'})
```

## 🔒 Security

### Production Deployment

1. **Change Secret Key**
```python
app.config['SECRET_KEY'] = 'your-secure-random-key-here'
```

2. **Disable Debug Mode**
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

3. **Add Authentication**
```python
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    # Your authentication logic
    return username == 'admin' and password == 'secure_password'

@app.route('/api/protected')
@auth.login_required
def protected():
    return jsonify({'message': 'Authenticated!'})
```

4. **Use HTTPS**
Always use HTTPS in production

5. **Rate Limiting**
```bash
pip install flask-limiter
```

```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/api/endpoint')
@limiter.limit("10 per minute")
def limited_endpoint():
    return jsonify({'message': 'Rate limited'})
```

## 📊 Monitoring

### View Logs
Flask logs appear in the console where you started the server.

### Access Logs
Enable access logging:
```python
import logging
logging.basicConfig(level=logging.INFO)
```

### Error Handling
Custom error pages are already configured:
- 404: Not Found
- 500: Internal Server Error

## 🐛 Troubleshooting

### Issue: Port Already in Use
**Solution:** Change the port or kill the process using port 5000
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Or change port in flask_app.py
```

### Issue: Cannot Access from Other Devices
**Solution:** Check firewall settings and ensure host is '0.0.0.0'

### Issue: Modules Not Available
**Solution:** Install required packages
```bash
pip install -r requirements.txt
```

### Issue: Templates Not Found
**Solution:** Ensure `templates/` folder exists with HTML files

## 🚀 Deployment Options

### Option 1: Local Development
```bash
python flask_app.py
```

### Option 2: Production Server (Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 flask_app:app
```

### Option 3: Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "flask_app.py"]
```

### Option 4: Cloud Deployment
- Heroku
- AWS Elastic Beanstalk
- Google Cloud Run
- Azure App Service

## 📱 Mobile Access

Access from mobile devices on the same network:
```
http://<your-computer-ip>:5000
```

Find your IP:
```bash
ipconfig  # Windows
```

## 🎯 Best Practices

1. **Always use HTTPS in production**
2. **Implement authentication**
3. **Enable rate limiting**
4. **Monitor logs**
5. **Regular backups**
6. **Keep dependencies updated**
7. **Use environment variables for secrets**
8. **Implement CORS properly**
9. **Validate all inputs**
10. **Handle errors gracefully**

## 📚 Additional Resources

- Flask Documentation: https://flask.palletsprojects.com/
- REST API Best Practices
- Web Security Guidelines
- AKIRA System Documentation

---

**AKIRA Web Interface - Control Your AI System from Anywhere** 🌐
