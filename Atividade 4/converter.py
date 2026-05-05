def converter(temp, escala):
    if escala == "Celsius":
        return (temp*(9/5)) + 32
    if escala == "Fahrenheit":
        return (temp-32) * (5/9)
    return "erro"