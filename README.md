# Travel Itinerary Organizer

## Project Overview

The Travel Itinerary Organizer is a software solution designed to assist users in planning and organizing their travel itineraries effectively. The application enables users to create, manage, and visualize detailed travel plans, including destinations, activities, and accommodations details. By implementing a user-friendly command-line interface (CLI) and utilizing SQLAlchemy ORM for data management, the application aims to streamline the process of itinerary planning, ensuring a smooth and enjoyable travel experience for users.

## Benefits

- Simplifies itinerary planning process for users, saving time and effort.
- Facilitates efficient organization and visualization of travel plans.
- Enhances user experience with a user-friendly CLI interface.

## Timeline

1. Project planning and setup, database design, and ORM implementation.
2. CLI interface development, CRUD operations for key parameters.
3. Data validation, error handling, and testing.
4. Documentation preparation, final testing, and project submission.

## How to Use

To use the Travel Itinerary Organizer, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pipenv install`.
3. Enter the virtual environment using `pipenv shell`.
3. Run the `seed.py` file to generate sample data using `python seed.py`.
3. Run the `cli.py` file to get the CLI application using `python cli.py`.
4. Use the provided command-line interface (CLI) to navigate through different menus and perform various actions such as creating trips, adding destinations, managing accommodations, and organizing activities.

## Usage

Browse your planned trips! Trips have many destinations to visit! The destinations have many accomodations to stay and activities to do!

The Travel Itinerary Organizer provides the following main menu options:

### Trips Menu

Manage trips, including:

- Listing all available trips
- Finding a trip by name or ID
- Getting trip details
- Creating a new trip
- Updating an existing trip
- Deleting a trip

### Destinations Menu

Manage destinations, including:

- Listing all available destinations
- Adding a new destination
- Finding a destination by name or ID
- Getting a destination's activities and accommodations
- Finding the most expensive or cheapest accommodation for a destination
- Updating an existing destination
- Deleting a destination

### Accommodations Menu

Manage accommodations, including:

- Listing all available accommodations
- Adding a new accommodation
- Finding an accommodation by name or ID
- Getting accommodation notes
- Listing the top 5 most expensive or cheapest accommodations
- Updating an existing accommodation
- Deleting an accommodation

### Activities Menu

Manage activities, including:

- Listing all available activities
- Adding a new activity
- Finding an activity by name or ID
- Getting an activity's description
- Listing the top 5 most fun or least fun activities
- Updating an existing activity
- Deleting an activity

Each menu provides specific options to perform corresponding actions. Simply follow the prompts and input your choices to interact with the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

