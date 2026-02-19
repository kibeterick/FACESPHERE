# Quick Actions Guide - AKIRA System

## 🚀 Overview

Quick Actions are now fully functional across all pages! They automatically navigate you to the right place or perform actions instantly.

---

## 📊 Dashboard Quick Actions

**Location:** http://localhost:5000/dashboard

| Action | What It Does |
|--------|--------------|
| 📄 Generate Report | Opens a beautiful formatted report in new tab |
| 🤖 Open Assistant | Takes you to AI assistant chat |
| 🏠 Control IoT | Opens IoT device control panel |
| 🎥 View Surveillance | Opens surveillance monitoring |

---

## 🤖 Assistant Quick Actions

**Location:** http://localhost:5000/assistant

| Action | What It Does |
|--------|--------------|
| ⏰ Time | Automatically asks "What time is it?" |
| 🌤️ Weather | Automatically asks "What is the weather?" |
| 📋 Tasks | Automatically asks "Show my tasks" |
| 💡 Lights | Automatically asks "Turn on living room light" |
| 🏠 IoT Control | Takes you to IoT control panel |

**How it works:** Click any button and it automatically fills the command and sends it to Akira!

---

## 🏠 IoT Quick Actions

**Location:** http://localhost:5000/iot

| Action | What It Does |
|--------|--------------|
| 💡 All Lights ON | Turns on all lights in your home |
| 🌙 All Lights OFF | Turns off all lights |
| 🏠 Comfort Mode | Sets temperature to 72°F + turns on lights |
| 🚪 Away Mode | Locks doors + turns off lights + sets temp to 68°F |
| 📊 View Dashboard | Takes you to main dashboard |

**Comfort Mode includes:**
- Temperature set to 72°F
- Lights turned on
- System optimized for comfort

**Away Mode includes:**
- All lights turned off
- Doors locked
- Temperature set to 68°F (energy saving)
- Security enabled

---

## 🎥 Surveillance Quick Actions

**Location:** http://localhost:5000/surveillance

| Action | What It Does |
|--------|--------------|
| 📹 Enable All Cameras | Activates all 4 cameras for full coverage |
| 🚨 Lockdown Mode | Maximum security: locks doors, enables cameras, alerts authorities |
| ➕ Add Person | Add new authorized person to access list |
| 📺 Live Feeds | View all camera feeds in real-time |
| 📊 Dashboard | Return to main dashboard |

**Lockdown Mode includes:**
- All doors locked
- All cameras recording
- Authorities notified
- Alarm system armed

---

## 📈 Marketing Quick Actions

**Location:** http://localhost:5000/marketing

| Action | What It Does |
|--------|--------------|
| 📧 Create Campaign | Prompts for campaign name and creates it automatically |
| 👥 Segment Customers | Automatically segments customers by value (High/Medium/Low) |
| 📊 View Analytics | Opens marketing analytics report |

**Create Campaign:**
1. Click button
2. Enter campaign name
3. Campaign is created and activated automatically!

**Segment Customers:**
- Automatically analyzes all customers
- Creates High-Value, Medium-Value, Low-Value segments
- Shows results instantly

---

## 🎯 How Quick Actions Work

### Automatic Navigation
Quick Actions automatically take you to the right page:
```javascript
onclick="location.href='/assistant'"  // Goes to assistant page
```

### Automatic Commands
Quick Actions can send commands automatically:
```javascript
function quickCommand(command) {
    document.getElementById('commandInput').value = command;
    sendCommand();  // Sends automatically!
}
```

### Automatic API Calls
Quick Actions can call APIs and perform actions:
```javascript
fetch('/api/iot/control', {
    method: 'POST',
    body: JSON.stringify({device_id: 'light_001', action: 'on'})
})
```

---

## 💡 Benefits

### 1. One-Click Actions
No need to type commands or navigate menus - just click!

### 2. Smart Automation
Actions perform multiple tasks automatically:
- Away Mode: locks doors + turns off lights + adjusts temperature
- Comfort Mode: optimizes everything for comfort
- Lockdown Mode: maximum security with one click

### 3. Instant Feedback
Every action shows confirmation:
- ✅ Success messages
- 📊 Status updates
- 🔔 Notifications

### 4. Context-Aware
Quick Actions are relevant to each page:
- Dashboard: Navigation to other pages
- Assistant: Common questions
- IoT: Device control modes
- Surveillance: Security actions
- Marketing: Campaign management

---

## 🔧 Technical Details

### Frontend (JavaScript)
```javascript
function setComfortMode() {
    // Multiple API calls in sequence
    controlDevice('thermo_001', 'set', {temperature: 72});
    controlDevice('light_001', 'on');
    alert('✅ Comfort Mode Activated!');
}
```

### Backend (Flask API)
```python
@app.route('/api/iot/control', methods=['POST'])
def api_iot_control():
    data = request.get_json()
    device_id = data.get('device_id')
    action = data.get('action')
    # Perform action...
    return jsonify({'result': 'Success'})
```

---

## 📱 Mobile Friendly

All Quick Actions work on mobile devices:
- Touch-friendly buttons
- Responsive design
- Works on all screen sizes

---

## 🎨 Customization

You can add your own Quick Actions by editing the templates:

### Example: Add Custom Action
```html
<button onclick="myCustomAction()">🎯 My Action</button>

<script>
function myCustomAction() {
    // Your custom code here
    alert('Custom action executed!');
}
</script>
```

---

## 🚀 Usage Examples

### Example 1: Leaving Home
1. Go to IoT page
2. Click "🚪 Away Mode"
3. Everything is secured automatically!

### Example 2: Quick Question
1. Go to Assistant page
2. Click "⏰ Time" button
3. Get instant answer!

### Example 3: Security Alert
1. Go to Surveillance page
2. Click "🚨 Lockdown Mode"
3. Maximum security activated!

### Example 4: Marketing Campaign
1. Go to Marketing page
2. Click "📧 Create Campaign"
3. Enter name
4. Campaign is live!

---

## ✅ What's New

### Before:
- Buttons showed "Feature coming soon!"
- Had to manually navigate
- Had to type every command

### After:
- All buttons are functional
- Automatic navigation
- One-click actions
- Smart automation
- Instant feedback

---

## 🎉 Summary

Quick Actions transform your AKIRA system into a truly automated experience:

✅ **No more typing** - Just click buttons
✅ **No more navigation** - Automatic page switching
✅ **No more multiple steps** - One click does it all
✅ **Smart automation** - Multiple actions combined
✅ **Instant results** - Immediate feedback

**Your system now works FOR you, not the other way around!**

---

## 📞 Quick Reference

| Page | Quick Actions Count | Most Useful |
|------|---------------------|-------------|
| Dashboard | 4 | Generate Report |
| Assistant | 5 | Quick Commands |
| IoT | 5 | Comfort/Away Mode |
| Surveillance | 5 | Lockdown Mode |
| Marketing | 3 | Create Campaign |

**Total: 22 Quick Actions across all pages!**

---

**Enjoy your fully automated AKIRA system!** 🚀

