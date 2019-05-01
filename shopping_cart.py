# shopping_cart.py
import datetime
import locale

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#Convert to USD Format
def to_usd(value):
        locale.setlocale(locale.LC_ALL, 'en_US.utf-8') 
        s = locale.currency(value, grouping=True)
        return s

#Convert Month Code
def month_converter(monthCode):
    full_month = {'1':'January','2':'February','3':'March','4':'April',
    '5':'May','6':'June','7':'July','8':'August','9':'September','10':'October',
    '11':'November', '12':'December'}
    return full_month[monthCode]

#Convert Timestamps
def hf_timestamp(utc_Stamp):
    today = datetime.datetime.now()
    year = str(today.year)
    month = str(today.month)
    month = month_converter(month)
    day = str(today.day)
    hour = str(today.hour)
    minute = str(today.minute)
    today = month + " " + day + ", " + year + " " + hour + ":" + minute
    return today 

#Introduce the User
print("Welcome to Matt's Grocery Store! You are now ready to create a new receipt.")

print("")

#create the list to store the item numbers
receipt_list = []
subtotal = 0.0
receipt_counter = 0

# While loop to determine products
while True:
    # capturing user input and storing in a variable
    user_input = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    
    if user_input == "Done" or user_input == "DONE" or user_input == "done":
        break

    # demonstrating ability to recognize what the input was, although you might also want to check its datatype
    if user_input != "Done":
            matching_product = [product for product in products if product["id"] == int(user_input)]
            if matching_product != []:
                receipt_list.append(matching_product)
                receipt_counter = receipt_counter + 1
                subtotal = subtotal + float(matching_product[0]["price"])
            else:
                print("Uh oh! You have entered an invalid product ID. Please try again")

#print the receipt
print("")   
print("------------------------------------------------------------")
print("Matt's Grocery Store")
print("------------------------------------------------------------")
print("www.mystore.com")
print("+1 (202) 555-5555")
now = datetime.datetime.now()
print("Checkout Time: " + hf_timestamp(now))
print("------------------------------------------------------------")
print("Shopping Cart Items:")
rec_count = 0
for item in receipt_list:
    print("+ " + str(item[0]["name"]) + " (" + to_usd(item[0]["price"]) + ")")
    rec_count = rec_count + 1
print("------------------------------------------------------------")
print("Subtotal: " + to_usd(subtotal))

#calculate tax
tax_rate  = 0.06

total_tax = subtotal * (tax_rate)
print("Sales Tax: (6%): " +  to_usd(total_tax))

#Caclulate Total price
total_price = subtotal + total_tax
print("Total: " + to_usd(total_price))
print("------------------------------------------------------------")
print("You have purchased " + str(receipt_counter) + " items")
print("")

