from infrastructure.enums.enum_icon import Icon
from services.cafeteria_item_service import CafeteriaItemService

cafeteria_item_service = CafeteriaItemService()


def start_cafeteria():
    print(f"{Icon.DogIcon.value} Welcome to Storm's Woofeteria. {Icon.DogIcon.value}")
    print("Here is what Chef Storm has to offer.")
    print("Food")
    cafeteria_item_service.print_cafeteria_menu()


if __name__ == '__main__':
    start_cafeteria()
