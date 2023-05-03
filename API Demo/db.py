import sqlalchemy
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker

db_uri = "sqlite:///db.sqlite"

engine = sqlalchemy.create_engine(db_uri)
factory = sessionmaker(bind=engine)

Base = sqlalchemy.orm.declarative_base()

class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    aufgabe = Column(String())
    fortschritt = Column(Integer())
    fertig = Column(Boolean())

class Benutzer(Base):
    __tablename__ = "benutzer"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    nutzername = Column(String())
    alter = Column(Integer())


Base.metadata.create_all(engine)
