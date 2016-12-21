from flask import Flask
app = Flask(__name__)

import catalog.views
from catalog.database import init_db
from catalog.database import db_session

init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()



