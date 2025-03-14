import sqlite3
from contextlib import closing


db_path="sqlite3.db"

try:
    with closing(sqlite3.connect(db_path)) as db_conn:
        db_conn.row_factory = sqlite3.Row
        with closing(db_conn.cursor()) as cursor:
            try:
                query_1= "SELECT * from demo WHERE id > 14"
                cursor.execute(query_1)
                rows = cursor.fetchall()
                print("Name of rows with id>14")
                for row in rows:
                    print(row["name"])
            except Exception as e:
                print(f"Error executing query_1: {e}")
            # Delete Row based on the user input
            try:
                del_row = int(input("enter the row ID for deletion: "))
                query_2= "DELETE from demo WHERE id < ?"
                cursor.execute(query_2, (del_row,))
                num_rows = cursor.rowcount
                print(f"{num_rows} rows affected.")
                db_conn.commit()
            except Exception as e:
                print(f"Error executing query_2: {e}")
except sqlite3.Error as e :
    print(f"Database execution Error: {e}")
