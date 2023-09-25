import os


DATABASE = os.environ["DATABASE"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_NAME = os.environ["TASK_DB_NAME"]
DB_HOST = os.environ["DB_HOST"]

DB_URL = f"{DATABASE}+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
