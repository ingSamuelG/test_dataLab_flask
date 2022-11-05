import os
import re
from app import create_app, db
import datetime
import math
import click

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    #assumptions
    return dict()


