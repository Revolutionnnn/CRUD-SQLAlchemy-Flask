from dotenv import load_dotenv
import os
load_dotenv()

user = os.environ['MY_SQL_USER']
password = os.environ['MY_SQL_PASSWORD']
host = os.environ['MY_SQL_HOST']
database = os.environ['MY_SQL_DATABASE']
