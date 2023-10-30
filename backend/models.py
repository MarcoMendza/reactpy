from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    RFC = Column(String(16), primary_key=True)
    correo = Column(String(45))
    contra = Column(String(45))
    nombreP = Column(String(45))
    apellidoP = Column(String(45))
    apellidoM = Column(String(45))
    telefono = Column(String(45))
    direccion = Column(String(225))

class Almacen(Base):
    __tablename__ = 'almacen'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(45))
    direccion = Column(String(225))
    capacidadMaxima = Column(Integer)

class MateriaPrimas(Base):
    __tablename__ = 'materia_primas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(45))
    cantidad = Column(Integer)
    almacen = Column(Integer, ForeignKey('almacen.id'))
    FechaMod = Column(Date)

    almacen_rel = relationship("Almacen", back_populates="materia_primas_rel")

class Productos(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(45))
    cantidad = Column(Integer)
    almacen_id = Column(Integer, ForeignKey('almacen.id'))

    almacen_rel = relationship("Almacen", back_populates="productos_rel")

class Pedidos(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    status = Column(String(45))
    cliente = Column(String(16), ForeignKey('cliente.RFC'))
    producto = Column(Integer, ForeignKey('productos.id'))

    cliente_rel = relationship("Cliente", back_populates="pedidos_rel")
    producto_rel = relationship("Productos", back_populates="pedidos_rel")

# Back relationships
Almacen.materia_primas_rel = relationship("MateriaPrimas", order_by=MateriaPrimas.id, back_populates="almacen_rel")
Almacen.productos_rel = relationship("Productos", order_by=Productos.id, back_populates="almacen_rel")
Cliente.pedidos_rel = relationship("Pedidos", order_by=Pedidos.id, back_populates="cliente_rel")
Productos.pedidos_rel = relationship("Pedidos", order_by=Pedidos.id, back_populates="producto_rel")

# Database connection
DATABASE_URL = "sqlite:///./test.db"  # Change to your actual database URL
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

