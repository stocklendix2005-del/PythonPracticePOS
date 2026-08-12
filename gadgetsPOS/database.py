import sqlite3

# from customers import open_customers


def init_db():
    conn = sqlite3.connect("phones.db")
    c = conn.cursor()

    c.execute("PRAGMA foreign_keys = ON;")

    # Phones Table
    c.execute("""
        CREATE TABLE IF NOT EXISTS phones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_code TEXT GENERATED ALWAYS AS ('G' || PRINTF('%04d', id)),
            brand TEXT,
            model TEXT,
            price INTEGER,
            category TEXT,
            quantity INTEGER
    );
""")

    # Sales Table
    c.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_code TEXT GENERATED ALWAYS AS('SL'||PRINTF('%04d',id)) VIRTUAL,
            customer TEXT,
            location INTEGER,
            date INTEGER,
            vat INTEGER,
            grand_total INTEGER
        )
    """)

    # Customer Table
    c.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_code TEXT GENERATED ALWAYS AS('CUS' || PRINTF('%04d',id)),
            id_number INTEGER NOT NULL,
            name TEXT,
            location TEXT,
            mobile TEXT,
            status TEXT
            )
            """)

    # sale_items table
    c.execute("""
        CREATE TABLE IF NOT EXISTS sale_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_id TEXT NOT NULL,
            item_id INTEGER NOT NULL,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            total_price REAL NOT NULL,
            
            FOREIGN KEY(sale_id) REFERENCES sales(sale_id)
            )""")

    conn.commit()
    conn.close()


init_db()


def get_connection():
    return sqlite3.connect("phones.db")


def get_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    return customers


def get_gadgets():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phones")
    gadgets = cursor.fetchall()
    return gadgets


def get_sales():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales")
    sales = cursor.fetchall()
    return sales


def get_notification():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phones WHERE quantity<5")
    low_stock = cursor.fetchall()
    return low_stock


def get_searchCustomer(term):
    conn = get_connection()
    cursor = conn.cursor()
    if term:
        cursor.execute(
            """SELECT * FROM customers WHERE 
            LOWER(name) LIKE LOWER(?) OR 
            LOWER(mobile) LIKE LOWER(?) OR 
            LOWER(customer_code) LIKE LOWER(?) OR 
            LOWER(id_number) LIKE LOWER(?)""",
            ("%" + term + "%", "%" + term + "%", "%" + term + "%", "%" + term + "%"),
        )
        searched_results = cursor.fetchall()
        return searched_results
    else:
        print("no match")


def update_customers(id, name, location, mobile, status):
    conn = get_connection()
    cursor = conn.cursor()
    id = id
    name = name
    location = location
    mobile = mobile
    status = status
    cursor.execute(
        """UPDATE customers SET 
                            name=(?),
                            location=(?),
                            mobile=(?),
                            status=(?)
                            WHERE
                            id = (?)
                            """,
        (name, location, mobile, status, id),
    )
    conn.commit()
    conn.close()
