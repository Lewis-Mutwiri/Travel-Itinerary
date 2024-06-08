
from helpers import (
    exit_program,
    list_trips,
    find_trip_by_name,
    find_trip_by_id,
    create_trip,
    update_trip,
    delete_trip,
    get_duration,
    get_description,
    get_destinations,
    add_destination,
    find_destination_by_name,
    find_destination_by_id,
    delete_destination,
    update_destination,
    get_accommodations,
    list_destinations,
    find_most_expensive_accommodation,
    find_cheapest_accommodation,
    list_accommodations,
    find_accommodation_by_id,
    find_accommodation_by_name,
    add_accommodation,
    delete_accommodation,
    update_accommodation,
    get_notes,
    get_five_cheapest_accommodations,
    get_five_most_expensive_accommodations,
    list_activities,
    find_activity_by_id,
    find_activity_by_name,
    create_activity,
    update_activity,
    delete_activity,
    get_activities,
    get_activity_description,
    get_five_least_fun_activities,
    get_five_most_fun_activities
)


from colorama import init, Fore, Style
import emoji

init(autoreset=True)

def main():
    while True:
        menu()
        choice = input(Fore.BLUE + "> " + Style.RESET_ALL)
        if choice == "0":
            exit_program()
        elif choice == "1":
            trips_menu()
            handle_trips_menu()
        elif choice == "2":
            destinations_menu()
            handle_destinations_menu()
        elif choice == "3":
            accommodations_menu()
            handle_accommodations_menu()
        elif choice == "4":
            activities_menu()
            handle_activities_menu()
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

def handle_trips_menu():
    while True:
        choice = input(Fore.BLUE + "Trips Menu > " + Style.RESET_ALL)
        if choice == "0":
            return
        elif choice == "5":
            list_trips()
        elif choice == "6":
            find_trip_by_name()
        elif choice == "7":
            find_trip_by_id()
        elif choice == "8":
            get_description()
        elif choice == "9":
            get_duration()
        elif choice == "10":
            get_destinations()
        elif choice == "11":
            create_trip()
        elif choice == "12":
            update_trip()
        elif choice == "13":
            delete_trip()
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

def handle_destinations_menu():
    while True:
        choice = input(Fore.BLUE + "Destinations Menu > " + Style.RESET_ALL)
        if choice == "0":
            return
        elif choice == "14":
            list_destinations()
        elif choice == "15":
            add_destination()
        elif choice == "16":
            find_destination_by_name()
        elif choice == "17":
            find_destination_by_id()
        elif choice == "18":
            get_activities()
        elif choice == "19":
            get_accommodations()
        elif choice == "20":
            find_most_expensive_accommodation()
        elif choice == "21":
            find_cheapest_accommodation()
        elif choice == "22":
            update_destination()
        elif choice == "23":
            delete_destination()
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

def handle_accommodations_menu():
    while True:
        choice = input(Fore.BLUE + "Accommodations Menu > " + Style.RESET_ALL)
        if choice == "0":
            return
        elif choice == "24":
            list_accommodations()
        elif choice == "25":
            add_accommodation()
        elif choice == "26":
            find_accommodation_by_name()
        elif choice == "27":
            find_accommodation_by_id()
        elif choice == "28":
            get_notes()
        elif choice == "29":
            get_five_most_expensive_accommodations()
        elif choice == "30":
            get_five_cheapest_accommodations()
        elif choice == "31":
            update_accommodation()
        elif choice == "32":
            delete_accommodation()
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

def handle_activities_menu():
    while True:
        choice = input(Fore.BLUE + "Activities Menu > " + Style.RESET_ALL)
        if choice == "0":
            return
        elif choice == "33":
            list_activities()
        elif choice == "34":
            create_activity()
        elif choice == "35":
            find_activity_by_name()
        elif choice == "36":
            find_activity_by_id()
        elif choice == "37":
            get_activity_description()
        elif choice == "38":
            get_five_most_fun_activities()
        elif choice == "39":
            get_five_least_fun_activities()
        elif choice == "40":
            update_activity()
        elif choice == "41":
            delete_activity()
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

def menu():
    print(Fore.GREEN + "\n🌍🧳🌴 Welcome to the Travel Itinerary Organizer! 🌴🧳🌍")
    print(Fore.YELLOW + "----------------------------------------------")
    print(Fore.CYAN + "📅 Browse Your Planned Trips!")
    print(Fore.CYAN + "🗺️ Trips Have Many Destinations to Visit!")
    print(Fore.CYAN + "🏨 The Destinations Have Many Accommodations to Stay and Activities to Do!")
    print(Fore.YELLOW + "----------------------------------------------")
    print(Fore.YELLOW + "📋 Menu 📋")
    print(Fore.MAGENTA + "Please select an option:")
    print("1: " + emoji.emojize(":airplane:") + " Trips Menu")
    print("2: " + emoji.emojize(":world_map:") + " Destinations Menu")
    print("3: " + emoji.emojize(":hotel:") + " Accommodations Menu")
    print("4: " + emoji.emojize(":performing_arts:") + " Activities Menu")
    print("0: \U0001F6AB" + Fore.RED + " Exit Program")


def trips_menu():
    print("")
    print(Fore.YELLOW + "🛫🧳📜 Trips Menu")
    print(Fore.CYAN + "Please select an option:")
    print("5: List all trips")
    print("6: Find trip by name")
    print("7: Find trip by id")
    print("8: Get trip's description")
    print("9: Get trip's duration")
    print("10: Get trip's destinations")
    print("11: Create trip")
    print("12: Update trip")
    print("13: Delete trip")
    print("0: \U0001F6AB Return to Main Menu")


def destinations_menu():
    print("")
    print(Fore.YELLOW + "🗺️🌴📦 Destinations Menu")
    print(Fore.CYAN + "Please select an option:")
    print("14: List all destinations")
    print("15: Add new destination")
    print("16: Find destination by name")
    print("17: Find destination by id")
    print("18: Get destination's activities sorted by fun rating")
    print("19: Get destination's all accommodations")
    print("20: Find destination's most expensive accommodation")
    print("21: Find destination's cheapest accommodation")
    print("22: Update destination")
    print("23: Delete destination")
    print("0: \U0001F6AB Return to Main Menu")


def accommodations_menu():
    print("")
    print(Fore.YELLOW + "🏨🛏️ Accommodations Menu")
    print(Fore.CYAN + "Please select an option:")
    print("24: List all accommodations")
    print("25: Add new accommodation")
    print("26: Find accommodation by name")
    print("27: Find accommodation by id")
    print("28: Get accommodation's notes")
    print("29: List the top 5 most expensive accommodations")
    print("30: List the top 5 cheapest accommodations")
    print("31: Update accommodation")
    print("32: Delete accommodation")
    print("0: \U0001F6AB Return to Main Menu")

def activities_menu():
    print("")
    print(Fore.YELLOW + "🎭🎉 Activities Menu")
    print(Fore.CYAN + "Please select an option:")
    print("33: List all activities")
    print("34: Add new activity")
    print("35: Find activity by name")
    print("36: Find activity by id")
    print("37: Get activity's description")
    print("38: List the top 5 most fun activities")
    print("39: List the top 5 least fun activities")
    print("40: Update activity")
    print("41: Delete activity")
    print("0: \U0001F6AB Return to Main Menu")



if __name__ == "__main__":
    main()
