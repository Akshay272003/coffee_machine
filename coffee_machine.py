# python 3.10
# author : Akshay Mundra
# coffee machine
import shelve
import admin_querys

def res_check(ing, choice):
    """check for the resource availability for a query"""
    if(ing["water"] <= res["water"] and ing["milk"] <= res["milk"] and ing["choco"] <= res["choco"] and ing["sugar"] <= res["sugar"] and ing["coffee"] <= res["coffee"]):
        print("Resources Available")
        ask_order_confirmation(ing, choice)
    else:
        print("Sorry! Resources are not available.")


def ask_order_confirmation(ing, choice):
    """ask for the confirmation of order"""
    confirm = input("\nDo you want to confirm this order y for yes or any to cancel: ")
    if confirm == 'y':
        cost = coffee_data[choice]["cost"]
        user_money = cost_validation(cost)
        place_order(ing)
        print(f"{user_money - cost} rs. is returned. ")

        global money
        money += cost

    else:
        print("***Order cancled.")

def cost_validation(cost):
    user_money = int(input("Enter payment : "))
    while user_money < cost:
        money = int(input(f"Enter {cost - user_money} rs. more :  "))
        user_money += money
    return user_money

def place_order(ing):
    """ serving the order to coustomer and resource updation"""
    print("Here is your coffee sir! ")
    # resources updation
    res["water"] = res["water"] - ing["water"]
    res["coffee"] = res["coffee"] - ing["coffee"]
    res["milk"] = res["milk"] - ing["milk"]
    res["sugar"] = res["sugar"] - ing["sugar"]
    res["choco"] = res["choco"] - ing["choco"]


def show_menu():
    """shows the menu of items"""
    print("\t -------------Menu------------\n")
    for key, value in coffee_data.items():
        print(f"{key:<20}   :   {value['cost']:>20} rs.")
    
def data_saver():
    """saves the data using shelve module"""
    shelf_file["coffee_data"] = coffee_data
    shelf_file["res"] = res
    shelf_file["money"] = money


if __name__ == "__main__":
    # fetching the data from shelve files
    shelf_file = shelve.open("coffees")
    coffee_data = shelf_file["coffee_data"]
    res = shelf_file["res"]
    money = shelf_file["money"]
    
    is_working = True
    show_menu()
    

    while is_working:
        print("\nExtra query : off/report/addr : ")
        choice = input("--->>  ")

        if choice == "off":
            is_working = False
            data_saver()
            shelf_file.close()

        elif choice == "report":
            # resource availability report
            for key, item in res.items():
                print(f"{key:<10} : {item}")
        elif choice == "menu":
            show_menu()

        elif choice == "admin":
            password = input("Enter admin password : ")
            if(password == "12345"):
                admin_querys.controller(shelf_file)
                coffee_data = shelf_file["coffee_data"]
                res = shelf_file["res"]

            else:
                print("Wrong Password")

        else:
            if choice in coffee_data:
                res_check(coffee_data[choice]["ingredients"], choice)