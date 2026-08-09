phones = [{"Brand": "iPhone", "Model": "17 Pro Max", "Price": 180000},
          {"Brand": "Samsung", "Model": "S26 Ultra", "Price": 175000},
          {"Brand": "Oppo", "Model": "Reno 1", "Price": 30000}
]
def display_phones(phones):
    for i in range(len(phones)):
        phone = phones[i]
        print(i+1, phone["Brand"], phone["Model"], phone["Price"])

def find_phones(phones):
    name = input("Enter Phone ")
    for phone in phones:
        if phone["Brand"].lower() == name.lower():
            print("Found: ", phone["Brand"],phone["Model"],phone["Price"])
            return
        
    print("Invalid Option")

def add_phones(phones):
    brand = input("Enter Brand: ")
    model = input("Enter Model: ")
    price = int(input("Enter Price: "))

    phones.append({"Brand": brand,
                  "Model": model,
                  "Price": price})
    print("Phone Added Successfully! ")
    for i in range(len(phones)):
        phone = phones[i]
        print(i+1, phone["Brand"], phone["Model"], phone["Price"])

def delete_phone(phones):
    for phone in phones:
        delete = input("Enter Brand you want to delete ")
        if delete.lower() == phone["Brand"].lower():
            phones.remove(phone)
            print ("Phone Successfully Deleted")
            return
        print("Phone not found! ")
        
def update_price(phones):
    name = (input("Enter Brand to Update Price "))
    for phone in phones:
        if phone["Brand"].lower() == name.lower():
            new_price = int(input("Enter New Price "))
            phone["Price"] = new_price
            print("Price Updated Successfully ")
            return
    print("Invalid!")
        
        
welcome = input("Welcome Proceed to menu? yes/no ")
print(welcome)
if welcome.lower() == "yes".lower():
    while True:
        print("\n1. Display Phones. ")
        print("2. Find Phone.🔍")
        print("3. Add a Phone. ")
        print("4. Delete Phone. ")
        print("5. Update Price")
        print("6. Exit")
        choice = input("Enter Option ")
        if choice == "1":
            display_phones(phones)
        elif choice == "2":
            find_phones(phones)
        elif choice == "3":
            add_phones(phones)
        elif choice == "4":
            delete_phone(phones)
        elif choice == "5":
            update_price(phones)
        elif choice == "6":
            print("Thank You")
            break
        
            
else:
    print("Thank You.")
    




    
    



   


    

                  

    