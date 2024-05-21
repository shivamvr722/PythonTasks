import psycopg2

# forming the connection 
def create_connection():
    return psycopg2.connect( 
        database="task_management", 
        user='postgres', 
        password='Dev@123', 
        host='127.0.0.1', 
        port='5432'
    )