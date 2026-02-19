# How to Setup Gemini API Key

## Step 1: Get Your Gemini API Key

1. **Visit Google AI Studio:**
   - Go to: https://makersuite.google.com/app/apikey
   - Or: https://aistudio.google.com/app/apikey

2. **Sign in with your Google Account**
   - Use any Google account (Gmail, etc.)

3. **Create API Key:**
   - Click "Create API Key" button
   - Select "Create API key in new project" (or use existing project)
   - Copy the API key that appears

4. **Important:** Save your API key somewhere safe!

## Step 2: Add API Key to Your System

### Option A: I'll Update It For You (Recommended)
Just provide me your API key and I'll add it to the `.env` file for you.

**Example:**
```
My Gemini API key is: AIzaSyABC123def456GHI789jkl012MNO345pqr
```

### Option B: Manual Update
1. Open the `.env` file in your project folder
2. Find the line: `GEMINI_API_KEY=`
3. Add your key after the `=` sign
4. Save the file

**Before:**
```
GEMINI_API_KEY=
```

**After:**
```
GEMINI_API_KEY=AIzaSyABC123def456GHI789jkl012MNO345pqr
```

## Step 3: Restart Your Server

After adding the key, restart the Flask server:

```bash
# Stop the current server (Ctrl+C)
# Then start it again:
python flask_app.py
```

## Step 4: Test It Works

Visit your assistant page and ask a question:
- http://localhost:5000/assistant
- Type: "What is artificial intelligence?"
- You should get an intelligent AI response!

## Troubleshooting

### "Enable AI responses by adding GEMINI_API_KEY"
- This means the key is not set or is empty
- Check your `.env` file
- Make sure there are no spaces around the key
- Restart the server after adding the key

### "API key invalid"
- Double-check you copied the entire key
- Make sure there are no extra spaces
- Try generating a new key

### Still not working?
1. Check the `.env` file exists in the project root
2. Verify the key starts with `AIza`
3. Make sure you restarted the server
4. Check console for error messages

## Security Tips

⚠️ **IMPORTANT:**
- Never share your API key publicly
- Don't commit `.env` file to Git (it's already in .gitignore)
- Keep your key private
- If exposed, delete it and create a new one

## API Key Format

Gemini API keys look like this:
```
AIzaSyABC123def456GHI789jkl012MNO345pqr
```

- Starts with `AIza`
- About 39 characters long
- Mix of letters and numbers

## Free Tier Limits

Google Gemini Free Tier:
- 60 requests per minute
- 1,500 requests per day
- Free forever!

## What You Can Do With Gemini

Once configured, your AKIRA system can:
- Answer questions intelligently
- Have natural conversations
- Provide recommendations
- Analyze data
- Generate creative content
- Help with tasks
- And much more!

## Quick Setup Summary

1. Get key: https://makersuite.google.com/app/apikey
2. Tell me your key OR add to `.env` file manually
3. Restart server: `python flask_app.py`
4. Test at: http://localhost:5000/assistant

---

**Ready to add your key?** Just provide it to me and I'll update the `.env` file for you! 🚀
