def add_gadgets():
    import sqlite3
    conn = sqlite3.connect("phones.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS phones(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              brand TEXT,
              model TEXT,
              price INTEGER,
              category TEXT,
              quantity INTEGER)""" )
    brand = input("Enter brand name: ")
    model = input("Enter model name: ")
    price = int(input("Set Price: "))
    category = input("Enter category: ")
    quantity = int(input("Enter Qty: "))
    c.execute("""INSERT INTO phones(brand,model,price,category,quantity)
              VALUES(?,?,?,?,?)""",(brand,model,price,category,quantity))
    conn.commit()
    conn.close()
    print("Gadget Added Successfully")



    conn = sqlite3.connect("phones.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS sales(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              item TEXT,
              customer TEXT,
              quantity INTEGER,
              price INTEGER,
              total_price INTEGER,
              vat INTEGER,
              location TEXT,
              date TEXT)""" )
    conn.commit()
    conn.close()

def display_gadgets():
    import sqlite3
    conn = sqlite3.connect("phones.db")
    c = conn.cursor()

    print("\n===GADGET VIEW===")
    print("1. View all gadgets")
    print("2. Categories")
    option = input("Enter Option: ")
    if option == "1":
            c.execute("SELECT * FROM phones")
            phones = c.fetchall()
            print("\n----------GADGETS----------")
            print("No Brand     Model     Price  Category   Qty")
            for i, phone in enumerate(phones, start=1):
                print(i, "|", phone[1], "|", phone[2], "|", phone[3], "|", phone[4], "|", phone[5])
            conn.close()
            return
    elif option == "2":
        display_category()

def search_gadgets():
    import sqlite3
    conn = sqlite3.connect("phones.db")
    c = conn.cursor()

    name = input("Enter Brand Name to find: ")
    c.execute("SELECT * FROM phones WHERE LOWER(brand) = LOWER(?)",(name,))
    result = c.fetchall()

    if len(result) == 0:
        print("Nothing To Show! ")
    else:
        for phone in result:
            print("\nBrand:",phone[1])
            print("Model: ", phone[2])
            print("price: ", phone[3])
            print("Qty: ", phone[5])
    conn.close()  

def delete_phone():
    import sqlite3
    conn = sqlite3.connect("phones.db")
    c = conn.cursor()

    name = input("Enter brand to delete: ")
    c.execute("DELETE FROM phones WHERE LOWER(brand) = LOWER(?)",(name,))
    conn.commit()
    if c.rowcount == 0:
        print("No gadget found! ")
    else:
        print(c.rowcount," Gadget(s) deleted successfully")

    conn.close()

def sales_table():
    import sqlite3
    conn = sqlite3.connect("phones.db")
    c = conn.cursor()
    
    c.execute("""CREATE TABLE IF NOT EXISTS sales(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              brand TEXT,
              model TEXT,
              price INTEGER,
              quantity INTEGER,
              total INTEGER,
              date TEXT)""")
    conn.commit()
    conn.close()

from datetime import datetime
import sqlite3
def sale_processing():
    conn = sqlite3.connect("phones.db")
    c = conn.cursor()

    brand = input("Enter brand to sell ")
    c.execute("SELECT * FROM phones WHERE LOWER(brand) = LOWER(?)",(brand,))
    phone = c.fetchone()

    if not phone:
        print("Nothing to show ")
        conn.close()
        return
    
    qty = int(input("Enter Quantity: "))
    if qty > phone[5]:
        print("Insufficient stock! ")
        conn.close()
        return
    
    new_price = phone[5] - qty
    total = phone[3] * qty

    c.execute("UPDATE phones SET quantity = ? WHERE id = ?",(new_price,phone[0]))
    c.execute("""INSERT INTO sales(brand,model,price,quantity,total,date)
              VALUES(?,?,?,?,?,?)""",(phone[1],phone[2],phone[3],qty,total,datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))
    conn.commit()
    c.execute("SELECT * FROM sales WHERE quantity = ? AND date = ?",(qty,datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))
    gadget = c.fetchone()
    print(f"{gadget[1]} {gadget[2]} sold {qty} piece(s)")
    receipt = input(f"Do you want to generate a receipt? yes/no: ")
    if receipt == "yes".lower():
        print(f"\n---------SALES RECEIPT-------")
        print(f"Date: {gadget[6]} ")
        print(f"LEN ELECTRONICS")
        print(f"Item: {gadget[1]} {gadget[2]}")
        print(f"Quantity: {qty}")
        print(f"Price: Kes {gadget[3]}")
        print(f"Total: Kes {total}")
        print(f"==========================")
    elif receipt == "no".lower():
        return
    conn.close()

def view_sales():
    conn = sqlite3.connect("phones.db")
    c = conn.cursor()

    c.execute("SELECT * FROM sales")
    sales = c.fetchall()
    if not sales:
        print("Nothing to show!")
    else:
        print("======SALES=====")
        for sale in sales:
            print(sale[0],"||",sale[1], "|",sale[2],"|",sale[3],"|",sale[4],"|",sale[5],"|",sale[6])
    conn.close()

def low_stock_alert():
    conn = sqlite3.connect("phones.db")
    c = conn.cursor()
    c.execute("SELECT * FROM phones WHERE quantity < 5")
    low = c.fetchall()
    for i, lo in enumerate(low, start=1):
        print(f"⚠ ⚠ {i} {lo[1]} {lo[2]} is low! ⚠ ⚠")
    conn.close()


def display_category():
    conn = sqlite3.connect("phones.db")
    c = conn.cursor()

    print("\n===CATEGORIES===")
    print("1. Phones")
    print("2. Tablets")
    print("3. Computers")
    def category_logic():
        c.execute("SELECT * FROM phones WHERE LOWER(category) = LOWER(?)",(name,))
        phones = c.fetchall()
        if len(phones) == 0:
            print(f"{len(phones)} {name} found!")
        else:
            print(f"----{len(phones)} {name} found----")
            for i, phone in enumerate(phones, start=1):
                print(f"{i} {phone[1]} {phone[2]} | {phone[3]} | {phone[5]}")
    option = input("Enter option: ")
    if option == "1":
        name = "phones"
        category_logic()
    elif option == "2":
        name = "tablets"
        category_logic()
    elif option == "3":
        name = "computers"
        category_logic()
        conn.close()
        return
    else:
        print("Invalid!")

def update_inventory():
    conn = sqlite3.connect("phones.db")
    c = conn.cursor()
    brand = input("Enter Brand to Update Qty:")
    model = input("Which model: ")
    quantity = int(input("Enter Qty to Add On: "))
    c.execute("UPDATE phones SET quantity = (quantity + ?) WHERE LOWER(brand) = LOWER(?) AND LOWER(model) = LOWER(?)",(quantity,brand,model))
    conn.commit()
    print(f"{c.rowcount} Item(s) Updated successfully")
    conn.close()

sales_table()
while True:
    print("\n=================MENU=================")
    low_stock_alert()
    print("1. Add Gadgets ")
    print("2. Display Gadgets ")
    print("3. Search Gadgets ")
    print("4. Delete Gadget")
    print("5. Make a sell")
    print("6. View sales")
    print("7. View category")
    print("8. Update Inventory")
    print("0. Exit")
    option = input("Enter Option: ")
    if option == "1":
         add_gadgets()
    elif option == "2":
        display_gadgets()
    elif option == "3":
        search_gadgets()
    elif option == "4":
        delete_phone()
    elif option == "5":
        sale_processing()
    elif option == "6":
        view_sales()
    elif option == "7":
        display_category()
    elif option == "8":
        update_inventory()
    elif option == "0":
        break
    

