def verificar_maioridade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"
    
idade_usuario = int(input("digite sua idade: "))

status = verificar_maioridade(idade_usuario)
print(f"você é {status}.")