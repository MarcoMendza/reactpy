from reactpy import component, html, use_state, use_effect
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

# Suponiendo que get_products_data es una función que obtiene los datos de la tabla Productos
# async def get_products_data():
#     # Tu lógica para obtener los datos
#     pass

bootstrap_css = html.link({
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
})

@component
def ProductTable():
    products_data, set_products_data = use_state([])

    async def fetch_data():
        # Suponiendo que get_products_data es una función que obtiene los datos de la tabla Productos
        # data = await get_products_data()
        # Simulando datos como ejemplo
        data = [
            {"nombre": "Producto 1", "cantidad": 10, "almacen_id": 1},
            {"nombre": "Producto 2", "cantidad": 15, "almacen_id": 2},
            # ... más datos
        ]
        set_products_data(data)

    use_effect(fetch_data)

    rows = [
        html.tr([
            html.td(product["nombre"]),
            html.td(str(product["cantidad"])),
            html.td(str(product["almacen_id"])),
        ]) for product in products_data
    ]

    return html.div(
        {
            "class_name": "container",
            "style": {
                "margin-top": "20px"
            }
        },
        bootstrap_css,
        html.table(
            {
                "class_name": "table table-striped table-bordered table-hover"
            },
            html.thead(
                html.tr([
                    html.th("Nombre"),
                    html.th("Cantidad"),
                    html.th("ID Almacen"),
                ])
            ),
            html.tbody(
                rows
            )
        )
    )

app = FastAPI()

configure(app, ProductTable)
