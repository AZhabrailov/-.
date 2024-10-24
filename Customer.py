import sqlite3




class Customer:
    def __init__(self, name, amount, num):
        self.name = name
        self.amount = amount
        self.num = num

    def __str__(self):
        return f"Customer: {self.name}, Number of People: {self.amount}, Number: {self.num}"

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

def create_table(db_file):
    with create_connection(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                             name text,
                             amount integer,
                             num integer
                         )''')

def add_customer(db_file, name, amount, num):
    with create_connection(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, amount, num) VALUES (?, ?, ?)", (name, amount, num))

def delete_customer(db_file, name):
    with create_connection(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE name = ?", (name,))

def print_database_info(db_file):
    with create_connection(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()

        if rows:
            print("Список клиентов::")
            for row in rows:
                print(Customer(row[0], row[1], row[2]))
        else:
            print("The customers table is empty.")


db_file = "customers.db"

create_table(db_file)

"""
add_customer(db_file, 'Влада', 3, 101)
add_customer(db_file, 'Миша', 4, 102)"""

