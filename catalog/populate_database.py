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

# CatalogItems
item1 = CatalogItem(name="Bar", description="Baz", category_id=1)
session.add(item1)
session.commit()

# Images
image1 = Images(file_path="~/Courses/Udacity/FullStack_Nanodegree/catalog/catalog/foo.jpg")
session.add(image1)
session.commit()

