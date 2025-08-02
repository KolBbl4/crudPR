from dabase import selctDB
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from parserData import parcAndInsert

app = FastAPI()

@app.post('/')
def wed():
    conten = selctDB()
    html_content = ""
    for textConten in conten:
        html_content = textConten.data +'</br>'+ html_content
    return HTMLResponse(content=html_content)

def main() -> None:
    wed()
if __name__ == "__main__":
    main()