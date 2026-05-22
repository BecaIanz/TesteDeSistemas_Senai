from areas import area_elipse, area_quadrado, area_triangulo

def test_area_quadrado():
    assert area_quadrado(2) == 4

def test_area_triangulo():
    assert area_triangulo(5,4) == 10

def test_area_elipse():
    assert area_elipse(6,3) == 56.5486