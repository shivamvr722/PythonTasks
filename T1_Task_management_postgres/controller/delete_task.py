import sys
sys.path.insert(0, "/home/shivam-rana/python/T1_Task_management/")
from dbconnection.dbconnect import create_connection

conn = create_connection()
cursor = conn.cursor()


def delete_task(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    cursor.execute(sql, id)
    conn.commit()
    if(cursor.rowcount):
        return cursor.rowcount
    else:
        return False