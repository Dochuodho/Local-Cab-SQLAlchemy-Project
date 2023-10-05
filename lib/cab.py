#lib/cab.py
#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column,Integer, String, create_engine,desc, CheckConstraint, PrimaryKeyConstraint, UniqueConstraint, Index, DateTime 
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    gender = Column(String())
    email = Column(String())
    booking_time = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"The rider's name is {self.name} and the booking time is {self.booking_time}"

if __name__ == '__main__':
    engine = create_engine('sqlite:///cab.db')
    Base.metadata.create_all(engine)

#configuring a session
Session = sessionmaker(bind=engine)
#use  'Session' class to create 'session' object
session = Session()

derrick = Customer(name="Derrick", gender="male", email="derrick@gmail.com") 
whitney = Customer(name="Whitney", gender="female", email="whitney@gmail.com") 
wendy = Customer(name="Wendy", gender="female", email="wendy@gmail.com") 

session.add_all([derrick, whitney,wendy])
session.commit()



