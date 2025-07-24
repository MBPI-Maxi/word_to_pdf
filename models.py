from sqlalchemy.orm import declarative_base
from sqlalchemy import ( 
    Column, 
    DateTime,
    Integer,
    String, 
    func,
)

Base = declarative_base()

class Workstation(Base):
    __tablename__ = "Workstations"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    workstation_name = Column(String(120), nullable=True, unique=True)
    default_path = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
