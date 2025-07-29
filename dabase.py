import models as model
import sqlalchemy as sql
from sqlalchemy.orm import Session

engine  = sql.create_engine("postgresql+psycopg2://admin:12345@localhost/crudDB2")

def insertContent(content: str):
    session = Session(bind=engine)

    dataParser  = model.ParserData( 
            title = "Заголовок2",
            data = content
    )

    session.add(dataParser)

    session.commit()

    session.close()
