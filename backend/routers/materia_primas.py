from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/materia_primas/", response_model=schemas.MateriaPrimas)
def create_materia_primas(materia_primas: schemas.MateriaPrimasCreate, db: Session = Depends(database.get_db)):
    db_materia_primas = models.MateriaPrimas(**materia_primas.dict())
    db.add(db_materia_primas)
    db.commit()
    db.refresh(db_materia_primas)
    return db_materia_primas

@router.get("/materia_primas/{id}", response_model=schemas.MateriaPrimas)
def read_materia_primas(id: int, db: Session = Depends(database.get_db)):
    db_materia_primas = db.query(models.MateriaPrimas).filter(models.MateriaPrimas.id == id).first()
    if db_materia_primas is None:
        raise HTTPException(status_code=404, detail="Materia Prima no encontrada")
    return db_materia_primas

@router.put("/materia_primas/{id}", response_model=schemas.MateriaPrimas)
def update_materia_primas(id: int, materia_primas: schemas.MateriaPrimasCreate, db: Session = Depends(database.get_db)):
    db_materia_primas = db.query(models.MateriaPrimas).filter(models.MateriaPrimas.id == id).first()
    if db_materia_primas is None:
        raise HTTPException(status_code=404, detail="Materia Prima no encontrada")
    for key, value in materia_primas.dict().items():
        setattr(db_materia_primas, key, value)
    db.commit()
    db.refresh(db_materia_primas)
    return db_materia_primas

@router.delete("/materia_primas/{id}", response_model=schemas.MateriaPrimas)
def delete_materia_primas(id: int, db: Session = Depends(database.get_db)):
    db_materia_primas = db.query(models.MateriaPrimas).filter(models.MateriaPrimas.id == id).first()
    if db_materia_primas is None:
        raise HTTPException(status_code=404, detail="Materia Prima no encontrada")
    db.delete(db_materia_primas)
    db.commit()
    return db_materia_primas
