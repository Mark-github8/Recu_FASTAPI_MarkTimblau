def schema(usuari) -> dict:
    send_usuari = {
        "id": usuari["id"],
        "nom": usuari["nom"],
        "cognom": usuari["cognom"],
        "edat": usuari["edat"],
        "treball": usuari["treball"],
        "alcada": usuari["alcada"]
    }
    return send_usuari
def schemas(usuaris) -> list[dict]:
    return [schema(usuari) for k,usuari in usuaris.items()]