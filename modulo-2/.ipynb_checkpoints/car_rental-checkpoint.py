import os

options = {
    "0": "Mostrar portifólio",
    "1": "Alugar um carro",
    "2": "Devolver um carro",
}

portifolio = [
    ["Chevrolet Tracker", 120],
    ["Chevrolet Onix", 90],
    ["Chevrolet Spin", 150],
    ["Hyundai HB20", 85],
    ["Hyundai Tucson", 120],
    ["Fiat Uno", 60],
    ["Fiat Mobi", 70],
    ["Fiat Pulse", 130]
]

rental_walet = [
] 

def Clear():
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear')


def Keep_or_go():
    print("0: Continuar | 1: Sair")
    option = int(input())

    Clear()

    if option == 0:
        return Welcome()
    else: 
        return "O programa foi finalizado"


def Portifolio():
    print("\n==================================================")
    print("| Veja os carros disponíveis no nosso portifólio |")
    print("==================================================")

    print("\n=============================================")
    i = 0 
    for item in portifolio:
        print("-> [{}] {} - R$: {} por dia".format(i, item[0], item[1]))
        i += 1
    print("=============================================")

    Keep_or_go()


def Rentals():
    print("=====================================")
    print("| Escolha o carro que deseja alugar |")
    print("=====================================")

    print("\n=============================================")
    i = 0 
    for item in portifolio:
        print("-> [{}] {} - R$: {} por dia".format(i, item[0], item[1]))
        i += 1
    print("=============================================")

    print("\n=============================")
    print("| Escolha o código do carro |")
    print("=============================")
    code = int(input("-> "))

    print("\n==========================================")
    print("| Escolha por quantos dias deseja alugar |")
    print("==========================================")
    days = int(input("-> "))

    rental_price = portifolio[code][1] * days

    print("\nVocê escolheu {} por {} dias".format(portifolio[code][0], days))
    print("\nO aluguel totaliza R$: {}. Deseja alugar?".format(rental_price))
    print("\n0: SIM | 1: NÃO")
    option = int(input())
    if option == 0:
        rental_walet.append([portifolio[code][0], portifolio[code][1]])
        del portifolio[code]
        print("\n==================================")
        print("| Aluguel concluído com sucesso! |")
        print("==================================")
        Keep_or_go()
    else:
        Welcome()


def Car_return():
    print("===================")
    print("| Carros alugados |")
    print("===================")

    print("\n=============================================")
    i = 0
    for item in rental_walet:
        print("-> [{}] {} - R$: {} por dia".format(i, item[0], item[1]))
        i += 1
    print("=============================================")

    print("\n=================================================")
    print("| Escolha o código do carro que deseja devolver |")
    print("=================================================")
    
    code = int(input("-> "))
    portifolio.append([rental_walet[code][0], rental_walet[code][1]])
    del rental_walet[code]

    print("\n=================================")
    print("| Obrigada por devolver o carro |")
    print("=================================")

    Keep_or_go()


def Welcome():
    Clear()

    print("====================")
    print("| LOCADORA DA MATI |")
    print("====================")

    print("\n=======================")
    print("| O que deseja fazer? |")
    print("=======================")

    print("\n=======================")
    i = 0
    for id, name in options.items():
        print("{}: {}".format(i, name))
        i += 1
    print("=======================")
    
    option = int(input("\n-> "))

    Clear()

    if option == 0:
        return Portifolio()
    elif option == 1:

        return Rentals()
    else:
        return Car_return()



Welcome()