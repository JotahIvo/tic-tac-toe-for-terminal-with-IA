import os, sys
from game import TicTacToeGame


def main():
    while True:
        os.system('clear')
        print('''
Instruções do Jogo: 
-> Você controla o X e a IA controla o O.
-> Você começa jogando e a cada jogada sua a IA faz uma jogada.
-> Para jogar vocêdeve escolher em qul linha e em qual coluna você deseja inseriri o X.
-> Para vencer você deve completar uma linha, coluna ou diagonal com X.
-> Se nenhum dos dois conseguir então o jogo empata.

PARA JOGAR PRESSIONE ENTER (boa sorte para vencer essa IA...)
''')
        input()

        #game
        game = TicTacToeGame()
        game.run_game()

        input()


if __name__ == "__main__":
    main()