from flask import Flask

__version__ = '0.1.0'

def create_app():
  return Flask(__name__)

app = create_app()