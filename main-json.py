from flask import Flask

import json

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)

print(app.config.get("SQLALCHEMY_DATABASE_URI"))
print(app.config.get("SECRET_KEY"))
print(app.config.get("JWT_SECRET_KEY"))

if __name__ == '__main__':
    app.run(debug=True)