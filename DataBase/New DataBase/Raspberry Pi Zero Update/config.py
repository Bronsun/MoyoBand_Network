from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


Base = automap_base()
engine = create_engine("postgresql+psycopg2://ukeybyqq:p2HS4u8sycy-NBKfG6x_hq0lqI9YU1iB@balarama.db.elephantsql.com:5432/ukeybyqq") 
Base.prepare(engine,reflect=True)

Band = Base.classes.band

session=Session(engine)
