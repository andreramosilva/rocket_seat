from sqlalchemy import Column, Integer, String , BIGINT, ForeignKey
from src.models.sqllite.settings.base import Base

class People(Base):
    __tablename__ = 'people'

    id = Column(BIGINT, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(BIGINT, nullable=False)
    pet_id = Column(BIGINT, nullable=False)

    def __repr__(self):
        return f'People(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, age={self.age}, pet_id={self.pet_id})'