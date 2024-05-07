from typing import Optional
from pydantic import BaseModel, Field


class Producto(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(min_length=1)
    categoria: str = Field(min_length=1)
    descripcion: str = Field(min_length=1, max_length=100)
    precio: float = Field(gt=0)
    stock: int = Field(default=0, ge=0) # Cantidad de stock (por defecto 0, no negativa)
    stock_minimo: Optional[int] = None # Nivel mínimo de stock opcional (puede ser None)
    stock_maximo: Optional[int] = None # Nivel máximo de stock opcional (puede ser None)
    activo: bool = Field(default=True) # Indica si el producto está activo (por defecto True)
    class Config:
        json_schema_extra = {
        'example': {
        'nombre': 'Silla',
        'categoria': 'Mueble',
        'descripcion': 'Una silla de escritorio',
        'precio': 90000.99,
        'stock': 10, # Ejemplo de cantidad de stock
        'stock_minimo': 5, # Ejemplo de stock mínimo
        'stock_maximo': 20, # Ejemplo de stock máximo {
        }
    }
    