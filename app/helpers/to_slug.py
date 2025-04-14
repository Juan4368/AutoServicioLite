import re
import unicodedata

def to_slug(texto: str) -> str:
    # Normaliza acentos y convierte a ASCII
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")

    # Reemplaza cualquier caracter no alfanumérico por espacios
    texto = re.sub(r"[^a-zA-Z0-9\s-]", "", texto)

    # Convierte espacios y guiones múltiples a un solo guion
    texto = re.sub(r"[\s_-]+", "-", texto)

    # Elimina guiones al inicio o final y convierte a minúsculas
    return texto.strip("-").lower()

