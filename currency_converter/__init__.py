from flask import Flask

app = Flask(__name__)

from currency_converter.api import *


@app.route('/')
def index():
    return 'Finvinci Currency Converter'
