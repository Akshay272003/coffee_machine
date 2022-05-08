import shelve

def controller(shelf_file):
    choice = input("Enter the query : ")
    if(choice == "add resources"):
        add_resources(shelf_file)
    elif(choice == "add coffee"):
        add_coffee(shelf_file)
    else:
        pass

# def open_shelf():
#     shelf_file = shelve.open("coffees")
#     return shelf_file

def data_saver(res, coffee_data, shelf_file):
    shelf_file["res"] = res
    shelf_file["coffee_data"] = coffee_data

def add_resources(shelf_file):
    """ adding resources using data validation"""
    coffee_data, res = shelf_file["coffee_data"], shelf_file["res"]
    resource_choice = input("Enter water/milk/choco/coffee/sugar : ")
    if resource_choice in res:
        amount = int(input("Enter amount : "))
        if(amount >= 0):
            res[resource_choice] += amount
            
            data_saver(res, coffee_data, shelf_file)
            print("Resources added successfully ")

        else:
            print("Invalid input")
    else:
        print("Invalid resource")


def add_coffee(shelf_file):

    def coffee_updater():
        cost = int(input("Enter the cost of this coffee : "))
        
        # ingridients
        water = int(input("Enter amount of water : "))
        coffee = int(input("Enter amount of coffee : "))
        milk = int(input("Enter amount of milk : "))
        choco = int(input("Enter amount of choco : "))
        sugar = int(input("Enter amount of sugar : "))

        coffee_data[coffee_name] = {
            "ingredients":{
                "water":water,
                "coffee":coffee,
                "milk":milk,
                "choco":choco,
                "sugar":sugar
            },
            "cost": cost
        }
        print("New recipie added successfully! ")
        data_saver(res, coffee_data, shelf_file)

    # func updater ends

    coffee_data = shelf_file["coffee_data"]
    res = shelf_file["res"]
    coffee_name = input("Enter the new coffee name : ")
    
    if coffee_name in coffee_data:
        choice = input("Sir, this coffee is already available, do you want to edit this coffee...y/n : ")
        if choice == "y":
            coffee_updater()
        else:
            pass
    else:
        coffee_updater()

    


if __name__ == "__main__":
    
    controller()