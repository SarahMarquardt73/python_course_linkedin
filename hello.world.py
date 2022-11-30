dog_name = "Benny"
print(dog_name)

#f string
# Adds variable buckets to a string
#Variable rules include: Using only letters/numbers/underscores, cannot start with number, cannot use a space
#Avoid python key words
#Most common errors are misspelling the variables.
print(f"My dog name is {dog_name}. {dog_name} is cute")

my_name = "Sarah"
my_age = 22

print(f"My name is {my_name} and I am {my_age} years old")

print(my_name.upper())

#Organization... Functions!
def say_hello(name): #Defining the contents within the say hello variable. Adding a name parameter
    print(f"hello {name}") #Add a f string

say_hello("Julie") #Name that is passed. Provide a name

#The output is "hello Julie"

#Next example
def describe_yourself(name, age):
    print(f"My name is {name} and I am {age}")
describe_yourself("Sarah", 22)

#Practice: Return a integer and its square
def example_one(integer):
    print(f"The square of {integer} is {integer*integer}")
example_one(2)

#Return a variable
#Stores a string into a variable
def pizza_name(topping):
    return f"{topping.title()} Pizza"
pizza = pizza_name("cheese")
print(pizza)

def times_two(num):
    return num * 2
print(times_two(2))

#Example
def sandwich_name(meat):
    return f"{meat.title()} Sandwich"
sandwich=sandwich_name("turkey")
print(sandwich)

def sandwich_name(meat):
    return f"{meat.title()} sandwich"
sandwich1=sandwich_name("ham")
print(sandwich1)

def pizza(topping):
    return f"{topping.title()} pizza"
topping1=pizza("cheese")
print(topping1)

def pizza(topping):
    return f"{topping.title()} pizza"
topping2=pizza("sausage")
print(topping2)

def pizza(topping):
    return f"{topping.title()} pizza"
topping3 = pizza("Ham")
print(topping3)

#Lists!
pizza_toppings = ["cheese", "ham", "peppers"]
print(pizza_toppings)

#Add pineapple to the end of the list
pizza_toppings.append("pineapple")

#add mushrooms as the very first object in the list
pizza_toppings.insert(0, "mushrooms")
print(pizza_toppings)

#Delete mushrooms
del pizza_toppings[0]
print(pizza_toppings)

#delete pineapple
pizza_toppings.pop()
print(pizza_toppings)

#No cheese
pizza_toppings.remove("cheese")
print(pizza_toppings)

#What happens when you try to remove duplicates?
pizza_toppings = ["cheese", "cheese", "ham", "peppers"]
pizza_toppings.remove("cheese")
print(pizza_toppings)
#One instance of cheese because it only removed at the begining

#Example 3, make a list of all the places I want to visit
travel = ["Miami", "Boston", "NYC", "Dublin"]
print(travel)

#Remove miami
travel.remove("Miami")
print(travel)

#Add Los Angelos
travel.append("Los Angelos")
print(travel)

#Add Toronto
travel.insert(0, "Toronto")
print(travel)

#Remove Los Angelos 
travel.pop()
print(travel)

#Loops
#Print each individual element in a list without [' '] in the output
pizza_toppings = ["cheese", "ham", "peppers"]
for my_topping in pizza_toppings:
    message = f"I would like to have {my_topping} on my pizza"
    print(message)
#This method prints out 3 different sentences starting with "I would like to have" and the pizza topping in the list

#Lets try some math
my_numbers = [1,2,3]
my_square_numbers = []
for number in my_numbers:
    my_square_numbers.append(number**2)
print(my_square_numbers)

#Lets loop through odd numbers
my_numbers1 = [3,5,7]
my_numbers1_squared = []
for number in my_numbers1:
   my_numbers1_squared.append(number**2)
print(my_numbers1_squared)
#Output is 9, 25, 49

#Keep lists of numbers.
#Lets say we want a list of 1-5 we would write it like this:
for i in [1,2,3,4,5]:
    print(i)
#However, lets say we need a list to 10 instead of 5
for i in range(1, 11):
    print(i)
#Didn't get to 100, stops once it gets to 100. Lets change it to 101 ao that 100 is included

print(list(range(1,11)))

#If then statements
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers_greater_than_five = []

for i in numbers:
    if i > 5:
        numbers_greater_than_five.append(i)
print(numbers_greater_than_five)

#Example: If else statement for black friday! Pants are $20 and shirts are $15
merchandise = ["Pants", "Shirt"]
print("We have the following items:")
for clothing in merchandise:
    if clothing == "Pants":
        print(f"{clothing} ($20)")
    else:
        print(f"{clothing} ($15)")
#Output:Pants ($20). Shirt ($15)

#Example: Pizza shop is having a sale on slices. $2.00 for cheese $3.00 for ham
pizza_topping = ["Cheese", "Ham"]
print("We have the following toppings:")
for topping in pizza_topping:
    if topping == "Cheese":
        print(f"{topping} is $2.00")
    else:
        print(f"{topping} is $3.00")
#Output: Cheese is $2.00. Ham is $3.00

#Final Challenge: Make a Pizza restaurant list
#Here are my expected outputs.
# Welcome to Sarah's Pizzaria
# Our available toppings are
# Cheese (free)
# Ham ($1 extra)

pizza_topping = ["Cheese", "Ham"]
def format_topping(topping):
    if topping == "Cheese":
        return f"{topping.title()} (free)"
    else:
        return f"{topping.title()} ($1 Extra)"
print(format_topping("Cheese") == "Cheese (free)")
print(format_topping("Ham") == "Ham ($1 Extra)") #This tests the statement


def print_menu(toppings):
    print("Welcome to Julie's Pizzeria")
    print("Our available toppings are:")
    for topping in toppings:
        print(format_topping(topping))
print_menu(pizza_toppings)


   
    






