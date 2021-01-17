import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='cxzzxcCC',
         host='127.0.0.1',
         database='m3_knan')

# create_movies_table_query = """
# CREATE TABLE movies(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(100),
#     release_year YEAR(4),
#     genre VARCHAR(100),
#     collection_in_mil INT
# )
# """

create_movies_table_query = """
CREATE TABLE movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
"""
with conn.cursor() as cursor:
    cursor.execute(create_movies_table_query)
    conn.commit()


show_db_query = "SHOW TABLES"
with conn.cursor() as cursor:
    cursor.execute(show_db_query)
    for db in cursor:
        print(db)
        
conn.close()