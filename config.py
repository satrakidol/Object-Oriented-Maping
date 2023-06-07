from dotenv import load_dotenv
import os


APP_ROOT = os.path.dirname(__file__)
dotenv_path = os.path.join(APP_ROOT, '.env')
print(dotenv_path)
load_dotenv(dotenv_path)

connection_string = os.getenv("DBURL")
print(f"connection_string = {connection_string}")

SECRET_KEY = os.getenv("SECRET_KEY")
