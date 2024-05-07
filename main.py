from fastapi import FastAPI, HTTPException, status
from modelo import Producto

app = FastAPI()
list_producto = []

@app.post("/productos")
async def crear_producto(producto: Producto) -> dict:
    list_producto.append(producto)
    return {
       "producto" : producto
    }

@app.get("/productos")
async def listar_producto() ->dict:
    return {
        "producto" : list_producto
    }

@app.get("/productos/{id}")
async def obtener_producto(producto_id: int) -> dict:
    for producto in list_producto:
        if producto.id == producto_id:
            return{
                "producto" : producto
            }   
@app.put("/productos/{id}")
async def modificar_producto(producto_data: Producto, producto_id: int) -> dict:
    for producto in list_producto: 
        if producto.id == producto_id:
            producto.nombre = producto_data.nombre
            producto.categoria = producto_data.categoria
            producto.descripcion = producto_data.descripcion
            producto.precio = producto_data.precio
            producto.stock = producto_data.stock
            producto.stock_minimo = producto_data.stock_minimo
            producto.stock_maximo = producto_data.stock_maximo
            producto.activo = producto_data.activo
            return{
                "mensaje" : "Producto modificado",
                "producto" : producto
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Producto no existe",)

@app.get("/productos/{id}/stock")
async def obtener_stock(producto_id:int) -> dict:
    for producto in list_producto:
        if producto.id == producto_id:
            return{
                "stock" : producto.stock,
                "stock_minimo" : producto.stock_minimo,
                "stock_maximo" : producto.stock_maximo,
                "activo" : producto.activo }  
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Producto no existe",)


@app.put("/productos/{id}/desactivar")
async def modificar_producto( producto_id: int) -> dict:
    for producto in list_producto: 
        if producto.id == producto_id:
            producto.activo = False
            return { 
                "mensaje" : "Producto desactivado",
                "producto" : producto
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Producto no existe",)