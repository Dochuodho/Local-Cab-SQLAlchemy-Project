#lib/cab.py
#!/usr/bin/python3
from datetime import datetime
from sqlalchemy import Column,Integer, String, create_engine,DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref

Base = declarative_base()
#many to many relationship between drivers and customers
#one to many relationship between drivers and customers
#one to many relationship between customer and reviews

#many-to-many with table 
driver_customer = Table(
    'driver_customers',
    Base.metadata,
    Column('driver_id', ForeignKey('drivers.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True,
)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    gender = Column(String())
    email = Column(String())
    booking_time = Column(DateTime(), default=datetime.now())

    drivers = relationship('Driver', secondary=driver_customer, back_populates='customers')



    reviews = relationship('Review', backref=backref('customer'))


    def __repr__(self):
        return f"The rider's name is {self.name} and the booking time is {self.booking_time}"
    
class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    license_number = Column(Integer())
    phone_number = Column(Integer())

    customers = relationship('Customer', secondary=driver_customer, back_populates='drivers')



class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    rating = Column(Integer())
    comments = Column(String())
    created_at = Column(DateTime())
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    


if __name__ == '__main__':
    engine = create_engine('sqlite:///cabs.db')
    Base.metadata.create_all(engine)







