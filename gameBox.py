from war import War
from TicTacToe import TicTacToe

War = War()
TTT = TicTacToe()

print("Your game options are: ")

print("\t(1) War")
print("\t\tA Two player game of flipping and collecting cards until one person holds all of the cards,")
print("\t\tbut watch out, there's a twist if you flip over the sae card!")

print("\t(2) Tic Tac Toe")
print("\t\tA one or two player game where people take turns placing an X or an O attemping to get three in a row")

while True:
    try:
        game = int(input("\nPlease input the number of the game you would like to play: "))
        break
    except ValueError:
        print("That was not a game number!")

if game == 1:
    War.game()

elif game == 2:
    TTT.game()
