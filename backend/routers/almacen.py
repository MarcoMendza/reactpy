from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/almacen/", response_model=schemas.Almacen)
def create_almacen(almacen: schemas.AlmacenCreate, db: Session = Depends(database.get_db)):
    db_almacen = models.Almacen(**almacen.dict())
    db.add(db_almacen)
    db.commit()
    db.refresh(db_almacen)
    return db_almacen

@router.get("/almacen/{id}", response_model=schemas.Almacen)
def read_almacen(id: int, db: Session = Depends(database.get_db)):
    db_almacen = db.query(models.Almacen).filter(models.Almacen.id == id).first()
    if db_almacen is None:
        raise HTTPException(status_code=404, detail="Almacen no encontrado")
    return db_almacen

@router.put("/almacen/{id}", response_model=schemas.Almacen)
def update_almacen(id: int, almacen: schemas.AlmacenCreate, db: Session = Depends(database.get_db)):
    db_almacen = db.query(models.Almacen).filter(models.Almacen.id == id).first()
    if db_almacen is None:
        raise HTTPException(status_code=404, detail="Almacen no encontrado")
    for key, value in almacen.dict().items():
        setattr(db_almacen, key, value)
    db.commit()
    db.refresh(db_almacen)
    return db_almacen

@router.delete("/almacen/{id}", response_model=schemas.Almacen)
def delete_almacen(id: int, db: Session = Depends(database.get_db)):
    db_almacen = db.query(models.Almacen).filter(models.Almacen.id == id).first()
    if db_almacen is None:
        raise HTTPException(status_code=404, detail="Almacen no encontrado")
    db.delete(db_almacen)
    db.commit()
    return db_almacen
