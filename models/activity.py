from sqlalchemy import Column, Integer, String, ForeignKey, desc
from sqlalchemy.orm import relationship
from init import Base, session

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    rating = Column(Integer)
    destination_id = Column(Integer, ForeignKey('destinations.id'))
    

    # Relationship with Destination (many-to-one)
    destination = relationship("Destination", back_populates="activities")

    def __repr__(self):
        return f"Activity(id={self.id}, name={self.name}, rating={self.rating})"

    @classmethod
    def add_activity(cls, name, destination_id, description=None, rating=None):
        """
        Add a new activity to the database.

        :param name: The name of the activity.
        :param destination_id: The destination id of the activity.
        :param description: (Optional) Any description about the activity.
        :param rating: (Optional) The rating of the activity (scale of 1 to 5 stars).
        """
        new_activity = Activity(name=name, destination_id=destination_id, description=description, rating=rating)
        session.add(new_activity)
        session.commit()

    @classmethod
    def get_all_activities(cls):
        """
        Retrieve all activities from the database.

        :return: A list of Activity objects representing all activities.
        """
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, activity_id):
        """
        Find an activity by its ID.

        :param activity_id: The ID of the activity to find.
        :return: The Activity object if found, None otherwise.
        """
        return session.query(cls).filter_by(id=activity_id).first()

    @classmethod
    def find_by_name(cls, name):
        """
        Find an activity by its name (case-insensitive and includes partial matches).

        :param name: The name of the activity to find.
        :return: A list of Activity objects matching the name criteria.
        """
        return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()

    @staticmethod
    def delete_activity(activity_id):
        """
        Delete an activity from the database.

        :param activity_id: The ID of the activity to delete.
        """
        activity = session.query(Activity).get(activity_id)
        if activity:
            session.delete(activity)
            session.commit()

    @staticmethod
    def update_activity(activity_id, name=None, description=None, destination_id=None, rating=None):
        """
        Update an existing activity in the database.

        :param activity_id: The ID of the activity to update.
        :param name: (Optional) The new name of the activity.
        :param description: (Optional) The new description of the activity.
        :param destination_id: (Optional) The new destination of the activity.
        :param rating: (Optional) The new rating of the activity.
        """
        activity = session.query(Activity).get(activity_id)

        if activity:
            if name:
                activity.name = name
            if description:
                activity.description = description
            if destination_id:
                activity.destination_id = destination_id
            if rating:
                activity.rating = rating

            session.commit()

    @classmethod
    def find_top5_fun_activities(cls):
        """
        Find the top 5 most fun activities based on their ratings.

        :return: A list of the top 5 most fun Activity objects.
        """
        return session.query(cls).order_by(desc(cls.rating)).limit(5).all()

    @classmethod
    def find_top5_least_fun_activities(cls):
        """
        Find the top 5 least fun activities based on their ratings.

        :return: A list of the top 5 least fun Activity objects.
        """
        return session.query(cls).order_by(cls.rating).limit(5).all()
