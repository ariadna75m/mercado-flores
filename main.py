from fastapi import FastAPI

app = FastAPI(title="Mercado de Flores de Acho API")

CATALOGO = [
    {"id": 1, "nombre": "Docena de Rosas Rojas", "precio": 35.0, "stock": True},
    {"id": 2, "nombre": "Ramo de Girasoles", "precio": 25.0, "stock": True},
    {"id": 3, "nombre": "Arreglo Día de la Madre", "precio": 80.0, "stock": True},
]

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API del Mercado de Flores de Acho"}

@app.get("/catalogo")
def obtener_catalogo():
    return {"productos": CATALOGO}

@app.get("/delivery/{distrito}")
def calcular_delivery(distrito: str):
    costo = 10.0 if distrito.lower() == "rimac" else 18.0
    return {"distrito": distrito, "costo_envio": costo}