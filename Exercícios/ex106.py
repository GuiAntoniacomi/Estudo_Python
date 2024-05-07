def ajuda(com):
    help(com)


def título(msg, cor=0):
    tam = len(msg)
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


#Programa principal
comando = " "
while True:
    título('SISTEMA DE AJUDA PYHELP')
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
título('ATÉ LOGO')