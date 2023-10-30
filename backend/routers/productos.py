from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/productos/", response_model=schemas.Producto)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(database.get_db)):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.get("/productos/{id}", response_model=schemas.Producto)
def read_producto(id: int, db: Session = Depends(database.get_db)):
    db_producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@router.put("/productos/{id}", response_model=schemas.Producto)
def update_producto(id: int, producto: schemas.ProductoCreate, db: Session = Depends(database.get_db)):
    db_producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    for key, value in producto.dict().items():
        setattr(db_producto, key, value)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.delete("/productos/{id}", response_model=schemas.Producto)
def delete_producto(id: int, db: Session = Depends(database.get_db)):
    db_producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(db_producto)
    db.commit()
    return db_producto
