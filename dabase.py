import models as model
import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

class dabase:
        engine  = None
        def __init__(self, textConnectDB):
                self.engine = sql.create_engine(textConnectDB)

        def insertContent(self,content: str) ->None:
                session = Session(bind=self.engine )

                dataParser  = model.ParserData( 
                        title = "Заголовок2",
                        data = content
                )
                session.add(dataParser)
                session.commit()
                session.close()

        def selctDB (self)->list:
                Session = sessionmaker(bind=self.engine)
                session = Session()
        
                results = session.query(model.ParserData).all()
                session.close()
                return results

        def selctID (self,id: int) ->list:
                Session = sessionmaker(bind=self.engine)
                session = Session()
        
                results =  session.get(model.ParserData,id)
                session.close()

                return results