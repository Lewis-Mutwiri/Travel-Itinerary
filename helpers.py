import datetime
from models.trip import Trip
from models.destination import Destination
from models.accommodation import Accommodation
from models.activity import Activity


def exit_program():
    print("Thank you for using Travel Itinerary Organizer!")
    exit()


def list_trips():
    all_trips = Trip.get_all_trips()
    print("All trips:")
    for trip in all_trips:
        print(trip)


def find_trip_by_name():
    name = input("Enter the trip's name: ")
    trips = Trip.find_by_name(name)
    if trips:
        print("Trips found:")
        for trip in trips:
          print(trip)
    else: 
        print(f'Trip "{name}" not found')


def find_trip_by_id():
    # Use a trailing underscore not to override the built-in id function
    id_ = input("Enter the trip's id: ")
    trip = Trip.find_by_id(id_)
    if trip:
        print("Trip found:", trip)
    else: 
        print(f'Trip "{id_}" not found')


def create_trip():
    while True:
        name = input("Enter the trip's name: ")
        start_date = input("Enter the Trip's start date in YYYY-MM-DD format: ")
        end_date = input("Enter the Trip's end date in YYYY-MM-DD format: ")
        description = input("Enter the trip's description: ")

        try:
            # Validate date format
            datetime.datetime.strptime(start_date, "%Y-%m-%d")
            datetime.datetime.strptime(end_date, "%Y-%m-%d")
            # Ensure end_date is after start_date
            if end_date <= start_date:
                raise ValueError("End date must be after start date")

            # If all validations pass, add the trip
            trip = Trip.add_trip(name, start_date, end_date, description)
            print(f'Success: "{name}" Trip created')
            break
        except ValueError as ve:
            print("Error creating trip: ", ve)


def update_trip():
    while True:
        id_ = input("Enter the trip's id: ")
        trip = Trip.find_by_id(id_)
        if not trip:
            print(f'Trip {id_} not found')
            return

        name = input("Enter the trip's new name (press Enter to keep current name): ")
        start_date = input("Enter the trip's new start date in YY-MM-DD format (press Enter to keep current start date): ")
        end_date = input("Enter the trip's new end date in YY-MM-DD format (press Enter to keep current end date): ")
        description = input("Enter the trip's new description (press Enter to keep current description): ")

        try:
            # Validate date format if entered
            if start_date:
                datetime.datetime.strptime(start_date, "%Y-%m-%d")
            if end_date:
                datetime.datetime.strptime(end_date, "%Y-%m-%d")
                # Ensure end_date is after start_date if both are entered
                if start_date and end_date and end_date <= start_date:
                    raise ValueError("End date must be after start date")

            
            Trip.update_trip(id_, name=name or trip.name, start_date=start_date or trip.start_date, 
                             end_date=end_date or trip.end_date, description=description or trip.description)
            print(f'Successfully updated trip: {trip}')
            break
        except ValueError as ve:
            print("Error updating trip: ", ve)



def delete_trip():
    id_ = input("Enter the trip's id: ")
    trip = Trip.find_by_id(id_)
    if trip:
        trip_name = trip.name
        Trip.delete_trip(id_)
        print(f'Trip "{trip_name}" deleted')
    else:
        print(f'Trip "{id_}" not found')



def get_duration():
    id_ = input("Enter the trip's id: ")
    if trip := Trip.find_by_id(id_):
        trip_duration = trip.duration()
        print(f"The duration of the trip '{trip.name}' is {trip_duration} days.")
    else:
        print("Trip not found.")

def get_destinations():
    trip_id = input("Enter the trip's id: ")
    trip = Trip.find_by_id(trip_id)
    if trip:
        destinations = trip.get_destinations()
        if destinations:
            print(f"Destinations for Trip '{trip.name}':")
            for destination in destinations:
                print(f"Destination: {destination.name}, ID: {destination.id}")
        else:
            print(f"No destinations found for Trip '{trip.name}'.")
    else:
        print("Trip not found.")


