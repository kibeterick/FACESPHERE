# Complete API Keys Setup Guide

## Current Status

Your `.env` file is ready but needs API keys to be added. Here's what you have:

```
GEMINI_API_KEY=          ← Empty (needed for AI responses)
OPENAI_API_KEY=          ← Empty (optional)
GOOGLE_API_KEY=          ← Empty (optional)
WEATHER_API_KEY=         ← Empty (optional, for real weather)
NEWS_API_KEY=            ← Empty (optional)
```

---

## 🔑 Priority 1: Gemini API Key (REQUIRED for AI)

### What It Does:
- Powers intelligent AI responses
- Enables natural conversations
- Required for Virtual Assistant page
- Makes your system truly intelligent

### How to Get It:

1. **Visit Google AI Studio:**
   - Go to: https://makersuite.google.com/app/apikey
   - Or: https://aistudio.google.com/app/apikey

2. **Sign In:**
   - Use your Google account (any Gmail account works)

3. **Create API Key:**
   - Click "Create API Key" button
   - Select "Create API key in new project" (or use existing)
   - Copy the key (starts with `AIza`)

4. **Add to .env:**
   ```
   GEMINI_API_KEY=AIzaSyABC123def456GHI789jkl012MNO345pqr
   ```

5. **Restart Server:**
   ```bash
   python flask_app.py
   ```

### Free Tier:
- ✅ 60 requests per minute
- ✅ 1,500 requests per day
- ✅ Free forever!

---

## 🌤️ Priority 2: Weather API Key (OPTIONAL)

### What It Does:
- Shows real weather data
- 5-day forecasts
- Current conditions
- Without it: Uses simulated weather (still works!)

### How to Get It:

1. **Visit OpenWeatherMap:**
   - Go to: https://openweathermap.org/api

2. **Sign Up:**
   - Click "Sign Up" (free account)
   - Verify your email

3. **Get API Key:**
   - Go to "API Keys" section
   - Copy your default key
   - Or create a new one

4. **Add to .env:**
   ```
   WEATHER_API_KEY=your_openweathermap_key_here
   ```

5. **Restart Server**

### Free Tier:
- ✅ 60 calls per minute
- ✅ 1,000,000 calls per month
- ✅ Current weather + 5-day forecast

---

## 🔍 Priority 3: Google API Key (OPTIONAL)

### What It Does:
- Google Cloud services
- Maps integration (future)
- Additional Google services
- Not required for current features

### How to Get It:

1. **Visit Google Cloud Console:**
   - Go to: https://console.cloud.google.com/

2. **Create Project:**
   - Click "Select a project" → "New Project"
   - Name it (e.g., "AKIRA System")

3. **Enable APIs:**
   - Go to "APIs & Services" → "Library"
   - Enable the APIs you need

4. **Create Credentials:**
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "API Key"
   - Copy the key

5. **Add to .env:**
   ```
   GOOGLE_API_KEY=your_google_cloud_api_key
   ```

---

## 🤖 Priority 4: OpenAI API Key (OPTIONAL)

### What It Does:
- Alternative to Gemini
- GPT models access
- Not required (Gemini is primary)

### How to Get It:

1. **Visit OpenAI:**
   - Go to: https://platform.openai.com/

2. **Sign Up:**
   - Create account
   - Add payment method (required)

3. **Get API Key:**
   - Go to API Keys section
   - Create new key
   - Copy it

4. **Add to .env:**
   ```
   OPENAI_API_KEY=sk-proj-...
   ```

### Note:
- ⚠️ Not free (pay per use)
- Not required for AKIRA
- Gemini is recommended

---

## 📰 Priority 5: News API Key (OPTIONAL)

### What It Does:
- Real news headlines
- News integration (future feature)
- Not currently used

### How to Get It:

1. **Visit NewsAPI:**
   - Go to: https://newsapi.org/

2. **Sign Up:**
   - Free account

3. **Get API Key:**
   - Copy from dashboard

4. **Add to .env:**
   ```
   NEWS_API_KEY=your_newsapi_key
   ```

---

## 📝 How to Add API Keys

### Method 1: Manual Edit (Easy)

1. **Open `.env` file** in your project folder

2. **Find the line** for the API key you want to add

3. **Add your key** after the `=` sign:
   ```
   GEMINI_API_KEY=AIzaSyABC123def456GHI789jkl012MNO345pqr
   ```

4. **Save the file**

5. **Restart the server:**
   ```bash
   python flask_app.py
   ```

### Method 2: Tell Me (I'll Update)

Just provide your API keys and I'll update the `.env` file for you:

