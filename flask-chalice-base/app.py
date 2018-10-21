#!/usr/bin/venv python3

from chalice import Chalice

app = Chalice(app_name='flask-chalice-base')


@app.route('/')
def index():
    return {'hello': 'world'}
