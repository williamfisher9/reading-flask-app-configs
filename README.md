# Reading Flask App Configurations
Flask configurations can be placed directly in the flask application file.

They can also be placed in one of the following:
- Environment variables file (.env file)
  - dotenv is used to publish the contents of .env file as environment variables and then the OS library is used to read these environment variables.
- Object file (.py file)
  - A file is created with .py extension containing all variables and then properties are read directly from the object.
- JSON file (.json file)
  - Properties are read from JSON file
- TOML file (.toml file)
  - Similar to JSON, properties are read from TOML file.
- Properties file
  - Read configurations from properties files using jproperties or configparser libraries.
