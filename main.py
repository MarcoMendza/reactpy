from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html
from fastapi.staticfiles import StaticFiles
from reactpy.core.hooks import create_context
from reactpy_router import route, simple

from frontend.login import Login
from frontend.productos import ProductTable

app = FastAPI()

@component
def App():

    return simple.router(
        route("/", html.h1("Bienvenido")),  # Página principal
        route("/login", Login()),
        route("/productos", ProductTable()),
        route("*", html.h1("Página no encontrada"))  # Manejo de rutas no definidas
    )

# Opcional: Incluir routers FastAPI si los tienes
# app.include_router(api_router)

configure(app, App)
