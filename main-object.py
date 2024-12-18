from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

print(app.config.get("SQLALCHEMY_DATABASE_URI"))
print(app.config.get("SECRET_KEY"))
print(app.config.get("JWT_SECRET_KEY"))

if __name__ == '__main__':
    app.run(debug=True)