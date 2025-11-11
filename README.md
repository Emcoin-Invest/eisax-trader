# EisaX Trader MVP

A simulated trading platform for UAE & US stocks, ETFs, commodities, forex, and bonds.

## 🚀 Features

- **Multi-Asset Support**: Trade UAE stocks, US stocks, ETFs, commodities, forex, and bonds
- **Simulated Trading**: Practice trading with virtual money ($10,000 starting balance)
- **Portfolio Management**: Track holdings, P/L, and transaction history
- **Responsive Design**: Works on desktop, tablet, and mobile (PWA-ready)
- **Modern Theme**: Light blue, dark blue, and mate gold color scheme

## 📁 Project Structure

```
eisax-trader/
├── backend/
│   ├── requirements.txt
│   ├── main.py
│   ├── models.py
│   ├── db.py
│   └── assets.json
└── frontend/
    ├── package.json
    ├── tailwind.config.js
    ├── public/manifest.json
    └── pages/
        ├── index.tsx
        ├── portfolio.tsx
        └── markets.tsx
```

## 🛠️ Tech Stack

**Backend:**
- FastAPI (Python web framework)
- SQLAlchemy (ORM)
- SQLite (Database)
- Uvicorn (ASGI server)

**Frontend:**
- Next.js (React framework)
- TypeScript
- Tailwind CSS
- PWA support

## 📋 Setup Instructions

### Backend Setup

1. **Navigate to backend folder**
```bash
cd backend
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the server**
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend folder**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Run development server**
```bash
npm run dev
```

The app will be available at `http://localhost:3000`

## 📝 Remaining Files to Create

To complete the MVP, you need to create the following files. Use the "Add file" button on GitHub:

### Backend Files

#### `backend/main.py` - Main API server
#### `backend/models.py` - Database models  
#### `backend/db.py` - Database configuration
#### `backend/assets.json` - Sample assets data

### Frontend Files

#### `frontend/package.json` - Node dependencies
#### `frontend/tailwind.config.js` - Tailwind theme
#### `frontend/public/manifest.json` - PWA manifest
#### `frontend/pages/index.tsx` - Home page
#### `frontend/pages/portfolio.tsx` - Portfolio page
#### `frontend/pages/markets.tsx` - Markets page

## 🔧 Complete File Contents

For the complete code of all files, please refer to the conversation history or create files with the following templates:

- Backend uses FastAPI with SQLAlchemy models for Users, Assets, Holdings, and Transactions
- Frontend uses Next.js with TypeScript and Tailwind CSS
- Sample assets include: ADSB (UAE), AAPL (US), GLD (ETF), USD/JPY (Forex), UAE-BOND
- Static prices for demo: AAPL=$180, ADSB=AED 40, etc.

## 🚦 API Endpoints

- `GET /assets` - Get all available assets
- `GET /portfolio/{user_id}` - Get user portfolio
- `GET /price/{symbol}` - Get current price for symbol
- `POST /trade` - Execute buy/sell trade

## 🎨 Theme Colors

- Light Blue: `#5FA4E3`
- Dark Blue: `#263859`
- Mate Gold: `#F5C860`

## 📱 Running as PWA

Once deployed, users can install the app on their devices:
1. Open the app in a browser
2. Click "Install" or "Add to Home Screen"
3. The app will work offline and feel like a native app

## 🔐 Default User

For testing, you can use `user_id=1` which starts with $10,000 virtual cash.

## 📄 License

MIT License - Feel free to use for learning and development.

## 🤝 Contributing

This is an MVP for learning purposes. Feel free to fork and extend with:
- Real-time market data APIs
- Advanced charts (TradingView, Chart.js)
- Social features
- News integration
- Authentication system

---

**Built with ❤️ for traders and learners**
