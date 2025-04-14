from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de conexión
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear motor de conexión
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Probar la conexión
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 'Conexión exitosa a PostgreSQL en AWS RDS'"))
        print(result.scalar())  # Debe imprimir "Conexión exitosa a PostgreSQL en AWS RDS"
except Exception as e:
    print(f"Error de conexión: {e}")

# Sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia 
def get_db():
    db = SessionLocal()
    try:
        yield db  # El `db` se inyecta en los endpoints
    finally:
        db.close()  # Aquí se asegura el cierre de sesión siempre
