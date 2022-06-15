""" Here we would like to use the secrets library to generate a random secret key.
    After generating a random secret key write that key to .env file created from this script.
    This is a file to not use after the app has been created.  It will just help in starting out the project.
    It will throw an error if you try to use this program twice in the same directory."""
import secrets
key = secrets.token_urlsafe(16)

with open("./.env", "x") as f:
    f.write(f'SECRET_KEY = {key}')
    f.close()