import os

from flask import Flask

from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()   # Parse a .env file and then load all the variables found as environment variables.

app = Flask(__name__)

FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
SECRET_KEY = os.environ.get("SECRET_KET")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KET")
DATABASE = os.environ.get("SQLALCHEMY_DATABASE_URI")

print(DATABASE)

if __name__ == '__main__':
    app.run(debug=True)