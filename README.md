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
  - Flask reads TOML files without a section. If section is to be used, read the file in binary mode and load the property key and value then set flask config param.
    ```
    with open('config\\app_configs.toml', 'rb') as f:
      config = tomllib.load(f)

    print(config['flask']['SECRET_KEY'])

    app.config['SECRET_KEY] = config['flask']['SECRET_KEY']
    ```
- Properties file
  - Read configurations from properties files using jproperties or configparser libraries.
