from usuarios import autenticar

def test_autenticar():
    assert autenticar("thais", 1234) == "Sucesso"
    assert autenticar("rebeca", 134) == "Senha Incorreta"
    assert autenticar("fernanda", 1234) == "Usuario não encontrado"
    