# destination.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from init import Base, session
from .accommodation import Accommodation


class Destination(Base):
    __tablename__ = 'destinations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    trip_id = Column(Integer, ForeignKey('trips.id'))

    # Relationship with Trip (many-to-one)
    trip = relationship("Trip", back_populates="destinations")

    # Relationship with Accommodation (one-to-many)
    accommodations = relationship("Accommodation", back_populates="destination")

    # Relationship with Activity (one-to-many)
    activities = relationship("Activity", back_populates="destination")

    def __repr__(self):
        return f"Destination(id={self.id}, name={self.name}, Trip ID={self.trip_id})"
    
    @classmethod
    def add_destination(cls, name, trip_id):
        """
        Add a new destination to the database.

        :param name: The name of the destination.
        :param trip_id: The trip id of the destination.
        """
        new_destination = Destination(name=name, trip_id=trip_id)
        session.add(new_destination)
        session.commit()

    @classmethod
    def get_all_destinations(cls):
        """
        Retrieve all destinations from the database.

        :return: A list of Destinations objects representing all destinations.
        """
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, destination_id):
        """
        Find a destination by its ID.

        :param destination_id: The ID of the destination to find.
        :return: The Destination object if found, None otherwise.
        """
        return session.query(cls).filter_by(id=destination_id).first()

    @classmethod
    def find_by_name(cls, name):
        """
        Find a destination by its name (case-insensitive and includes partial matches).

        :param name: The name of the destination to find.
        :return: A list of Destination objects matching the name criteria.
        """
        return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()
    
    @staticmethod
    def delete_destination(destination_id):
        """
        Delete a destination from the database.

        :param destination_id: The ID of the destination to delete.
        """
        destination = session.query(Destination).get(destination_id)
        if destination:
            session.delete(destination)
            session.commit()

    @staticmethod
    def update_destination(destination_id, name=None, trip_id=None):
        """
        Update an existing destination in the database.

        :param destination_id: The ID of the destination to update.
        :param name: (Optional) The new name of the destination.
        :param trip_id: (Optional) The new trip of the destination.
        """
        destination = session.query(Destination).get(destination_id)
        if destination:
            if name:
                destination.name = name
            if trip_id:
                destination.trip_id = trip_id

            session.commit()

    def get_accommodations(self):
        """
        Retrieve all accommodations associated with this destination.

        :return: A list of Accommodation objects representing all accommodations for this destination.
        """
        return self.accommodations
    
    @staticmethod
    def get_most_expensive_accommodation(destination_id):
        """
        Retrieve the most expensive accommodation associated with a destination.

        :param destination_id: The ID of the destination.
        :return: The Accommodation object representing the most expensive accommodation for the destination.
        """
        return session.query(Accommodation).filter_by(destination_id=destination_id).order_by(Accommodation.price.desc()).first()
    
    @staticmethod
    def get_cheapest_accommodation(destination_id):
        """
        Retrieve the cheapest accommodation associated with a destination.

        :param destination_id: The ID of the destination.
        :return: The Accommodation object representing the cheapest accommodation for the destination.
        """
        return session.query(Accommodation).filter_by(destination_id=destination_id).order_by(Accommodation.price.asc()).first()

    def get_activities(self):
        """
        Retrieve all activities associated with this destination, sorted by most fun rating.

        :return: A list of Activity objects representing all activities for this destination, sorted by rating.
        """
        return sorted(self.activities, key=lambda activity: activity.rating, reverse=True)
