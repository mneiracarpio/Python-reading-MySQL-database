import mysql.connector

try:
    connection=mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="password",
        db="world"
    )
    if connection.is_connected():
        print("Success!")
        server_info = connection.get_server_info()
        print(server_info)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")
        row = cursor.fetchone()
        print("You are connected to {}".format(row))
except Exception as ex:
    print(ex)
finally:
    if connection.is_connected():
        connection.close()
        print("End of connection")