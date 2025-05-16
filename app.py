from flask import Flask
from controllers import book
from flask_cors import CORS  

app = Flask(__name__)
CORS(app) 

app.register_blueprint(book)

if __name__ == '__main__':
    app.run(port=5000)
