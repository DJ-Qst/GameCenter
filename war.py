from gameSetup import Setup


class War:
    def __init__(self):
        while True:
            self.setup = Setup()
            self.Players = self.setup.shuffleanddeal()
            self.NumPlayers = len(self.Players)
            if self.NumPlayers == 2:
                break
            print("There are too many, or not enough, players for this game, you may only have 2 players")
        self.playerMoves = None
        self.playerNumber = 1

    def turn(self):
        while len(self.Players[0]) != 52 or len(self.Players[1]) != 52:
            print(f"Player 1 has {len(self.Players[0])} cards")
            print(f"Player 2 has {len(self.Players[1])} cards\n\n")
            self.playerMoves = [item[0] for item in self.Players]
            for i in self.playerMoves:
                z = i
                if i == 14:
                    z = "Ace"
                if i == 11:
                    z = "Jack"
                if i == 12:
                    z = "Queen"
                if i == 13:
                    z = "King"
                print(f"Player {self.playerNumber} flipped a {z}")
                self.playerNumber += 1
            self.playerNumber = 1
            winner = self.checkwin()
            if winner == 0:
                print("Player 1 won this round")
                self.Players[0].append(self.playerMoves[1])
                self.Players[1].remove(self.playerMoves[1])
            if winner == 1:
                print("Player 2 won this round")
                self.Players[1].append(self.playerMoves[0])
                self.Players[0].remove(self.playerMoves[0])
            if winner == "GoToWar":
                print("It's time to go to war!!")
                self.gotowar()
            input("Press enter to continue")
            print("")

    def checkwin(self):
        moves = self.playerMoves
        # Checking if the cards are equal
        if moves.count(moves[0]) == len(moves):
            return "GoToWar"

        # Checking who won otherwise
        else:
            winner = moves.index(max(moves))
            return winner


    def gotowar(self):
        pass


game = War()
game.turn()
