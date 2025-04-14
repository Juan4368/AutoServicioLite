from sqlalchemy import create_engine
from infrastructure.data.database import DATABASE_URL, engine
from dotenv import load_dotenv
from infrastructure.database.models import Base

engine = create_engine(DATABASE_URL)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

print("Tablas creadas exitosamente.")


