from dabase import dabase
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()
dabase = dabase(os.getenv("DATABASE_URL"))

@app.post('/{item_id}')
def wed(item_id):
    html_content = int(item_id)
    html_content = dabase.selctID(html_content)

    return HTMLResponse(content=html_content.data)

@app.post('/')
def wedAll():
    conten = dabase.selctDB()
    html_content = ""
    for textConten in conten:
        html_content = textConten.data +'</br>'+ html_content

    return HTMLResponse(content=html_content)


def main(item_id:int) -> None:
    database_url = os.getenv("DATABASE_URL")
    print (database_url)
    conten = dabase.selctID(item_id)
    conten = dabase.selctDB()
    for textCon in conten:    
        print(textCon.data)

if __name__ == "__main__":
    main(1)