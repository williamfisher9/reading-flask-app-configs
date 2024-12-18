from flask import Flask
from jproperties import Properties

configs = Properties()  # Create a new property file parser.

with open('config.properties', 'rb') as config_file:
    configs.load(config_file)

app = Flask(__name__)

print(configs.get("JWT_SECRET_KEY"))

if __name__ == '__main__':
    app.run(debug=True)