import sqlite3

class database():
    def __init__(self) -> None:
        pass
        
    def connect(self):
        self.connection = sqlite3.connect("data.db")
        return self.connection
    
    def create_table(self): 
        with self.connection:
            self.connection.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, expiry_date TEXT);")

    def add(self, name, expiry_date):
        with self.connection:
            self.connection.execute("INSERT INTO data (name, expiry_date) VALUES (?,?);", (name, expiry_date))

    def delete(self, name):
        with self.connection: 
            self.connection.execute("DELETE FROM table WHERE name == name;", (name))

    def display(self):
        with self.connection:
            return self.connection.execute("SELECT * FROM data ORDER BY expiry_date ASC")