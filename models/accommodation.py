from sqlalchemy import Column, Integer, String, ForeignKey, desc
from sqlalchemy.orm import relationship
from init import Base, session

class Accommodation(Base):
    __tablename__ = 'accommodations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    notes = Column(String)
    destination_id = Column(Integer, ForeignKey('destinations.id'))

    # Relationship with Destination (many-to-one)
    destination = relationship("Destination", back_populates="accommodations")

    def __repr__(self):
        return f"Accommodation(id={self.id}, name={self.name}, Price={self.price})"

    @classmethod
    def add_accommodation(cls, name, destination_id, notes=None, price=None):
        """
        Add a new accommodation to the database.

        :param name: The name of the accommodation.
        :param destination_id: The destination id of the accommodation.
        :param notes: (Optional) Any notes about the accommodation.
        :param price: (Optional) The price of the accommodation.
        """
        new_accommodation = Accommodation(name=name, destination_id=destination_id, notes=notes, price=price)
        session.add(new_accommodation)
        session.commit()


    @classmethod
    def get_all_accommodations(cls):
        """
        Retrieve all accommodations from the database.

        :return: A list of Accommodations objects representing all accommodations.
        """
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, accommodation_id):
        """
        Find an accommodation by its ID.

        :param accommodation_id: The ID of the accommodation to find.
        :return: The Accommodation object if found, None otherwise.
        """
        return session.query(cls).filter_by(id=accommodation_id).first()
    
    @classmethod
    def find_by_name(cls, name):
        """
        Find an accommodation by its name (case-insensitive and includes partial matches).

        :param name: The name of the accommodation to find.
        :return: A list of Accommodations objects matching the name criteria.
        """
        return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()
    
    @staticmethod
    def delete_accommodation(accommodation_id):
        """
        Delete a accommodation from the database.

        :param accommodation_id: The ID of the accommodation to delete.
        """
        accommodation = session.query(Accommodation).get(accommodation_id)
        if accommodation:
            session.delete(accommodation)
            session.commit()

    @staticmethod
    def update_accommodation(accommodation_id, name=None, price=None, notes=None, destination_id=None):
        """
        Update an existing accommodation in the database.

        :param accommodation_id: The ID of the accommodation to update.
        :param name: (Optional) The new name of the accommodation.
        :param price: (Optional) The new price of the accommodation.
        :param notes: (Optional) The new notes of the accommodation.
        :param destination_id: (Optional) The new destination of the accommodation.
        """
        accomodation = session.query(Accommodation).get(accommodation_id)

        if accomodation:
            if name:
                accomodation.name = name
            if price:
                accomodation.price = price
            if notes:
                accomodation.notes = notes
            if destination_id:
                accomodation.destination_id = destination_id

            session.commit()

    @classmethod
    def get_notes(cls, accommodation_id):
        """
        Retrieve the notes of a specific accommodation.

        :param accommodation_id: The ID of the accommodation.
        :return: The notes of the accommodation if found, None otherwise.
        """
        accommodation = session.query(cls).filter_by(id=accommodation_id).first()

        if accommodation:
            return accommodation.notes
        else:
            return None

    @classmethod
    def get_five_most_expensive_accommodations(cls):
        """
        Retrieve the 5 most expensive accommodations.

        :return: A list of Accommodation objects representing the 5 most expensive accommodations.
        """
        return session.query(cls).order_by(desc(cls.price)).limit(5).all()

    @classmethod
    def get_five_cheapest_accommodations(cls):
        """
        Retrieve the 5 cheapest accommodations.

        :return: A list of Accommodation objects representing the 5 cheapest accommodations.
        """
        return session.query(cls).order_by(cls.price).limit(5).all()
