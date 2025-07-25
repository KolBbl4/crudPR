import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

BASE_NAME = "crudDB2"
USER_DATABASE = "admin"
PASSWORD_USER_DATABASE = "12345"
HOST_DATABASE = "localhost"


Base = declarative_base()
engine  = sql.create_engine("postgresql+psycopg2://admin:12345@localhost/crudDB2",echo=True)

class ParserData(Base):
    __tablename__ = 'parser_data'
    id = sql.Column(sql.Integer, primary_key = True)
    title = sql.Column(sql.String)
    data = sql.Column(sql.String)
    dattime = sql.Column(sql.DateTime(), default=datetime.now)
    
if __name__ == "__main__":
    Base.metadata.create_all(engine)