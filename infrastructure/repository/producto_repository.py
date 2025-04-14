from  infrastructure.database.models import product as productDB
from sqlalchemy.orm import Session
from config import get_db

class  ProductoRepository:
    def __init__(self, db: Session):
        self.db = db   

    # def get_all_productos(self):
    #     return self.db.query("SELECT * FROM productos")

    def get_producto_by_barcode_by_name(self, nombre: str, barcode: str) ->  list[productDB]:

        query = self.db.query(productDB)

        if nombre:
            query = query.filter(productDB.name.ilike(f"%{nombre}%"))
        if barcode:
            query = query.filter(productDB.barcode == barcode)

        return query.all()

        """  return self.db.query("SELECT * FROM productos WHERE name = ? AND barcode = ?", (nombre, barcode))
        
        def create_producto(self, producto_data):
            return self.db.execute("INSERT INTO productos (name, price) VALUES (?, ?)", (producto_data['name'], producto_data['price']))

        def update_producto(self, producto_id, producto_data):
            return self.db.execute("UPDATE productos SET name = ?, price = ? WHERE id = ?", (producto_data['name'], producto_data['price'], producto_id))

        def delete_producto(self, producto_id):
            return self.db.execute("DELETE FROM productos WHERE id = ?", (producto_id,)) """