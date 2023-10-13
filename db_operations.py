import sqlite3


class DbOperations:

  def connect_to_db(self):
    conn = sqlite3.connect('password_records.db')
    return conn

  def create_table(self, table_name = "password_info"):
    conn = self.connect_to_db()
    query = f'''
    CREATE TABLE IF NOT EXISTS {table_name}(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        website TEXT NOT NULL,
        username VARCHAR(200),
        password VARCHAR(50)
    );
    '''


    with conn as conn:
      cursor = conn.cursor()
      cursor.execute(query)
      print("Create the table")
