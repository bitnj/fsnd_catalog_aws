from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalog.database import Base

from catalog.models import Users, CatalogItem, Category, Images

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Categories
category1 = Category(name="Foo")
session.add(category1)
session.commit()

category2 = Category(name="Soccer")
session.add(category2)
session.commit()

# CatalogItems
item1 = CatalogItem(name="Bar", description="Baz")
session.add(item1)
session.commit()

item2 = CatalogItem(name="Soccer Ball", description="Size 4")
session.add(item2)
session.commit()

# Images
image1 = Images(file_path="~/Courses/Udacity/FullStack_Nanodegree/catalog/catalog/foo.jpg")
session.add(image1)
session.commit()

image2 = Images(file_path="~/Courses/Udacity/FullStack_Nanodegree/catalog/catalog/ball.jpg")
session.add(image2)
session.commit()
