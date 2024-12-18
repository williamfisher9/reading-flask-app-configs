from flask import Flask

import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'test188127812'
app.config['JWT_SECRET_KEY'] = 'test12983819'

if __name__ == '__main__':
    app.run(debug=True)