import json

def load_phones():
    try:
        with open("phones.json", "r") as file:
            return json.load(file)
    except:
        return[]
    
def save_phones(phones):
    with open("phones.json", "w") as file:
        json.dump(phones, file)

import json
from datetime import datetime

def load_sales():
    try:
        with open("sales.json", "r") as file:
            return json.load(file) 
    except:
        return[]
    
def save_sales(sales):
    with open("sales.json", "w") as file:
        json.dump(sales, file)

def display_phones(phones):
    if len(phones) == 0:
        print("Nothing to show ")
        return
    print("\nNo |  Brand  |  Model  |  Price  | Qty ")
    print("-------------------------------------------")
    for i, phone in enumerate(phones, start=1):
        print(i,"|", phone["brand"],"|", phone["model"], "|", phone["price"], "|", phone["quantity"])
        

def add_phones(phones):
        Brand = input("Enter Brand Name ")
        Model = input("Enter Model Name ")
        Price = int(input("Enter Price "))
        Category = input("Enter Category ")
        quantity = int(input("Enter Quantity "))

        phones.append({"brand": Brand,
                           "model": Model,
                           "price": Price,
                           "category": Category,
                           "quantity": quantity})
        save_phones(phones)
        print("Gadget added successfully ")

def find_phones(phones):
    name = input("Enter brand name? ")
    found = False
    for phone in phones:
        if phone["brand"].lower() == name.lower():
            print(phone["brand"], phone["model"], phone["price"])
            found = True
    if not found:
        print("Invalid!")
           
def delete_phones(phones):
    name = input("Enter brand to delete ")
    for phone in phones:
        if phone["brand"].lower() == name.lower():
            phones.remove(phone)
            save_phones(phones)
            print("Phone Deleted Successfully")
            return
    print("Not found! ")

def update_price(phones):
    name = input("Enter brand to update ")
    for phone in phones:
        if phone["brand"].lower() == name.lower():
            phone["price"] = int(input("Enter new price "))
            print(phone["brand"], phone["model"], phone["price"])
            save_phones(phones)
            print("Price changed successfully")
            return
    print("Invalid!")

def sort_phones(phones):
    phones.sort(key=lambda phone: phone["price"])
    save_phones(phones)
    print("phone sorted successfully")

def display_category(phones):
    print("\n1. Phones")
    print("2. Laptops")
    print("3. Tablets")
    print("4. Add Category")
    option = input("Enter Option: ")
    if option.lower() == "1":
        category = "Phones"
    elif option.lower() == "2":
        category = "Laptops"
    elif option == "3":
        category = "Tablets"
    elif option == "4":
        add_phones(phones)
    else:
        print("Invalid Option! ")
        return
    found = False
    for phone in phones:
        if phone["category"].lower() == category.lower():
            print(phone["brand"], phone["model"], phone["price"])
            found = True
    if not found:
        print("No item(s) to show ")

def total_stock_value(phones):
    total = 0
    for phone in phones:
        ttl_value = phone["quantity"] * phone["price"]
        total += ttl_value
    print("Total Value: ", total)

def phones_statistics(phones):
    if len(phones) == 0:
        print("There is nothing to show ")
        return
    total_items = len(phones)
    phones_count = 0
    laptop_count = 0
    tablet_count = 0
    total_value = 0
    expensive = phones[0]
    cheapest = phones[0]

    for phone in phones:
        category = phone["category"].lower()
        if category == "phones":
            phones_count += 1
        elif category == "laptops":
            laptop_count += 1
        elif category == "tablets":
            tablet_count += 1
        total_value += phone["price"]

        if expensive["price"] < phone["price"]:
            expensive = phone    
        if cheapest["price"] > phone["price"]:
            cheapest = phone
    average_price = total_value/total_items 

    print("⭐⭐ STATISTICS. ⭐⭐")
    print("------------------------")  
    print("\n1. Total Gadgets: ", total_items)
    print("2. Total Phones: ", phones_count)
    print("3. Total Laptops: ", laptop_count)
    print("4. Total Tablets: ", tablet_count)
    print("5. Total Price Value: ", total_value)
    print("6. Average Price: ", average_price)
    print("7. Cheapest Gadget: ", )
    print(cheapest["brand"], cheapest["model"], cheapest["price"])
    print("8. Most Expensive: ")
    print(expensive["brand"], expensive["model"], expensive["price"])
    
    
