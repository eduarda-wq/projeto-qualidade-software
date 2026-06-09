from src.busca import sanitizar_busca

def test_busca_case_insensitive():
    
    termo_digitado = "ITALIANA"
    
    
    resultado = sanitizar_busca(termo_digitado)
    
  
    assert resultado == "italiana"