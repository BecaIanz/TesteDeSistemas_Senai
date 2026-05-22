usuarios = {"thais": 1234, "rebeca" : 4321, "helo" : 5678, "stati" : 8765 }

def autenticar(usuario, senha):
    for user, password in usuarios.items():
        if(user == usuario):
            if(password == senha):
                return "Sucesso"
            else:
                return "Senha Incorreta"
    return "Usuario não encontrado"
        
