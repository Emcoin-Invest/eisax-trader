# 🚀 EisaX Trader - Complete Setup Guide

**Follow these steps exactly to get your trading app running!**

---

## 📋 Prerequisites (Install These First)

### Step 1: Install Python
1. Go to https://www.python.org/downloads/
2. Download Python 3.10 or higher
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Verify installation:
   ```bash
   python --version
   ```
   Should show: `Python 3.10.x` or higher

### Step 2: Install Node.js
1. Go to https://nodejs.org/
2. Download the LTS version (recommended)
3. Install with default settings
4. Verify installation:
   ```bash
   node --version
   npm --version
   ```

### Step 3: Install Git
1. Go to https://git-scm.com/downloads
2. Download and install for your operating system
3. Verify installation:
   ```bash
   git --version
   ```

---

## 💻 Part 1: Setup Backend (10 minutes)

### Step 1: Clone the Repository
Open your terminal/command prompt and run:

```bash
# Navigate to where you want the project
cd Desktop

# Clone the repository
git clone https://github.com/Emcoin-Invest/eisax-trader.git

# Go into the project folder
cd eisax-trader
```

### Step 2: Setup Backend
```bash
# Navigate to backend folder
cd backend

# Install Python dependencies
pip install -r requirements.txt
```

**Wait for installation to complete (1-2 minutes)**

### Step 3: Start the Backend Server
```bash
# Run the FastAPI server
uvicorn main:app --reload
```

✅ **Success! You should see:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Step 4: Test the Backend
Open your browser and go to:
- **API Docs**: http://localhost:8000/docs
- **Get Assets**: http://localhost:8000/assets
- **Root**: http://localhost:8000/

You should see JSON data! ✅

**Keep this terminal window open!** The backend must stay running.

---

## 🎨 Part 2: Setup Frontend (OPTIONAL - For Full UI)

The backend is now fully functional! To add a web interface:

### Step 1: Open a NEW Terminal
**IMPORTANT**: Don't close the backend terminal!

```bash
# Navigate to project root
cd eisax-trader

# Create frontend folder
npx create-next-app@latest frontend --typescript --tailwind --app --src-dir --import-alias "@/*"
```

Press **Enter** for all prompts (accept defaults)

### Step 2: Navigate to Frontend
```bash
cd frontend
```

### Step 3: Install Dependencies
```bash
npm install
```

### Step 4: Start Frontend Server
```bash
npm run dev
```

✅ **Success! You should see:**
```
Ready - started server on http://localhost:3000
```

Open: http://localhost:3000

---

## 🧪 Testing Your Setup

### Test Backend API (Using Browser or Postman)

1. **Get All Assets**
   - URL: `GET http://localhost:8000/assets`
   - Should return: List of 6 assets (AAPL, ADSB, GLD, etc.)

2. **Get Asset Price**
   - URL: `GET http://localhost:8000/price/AAPL`
   - Should return: `{"symbol": "AAPL", "price": 180}`

3. **View API Documentation**
   - URL: http://localhost:8000/docs
   - Interactive API testing interface

---

## 🛠️ Common Issues & Solutions

### Issue 1: "python not found"
**Solution**: Reinstall Python and check "Add to PATH"

### Issue 2: "pip not found"
**Solution**: 
```bash
python -m pip install -r requirements.txt
```

### Issue 3: "Port 8000 already in use"
**Solution**: Stop other programs using port 8000, or use:
```bash
uvicorn main:app --reload --port 8001
```

### Issue 4: "Module not found"
**Solution**: Make sure you're in the backend folder:
```bash
cd backend
pip install -r requirements.txt
```

### Issue 5: Database errors
**Solution**: Delete trader.db and restart:
```bash
rm trader.db
uvicorn main:app --reload
```

---

## 📚 Understanding the Project

### Backend Structure
```
backend/
├── main.py          # FastAPI app with all API endpoints
├── models.py        # Database models (User, Asset, Holding, Transaction)
├── db.py            # Database configuration
├── assets.json      # Sample trading assets
├── requirements.txt # Python dependencies
└── trader.db        # SQLite database (created automatically)
```

### API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API info |
| `/assets` | GET | List all assets |
| `/portfolio/{user_id}` | GET | Get user portfolio |
| `/price/{symbol}` | GET | Get asset price |
| `/trade` | POST | Execute trade |

---

## 🎯 Next Steps

### You're Ready to:
1. ✅ Make API calls to your backend
2. ✅ Test trading functionality
3. ✅ Build custom frontend interfaces
4. ✅ Add more features (charts, news, etc.)

### Quick Start Trading (via API):
```python
import requests

# Get all assets
response = requests.get('http://localhost:8000/assets')
print(response.json())

# Get AAPL price
response = requests.get('http://localhost:8000/price/AAPL')
print(response.json())
```

---

## 📞 Need Help?

- Check API docs: http://localhost:8000/docs
- Review README.md for more info
- Make sure both Python and Node.js are installed correctly

---

## 🎉 Congratulations!

Your EisaX Trader backend is now running! You can:
- View asset data
- Check prices  
- Test API endpoints
- Build custom interfaces

**Backend**: http://localhost:8000  
**API Docs**: http://localhost:8000/docs  
**Repository**: https://github.com/Emcoin-Invest/eisax-trader

---

**Built with ❤️ - Happy Trading!** 🚀
