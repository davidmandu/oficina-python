######################################################
#        TRABALHO FINAL - OFICINA DE PYTHON          #
#                                                    #
#    NOMES: DAVID GALVÃO MANDU DA SILVA;             #
#           MIGUEL FERNANDES SANTOS.                 #
#                                                    #
#    DATA: --/--/2021                                #
#    PROJETO: CÁLCULOS DE ESTATÍSTCA BÁSICA.         #
#                                                    #
######################################################


# ##############PROCEDIMENTOS##############

# ==============MÉDIA ARITMÉTICA SIMPLES==============
def mediasimples(valores=()):
    media = 0

    for item in valores:
        media += item

    media = media / qtde_elementos
    print(f'Média Aritmética Simples = {media} ')
######################################################


# ==============MÉDIA ARITMÉTICA PONDERADA==============
def mediaponderada(valores=()):
    valorxpesos = 0
    soma_peso = 0

    for item in valores:
        peso = int(input(f'Digite o peso do valor {item}: '))
        valorxpesos += (peso * item)
        soma_peso += peso

    media_ponderada = valorxpesos / soma_peso
    print(f'Média Aritmética Ponderada = {media_ponderada}')
######################################################


# =##############INÍCIO DO PROGRAMA##############
qtde_elementos = int(input('Digite a quantidade de elementos da amostra: '))
elementos = []
for elemento in range(0, qtde_elementos):
    valor = int(input(f'Digite o {elemento+1}º valor: '))
    elementos.append(valor)

# ==============MENU DE ESCOLHA==============
print('''
                 ---MENU---
    | 1 - Média Aritmética Simples
    | 2 - Média Aritmética Ponderada
    | 3 - Moda
    | 4 - Mediana
    
    ''')
menu = int(input('Digite o número da Opção desejada: '))

# ==============EXECUÇÃO DOS PROCEDIMENTOS==============
if menu == 1:
    mediasimples(elementos)
elif menu == 2:
    mediaponderada(elementos)
