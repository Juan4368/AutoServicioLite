def get_xml_value(elem, path: str, cast=str, default=None):
    """
    Extrae el valor de un subelemento XML usando .findtext()
    y lo convierte al tipo deseado (str, int, float, bool).
    
    Args:
        elem: ElementTree.Element
        path: ruta relativa al subelemento, por ejemplo "Barcodes/Barcode/Value"
        cast: tipo al que quieres convertir (str, int, float, bool)
        default: valor a devolver si no se encuentra o falla la conversión

    Returns:
        Valor convertido o valor por defecto
    """
    raw = elem.findtext(path)
    if raw is None:
        return default
    try:
        if cast == bool:
            return raw.strip().lower() in ("true", "1", "yes")
        return cast(raw.strip())
    except (ValueError, TypeError):
        return default

