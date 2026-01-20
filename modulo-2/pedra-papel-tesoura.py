import os
import random 

def StartGame():
    moves = ["Pedra", "Papel", "Tesoura"]
    gamer_score = 0
    pc_score = 0
    
    while True:
        print("\n===============================================")
        print("| Bem vindo ao jogo de Pedra, Papel e Tesoura |")
        print("===============================================")

        print("\nPLACAR:")
        print("Você: {}".format(gamer_score))
        print("Computador: {}".format(pc_score))

        print("\nEscolha o seu lance:")
        print("0: Pedra | 1: Papel | 2: Tesoura")

        gamer_move = int(input())
        pc_move = random.randint(0, 2)

        if gamer_move == pc_move:
            result = "Empatou!" 
        elif gamer_move == 0 and pc_move == 1:
            pc_score += 1
            result = "O computador ganhou!"
        elif gamer_move == 0 and pc_move == 2:
            gamer_score += 1
            result = "Você ganhou!"
        elif gamer_move == 1 and pc_move == 0:
            gamer_score += 1
            result = "Vocẽ ganhou!"
        elif gamer_move == 1 and pc_move == 2:
            pc_score += 1
            result = "O computador ganhou!"
        elif gamer_move == 2 and pc_move == 0:
            pc_score += 1
            result = "O computador ganhou!"
        elif gamer_move == 2 and pc_move == 1:
            gamer_score += 1
            result = "Você ganhou!"
        

        print("\n========================================")
        print("Sua jogada: {}".format(moves[gamer_move]))
        print("Jogada do computador: {}".format(moves[pc_move]))
        print(result)
        print("========================================")

        print("\nJogar novamente?")
        print("0: Sim | 1: Não")
        option = int(input())

        if option == 0:
            os.system('clear')
        else:
            break

StartGame()