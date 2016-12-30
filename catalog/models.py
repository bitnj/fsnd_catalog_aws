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

class Images(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, nullable=False)
    file_path = Column(String(250), nullable=False)


class CatalogItem(Base):
    __tablename__ = 'catalog_item'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    image_id = Column(Integer, ForeignKey('images.id'))
    category = relationship(Category)
    users = relationship(Users)
    images = relationship(Images)


