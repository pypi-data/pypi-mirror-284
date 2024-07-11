from datetime import datetime
from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


def get_engine(database: str, echo: bool = False):
    """
    Create DB Engine
    """
    engine = create_engine(database, echo=echo)

    return engine


def get_session(engine):
    """
    Create DB Session
    """
    session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )

    return session


def create_tables(engine):
    """
    Create Tables
    """
    Base.metadata.create_all(bind=engine)


def upsert(session, model, **kwargs) -> int:
    """
    Insert data
    Update existing data, if any
    """
    table = model.__table__
    primary_key = list(table.primary_key.columns.keys())[0]

    instance = (
        session.query(model).filter_by(**{primary_key: kwargs[primary_key]}).first()
    )

    if instance:
        # Update updated_at when changes are made
        for key, value in kwargs.items():
            if getattr(instance, key) != value:
                setattr(instance, key, value)
                instance.updated_at = datetime.now()
        session.add(instance)
    else:
        # Insert new instance
        instance = model(**kwargs)
        session.add(instance)

    try:
        session.commit()
        return instance.id
    except exc.SQLAlchemyError as e:
        session.rollback()
        print(f"Error occurred: {e}")
        print(model)
        print(instance)
        # Handle the error gracefully, optionally log it
        # You can choose to raise an exception or handle it as per your application's needs
    finally:
        session.close()
