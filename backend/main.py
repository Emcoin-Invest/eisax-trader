from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db import SessionLocal, engine
import models
import json

app = FastAPI(title="EisaX Trader API")
models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STATIC_PRICES = {"AAPL": 180, "ADSB": 40, "GLD": 200, "USD/JPY": 144, "VIG": 160, "UAE-BOND": 102}

@app.get("/")
def read_root():
    return {"message": "EisaX Trader API", "version": "1.0"}

@app.get("/assets")
def get_assets():
    with open("assets.json") as f:
        assets = json.load(f)
    return assets

@app.get("/portfolio/{user_id}")
def get_portfolio(user_id: int):
    db = SessionLocal()
    holdings = db.query(models.Holding).filter(models.Holding.user_id == user_id).all()
    response = []
    for h in holdings:
        asset = db.query(models.Asset).filter(models.Asset.id == h.asset_id).first()
        response.append({
            "symbol": asset.symbol,
            "qty": h.qty,
            "avg_price": h.avg_price,
            "name": asset.name,
            "category": asset.category
        })
    db.close()
    return response

@app.get("/price/{symbol}")
def price(symbol: str):
    return {"symbol": symbol, "price": STATIC_PRICES.get(symbol, 1.0)}

@app.post("/trade")
def trade(user_id: int, asset_id: int, action: str, qty: float, price: float):
    db = SessionLocal()
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if action == "buy":
        cost = qty * price
        if user.cash < cost:
            db.close()
            raise HTTPException(status_code=400, detail="Insufficient cash")
        user.cash -= cost
        holding = db.query(models.Holding).filter(
            models.Holding.user_id == user_id, models.Holding.asset_id == asset_id
        ).first()
        if not holding:
            holding = models.Holding(user_id=user_id, asset_id=asset_id, qty=qty, avg_price=price)
            db.add(holding)
        else:
            total_qty = holding.qty + qty
            holding.avg_price = (holding.avg_price * holding.qty + price * qty) / total_qty
            holding.qty = total_qty
        txn = models.Transaction(user_id=user_id, type="buy", asset_id=asset_id, qty=qty, price=price)
        db.add(txn)
    elif action == "sell":
        holding = db.query(models.Holding).filter(
            models.Holding.user_id == user_id, models.Holding.asset_id == asset_id
        ).first()
        if not holding or holding.qty < qty:
            db.close()
            raise HTTPException(status_code=400, detail="Not enough holdings")
        holding.qty -= qty
        user.cash += qty * price
        txn = models.Transaction(user_id=user_id, type="sell", asset_id=asset_id, qty=qty, price=price)
        db.add(txn)
    db.commit()
    db.close()
    return {"result": "success"}
