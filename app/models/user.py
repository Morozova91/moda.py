# Задача "Модели SQLAlchemy":
from app.backend.db import Base
# from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
# from sqlalchemy.orm import relationship
from app.backend.db import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('Task', back_populates='user')

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))