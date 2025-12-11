import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','.env'))

db_file = os.getenv('SQLITE_DB_FILE')
print(db_file)
my_name = os.getenv('MY_NAME')
print(my_name)
