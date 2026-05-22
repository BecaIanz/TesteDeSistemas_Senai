def medidas(med, tipo):
    if tipo == "cm":
        return med*100
    elif tipo == "m":
        return med/100
    else:
        return "erro"
    
def volume(vol, tipo):
    if tipo == "l":
        return vol/1000
    elif tipo == "ml":
        return vol*1000
    else:
        return "erro"
    
def moeda(val, tipo):
    if tipo == "real":
        return val*5
    if tipo == "dolar":
        return val/5
    else:
        return "erro"