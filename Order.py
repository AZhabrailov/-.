import sqlite3

class Order:
    def __init__(self, name, order_details):
        self.name = name
        self.order_details = order_details

    def __str__(self):
        return f"Customer: {self.name}, Order Details: {self.order_details}" 

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                         name text,
                         order_details text
                     )''')
    conn.commit()

def add_order(conn, name, order_details):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (name, order_details) VALUES (?, ?)", (name, order_details))
    conn.commit()

def delete_order(conn, name):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders WHERE name = ?", (name,))
    conn.commit()

def get_orders(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(Order(row[0], row[1]))  
    else:
        print("Order list is empty.")


db_file = "orders.db"


conn = create_connection(db_file)
create_table(conn)


"""add_order(conn, 'Влада', 'Пицца')
add_order(conn, 'Михаил', 'Паста')"""

conn.close()