def get_description():
    id_ = input("Enter the trip's id: ")
    if trip := Trip.find_by_id(id_):
        print(f"Trip Name: {trip.name}")
        print(f"Description: {trip.description}")
    else:
        print("Trip not found.")

def add_destination():
    name = input("Enter the destination's name: ")
    trip_id = input("Enter the trip's id: ")
    trip = Trip.find_by_id(trip_id)
    if trip:
        Destination.add_destination(name, trip_id)
        print(f"Destination '{name}' added to trip '{trip.name}' successfully.")
    else:
        print("No trip found with specified ID.")

def find_destination_by_name():
    name = input("Enter the destination's name: ")
    destinations = Destination.find_by_name(name)
    if destinations:
        print("Destinations found:")
        for destination in destinations:
          print(destination)
    else: 
        print(f'Destination "{name}" not found')


def find_destination_by_id():
    # Use a trailing underscore not to override the built-in id function
    id_ = input("Enter the destination's id: ")
    destination = Destination.find_by_id(id_)
    if destination:
        print("Destination found:", destination)
    else: 
        print(f'Destination "{id_}" not found')

def delete_destination():
    id_ = input("Enter the destination's id: ")
    destination = Destination.find_by_id(id_)
    if destination:
        destination_name = destination.name
        Destination.delete_destination(id_)
        print(f'Destination "{destination_name}" deleted')
    else:
        print(f'Destination "{id_}" not found')

def update_destination():
    while True:
        id_ = input("Enter the destination's id: ")
        destination = Destination.find_by_id(id_)
        if not destination:
            print(f'Destination {id_} not found')
            return

        name = input("Enter the destination's new name: ")
        trip_id = input("Enter the destination's new trip id: ")

        # Check if the trip ID exists
        if not Trip.find_by_id(trip_id):
            print(f'Trip with id {trip_id} not found')
            continue

        try:
            Destination.update_destination(id_, name=name, trip_id=trip_id)
            print(f'Successfully updated destination: {destination}')
            break
        except ValueError as ve:
            print("Error updating destination: ", ve)



def get_accommodations():
    destination_id = input("Enter the destination's id: ")
    destination = Destination.find_by_id(destination_id)
    if destination:
        accommodations = destination.get_accommodations()
        if accommodations:
            print(f"Accommodations for Destination '{destination.name}':")
            for accommodation in accommodations:
                print(f"Accommodation: {accommodation.name}, ID: {accommodation.id}, Price:{accommodation.price}")
        else:
            print(f"No accommodations found for Destination '{destination.name}'.")
    else:
        print("Destination not found.")

def list_destinations():
    all_destinations = Destination.get_all_destinations()
    print("All destinations:")
    for destination in all_destinations:
        print(destination)

def find_most_expensive_accommodation():
    destination_id = input("Enter the destination's id: ")
    destination = Destination.find_by_id(destination_id)
    if destination:
        most_expensive_accommodation = destination.get_most_expensive_accommodation(destination_id)
        if most_expensive_accommodation:
            print(f"Most Expensive Accommodation for Destination '{destination.name}':")
            print(f"Accommodation: {most_expensive_accommodation.name}, Price: {most_expensive_accommodation.price}")
        else:
            print(f"No accommodations found for Destination '{destination.name}'.")
    else:
        print("Destination not found.")

def find_cheapest_accommodation():
    destination_id = input("Enter the destination's id: ")
    destination = Destination.find_by_id(destination_id)
    if destination:
        cheapest_accommodation = destination.get_cheapest_accommodation(destination_id)
        if cheapest_accommodation:
            print(f"Cheapest Accommodation for Destination '{destination.name}':")
            print(f"Accommodation: {cheapest_accommodation.name}, Price: {cheapest_accommodation.price}")
        else:
            print(f"No accommodations found for Destination '{destination.name}'.")
    else:
        print("Destination not found.")

def list_accommodations():
    all_accommodations = Accommodation.get_all_accommodations()
    print("All accommodations:")
    for accommodation in all_accommodations:
        print(accommodation)

