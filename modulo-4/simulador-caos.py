import random

class Academia:
    def __init__(self):
        self.halters = [i for i in range(10, 36) if i % 2 == 0] 
        self.porta_halters = {}
        self.reiniciar_o_dia()


    def reiniciar_o_dia(self):
        self.porta_halters = { i: i for i in self.halters }


    def listar_halters(self):
        return [i for i in self.porta_halters.values() if i != 0]
    

    def listar_espacos(self):
        return [i for i, j in self.porta_halters.items() if j == 0]
    

    def pegar_halters(self, peso):
        halt_position = list(self.porta_halters.values()).index(peso)
        key_halt = list(self.porta_halters.keys())[halt_position]
        self.porta_halters[key_halt] = 0
        return peso
    

    def devolver_halter(self, position, peso):
        self.porta_halters[position] = peso
    
    
    def calcular_o_caos(self):
        num_caos = [i for i, j in self.porta_halters.items() if i != j]
        caos = len(num_caos) / len(self.porta_halters)
        return caos


class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo #1: normal | 2: bagunceiro
        self.academia = academia
        self.peso = 0


    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halters()
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_halters(self.peso)


    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()

        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                position = random.choice(espacos)
                self.academia.devolver_halter(position, self.peso)
        elif self.tipo == 2:
            position = random.choice(espacos)
            self.academia.devolver_halter(position, self.peso)
        
        self.peso = 0

academia = Academia()
usuarios = [Usuario(1, academia) for i in range(10)]
usuarios += [Usuario(2, academia) for i in range(1)]
random.shuffle(usuarios)

list_caos = []

for k in range(50):
    academia.reiniciar_o_dia()
    for i in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
    list_caos += [academia.calcular_o_caos()]

import seaborn as sns
sns.displot(list_caos)

