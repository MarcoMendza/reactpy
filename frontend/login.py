import httpx
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state

bootstrap_css = html.link({
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
})

@component
def Login():
    email, set_email = use_state("")  
    password, set_password = use_state("")
    error_message, set_error_message = use_state("")

    async def handle_submit(e):
        e.prevent_default()  # Para evitar la recarga de la página
        if email and password:
            async with httpx.AsyncClient() as client:
                response = await client.post('/login/', json={
                    'email': email,
                    'password': password
                })
                if response.status_code == 200:
                    print('aa')
                    # Autenticación exitosa, redirige o actualiza el estado como sea necesario
                    return html.script("window.location.href = '/productos';")
                elif response.status_code == 400 or response.status_code == 401:
                    print('bb')
                    set_error_message("Credenciales inválidas")
                else:
                    print('cc')
                    set_error_message("Error en el servidor")

    return html.div(
        {
            "style": {
                "background-color": "#262254",
                "height": "100vh",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center"
            }
        },
        bootstrap_css,
        html.form(
            {
                "on_submit": handle_submit,
                "class_name": "card p-4",
                "style": {
                    "width": "400px"
                },
                "prevent_default": True
            },
            html.div(
                {
                    "class_name": "mb-3"
                },
                html.label(
                    {
                        "for": "email",
                        "class_name": "form-label"
                    },
                    "Correo Electronico"
                ),
                html.input({
                    "type": "email",
                    "id": "email",
                    "placeholder": "Ingresa tu correo",
                    "on_change": lambda e: set_email(e["target"]["value"]),
                    "value": email,
                    "class_name": "form-control"
                }),
            ),
            html.div(
                {
                    "class_name": "mb-3"
                },
                html.label(
                    {
                        "for": "password",
                        "class_name": "form-label"
                    },
                    "Contraseña"
                ),
                html.input({
                    "type": "password",
                    "id": "password",
                    "placeholder": "Contraseña",
                    "on_change": lambda e: set_password(e["target"]["value"]),
                    "value": password,
                    "class_name": "form-control"
                }),
            ),
            error_message and html.div(
                {
                    "class_name": "alert alert-danger",
                    "role": "alert"
                },
                error_message
            ),
            html.button(
                {
                    "type": "submit",
                    "class_name": "btn btn-primary"
                },
                "Ingresar"
            )
        )
    )
