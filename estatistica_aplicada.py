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

#             1 - MÉDIA ARITMÉTICA SIMPLES
def mediasimples(valores=()):
    valores.sort()
    print(f'Amostra ordenada = {valores}')
    media = 0

    for item in valores:
        media += item

    media = media / qtde_elementos
    print(f'Média Aritmética Simples = {media} ')
#####################################################


#             2 - MÉDIA ARITMÉTICA PONDERADA
def mediaponderada(valores=()):
    valores.sort()
    print(f'Amostra ordenada = {valores}')
    valorxpesos = 0
    soma_peso = 0

    for item in valores:
        peso = int(input(f'Digite o peso do valor {item}: '))
        valorxpesos += (peso * item)
        soma_peso += peso

    media_ponderada = valorxpesos / soma_peso
    print(f'Média Aritmética Ponderada = {media_ponderada}')
#####################################################


#             3 - MODA
def moda(valores=()):
    valores.sort()
    print(f'Amostra ordenada = {valores}')
    dic = {item: 0 for item in valores}
    for item in valores:
        if item in dic.keys():
            dic[item] += 1
    valor_moda = [item for item in dic.values()]
    resultado_moda = [numero for numero in dic.keys() if dic[numero] == max(valor_moda) and max(valor_moda) > 1]

    if len(resultado_moda) != 0:
        print(f' Moda = {resultado_moda}')
    else:
        print('Amostra Amodal')
#####################################################


#             4 - MEDIANA
def mediana(valores=()):
    valores.sort()
    print(f'Amostra ordenada = {valores}')
    if qtde_elementos % 2 == 0:
        med = (valores[int((qtde_elementos / 2) - 1)] + valores[int((qtde_elementos / 2))]) / 2
        print(f'Mediana = {med}')
    else:
        med = valores[int((qtde_elementos / 2))]
        print(f'Mediana = {med}')
#####################################################


#             5 - PRIMEIRO QUARTIL
def primeiroquartil(valores=()):
    valores.sort()
    print(f'Amostra ordenada = {valores}')
    if qtde_elementos % 4 == 0:
        q1 = (valores[int((qtde_elementos / 4) - 1)] + valores[int((qtde_elementos / 4))]) / 2
        print(f'Primeiro Quartil = {q1}')
    else:
        q1 = valores[int((qtde_elementos / 4))]
        print(f'Primeiro Quartil = {q1}')
#####################################################


#             6 - TERCEIRO QUARTIL
def terceiroquartil(valores=()):
    valores.sort()
    print(f'Amostra ordenada = {valores}')
    if (3 * qtde_elementos) % 4 == 0:
        q3 = (valores[int((3 * qtde_elementos / 4) - 1)] + valores[int((3 * qtde_elementos / 4))]) / 2
        print(f'Terceiro Quartil = {q3}')
    else:
        q3 = valores[int(((3 * qtde_elementos) / 4))]
        print(f'Terceiro Quartil = {q3}')
#####################################################


# #################INÍCIO DO PROGRAMA################
qtde_elementos = int(input('Digite a quantidade de elementos da amostra: '))
elementos = []
for elemento in range(0, qtde_elementos):
    valor = int(input(f'Digite o {elemento+1}º valor: '))
    elementos.append(valor)

# ==================MENU DE ESCOLHA==================
print('''
                 ---MENU---
    | 1 - Média Aritmética Simples
    | 2 - Média Aritmética Ponderada
    | 3 - Moda
    | 4 - Mediana
    | 5 - Primeiro Quartil
    | 6 - Terceiro Quartil
    | 7 - Amplitude
    | 8 - Desvio-Padrão
    | 9 - Calcular Tudo
    | 0 - Encerrar
    
    ''')
menu = int(input('Digite o número da Opção desejada: '))

# =============EXECUÇÃO DOS PROCEDIMENTOS============
if menu == 1:
    mediasimples(elementos)
elif menu == 2:
    mediaponderada(elementos)
elif menu == 3:
    moda(elementos)
elif menu == 4:
    mediana(elementos)
elif menu == 5:
    primeiroquartil(elementos)
elif menu == 6:
    terceiroquartil(elementos)

