import pymysql.cursors
import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 3306)
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_DATABASE = os.getenv("DB_DATABASE", "intros-ai")

database = pymysql.connect(
     host=DB_HOST,
     port=DB_PORT,
     user=DB_USER,
     password=DB_PASSWORD,
     db=DB_DATABASE
)

# columns can either take the list of columns to select or an empty list or None to select all columns
def select(table, columns=None):
     """Select rows from a given table

     Args:
         table (String): The table to select from
         columns (List of Strings, optional): The columns to add to the result of selected rows. Defaults to None.

     Returns:
         List of dicts: List of key/value dicts for rows returned with the column names
     """
     rows_list = []
     if not columns:
          columns_str = "*"
     else:
          columns_str = ", ".join(columns)
     cursorObject = database.cursor()
     insertStatement = "SELECT {} FROM {}".format(columns_str, table)
     cursorObject.execute(insertStatement)
     rows = cursorObject.fetchall()
     num_fields = len(cursorObject.description)
     field_names = [i[0] for i in cursorObject.description]
     for row in rows:
          record = {}
          for i in range(num_fields):
               record[field_names[i]] = row[i]
          rows_list.append(record)
     return rows_list