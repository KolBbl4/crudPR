import models as model
import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


def insertContent(content: str) ->None:
    engine  = sql.create_engine("postgresql+psycopg2://admin:12345@localhost/crudDB2")
    session = Session(bind=engine)

    dataParser  = model.ParserData( 
            title = "Заголовок2",
            data = content
    )

    session.add(dataParser)

    session.commit()

    session.close()

def selctDB ()->list:
        engine  = sql.create_engine("postgresql+psycopg2://admin:12345@localhost/crudDB2")
        Session = sessionmaker(bind=engine)
        session = Session()
  
        results = session.query(model.ParserData).all()
        session.close()
        return results

def selctID (id: int) ->list:
        engine  = sql.create_engine("postgresql+psycopg2://admin:12345@localhost/crudDB2")
        Session = sessionmaker(bind=engine)
        session = Session()
  
        results =  session.get(model.ParserData,id)
        session.close()
        return results