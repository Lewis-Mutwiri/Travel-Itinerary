from models.trip import Trip
from models.accommodation import Accommodation
from models.destination import Destination
from models.activity import Activity
from init import Base, engine
from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

fake = Faker()

try:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")
except SQLAlchemyError as e:
    print("Error creating database tables:", e)

def generate_seed_data():
    Base.metadata.bind = engine
    
    # Create session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    try:
        trips = []
        
        japan = Trip(
                name='Japan Exploration',
                start_date='2024-05-15',
                end_date='2024-05-20',
                description= 'Experience the unique blend of tradition and modernity in Japan, from bustling Tokyo to serene Kyoto.'
            )
        trips.append(japan)
        session.add(japan)

        italy = Trip(
                name='Italian Odyssey',
                start_date='2024-06-10',
                end_date='2024-06-20',
                description= 'Journey through the historic streets of Italy, from the ancient ruins of Rome to the romantic canals of Venice.'
            )
        trips.append(italy)
        session.add(italy)

        brazil = Trip(
                name='Brazilian Adventure',
                start_date='2024-07-10',
                end_date='2024-07-27',
                description= 'Embark on an exciting adventure in Brazil, from the vibrant beaches of Rio de Janeiro to the lush Amazon rainforest.'
            )
        trips.append(brazil)
        session.add(brazil)

        thailand = Trip(
                name='Thailand Escape',
                start_date='2024-08-01',
                end_date='2024-08-23',
                description= 'Explore the rich culture and stunning landscapes of Thailand, from bustling Bangkok to the tranquil islands of Phuket.'
            )
        trips.append(thailand)
        session.add(thailand)

        spain = Trip(
                name='Spanish Fiesta',
                start_date='2024-09-01',
                end_date='2024-10-15',
                description= ' Immerse yourself in the vibrant culture of Spain, from the lively streets of Barcelona to the historic landmarks of Madrid.'
            )
        trips.append(spain)
        session.add(spain)

        destinations = [] 
        for _ in range(20):
            destination = Destination(
                name=fake.city() + " City",
                trip=fake.random_element(trips)
            )
            destinations.append(destination)
            session.add(destination)

        accommodations = []
        for _ in range(50):
            accommodation = Accommodation(
                name=fake.company(),
                price=fake.random_number(digits=3),
                notes=fake.sentence(),
                destination=fake.random_element(destinations)
            )
            accommodations.append(accommodation)
            session.add(accommodation)

        activities = []
        for _ in range(50):
            activity = Activity(
                name=fake.word(),
                description=fake.text(),
                destination=fake.random_element(destinations),
                rating=fake.random_int(min=1, max=5)
            )
            activities.append(activity)
            session.add(activity)

        session.commit()

        return trips

    except Exception as e:
        # Rollback the transaction if an exception occurs
        session.rollback()
        raise e

    finally:
        session.close()

if __name__ == "__main__":

    generate_seed_data()

