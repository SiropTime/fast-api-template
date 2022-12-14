from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from utility import *

templates = Jinja2Templates(directory=TEMPLATES_PATH)

app = FastAPI()
app.mount(f"/{STATIC_FILES_PATH}", StaticFiles(directory=STATIC_FILES_PATH), name="static")


# Importing to use controllers from another package
from app.controllers import app
