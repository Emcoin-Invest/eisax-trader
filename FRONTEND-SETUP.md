# 🎨 Frontend Setup Guide - EisaX Trader

## Option 1: Quick Setup (RECOMMENDED - 5 minutes)

This is the FASTEST way to get your frontend running!

### Step 1: Open a NEW Terminal
**IMPORTANT**: Keep your backend running in the other terminal!

### Step 2: Navigate to Your Project
```bash
cd eisax-trader
```

### Step 3: Create Frontend
```bash
npx create-next-app@latest frontend --typescript --tailwind
```

**When prompted**:
- Would you like to use TypeScript? → **Yes**
- Would you like to use ESLint? → **Yes**  
- Would you like to use Tailwind CSS? → **Yes**
- Would you like to use `src/` directory? → **No**
- Would you like to use App Router? → **Yes** 
- Would you like to customize the default import alias? → **No**

Wait 1-2 minutes for installation...

### Step 4: Navigate to Frontend
```bash
cd frontend
```

### Step 5: Start Frontend
```bash
npm run dev
```

✅ **SUCCESS!** Open: http://localhost:3000

You'll see the Next.js welcome page!

---

## Option 2: Full Custom UI Setup (30 minutes)

To get the custom EisaX Trader pages with portfolio and markets:

### After completing Option 1, add these custom pages:

#### 1. Update `frontend/tailwind.config.js`
Replace the content with:
```js
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        lightblue: "#5FA4E3",
        darkblue: "#263859",
        mategold: "#F5C860",
      },
    },
  },
  plugins: [],
}
```

#### 2. Create `frontend/app/page.tsx`
Replace the content with:
```tsx
export default function Home() {
  return (
    <div className="bg-darkblue min-h-screen flex flex-col justify-center items-center">
      <h1 className="text-5xl text-mategold font-bold mb-8">EisaX Trader</h1>
      <p className="text-white text-xl mb-8">Simulated Trading Platform</p>
      <div className="flex gap-4">
        <a href="/portfolio" className="bg-mategold px-6 py-3 rounded text-darkblue font-bold hover:opacity-90">
          Portfolio
        </a>
        <a href="/markets" className="bg-lightblue px-6 py-3 rounded text-white font-bold hover:opacity-90">
          Markets
        </a>
      </div>
    </div>
  )
}
```

#### 3. Create `frontend/app/portfolio/page.tsx`
Create this file:
```tsx
"use client"
import { useEffect, useState } from "react";

export default function Portfolio() {
  const [portfolio, setPortfolio] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/portfolio/1")
      .then((res) => res.json())
      .then(data => {
        setPortfolio(data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="bg-lightblue min-h-screen p-8">
      <h1 className="text-4xl font-bold text-darkblue mb-8">My Portfolio</h1>
      
      {loading ? (
        <p className="text-white">Loading...</p>
      ) : portfolio.length === 0 ? (
        <div className="bg-white rounded-xl p-8 shadow-lg">
          <p className="text-darkblue text-xl">No holdings yet. Start trading!</p>
          <a href="/markets" className="mt-4 inline-block bg-mategold px-6 py-3 rounded font-bold">
            Browse Markets
          </a>
        </div>
      ) : (
        <div className="bg-white rounded-xl shadow-lg overflow-hidden">
          <table className="w-full">
            <thead className="bg-darkblue text-white">
              <tr>
                <th className="p-4 text-left">Asset</th>
                <th className="p-4 text-left">Category</th>
                <th className="p-4 text-right">Quantity</th>
                <th className="p-4 text-right">Avg Price</th>
              </tr>
            </thead>
            <tbody>
              {portfolio.map((holding: any, idx: number) => (
                <tr key={idx} className="border-b hover:bg-gray-50">
                  <td className="p-4">
                    <div className="font-bold text-darkblue">{holding.name}</div>
                    <div className="text-sm text-gray-500">{holding.symbol}</div>
                  </td>
                  <td className="p-4 text-gray-600">{holding.category}</td>
                  <td className="p-4 text-right font-semibold">{holding.qty}</td>
                  <td className="p-4 text-right font-semibold">${holding.avg_price}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
```

#### 4. Create `frontend/app/markets/page.tsx`
Create this file:
```tsx
"use client"
import { useEffect, useState } from "react";

export default function Markets() {
  const [assets, setAssets] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/assets")
      .then((res) => res.json())
      .then(data => {
        setAssets(data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="bg-lightblue min-h-screen p-8">
      <h1 className="text-4xl font-bold text-darkblue mb-8">All Markets</h1>
      
      {loading ? (
        <p className="text-white">Loading assets...</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {assets.map((asset: any) => (
            <div key={asset.id} className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition">
              <div className="flex justify-between items-start mb-4">
                <div>
                  <h2 className="text-2xl font-bold text-darkblue">{asset.symbol}</h2>
                  <p className="text-gray-600">{asset.name}</p>
                </div>
                <span className="bg-mategold px-3 py-1 rounded-full text-sm font-semibold text-darkblue">
                  {asset.category}
                </span>
              </div>
              <button className="w-full bg-darkblue text-white py-2 rounded font-semibold hover:bg-opacity-90">
                View Details
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
```

---

## 🎯 What You Get

### With Option 1 (Quick Setup):
- ✅ Next.js + TypeScript running
- ✅ Tailwind CSS ready
- ✅ Modern development environment
- ⏱️ Time: 5 minutes

### With Option 2 (Full Setup):
- ✅ Custom EisaX theme (light blue, dark blue, mate gold)
- ✅ Home page with navigation
- ✅ Portfolio page (shows your holdings)
- ✅ Markets page (shows all tradable assets)
- ✅ Connected to your backend API
- ⏱️ Time: 30 minutes total

---

## 🚀 Quick Commands Summary

```bash
# From eisax-trader folder:
cd eisax-trader

# Create frontend:
npx create-next-app@latest frontend --typescript --tailwind

# Start it:
cd frontend
npm run dev
```

**Frontend**: http://localhost:3000  
**Backend**: http://localhost:8000

---

## 📝 Notes

- Keep BOTH terminals running (backend + frontend)
- Backend must be on port 8000
- Frontend will be on port 3000
- Make sure to accept defaults when creating Next.js app

---

## 🎉 You're Done!

Once both are running:
- Visit http://localhost:3000 to see your app
- Navigate between pages
- View your portfolio
- Browse markets
- All data comes from your backend!

**Happy Trading!** 🚀
