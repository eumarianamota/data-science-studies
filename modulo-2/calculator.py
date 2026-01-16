import os

operations = {
    "+": "Adição",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    "**": "Potenciação"
}

def Calculation(op, v1, v2):
    if op == 0:
        return  v1 + v2
    elif op == 1:
        return v1 - v2
    elif op == 2:
        return v1 * v2
    elif op == 3:
        return v1 / v2
    elif op == 4:
        return v1 ** v2


def Calculator():
    while True:
        os.system("clear")

        print('=============================')

        i = 0
        for op, name in operations.items():
            print("{}:{}".format(i, name))
            i += 1
        
        print('=============================')
        
        print("\nEscolha a operação que deseja realizar:")

        op = int(input())
        op_string = list(operations.keys())[op]

        print('\n=============================')
        print("{} foi a operação escolhida!".format(op_string))
        print('=============================')

        print("\nQual o primeiro valor?")
        v1 = float(input())
        print("Qual o segundo valor?")
        v2 = float(input())

        result = Calculation(op, v1, v2)

        print('\n=============================')
        print("{} {} {} = {}".format(v1, op_string, v2, result))
        print('=============================')

        print("\nDeseja fazer mais alguma operação? 0: SIM 1:NÂO")
        
        comand = input()
        if comand == "1":
            print('\n============================================')
            print("Operação finalizada, obrigada e até mais!")
            print('============================================')
            break        

Calculator()