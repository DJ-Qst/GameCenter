from gameSetup import Setup


class War:
    def __init__(self):
        self.setup = Setup()
        self.Players = self.setup.shuffleanddeal()
        self.NumPlayers = len(self.Players)
        self.playerMoves = None

    def turn(self):
        self.playerMoves = [item[0] for item in self.Players]
        for i in self.playerMoves:
            for x in range(len(self.playerMoves)):
                print(f"Player {x+1} flipped a {i}")


game = War()
game.turn()
