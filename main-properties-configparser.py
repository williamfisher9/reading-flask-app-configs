from flask import Flask
import configparser # pip install configparser

config = configparser.ConfigParser()
config.read('config-parser.properties')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.get("GENERAL", "SQLALCHEMY_DATABASE_URI")

print(config.get("GENERAL", "SQLALCHEMY_DATABASE_URI"))
print(config['GENERAL']['SQLALCHEMY_DATABASE_URI'])
print(app.config.get("SQLALCHEMY_DATABASE_URI"))
print(config["GENERAL"].getint())

if __name__ == '__main__':
    app.run(debug=True)