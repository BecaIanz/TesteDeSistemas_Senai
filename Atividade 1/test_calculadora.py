from calculadora import somar, subtrair, divisao, multiplicacao

def test_soma():
    assert somar(2,3) == 5
    
def test_subtrair():
    assert subtrair(4,2) == 2
    
def test_divisao():
    assert divisao(10,2) == 5
    assert divisao(2,0) == "erro"
    
def test_multi():
    assert multiplicacao(2,2) == 4