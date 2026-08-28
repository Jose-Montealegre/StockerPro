from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate

def create_customer(
    db: Session,
    customer: CustomerCreate
):
    existing_document = db.query(Customer).filter(
        Customer.documento == customer.documento
    ).first()
    
    if existing_document:
        raise HTTPException(
            status_code=400,
            detail="Ya existe un cliente con este documento"
        )
    
    existing_email = db.query(Customer).filter(
        Customer.correo == customer.correo
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Ya existe un cliente con este correo"
        )

    new_customer = Customer(
        nombre=customer.nombre,
        documento=customer.documento,
        correo=customer.correo,
        telefono=customer.telefono
    )

    try:
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)

        return new_customer

    except Exception:
        db.rollback()
        raise


def get_customers(db: Session):
    return db.query(Customer).all()



def get_customer_by_id(
    db: Session,
    customer_id: int
):
    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    return customer


def update_customer(
    db: Session,
    customer_id: int,
    customer_data: CustomerUpdate
):
    customer = get_customer_by_id(
        db,
        customer_id
    )

    existing_document = db.query(Customer).filter(
        Customer.documento == customer_data.documento,
        Customer.id != customer_id
    ).first()

    if existing_document:
        raise HTTPException(
            status_code=400,
            detail="Ya existe otro cliente con este documento"
        )

    existing_email = db.query(Customer).filter(
        Customer.correo == customer_data.correo,
        Customer.id != customer_id
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Ya existe otro cliente con este correo"
        )

    customer.nombre = customer_data.nombre
    customer.documento = customer_data.documento
    customer.correo = customer_data.correo
    customer.telefono = customer_data.telefono

    try:
        db.commit()
        db.refresh(customer)

        return customer

    except Exception:
        db.rollback()
        raise


def delete_customer(
    db: Session,
    customer_id: int
):
    customer = get_customer_by_id(
        db,
        customer_id
    )

    try:
        db.delete(customer)
        db.commit()

        return {
            "mensaje": "Cliente eliminado correctamente"
        }

    except Exception:
        db.rollback()
        raise