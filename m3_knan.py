# https://realpython.com/python-mysql/

import mysql.connector
print("-------Hello world!---------")
print("----------------------------")
print("Connect to knan project's database")
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

# create_movies_table_query = """
# CREATE TABLE main(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     device DECIMAL(15),
#     pcb_main DECIMAL(15),
#     c_sensor DECIMAL(15),
#     c_oled DECIMAL(15),
#     note VARCHAR(100)
# )
# """
# with conn.cursor() as cursor:
#     cursor.execute(create_movies_table_query)
#     conn.commit()
print("Plz select the tables you want to display:")

show_db_query = "SHOW TABLES"
with conn.cursor() as cursor:
    cursor.execute(show_db_query)
    for db in cursor:
        print(db)
# # Connect to knan project's database
# cnx = mysql.connector.connect(user='scott', password='password',
#                               host='127.0.0.1',
#                               database='employees')
print("Show main's tables data schema:")
show_table_query = "DESCRIBE main"
with conn.cursor() as cursor:
    cursor.execute(show_table_query)
    # Fetch rows from last executed query
    result = cursor.fetchall()
    for row in result:
        print(row)

#Insert new records to table

# insert_movies_query = """
# INSERT INTO main (device, pcb_main, c_sensor, c_oled, note)
# VALUES
#     (232114010001, 232114010005, 232114050011, 232114060021, ""),
#     (232114010002, 232114010003, 232114050012, 232114060013, "dsadsad")
# """
# with conn.cursor() as cursor:
#     cursor.execute(insert_movies_query)
#     conn.commit()
print("Show main's table's content:")
select_movies_query = "SELECT * FROM main LIMIT 10"
with conn.cursor() as cursor:
    cursor.execute(select_movies_query)
    result = cursor.fetchall()
    for row in result:
        print(row)
        
conn.close()