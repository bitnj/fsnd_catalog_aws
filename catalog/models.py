# SQLAlchemy IMPORTS
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from catalog.database import Base


# TABLE DEFINITIONS
# Python classes mapped to tables via SQLAlchemy ORM
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

    @property
    def serialize(self):
        """return object data in a serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
        }


class CatalogItem(Base):
    __tablename__ = 'catalog_item'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    image_filename = Column(String(250))
    image_url = Column(String(250))
    category = relationship(Category)
    users = relationship(Users)

    @property
    def serialize(self):
        """return object data in a serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category_id': self.category_id,
            'image_id': self.image_id,
        }
