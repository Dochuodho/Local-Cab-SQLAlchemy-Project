#lib/cab.py
#!/usr/bin/python3
from datetime import datetime
from sqlalchemy import Column,Integer, String, create_engine,DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref
from prettytable import PrettyTable

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
    Session = sessionmaker(bind = engine)
    session = Session()

    menu = '''
    LOCAL CAB

    1: CREATE CUSTOMER                         
    2: VIEW CUSTOMER
    3: UPDATE CUSTOMER
    4: DELETE CUSTOMER
    5: ADD NEW DRIVER
    7: EXIT

'''

while True:
    print(menu)
    user_choice = input('Enter choice: ')

    if user_choice == "1":
        customer = Customer()
        customer.name = input('Enter name: ')
        customer.gender = input('Enter customer gender: ')
        customer.email = input('Enter email: ')
        customer.booking_time = datetime.now()

        driver = session.query(Driver).filter_by(id =  customer.driver_id).first()

        if driver:
            session.add(customer)
            session.commit()
            print('saved')

    elif user_choice == "2":
        customers = session.query(Customer).all()
        table = PrettyTable()
        for customer in customers:
            table.add_row([customer.id, customer.name, customer.gender, customer.email])

        print(table)

    elif user_choice == "3":
        customer_id = input('Enter customer id: ')
        customer = session.query(Customer).filter_by(id=customer_id).first()

    if customer:
        customer.name = input('Enter your name: ')
        customer.gender = input('Enter your gender: ')
        customer.email = input('Enter your email address: ')
        customer.booking_time = datetime.now()

        driver = session.query(Driver).filter_by(id = customer.driver_id).first()

        if driver:
            session.commit()
            print("Successful")


    elif user_choice == "4":
        #Delete customer record
        customer_name = input("Type the customer's id that you want to delete: ")
        customer = session.query(Customer).filter_by(name=customer_name).first()
        if customer:
            session.delete(customer)
            session.commit()
            print(f"{customer_name} deleted ")

        else:
            print(f"{customer_id} not found")

    elif user_choice == "5":
        #Adding a driver
        new_driver = Driver()
        new_driver.name = input("Enter the driver's name")
        new_driver.license_number = input("Enter the licence plate")
        new_driver.phone_number = input("Enter the driver's phone number")

        name_exists = session.query(Driver).filter_by(name = new_driver.name).first()
        if name_exists:
            print("Driver class already exists")

        else:
            session.add(new_driver)
            session.commit()
            print("Driver class added successfully")

    elif user_choice  == "9":
        print('exiting')

    else:
        print("Invalid")

    






        

       






    






