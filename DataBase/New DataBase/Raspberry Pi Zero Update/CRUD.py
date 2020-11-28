from config import Base,engine,session,Band

def UpdateStats(MAC,HeartRate,Temperature,Saturation):
    band_update = session.query(Band).filter_by(MAC=MAC).first()
    if band_update is None:
        print("Nie ma takiej opaski")
        session.bind.dispose()
    else:
        band_update.HeartRate = HeartRate
        band_update.Temperature = Temperature
        band_update.Saturation = Saturation
        session.commit()
        session.bind.dispose()
        print = "Baza danych zaktualizowana"

