import os
from flask import Flask
app = Flask(__name__)

BASE_PATH = os.path.dirname(__file__)


# for uploading image files
from flask_uploads import UploadSet, IMAGES, configure_uploads
app.config['UPLOADS_DEFAULT_DEST'] = BASE_PATH + '/static/img/'
app.config['UPLOADS_DEFAULT_URL'] = 'http://localhost:5000/static/img/'
app.config['UPLOADED_IMAGES_DEST'] = BASE_PATH + '/static/img/'
app.config['UPLOADED_IMAGES_URL'] = 'http://localhost:5000/static/img/'
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

import catalog.views
from catalog.database import init_db
from catalog.database import db_session

init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
