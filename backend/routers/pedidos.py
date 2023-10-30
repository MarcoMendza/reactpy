from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/pedidos/", response_model=schemas.Pedido)
def create_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(database.get_db)):
    db_pedido = models.Pedido(**pedido.dict())
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

@router.get("/pedidos/{id}", response_model=schemas.Pedido)
def read_pedido(id: int, db: Session = Depends(database.get_db)):
    db_pedido = db.query(models.Pedido).filter(models.Pedido.id == id).first()
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return db_pedido

@router.put("/pedidos/{id}", response_model=schemas.Pedido)
def update_pedido(id: int, pedido: schemas.PedidoCreate, db: Session = Depends(database.get_db)):
    db_pedido = db.query(models.Pedido).filter(models.Pedido.id == id).first()
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    for key, value in pedido.dict().items():
        setattr(db_pedido, key, value)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

@router.delete("/pedidos/{id}", response_model=schemas.Pedido)
def delete_pedido(id: int, db: Session = Depends(database.get_db)):
    db_pedido = db.query(models.Pedido).filter(models.Pedido.id == id).first()
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    db.delete(db_pedido)
    db.commit()
    return db_pedido
