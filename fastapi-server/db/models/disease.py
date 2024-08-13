from sqlalchemy import Column, String, Integer, DateTime,  ForeignKey, PrimaryKeyConstraint, Text
from db.session import Base
from datetime import datetime


class Disease(Base):
    __tablename__ = "diseases"

    disease_id = Column(Integer, primary_key=True, index=True)
    disease_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    icon = Column(String(10), nullable=True)


class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String(255), nullable=False)


class DiseaseDepartment(Base):
    __tablename__ = "disease_departments"

    disease_id = Column(Integer, ForeignKey('diseases.disease_id'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('disease_id', 'department_id'),
    )


class UserDisease(Base):
    __tablename__ = "chat_history"

    ch_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), nullable=False)
    date_time = Column(DateTime, default=datetime)
    disease_name = Column(String, ForeignKey('diseases.disease_name'), index=True)
