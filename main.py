from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
import random

app = FastAPI()

@app.get("/",response_class=FileResponse)
def root():
    return FileResponse("images/" + os.listdir("images/")[random.randint(0,len(os.listdir("images/"))-1)])