**Example:**
```
My Gemini API key is: AIzaSyABC123def456GHI789jkl012MNO345pqr
My Weather API key is: abc123def456
```

---

## ✅ Verification

### Check if Gemini API is Working:

1. **Start server:**
   ```bash
   python flask_app.py
   ```

2. **Visit Assistant page:**
   - http://localhost:5000/assistant

3. **Ask a question:**
   - Type: "What is artificial intelligence?"

4. **Check response:**
   - ✅ If you get intelligent answer → Working!
   - ❌ If you see "Enable AI responses..." → Key not set

### Check if Weather API is Working:

1. **Visit Interactive page:**
   - http://localhost:5000/interactive

2. **Click "Refresh Status"**

3. **Check weather section:**
   - ✅ Real data → API working
   - ⚠️ "Simulated" → No API key (still works!)

---

## 🔐 Security Tips

### DO:
- ✅ Keep API keys private
- ✅ Never share them publicly
- ✅ Don't commit `.env` to Git (already in .gitignore)
- ✅ Regenerate if exposed

### DON'T:
- ❌ Share keys in screenshots
- ❌ Post keys online
- ❌ Commit to GitHub
- ❌ Share with untrusted people

---

## 🚨 Troubleshooting

### "Enable AI responses by adding GEMINI_API_KEY"

**Problem:** Gemini API key not set or invalid

**Solutions:**
1. Check `.env` file has the key
2. Verify no extra spaces around key
3. Restart the server
4. Check key starts with `AIza`
5. Try generating new key

### Weather Shows "Simulated"

**Problem:** Weather API key not set

**Solutions:**
1. This is normal without API key
2. System still works with simulated data
3. Add WEATHER_API_KEY for real data
4. Restart server after adding

### API Key Invalid

**Problem:** Key doesn't work

**Solutions:**
1. Double-check you copied entire key
2. Remove any spaces
3. Verify key is activated (may take minutes)
4. Check API limits not exceeded
5. Generate new key

---

## 📊 What Works Without API Keys

### ✅ Works Without Keys:
- IoT Control (full functionality)
- Person Detection (360° scanning)
- Music Player (all features)
- Notifications (complete system)
- User Profiles (all features)
- Emergency Alerts (full system)
- Dashboard (all metrics)
- Surveillance (monitoring)
- Marketing (campaigns)

### ⚠️ Needs Gemini Key:
- AI-powered responses
- Intelligent conversations
- Natural language processing

### ⚠️ Needs Weather Key:
- Real weather data
- (Uses simulated data without key)

---

## 🎯 Recommended Setup

### Minimum (Free):
```
GEMINI_API_KEY=your_gemini_key_here
```
This gives you full AI capabilities!

### Recommended (Free):
```
GEMINI_API_KEY=your_gemini_key_here
WEATHER_API_KEY=your_weather_key_here
```
This gives you AI + real weather!

### Complete (Mostly Free):
```
GEMINI_API_KEY=your_gemini_key_here
WEATHER_API_KEY=your_weather_key_here
GOOGLE_API_KEY=your_google_key_here
```
This gives you everything!

---

## 🚀 Quick Start

### Step 1: Get Gemini Key (2 minutes)
1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with Google
3. Click "Create API Key"
4. Copy the key

### Step 2: Add to .env
1. Open `.env` file
2. Find: `GEMINI_API_KEY=`
3. Add your key: `GEMINI_API_KEY=AIzaSy...`
4. Save file

### Step 3: Restart Server
```bash
python flask_app.py
```

### Step 4: Test It!
1. Visit: http://localhost:5000/assistant
2. Ask: "Hello, how are you?"
3. Get intelligent response!

---

## 📞 Need Help?

### Option 1: Tell Me Your Keys
Just provide your API keys and I'll update the `.env` file for you.

### Option 2: Manual Setup
Follow the guides above to add keys yourself.

### Option 3: Use Without Keys
Most features work without API keys! Only AI responses need Gemini key.

---

## 🎉 Summary

**Current Status:**
- ✅ `.env` file exists and ready
- ⚠️ API keys need to be added
- ✅ System works without keys (limited AI)

**Priority:**
1. **Gemini API Key** - Get this first! (Free, 2 minutes)
2. **Weather API Key** - Optional but nice (Free)
3. **Others** - Optional for future features

**Next Steps:**
1. Get Gemini API key
2. Add to `.env` file
3. Restart server
4. Enjoy full AI capabilities!

---

**Ready to add your API keys?** Just provide them and I'll update the `.env` file for you! 🚀
