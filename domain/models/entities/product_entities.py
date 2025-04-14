from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    id : int
    barcode : str
    name : str
    price : float
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime | None = None



    
