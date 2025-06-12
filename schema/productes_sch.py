def schema(producte) -> dict:
    send_producte = {
        "id": producte["id"],
        "nom": producte["nom"],
        "cost": producte["cost"],
        "quantitat": producte["quantitat"],
        "proveedor": producte["proveedor"],
        "ventes": producte["ventes"]
    }
    return send_producte
def schemas(productes) -> list[dict]:
    return [schema(producte) for k,producte in productes.items()]