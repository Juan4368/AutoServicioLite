import xml.etree.ElementTree as ET
from config import get_db 
from infrastructure.database.models import product  # Asegúrate de que el modelo Product esté definido en models.py
from app.helpers.get_xml_value import get_xml_value
import logging
from app.helpers.to_slug import to_slug

# Namespace necesario para leer xsi:type
XSI = "http://www.w3.org/2001/XMLSchema-instance"
NSMAP = {"xsi": XSI}

def cargar_productos_desde_xml():

    logging.basicConfig(
    filename="productos_duplicados.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
    try:
        tree = ET.parse("products.xml")
        root = tree.getroot()
        db = next(get_db())

        for item_product in root.findall('PosItem'):
            group_name = item_product.findtext('Name',default="Tienda")
            items_node = item_product.find('Items')

            if items_node is not None:
                post_items = items_node.findall('PosItem')

            else:

                post_items = [item_product]

            for post_items in post_items:
                    Name = post_items.findtext('Name', default="Sin nombre")
                    #verifica si el codigo de barras no existe
                    barcode = get_xml_value(post_items, "Barcodes/Barcode/Value", str, default=to_slug(Name))    
                    #si tiene precio cero no se inserta
                    Price = float(post_items.find('Price').text)
                    if Price == 0:
                        logging.info(f"Sin precio: {barcode} - {Name} - {Price}")
                        print(f"⚠️ Producto {Name} tiene precio cero, se omite.")
                        continue

                    #verificar si existe el codigo de barras y si es así no se inserta y continua
                    existe = db.query(product).filter(product.barcode == barcode).first()
                    if existe:
                        logging.info(f"Duplicado: {barcode} - {existe.name} - {existe.price}")
                        print(f"🔁 Producto con código {barcode} ya existe, se omite.")
                        continue

                    nuevo_producto = product(                  
                        barcode=barcode,
                        name=Name, 
                        description="", 
                        price=Price
                )
                    db.add(nuevo_producto)   
                    db.commit()
        print(f"Productos agregados correctamente.")

    except Exception as e:
        print(f"Error importando productos: {e} con código de barras {barcode} {Name} {Price}")
        db.rollback()
        
    finally:
        db.close()


