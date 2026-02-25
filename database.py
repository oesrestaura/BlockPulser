from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database for storing transaction data
DATABASE_URL = "sqlite:///blockpulse.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    tx_hash = Column(String, unique=True, index=True)
    from_address = Column(String)
    to_address = Column(String)
    value = Column(Float)


def init_db():
    # Create database tables
    Base.metadata.create_all(bind=engine)
