#Python Programming

#Variable
#students_counts = 1000
#print(students_counts)
#Boolean
#is_published = False
#String
#course_name = "This is python"
#print(is_published)
#print(course_name)

#Escape Sequences
#\"
#\'
#\
#\n

#Conversion
#x = input("x:")
#print(type(x))
#y = int(x) + 1
#print(f"x: {x},  y: {y}")
#int(x)
#float(x)
#bool(x)
#str(x)

#Conditional Statement
#temperature = 15
#if temperature > 30:
    #print("It's warm")
    #print("Drink water")
#elif temperature > 20:
    #print("It's nice")
#else:
    #print("It's cold")
#print("Done")

#Ternary Operator 
#age = 22
#if age >= 18:
    #print("Eligible")
#else:
    #print("Not Eligible")
#Ternary Operator
#message = "Eligible" if age >= 18 else" Not eligible"
#print(message)

#Logical Operators
#high_income = False
#good_credit = True
#student = False
#if not student:
    #print("Eligible")
#else:
    #print("Not Eligible")

#AND Operator = will list only if both conditions are men
#Or Operator = will list only if ONE condition is met

#Chaining Comparison Operators
#age = 22
#if 18<= age < 65:
    #print("Eligible")

#FOR LOOP
for number in range(1,10,2):
    print("Attempt", number , number  * ".")
#FOR ELSE
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break # allows to exit a loop , only FOR LOOP and WHILE LOOP
else:
    print("Attempted 3 times and failed")

#NESTED LOOPS
for x in range(5):
    for y in range(3):
        print(f"({x} , {y})" )

#WHILE LOOPS
number = 100
while number > 0:
    print(number)
    number //= 2
    break
#real example
command = ""
while command != "quit" and command != "QUIT":
    command = input(">")
    print("ECHO", command)

#Defining Functions
def greet(first_name , last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome Aboard")

greet("Mocha","Dog")

#Parameter is the input you are defining
#Parameter is first_name , last_name
#Argument is the value of the parameter
#Argument is "Mocha" ," Dog"

#Common way to write Function
def get_greeting(name):
    return f"Hi {name} how are you doing?"

message = get_greeting("Mocha")
print(message)

#Example 2 
def get_bread_from_bakery(name):
    message = f"I am getting {name} today"
    return message

bread_choice = input("what kind of bread would you like?")

order_message = get_bread_from_bakery(bread_choice)

print(order_message)