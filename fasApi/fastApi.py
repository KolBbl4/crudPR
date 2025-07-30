from fastapi import FastAPI
from fastapi.responses import HTMLResponse

api = FastAPI()

@api.get('/')
def wed():
    html_content = "<h2>Hello METANIT.COM!</h2>"
    return HTMLResponse(content=html_content)