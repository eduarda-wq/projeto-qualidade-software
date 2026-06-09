
from src.restaurante import filtrar_restaurantes_abertos

def test_deve_retornar_apenas_restaurantes_abertos():
   
    lista_restaurantes = [
        {"nome": "Pizzaria Italiana", "aberto": True},
        {"nome": "Sushi Express", "aberto": False},
        {"nome": "Burger House", "aberto": True}
    ]
    
  
    resultado = filtrar_restaurantes_abertos(lista_restaurantes)
    
    assert len(resultado) == 2
    assert resultado[0]["nome"] == "Pizzaria Italiana"
    assert resultado[1]["nome"] == "Burger House"