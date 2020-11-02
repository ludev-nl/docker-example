from my_app import app
from flask import jsonify
from datetime import datetime

@app.route('/')
def hello():
  return jsonify({'message': 'Hello from the server at ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)