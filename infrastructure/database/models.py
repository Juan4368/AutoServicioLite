from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.schema import Identity
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


# Base para modelos
Base = declarative_base()

class product(Base):
    __tablename__ = 'product'

    id = Column(Integer, Identity(start=1, cycle=False), primary_key=True, index=True)
    barcode = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)
