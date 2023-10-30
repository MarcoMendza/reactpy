from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/login/")
async def login(request: Request, db: Session = Depends(database.get_db), email: str = Form(...), password: str = Form(...)):
    user = db.query(models.Cliente).filter(models.Cliente.correo == email).first()
    if user is None or user.contra != password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"detail": "Login Successful"}

@router.post("/cliente/", response_model=schemas.Cliente)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(database.get_db)):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

@router.get("/cliente/{RFC}", response_model=schemas.Cliente)
def read_cliente(RFC: str, db: Session = Depends(database.get_db)):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.RFC == RFC).first()
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

@router.put("/cliente/{RFC}", response_model=schemas.Cliente)
def update_cliente(RFC: str, cliente: schemas.ClienteCreate, db: Session = Depends(database.get_db)):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.RFC == RFC).first()
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    for key, value in cliente.dict().items():
        setattr(db_cliente, key, value)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

@router.delete("/cliente/{RFC}", response_model=schemas.Cliente)
def delete_cliente(RFC: str, db: Session = Depends(database.get_db)):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.RFC == RFC).first()
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    db.delete(db_cliente)
    db.commit()
    return db_cliente
