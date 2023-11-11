from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
import os, uvicorn
from apps import create_app
from apps.config.config import config_dict

# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    app_config = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production]')

app = create_app(app_config)

templates = Jinja2Templates(directory="templates")

# Define a route that renders an HTML template


@app.get("/render_template/")
async def render_template(request: Request):
    # Variables that you want to pass to the template
    context = {"title": "FastAPI Jinja2 Example", "message": "Hello, FastAPI!"}

    # Render the template with the provided context
    return templates.TemplateResponse("D:\\deploy\\python-api-kubectl\\apps\\template\\index.html", {"request": request, "context": context})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
