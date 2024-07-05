
from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL
DATABASE_URL = 'mysql+pymysql://username:password@localhost/chemistry'

# Create an engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Define the base class for the models
Base = declarative_base()

# Define the Chemical model
class Chemical(Base):
    __tablename__ = 'Chemicals'
    chemical_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    formula = Column(String)
    state = Column(String)

# Query all chemicals
chemicals = session.query(Chemical).all()

# Print the list of chemicals
for chemical in chemicals:
    print(f"Name: {chemical.name}, Formula: {chemical.formula}, State: {chemical.state}")
