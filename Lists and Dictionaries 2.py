phones = [{"Brand": "iPhone", "Model": "17 Pro Max", "Price": 180000},
          {"Brand": "Samsung", "Model": "S26 Ultra", "Price": 175000},
          {"Brand": "Oppo", "Model": "Reno 1", "Price": 30000}
]
def total_phones(phones):
    total = len(phones)
    print(total)

def show_brands(phones):
    for phone in phones:
        print(phone["Brand"],phone["Model"])

def expensive_phones(phones):
    for phone in phones:
        if phone["Price"] > 100000:
            print(phone["Brand"])

total_phones(phones)
show_brands(phones)
expensive_phones(phones)




        
    