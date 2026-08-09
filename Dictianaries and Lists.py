phones = [{"Brand": "iPhone", "Model": "17 Pro Max", "Price": 180000},
          {"Brand": "Samsung", "Model": "S26 Ultra", "Price": 175000},
          {"Brand": "Oppo", "Model": "Reno 1", "Price": 30000}
]

#Adding a Phone
phones.append({"Brand":"Google", "Model": "Pixel 7", "Price": 120000})
for phone in phones:
    print(phone["Brand"], phone["Model"])
#cheapest phone
cheapest = phones[0]
for phone in phones:
    if phone["Price"] < cheapest["Price"]:
        cheapest = phone
print("Cheapest Phone is ", cheapest["Brand"], cheapest["Model"])
#phones past 50000
for phone in phones:
    if phone["Price"] >= 50000:
        print(phone["Brand"])
#total Number of Phones
total = len(phones)
print(total)
#total number of phones above 100000
count = 0
for phone in phones:
    if phone["Price"] >= 100000:
        count += 1
print(count)

    


        


   

    
  





         