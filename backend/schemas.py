from pydantic import BaseModel
from datetime import date

# Esquema para Cliente
class ClienteBase(BaseModel):
    correo: str
    contra: str
    nombreP: str
    apellidoP: str
    apellidoM: str
    telefono: str
    direccion: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    RFC: str

    class Config:
        orm_mode = True

# Esquema para Almacen
class AlmacenBase(BaseModel):
    nombre: str
    direccion: str
    capacidadMaxima: int

class AlmacenCreate(AlmacenBase):
    pass

class Almacen(AlmacenBase):
    id: int

    class Config:
        orm_mode = True

# Esquema para MateriaPrimas
class MateriaPrimasBase(BaseModel):
    nombre: str
    cantidad: int
    almacen: int  # Foreign key to Almacen
    FechaMod: date

class MateriaPrimasCreate(MateriaPrimasBase):
    pass

class MateriaPrimas(MateriaPrimasBase):
    id: int

    class Config:
        orm_mode = True

# Esquema para Productos
class ProductosBase(BaseModel):
    nombre: str
    cantidad: int
    almacen_id: int  # Foreign key to Almacen

class ProductosCreate(ProductosBase):
    pass

class Productos(ProductosBase):
    id: int

    class Config:
        orm_mode = True

# Esquema para Pedidos
class PedidosBase(BaseModel):
    fecha: date
    status: str
    cliente: str  # Foreign key to Cliente
    producto: int  # Foreign key to Productos

class PedidosCreate(PedidosBase):
    pass

class Pedidos(PedidosBase):
    id: int

    class Config:
        orm_mode = True
