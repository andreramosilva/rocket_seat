from src.models.sqllite.settings.base import Base
from sqlalchemy import Column, Integer, String , BIGINT

class Pets(Base):
    __tablename__ = 'pets'

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String , nullable=False)

    def __repr__(self):
        return f'Pets(id={self.id}, name={self.name}, type={self.type})'