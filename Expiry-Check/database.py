import sqlite3

class expiry_data():
    def __init__(self,connection) -> None:
        with connection:
            connection.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, expiry_date TEXT);")
    
    def connect(self, connection):
        connection = sqlite3.connect("data.db")
        return connection
    
    def add(self, connection, name, expiry_date):
        with connection:
            connection.execute("INSERT INTO data (name, expiry_date) VALUES (?,?);", (name, expiry_date))


    def delete(self, connection, name):
        with connection: 
            connection.execute("DELETE FROM table WHERE name == name;", (name))

    def display(connection):
        with connection:
            return connection.execute("SELECT * FROM data ORDER BY expiry_date ASC")