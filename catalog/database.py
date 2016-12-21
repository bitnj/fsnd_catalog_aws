# Setup taken from the SQLAlchemy in Flash tutorial which differs from
# the code demonstrated in the Udacity Full-Stack Nanodegree lectures

# SQLAlchemy Imports
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///catalog.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
    bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that they will be
    # registered properly on the metadata.  Otherwise you will have to import
    # them first before calling db_init()
    import catalog.models
    Base.metadata.create_all(bind=engine)

    
