from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fsnd_item_catalog.database import Base
from fsnd_item_catalog.models import Users, CatalogItem, Category, Images

engine = create_engine('postgresql://catalog:25lounge@localhost/catalog')
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
image1 = Images(file_path="")
session.add(image1)
session.commit()

