#Practicing my coding for python by creating my own bakery
def greet_customer(name):
    return f"Hi {name} , welcome to my bakery"

def get_bread_from_bakery(name):
    return f" I am getting {name} today"

#key value pair 
menu = {  
    "white": 3.00,
    "wheat": 3.50,
    "sourdough": 4.25,
    "rye":4.00
}

#Start
customer_name = input("what's your name?")
print(greet_customer(customer_name))
print("\nOur Menu:")
#bread will get the key like "white" , price will get the value like "3.00"
for bread,price in menu.items():
    print(f"-{bread} ${price:.2f}")
print("Type 'done' when finished selecting.\n")

#Creating an empty list to store the order
orders = [] 

#.strip removes spacing from start to end of string and .lower turns letters to lowercase
while True:
    bread_choice = input("What kind of bread would you like?").strip().lower()

    if bread_choice == "done":
        break
    elif bread_choice in menu:
        orders.append(bread_choice)
        print(get_bread_from_bakery(bread_choice))
    else:
        print("I'm sorry , we do not have that type of bread.")

#Summary 
print("\nYour bread order for the day")
total = 0
for bread in orders:
    total += menu[bread]
    print(f" - {bread}: ${menu[bread]:.2f}")

print(f"Total: ${total:.2f}")
print("Thank you for visiting the bakery!")
