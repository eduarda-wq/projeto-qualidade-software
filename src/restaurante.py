
def filtrar_restaurantes_abertos(restaurantes: list) -> list:
    abertos = []
    for restaurante in restaurantes:
        if restaurante.get("aberto") is True:
            abertos.append(restaurante)
    return abertos