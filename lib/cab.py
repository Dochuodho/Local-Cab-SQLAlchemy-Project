#lib/cab.py
#!/usr/bin/env python3
from sqlalchemy import Column,Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    gender = Column(String())


engine = create_engine('sqlite:///cab.db')
Base.metadata.create_all(engine)


