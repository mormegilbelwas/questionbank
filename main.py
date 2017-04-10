from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

from routes import *

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404