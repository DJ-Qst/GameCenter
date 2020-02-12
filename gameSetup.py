from random import shuffle


class Setup:
    def __init__(self):
        # Deck
        self.deckOfCards = [14, 14, 14, 14,
                            2, 2, 2, 2,
                            3, 3, 3, 3,
                            4, 4, 4, 4,
                            5, 5, 5, 5,
                            6, 6, 6, 6,
                            7, 7, 7, 7,
                            8, 8, 8, 8,
                            9, 9, 9, 9,
                            10, 10, 10, 10,
                            11, 11, 11, 11,
                            12, 12, 12, 12,
                            13, 13, 13, 13]

        # Getting Num Players
        while True:
            try:
                self.numPlayers = int(input("How many players are there: "))
                break
            except ValueError:
                print("That was not a valid input")

    def shuffleanddeal(self):
        start = 0
        players = []

        # Shuffling, 10 times because each time program is run, it's as if its a brand new deck
        for i in range(10):
            shuffle(self.deckOfCards)

        # Circling through the number of total players and appending each player to the list
        for player in range(self.numPlayers):
            player = self.deckOfCards[start::self.numPlayers]
            players.append(player)
            start += 1
        return players
