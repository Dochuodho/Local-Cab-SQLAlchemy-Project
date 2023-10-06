#lib/cab.py
#!/usr/bin/python3
from datetime import datetime
from sqlalchemy import Column,Integer, String, create_engine,DateTime 
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
    
class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    license_number = Column(String())

if __name__ == '__main__':
    engine = create_engine('sqlite:///cab.db')
    Base.metadata.create_all(engine)







