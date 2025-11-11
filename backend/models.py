from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
    cash = Column(Float, default=10000)

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    name = Column(String)
    category = Column(String)

class Holding(Base):
    __tablename__ = "holdings"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    asset_id = Column(Integer, ForeignKey("assets.id"))
    qty = Column(Float)
    avg_price = Column(Float)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String)
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=True)
    qty = Column(Float, nullable=True)
    price = Column(Float, nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
