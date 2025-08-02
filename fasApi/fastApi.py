from dabase import selctDB
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def wed():
    conten = selctDB()
    html_content = ""
    for textConten in conten:
        html_content = textConten +'</br>'+ html_content
    return HTMLResponse(content=html_content)
conten = selctDB()
print(conten)
# for textConten in conten:
#         html_content = textConten +'</br>'+ html_content