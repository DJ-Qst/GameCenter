from gameSetup import Setup


class War:
    def __init__(self):
        self.setup = Setup(numplayers=2)
        self.Players = self.setup.shuffleanddeal()
        # Variable storing
        self.playerMoves = None
        self.wonCards = []
        self.playerNumber = 1
        self.warCards = []
        self.lenWonCards = [[], []]
        self.flipper = None
        self.keepgoing = True

    def game(self):
        # While one player doesn't hold all of the cards
        while len(self.Players[0]) != 0 and len(self.Players[1]) != 0 and self.keepgoing:
            # Telling how many cards each person has
            print(f"\n\nPlayer 1 has {len(self.Players[0])} cards left")
            print(f"Player 2 has {len(self.Players[1])} cards left\n")
            self.getturncards()  # Getting cards for the turn

            # Converting the royalty/special numbers into words so it makes sense for user
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
                print(f"Player {self.playerNumber} flipped a {z}")  # Telling what each user printed
                self.playerNumber += 1
            self.playerNumber = 1  # Reseting player number for next turn

            winner = self.checkturnwin()  # Finding the winner of this turn

            # Telling winner and adding the cards or going to war
            if winner == 0:
                print("Player 1 won this round")
                self.Players[0].extend(self.playerMoves)
            if winner == 1:
                print("Player 2 won this round")
                self.Players[1].extend(self.playerMoves)
            if winner == "GoToWar":
                print("It's Time To Go To War!!!\n")
                self.gotowar()

            input("Press enter to continue")  # Basically just a wait function before moving on to next turn

        # If the war can't proceed, and one player doesn't hold all of the cards, but they won
        # because the war couldn't proceed
        if len(self.Players[0]) < 52 and len(self.Players[1]) < 52:
            pass

        # If one player holds all the cards, it finds the winner
        else:
            self.gamewinner()

    def getturncards(self):
        # Getting the moves for that turn
        self.playerMoves = [item[0] for item in self.Players]

        # Removing those cards from the player deck
        self.Players[0].pop(0)
        self.Players[1].pop(0)

    def checkturnwin(self):
        moves = self.playerMoves
        # Checking if the cards are equal
        if moves.count(moves[0]) == len(moves):
            return "GoToWar"

        # Checking who won otherwise
        else:
            winner = moves.index(max(moves))
            return winner

    def checkwarwin(self):
        moves = self.flipper  # Cards that were flipped in the war

        # Checking if the cards are equal
        if moves.count(moves[0]) == len(moves):
            return "GoToWar"

        # Checking who won otherwise
        else:
            winner = moves.index(max(moves))
            return winner

    def gamewinner(self):
        # Getting the len of player 1 & 2's cards
        self.lenWonCards[0] = len(self.Players[0])
        self.lenWonCards[1] = len(self.Players[1])

        # Finding out who won the game by getting the index of the higher value
        gamewinner = self.lenWonCards.index(max(self.lenWonCards))

        # Telling who won
        # First insert adds 1 so the index starts at 1
        # Second insert shows the number of cards by printing the len of the game winner
        print(f'Player {gamewinner + 1} won the game with {self.lenWonCards[gamewinner]} cards')

    def gotowar(self):
        # If one of the players doesn't have enough cards it breaks the game, and has the special ending
        if len(self.Players[0]) <= 5 or len(self.Players[1]) <= 5:
            if len(self.Players[0]) < 5:
                print("Oops, Player 1 doesn't have enough cards, Player 2 wins!")
            else:
                print("Oops, Player 2 doesn't have enough cards, Player 1 wins!")
            self.keepgoing = False

        # If war is possible
        else:
            # Clearing the list from a previous war and adding the current moves to the winnable cards
            self.warCards.clear()
            self.wonCards.extend(self.playerMoves)

            self.warCards = [item[0:4] for item in self.Players]  # Getting the cards used in the war from the players
            self.flipper = [item[3] for item in self.warCards]  # Getting the card that determines the winner
            for i in range(0, 4):  # Removing the war cards from the deck
                self.Players[0].pop(i)
                self.Players[1].pop(i)

            # Telling what the deciding card was
            print(f"Player 1 flipped: {self.flipper[0]}")
            print(f"Player 2 flipped: {self.flipper[1]}")

            winner = self.checkwarwin()  # Finding the winner
            # Adding the war cards to the winnable cards list
            self.wonCards.extend(self.warCards[0])
            self.wonCards.extend(self.warCards[1])

            # Deciding winner
            if winner == "GoToWar":
                print("There's another layer of war!")
                self.gotowar()  # Recursion if needed, with the winnable cards still available

            elif winner == 0:
                print("Player 1 won this war")
                self.Players[0].extend(self.wonCards)  # Adding the won cards to the players stack
                self.wonCards.clear()  # Clearing the list for future war's
            elif winner == 1:
                print("Player 2 won this war")
                self.Players[1].extend(self.wonCards)  # Adding the won cards to the players stack
                self.wonCards.clear()  # Clearing the list for future war's

        print("\n ")