def find_accommodation_by_name():
    name = input("Enter the accommodation's name: ")
    accommodations = Accommodation.find_by_name(name)
    if accommodations:
        print("Accommodations found:")
        for accommodation in accommodations:
          print(accommodation)
    else: 
        print(f'Accommodation "{name}" not found')


def find_accommodation_by_id():
    # Use a trailing underscore not to override the built-in id function
    id_ = input("Enter the accommodation's id: ")
    accommodation = Accommodation.find_by_id(id_)
    if accommodation:
        print("Accommodation found:", accommodation)
    else: 
        print(f'Accommodation "{id_}" not found')

def add_accommodation():
    name = input("Enter the accommodation's name: ")
    destination_id = input("Enter the destination's id: ")
    destination = Destination.find_by_id(destination_id)
    if destination:
        notes = input("Enter any notes about the accommodation (optional): ")
        price = input("Enter the price of the accommodation (optional): ")

        if price:
            try:
                price = float(price)
            except ValueError:
                print("Invalid price. Please enter a valid number.")
                return

        Accommodation.add_accommodation(name, destination_id, notes=notes, price=price)
        print(f"Accommodation '{name}' added to destination '{destination.name}' successfully.")
    else:
        print("No destination found with specified ID.")

def delete_accommodation():
    id_ = input("Enter the accommodation's id: ")
    accommodation = Accommodation.find_by_id(id_)
    if accommodation:
        accommodation_name = accommodation.name
        Accommodation.delete_accommodation(id_)
        print(f'Accommodation "{accommodation_name}" deleted')
    else:
        print(f'Accommodation "{id_}" not found')


def update_accommodation():
    accommodation_id = input("Enter the accommodation's ID: ")
    accommodation = Accommodation.find_by_id(accommodation_id)
    
    if not accommodation:
        print(f"Accommodation with ID {accommodation_id} not found.")
        return
    
    print(f"Updating accommodation with ID {accommodation_id}:")
    name = input("Enter the new name of the accommodation (leave empty to keep current): ")
    price = input("Enter the new price of the accommodation (leave empty to keep current): ")
    notes = input("Enter the new notes of the accommodation (leave empty to keep current): ")
    destination_id = input("Enter the new destination ID of the accommodation (leave empty to keep current): ")
    
    try:
        if name:
            accommodation.name = name
        if price:
            accommodation.price = float(price)
        if notes:
            accommodation.notes = notes
        if destination_id:
            accommodation.destination_id = destination_id

        accommodation.update_accommodation(accommodation_id, name=name, price=price, notes=notes, destination_id=destination_id)
        print(f"Accommodation with ID {accommodation_id} updated successfully.")
    except ValueError as ve:
        print("Error updating accommodation: ", ve)
        if "could not convert string to float" in str(ve):
            print("Price must be a number.")

def get_notes():
    id_ = input("Enter the accommodation's id: ")
    if accommodation := Accommodation.find_by_id(id_):
        print(f"Accommodation Name: {accommodation.name}")
        print(f"Notes: {accommodation.notes}")
    else:
        print("Accommodation not found.")

def get_five_most_expensive_accommodations():
    """
    Retrieve the 5 most expensive accommodations.

    :return: A list of Accommodation objects representing the 5 most expensive accommodations.
    """
    accommodations = Accommodation.get_five_most_expensive_accommodations()
    if accommodations:
        print("Five most expensive accommodations:")
        for accommodation in accommodations:
            print(f"Accommodation: {accommodation.name}, Price: {accommodation.price}")
    else:
        print("No accommodations found.")

def get_five_cheapest_accommodations():
    """
    Retrieve the 5 cheapest accommodations.

    :return: A list of Accommodation objects representing the 5 cheapest accommodations.
    """
    accommodations = Accommodation.get_five_cheapest_accommodations()
    if accommodations:
        print("Five cheapest accommodations:")
        for accommodation in accommodations:
            print(f"Accommodation: {accommodation.name}, Price: {accommodation.price}")
    else:
        print("No accommodations found.")

def list_activities():
    all_activities = Activity.get_all_activities()
    if all_activities:
        print("All activities:")
        for activity in all_activities:
            print(activity)
    else:
        print("No activities found.")

