from conversao import medidas, volume, moeda

def test_medidas():
    assert medidas(1, "cm") == 100
    assert medidas(100, "m") == 1
    assert medidas(100, "ml") == "erro"

def test_volume():
    assert volume(1000, "l") == 1
    assert volume(1, "ml") == 1000

def test_moeda():
    assert moeda(1, "real") == 5
    assert moeda(5, "dolar") == 1