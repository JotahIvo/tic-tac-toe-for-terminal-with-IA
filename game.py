import os, sys
import random  
from ia import ia_play


class TicTacToeGame:
    def __init__(self):
        self.player = "X" #indica de quem é a jogada
        self.attempts = 9
        self.current_attempt = 0
        self.tictactoe = [
                            [" "," "," "],
                            [" "," "," "],
                            [" "," "," "]
                        ]


    def print_interface(self):
        os.system("clear")
        print("    0   1   2")
        print("0:  " + self.tictactoe[0][0] + " | " + self.tictactoe[0][1] + " | " + self.tictactoe[0][2])
        print("   -----------")
        print("1:  " + self.tictactoe[1][0] + " | " + self.tictactoe[1][1] + " | " + self.tictactoe[1][2])
        print("   -----------")
        print("2:  " + self.tictactoe[2][0] + " | " + self.tictactoe[2][1] + " | " + self.tictactoe[2][2])
        print("\nJogada: " + str(self.current_attempt))


    def refresh_tictactoe(self, row, column):
        if self.player == "X":
            self.tictactoe[row][column] = "X"
        else:
            self.tictactoe[row][column] = "O"


    #função temporária de jogadas aleatória para testar o jogo
    def random_play(self):
        row = random.randrange(0, 3)
        column = random.randrange(0, 3)

        while self.tictactoe[row][column] != " ":  
            row = random.randrange(0, 3)
            column = random.randrange(0, 3)

        return [row, column]    


    #1: X venceu, -1: O venceu, 0: empate
    def verify_victory(self):
        #verificar linhas:
        for i in range(3):
            if self.tictactoe[i][0] == self.player and self.tictactoe[i][1] == self.player and self.tictactoe[i][2] == self.player:
                if self.player == "X":  
                    return 1
                elif self.player == "O":
                    return -1
                else:
                    return 0 

        #verificar colunas:
        for i in range(3):
            if self.tictactoe[0][i] == self.player and self.tictactoe[1][i] == self.player and self.tictactoe[2][i] == self.player:
                if self.player == "X":  
                    return 1
                elif self.player == "O":
                    return -1
                else:
                    return 0

        #verificar diagonais:
        if self.tictactoe[0][0] == self.player and self.tictactoe[1][1] == self.player and self.tictactoe[2][2] == self.player:
            if self.player == "X":  
                return 1
            elif self.player == "O":
                return -1
            else:
                return 0

        if self.tictactoe[0][2] == self.player and self.tictactoe[1][1] == self.player and self.tictactoe[2][0] == self.player:
            if self.player == "X":  
                return 1
            elif self.player == "O":
                return -1
            else:
                return 0    

        return 0


    def verify_input(self, row, column):
        if row > 2 or column > 2:
            return False
        
        if self.tictactoe[row][column] != " ":
            return False
        
        return True


    def run_game(self):
        while self.current_attempt <= self.attempts:
            os.system("clear")
            self.print_interface()

            if self.current_attempt == self.attempts:
                break

            if self.player == "O":
                row = int(input("Linha: "))
                column = int(input("Coluna: "))

                while self.verify_input(row, column) == False:
                    os.system("clear")
                    self.print_interface()
                    print("Input inválido, tente novamente!")
                    row = int(input("Linha: "))
                    column = int(input("Coluna: "))

                position = [row, column]
            else:
                position = ia_play(self.tictactoe, self.player)
                
            self.refresh_tictactoe(position[0], position[1])

            if self.verify_victory() != 0:
                self.print_interface()
                break

            self.player = "X" if self.player == "O" else "O"
            self.current_attempt += 1
 

        if self.verify_victory() == -1:
            print("\nParabéns, você conseguiu vencer a máquina!!!")
        elif self.verify_victory() == 1:
            print("\nPelo visto a IA é mais inteligente do que você! Tente novamente HAHAHA")
        else:
            print("\nEmpate! Melhor do que perder, não é mesmo?")

        input("\nPressione 'ENTER' 2 vezes para jogar novamente...")

        

