from dabase import selctDB,selctID
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post('/{item_id}')
def wed(item_id):
    html_content = int(item_id)
    html_content = selctID(html_content)

    return HTMLResponse(content=html_content.data)

@app.post('/')
def wedAll():
    conten = selctDB()
    html_content = ""
    for textConten in conten:
        html_content = textConten.data +'</br>'+ html_content

    return HTMLResponse(content=html_content)

def main(item_id:int) -> None:
    conten = selctID(item_id)
    conten = selctDB()
    for textCon in conten:    
        print(textCon.data)

if __name__ == "__main__":
    main(1)