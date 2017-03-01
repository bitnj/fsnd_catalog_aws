#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/fsnd_item_catalog/")

from fsnd_item_catalog import app as application
application.secret_key = 'Add your secret key'
