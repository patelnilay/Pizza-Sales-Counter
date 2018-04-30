# created by Nilay Patel
import json

# pizza dictionary
pizza_sold = {"John": {"Margarita": {"amount":0, "income":0},  "Marinara": {"amount":0, "income":0}, "Pepperoni": {"amount":0, "income":0},  "Veggie": {"amount":0, "income":0},  "Chicken": {"amount":0, "income":0},  "Four cheeses": {"amount":0, "income":0}, "Hawaiian":{"amount":0, "income":0}},"Susan": {"Margarita": {"amount":0, "income":0},  "Marinara": {"amount":0, "income":0}, "Pepperoni": {"amount":0, "income":0},  "Veggie": {"amount":0, "income":0},  "Chicken": {"amount":0, "income":0},  "Four cheeses": {"amount":0, "income":0}, "Hawaiian":{"amount":0, "income":0}},"Lauren": {"Margarita": {"amount":0, "income":0},  "Marinara": {"amount":0, "income":0}, "Pepperoni": {"amount":0, "income":0},  "Veggie": {"amount":0, "income":0},  "Chicken": {"amount":0, "income":0},  "Four cheeses": {"amount":0, "income":0}, "Hawaiian":{"amount":0, "income":0}},"Alex":{"Margarita": {"amount":0, "income":0},  "Marinara": {"amount":0, "income":0}, "Pepperoni": {"amount":0, "income":0},  "Veggie": {"amount":0, "income":0},  "Chicken": {"amount":0, "income":0},  "Four cheeses": {"amount":0, "income":0}, "Hawaiian":{"amount":0, "income": 0}}}


# menu option dictionary declaration
menu_options = {}

# function for total sales
def total_sold_shop():
    print("the total is")
    print (pizza_sold)

# function for quitting the program
def end():
    quit()

# function for loading save file
def load():
    global pizza_sold

    with open("pizza.json", "r") as file:
        pizza_sold = json.load(file)

# function for saving file
def save_file():
    global pizza_sold

    with open("pizza.json", "w") as file:
        json.dump(pizza_sold, file)
    # python open file

# function for counting pizza sales
def pizza_counter():
    global pizza_sold # make variable for use inside function

    # input data to be saved
    pizza_seller = input("Enter employee who sold it: ")
    pizza_name = input("Enter the pizza to update: ")
    pizza_amount = int(input("Enter how much by: "))

  # print(pizza_amount)  # debug
  # print(pizza_sold)  # debug
    pizza_sold[pizza_seller][pizza_name]["amount"] += pizza_amount # updating code

  # print(pizza_sold) # debug

    save_file() # function call

#diplating menu options
menu_options["total"] = total_sold_shop
menu_options["exit"] = end
menu_options["update"] = pizza_counter


def menu():
    load() # load file
    while 1: # keeps program running
        command = input("enter option: ").lower() # user chooses menu option. makes input lowercase by default
        if command in menu_options:
            menu_options[command]() # take input and runs the function by calling it.

menu() # actual call to run the program.