def find_activity_by_name():
    name = input("Enter the activity's name: ")
    activities = Activity.find_by_name(name)
    if activities:
        print("Activities found:")
        for activity in activities:
            print(activity)
    else:
        print(f'Activity "{name}" not found')

def find_activity_by_id():
    id_ = input("Enter the activity's id: ")
    activity = Activity.find_by_id(id_)
    if activity:
        print("Activity found:", activity)
    else:
        print(f'Activity "{id_}" not found')

def create_activity():
    while True:
        name = input("Enter the activity's name: ")
        destination_id = input("Enter the destination's id: ")
        description = input("Enter the activity's description: ")
        rating = input("Enter the activity's rating (1 to 5 stars): ")

        try:
            rating = int(rating)
            if rating < 1 or rating > 5 or not isinstance(rating, int):
                raise ValueError("Rating must be an integer between 1 and 5")

            destination = Destination.find_by_id(destination_id)
            if not destination:
                raise ValueError("Destination id does not correspond to a destination")

            Activity.add_activity(name, destination_id, description, rating)
            print(f'Success: "{name}" Activity created')
            break
        except ValueError as ve:
            if str(ve).startswith("invalid literal for int() with base 10"):
                print("Rating must be an integer between 1 and 5")
            else:
                print("Error creating activity: ", ve)




def update_activity():
    while True:
        id_ = input("Enter the activity's id: ")
        activity = Activity.find_by_id(id_)
        if not activity:
            print(f'Activity {id_} not found')
            return

        name = input("Enter the activity's new name (leave empty to keep current): ")
        description = input("Enter the activity's new description (leave empty to keep current): ")
        rating = input("Enter the activity's new rating (1 to 5 stars) (leave empty to keep current): ")

        try:
            if rating:
                rating = int(rating)
                if rating < 1 or rating > 5:
                    raise ValueError("Rating must be between 1 and 5")

            Activity.update_activity(id_, name=name, description=description, rating=rating)
            print(f'Successfully updated activity: {activity}')
            break
        except ValueError as ve:
            if str(ve).startswith("invalid literal for int() with base 10"):
                print("Rating must be an integer between 1 and 5")
            else:
                print("Error creating activity: ", ve)

def delete_activity():
    id_ = input("Enter the activity's id: ")
    activity = Activity.find_by_id(id_)
    if activity:
        activity_name = activity.name
        Activity.delete_activity(id_)
        print(f'Activity "{activity_name}" deleted')
    else:
        print(f'Activity "{id_}" not found')

def get_activities():
    destination_id = input("Enter the destination's id: ")
    destination = Destination.find_by_id(destination_id)
    if destination:
        activities = destination.get_activities()
        if activities:
            print(f"Activities for Destination '{destination.name}' sorted by highest fun rating:")
            for activity in activities:
                print(f"Activity: {activity.name}, ID: {activity.id}, Rating:{activity.rating}")
        else:
            print(f"No activities found for Destination '{destination.name}'.")
    else:
        print("Destination not found.")

def get_activity_description():
    id_ = input("Enter the activity's id: ")
    if activity := Activity.find_by_id(id_):
        print(f"Activity Name: {activity.name}")
        print(f"Description: {activity.description}")

def get_five_most_fun_activities():
    """
    Retrieve the 5 most fun activities.

    :return: A list of Activities objects representing the 5 most fun activities.
    """
    activities = Activity.find_top5_fun_activities()
    if activities:
        print("Five most fun activities:")
        for activity in activities:
            print(f"Activity: {activity.name}, Rating: {activity.rating}")
    else:
        print("No activity found.")

def get_five_least_fun_activities():
    """
    Retrieve the 5 least fun activities.

    :return: A list of Activity objects representing the 5 least fun activities.
    """
    activities = Activity.find_top5_least_fun_activities()
    if activities:
        print("Five least fun activities:")
        for activity in activities:
            print(f"Activity: {activity.name}, Rating: {activity.rating}")
    else:
        print("No activity found.")
