from flask import Flask
import tomllib  # pip install toml

app = Flask(__name__)
app.config.from_file("config.toml", load=tomllib.load, text=False)

print(app.config.get("SQLALCHEMY_DATABASE_URI"))
print(app.config.get("SECRET_KEY"))
print(app.config.get("JWT_SECRET_KEY"))
print(app.config.get("FLASK_DEBUG"))

if __name__ == '__main__':
    app.run(debug=True)