def filter_gadgets(phones):
    print("\n1. Under Kes 50,000")
    print("2. Kes 50,000 to Kes 100,000")
    print("3. Above 100,000")
    option = input("Enter Option ")
    found = False
    for phone in phones:
        price = phone["price"]
        if option == "1" and price < 50000:
            print(phone["brand"], phone["model"], phone["price"])
            found = True
        elif option == "2" and 50000 <= price <= 100000:
            print(phone["brand"], phone["model"], phone["price"])
            found = True
        elif option == "3" and price > 100000:
            print(phone["brand"], phone["model"], phone["price"])
            found = True
    if not found:
        print("Invalid! ")   

def low_stock_alert(phones):
    found = False
    for phone in phones:
        if phone["quantity"] < 5:
            print("⚠ LOW STOCK ALERT")
            print(phone["brand"], phone["model"], " Is Low!")
            found = True
    if not found:
        print("Healthy Stock")
            
def update_inventory(phones):
    change = input("Enter Brand To Update Qty:")
    for phone in phones:
        if change.lower() == phone["brand"].lower():
            new = int(input("Enter New Qty: "))
            phone["quantity"] = new
            save_phones(phones)
            print("Quantity Updated Successfully ")
            return
        
    print("Invalid ")  

def sale_phones(phones):
    sales = load_sales()
    sale = input("Enter Brand to sell ")
    for phone in phones:
        if sale.lower() == phone["brand"].lower():
            qty = int(input("Enter Qty: "))
            if qty > phone["quantity"]:
                print("Select a lower qty!! ")
                return
            phone["quantity"] -= qty
            save_phones(phones)
            total = qty * phone["price"]
            sales.append({"brand": phone["brand"],
                      "model": phone["model"],
                      "quantity": qty,
                      "price": phone["price"],
                      "total": total,
                      "date": datetime.now().strftime("%d-%m-%Y %H:%M")
                      })
        save_sales(sales)

             
        print(phone["brand"], phone["model"], " Sold successfully")
        print("Remaining", phone["quantity"])
        sales_receipt(phone, qty, total)
        return
    
    print("No gadget in stock!")

def view_sales():
    sales = load_sales()
    if len(sales) == 0:
        print("No Sale(s) to view")
        return
    
    print("\n-----SALES HISTORY-----")
    for i, sale in enumerate(sales, start=1):
        print(i, sale["brand"], sale["model"], "|",
              "Qty ", sale["quantity"],
              "| Sale total:", sale["total"],
              "|", sale["date"])
        
def sales_receipt(phone, qty, total):
    print("\n--------------RECEIPT--------------")
    print("Len.Co.Ke Gadgets")
    print("Date: ", datetime.now().strftime("%d%m%Y, %H:%M:%S"))
    print("Brand: ", phone["brand"])
    print("Model: ", phone["model"])
    print("Qty :", qty)
    print("Price: ", phone["price"])
    print("Total: ", total)

print("WELCOME TO PHONE MANAGER.")
welcome = input(" PROCEED? yes/no: ")
if welcome.lower() == "yes":
    password = input("Please Enter Password: ")
    if password == "4147":

        phones = load_phones()
        while True:
            print("\n-----MENU-----")
            low_stock_alert(phones)
            print("1. Display Phones📱")
            print("2. Add Gadgets➕")
            print("3. Search Phones🔍")
            print("4. Delete Phones❌")
            print("5. Update Price📈")
            print("6. Sort phones by price")
            print("7. Display Category")
            print("8. Statistics")
            print("9. Filter Gadgets")
            print("10.Gadgets Value")
            print("11. Udate Inventory")
            print("12. Make a Sale")
            print("13. View sales history")
            print("14. Exit")

            choice = input("Enter Option ")
            if choice == "1":
                display_phones(phones)
            elif choice == "2":
                add_phones(phones)
            elif choice == "3":
                find_phones(phones)
            elif choice == "4":
                delete_phones(phones)
            elif choice == "5":
                update_price(phones)
            elif choice == "6":
                sort_phones(phones)
            elif choice == "7":
                display_category(phones)
            elif choice == "8":
                phones_statistics(phones)
            elif choice == "9":
                filter_gadgets(phones)
            elif choice == "10":
                total_stock_value(phones)
            elif choice == "11":
                update_inventory(phones)
            elif choice == "12":
                sale_phones(phones)
            elif choice == "13":
                 view_sales()
            elif choice == "14":
                break
    else:
        print("Wrong Password! ")

elif welcome.lower() == "no":
    print("Thank You,")
    


    
    




        
          
    
        
        


    