import copy

from infrastructure.enums.enum_icon import Icon
from services.cafeteria_item_service import CafeteriaItemService
from services.cart_service import CartService

cafeteria_item_service = CafeteriaItemService()
cart_service = CartService()
menu_list = cafeteria_item_service.get_cafeteria_menu()

def start_cafeteria():
    print(f"{Icon.DogIcon.value} Welcome to Storm's Woofeteria. {Icon.DogIcon.value}")
    print("Here is what Chef Storm has to offer.")
    print("Food")
    cafeteria_item_service.print_cafeteria_menu()
    print("Please enter the relevant number from the menu, that corresponds to the item you wish to order.\n "
          "If you wish to order more than one item please separate each item number by comma.")
    user_input = input()
    item_ids = [int(x) for x in user_input.split(',') if x.strip().isdigit()]
    menu_list_copy = copy.deepcopy(menu_list)
    selected_menu_items = [item for item in menu_list_copy if item.Id in item_ids]
    selected_menu_items_original = [item for item in menu_list if item.Id in item_ids]
    for item in selected_menu_items:
        user_input = input(f"How many {item.Name} would you like to order?")
        item.Stock = int(user_input)
    for item in selected_menu_items_original:
        item.Stock = item.Stock - int(user_input)
    cart = cart_service.add_to_cart(selected_menu_items)
    print("Are you finished with your order? (Y/N)")
    user_input = input().capitalize()
    if user_input == "N":
        cart_service.print_cart(cart)
        print("Would you like to add or remove item(s) from your cart? (Add/Remove)")
        user_input = input().capitalize()
        if user_input == "Add".capitalize():
            print("Food")
            cafeteria_item_service.print_cafeteria_menu()
            print("Please enter the relevant number from the menu, that corresponds to the item you wish to order.\n "
                  "If you wish to order more than one item please separate each item number by comma.")
            user_input = input()
            item_ids = [int(x) for x in user_input.split(',') if x.strip().isdigit()]
            selected_menu_items = [item for item in menu_list if item.Id in item_ids]
            for item in selected_menu_items:
                user_input = input(f"How many {item.Name} would you like to order?")
                item.Stock = int(user_input)
            cart.Items.extend(selected_menu_items)
            cart = cart_service.update_cart(cart, cart.Items)
            cart_service.print_cart(cart)







if __name__ == '__main__':
    start_cafeteria()
