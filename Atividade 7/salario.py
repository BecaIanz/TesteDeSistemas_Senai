def calculo_salario(valor_hora, horas_trabalhadas):
    salario = valor_hora * horas_trabalhadas
    if salario <= 5000:
        desconto = salario * 0.11
    else:
        desconto = (salario * 0.14) + (salario * 0.05)
    
    salario_liquido = salario - desconto
    return salario_liquido