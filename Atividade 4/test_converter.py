from converter import converter

def test_converter():
    assert converter(10, "Celsius") == 50
    assert converter(50, "Fahrenheit") == 10
    assert converter(10, "outro coisa") == "erro"