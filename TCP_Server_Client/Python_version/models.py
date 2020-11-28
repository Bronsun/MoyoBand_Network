from sqlalchemy import create_engine, Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker

engine = create_engine('sqlite:///moyo.db',echo = True)
Session = sessionmaker(bind=engine)
session=Session()
Base = declarative_base()

class Patient(Base):
    __tablename__ ="patient"

    id = Column('id',Integer,primary_key=True)
    name = Column(String, nullable=False)
    lastname = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    sex = Column (String,nullable=False)
    bands = relationship('Band',backref="patient",lazy=True)
    def __repr__(self):
        return f"Patient('{self.name}','{self.lastname}','{self.age}','{self.sex}')"

class Band(Base):
    __tablename__="band"

    id = Column('id',Integer,primary_key=True)
    MAC = Column(String,nullable=False)
    room = Column(String)
    bed = Column (Integer)
    patient_id = Column(Integer,ForeignKey('patient.id'),nullable=True)




def AddPatient(name,lastname,age,sex):
    if name==None or lastname==None or age==None or sex==None:
        print("Brak poprawnych danych wpisz ponownie")
    else:
        patient_look = session.query(Patient).filter_by(name=name,lastname=lastname).first()
        if patient_look is None:
            patient = Patient(name=name,lastname=lastname,age=age,sex=sex)
            session.add(patient)
            session.commit()
            print("Pacjent dodany pomyślnie")
        else:
            print("Taki pacjent juz istnieje. Usun aby dodac na nowo")        

def AddBand (lastname,MAC,room,bed):
    if lastname == None or MAC == None:
        print("Brak poprawnych danych wpisz ponownie")
    else:
        band = Band(MAC=MAC,room=room,bed=bed,author=lastname)
        session.add(band)
        session.commit()
        return ("Opaska została przypisana poprawnie")

def ShowPatient():
    pacjenci = session.query(Patient).all()
    print(pacjenci)

def ShowBands():
    opaski = session.query(Band).all()
    print(opaski)

def DeletePatient(name,lastname):
    patient = session.query(Patient).filter_by(name=name,lastname=lastname).first()
    if patient is None:
        print("Nie ma takiego uzytkownika")
    else:
        session.delete(patient)
        session.commit()

if __name__ == "__main__":
    Base.metadata.create_all(engine)    


