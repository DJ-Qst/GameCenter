from random import choice


class TicTacToe:
    def __init__(self):
        # Value's sotred in each place of the board, number is equivalent to empty space
        self.places = {"a": 7, "b": 8, "c": 9, "d": 4,
                       "e": 5, "f": 6, "g": 1, "h": 2, "i": 3}
        # The board
        self.tttboard = [f"|{self.places['a']}|{self.places['b']}|{self.places['c']}|", "\n",
                         f"|{self.places['d']}|{self.places['e']}|{self.places['f']}|", "\n",
                         f"|{self.places['g']}|{self.places['h']}|{self.places['i']}|"]

        self.numPlayers = 0
        # Chosen place of Player 1
        self.p1place = 0
        # Chosen place of Player 2 or Computer depending on playmode
        self.p2place = 0
        self.true = True
        self.boardfull = False

    def game(self):
        # Deciding if there is only 1 or 2 players
        while True:
            try:
                self.numPlayers = int(input("How many players are there: "))
                if self.numPlayers != 1 and self.numPlayers != 2:
                    print("I'm sorry, but you may only have one or two players in this game")
                else:
                    break
            except ValueError:
                print("I'm sorry, but that was not an acceptable response")

        # Actual Game
        while self.true:
            # Updates Board every loop
            self.tttboard = [f"|{self.places['a']}|{self.places['b']}|{self.places['c']}|", "\n",
                          f"|{self.places['d']}|{self.places['e']}|{self.places['f']}|", "\n",
                          f"|{self.places['g']}|{self.places['h']}|{self.places['i']}|"]
            print("".join(self.tttboard))

            if self.numPlayers == 1:
                self.oneplayergame()
            elif self.numPlayers == 2:
                self.twoplayergame()

    def oneplayergame(self):
        if not self.boardfull:
            # Getting user place
            while True:
                try:
                    self.p1place = int(input("Where would you like to make your move: "))
                    break
                except ValueError:
                    print("Please use one of the available places, and input the number")

            # Getting computer place
            options = [k for k, v in self.places.items() if v != "X" and v != "O" and v != self.p1place]  # All Options
            corners = [x for x in options if x == "a" or x == "c" or x == "g" or x == "i"]  # All available Corners
            edges = [x for x in options if x == "b" or x == "d" or x == "f" or x == "h"]  # All available Edges

            if "e" in options:
                self.p2place = self.places['e']
            elif corners:
                self.p2place = self.places[choice(corners)]
            elif edges:
                self.p2place = self.places[choice(edges)]

            # Placing the moves
            self.oneplayerplacement()

            # Testing win
            winnerp1 = self.didp1win()
            winnerp2 = self.didp2win()
            if winnerp1 or winnerp2:
                # Printing the winning board
                self.tttboard = [f"|{self.places['a']}|{self.places['b']}|{self.places['c']}|", "\n",
                                 f"|{self.places['d']}|{self.places['e']}|{self.places['f']}|", "\n",
                                 f"|{self.places['g']}|{self.places['h']}|{self.places['i']}|"]
                print("".join(self.tttboard))

                # Telling who won
                if winnerp1:
                    print("Player 1 wins")
                if winnerp2:
                    print("The Computer Won")
                self.true = False
            self.isboardfull()

        if self.boardfull:
            # Printing the winning board
            self.tttboard = [f"|{self.places['a']}|{self.places['b']}|{self.places['c']}|", "\n",
                             f"|{self.places['d']}|{self.places['e']}|{self.places['f']}|", "\n",
                             f"|{self.places['g']}|{self.places['h']}|{self.places['i']}|"]
            print("\n\n" + "".join(self.tttboard))

            print("The board is full, this game is a draw")
            self.true = False

    def twoplayergame(self):
        if not self.boardfull:
            while True:
                # Getting P1 place
                try:
                    self.p1place = int(input("Where would you like to make your move: "))
                    break
                except ValueError:
                    print("Please use one of the available places, and input the number")

            self.p1placement()

            if not self.didp1win():
                while True:
                    # Getting P2 place
                    try:
                        self.p2place = int(input("Where would you like to make your move: "))
                        break
                    except ValueError:
                        print("Please use one of the available places, and input the number")

                self.p2placement()

            else:
                print("Player 1 wins")
                self.true = False

            if self.didp2win():
                print("Player 2 wins")
                self.true = False
            self.isboardfull()

        if self.boardfull:
            # Printing the winning board
            self.tttboard = [f"|{self.places['a']}|{self.places['b']}|{self.places['c']}|", "\n",
                             f"|{self.places['d']}|{self.places['e']}|{self.places['f']}|", "\n",
                             f"|{self.places['g']}|{self.places['h']}|{self.places['i']}|"]
            print("\n\n" + "".join(self.tttboard))

            print("The board is full, this game is a draw")
            self.true = False

    def oneplayerplacement(self):
        # This is an absolute dumpster fire

        for i in range(1):
            # P1 placement, if they input a already taken number, then they lose the turn
            if self.p1place == 7 and self.places['a'] != "X" and self.places['a'] != "O":
                self.places['a'] = "X"
            elif self.p1place == 8 and self.places['b'] != "X" and self.places['b'] != "O":
                self.places['b'] = "X"
            elif self.p1place == 9 and self.places['c'] != "X" and self.places['c'] != "O":
                self.places['c'] = "X"
            elif self.p1place == 4 and self.places['d'] != "X" and self.places['d'] != "O":
                self.places['d'] = "X"
            elif self.p1place == 5 and self.places['e'] != "X" and self.places['e'] != "O":
                self.places['e'] = "X"
            elif self.p1place == 6 and self.places['f'] != "X" and self.places['f'] != "O":
                self.places['f'] = "X"
            elif self.p1place == 1 and self.places['g'] != "X" and self.places['g'] != "O":
                self.places['g'] = "X"
            elif self.p1place == 2 and self.places['h'] != "X" and self.places['h'] != "O":
                self.places['h'] = "X"
            elif self.p1place == 3 and self.places['i'] != "X" and self.places['i'] != "O":
                self.places['i'] = "X"
            else:
                print("Player 1 loses this turn for inputing a taken number")
            if self.didp1win():
                break

            # Computer placement
            if self.p2place == 7 and self.places['a'] != "X" and self.places['a'] != "O":
                self.places['a'] = "O"
            elif self.p2place == 8 and self.places['b'] != "X" and self.places['b'] != "O":
                self.places['b'] = "O"
            elif self.p2place == 9 and self.places['c'] != "X" and self.places['c'] != "O":
                self.places['c'] = "O"
            elif self.p2place == 4 and self.places['d'] != "X" and self.places['d'] != "O":
                self.places['d'] = "O"
            elif self.p2place == 5 and self.places['e'] != "X" and self.places['e'] != "O":
                self.places['e'] = "O"
            elif self.p2place == 6 and self.places['f'] != "X" and self.places['f'] != "O":
                self.places['f'] = "O"
            elif self.p2place == 1 and self.places['g'] != "X" and self.places['g'] != "O":
                self.places['g'] = "O"
            elif self.p2place == 2 and self.places['h'] != "X" and self.places['h'] != "O":
                self.places['h'] = "O"
            elif self.p2place == 3 and self.places['i'] != "X" and self.places['i'] != "O":
                self.places['i'] = "O"
            else:
                print("Player 2 loses this turn for inputing a taken choice")

    def p1placement(self):
        if self.p1place == 7 and self.places['a'] != "X" and self.places['a'] != "O":
            self.places['a'] = "X"
        elif self.p1place == 8 and self.places['b'] != "X" and self.places['b'] != "O":
            self.places['b'] = "X"
        elif self.p1place == 9 and self.places['c'] != "X" and self.places['c'] != "O":
            self.places['c'] = "X"
        elif self.p1place == 4 and self.places['d'] != "X" and self.places['d'] != "O":
            self.places['d'] = "X"
        elif self.p1place == 5 and self.places['e'] != "X" and self.places['e'] != "O":
            self.places['e'] = "X"
        elif self.p1place == 6 and self.places['f'] != "X" and self.places['f'] != "O":
            self.places['f'] = "X"
        elif self.p1place == 1 and self.places['g'] != "X" and self.places['g'] != "O":
            self.places['g'] = "X"
        elif self.p1place == 2 and self.places['h'] != "X" and self.places['h'] != "O":
            self.places['h'] = "X"
        elif self.p1place == 3 and self.places['i'] != "X" and self.places['i'] != "O":
            self.places['i'] = "X"
        else:
            print("Player 1 loses this turn for inputing a taken number")

    def p2placement(self):
        if self.p2place == 7 and self.places['a'] != "X" and self.places['a'] != "O":
            self.places['a'] = "O"
        elif self.p2place == 8 and self.places['b'] != "X" and self.places['b'] != "O":
            self.places['b'] = "O"
        elif self.p2place == 9 and self.places['c'] != "X" and self.places['c'] != "O":
            self.places['c'] = "O"
        elif self.p2place == 4 and self.places['d'] != "X" and self.places['d'] != "O":
            self.places['d'] = "O"
        elif self.p2place == 5 and self.places['e'] != "X" and self.places['e'] != "O":
            self.places['e'] = "O"
        elif self.p2place == 6 and self.places['f'] != "X" and self.places['f'] != "O":
            self.places['f'] = "O"
        elif self.p2place == 1 and self.places['g'] != "X" and self.places['g'] != "O":
            self.places['g'] = "O"
        elif self.p2place == 2 and self.places['h'] != "X" and self.places['h'] != "O":
            self.places['h'] = "O"
        elif self.p2place == 3 and self.places['i'] != "X" and self.places['i'] != "O":
            self.places['i'] = "O"
        else:
            print("Player 2 loses this turn for inputing a taken choice")

    def didp1win(self):
        if self.places['a'] == self.places['e'] == self.places['i'] == "X":
            return True
        if self.places['g'] == self.places['e'] == self.places['c'] == "X":
            return True
        if self.places['b'] == self.places['e'] == self.places['h'] == "X":
            return True
        if self.places['d'] == self.places['e'] == self.places['f'] == "X":
            return True
        if self.places['a'] == self.places['b'] == self.places['c'] == "X":
            return True
        if self.places['c'] == self.places['f'] == self.places['i'] == "X":
            return True
        if self.places['g'] == self.places['h'] == self.places['i'] == "X":
            return True
        if self.places['a'] == self.places['d'] == self.places['g'] == "X":
            return True
        else:
            return False

    def didp2win(self):
        # Computer Testing
        if self.places['a'] == self.places['e'] == self.places['i'] == "O":
            return True
        if self.places['g'] == self.places['e'] == self.places['c'] == "O":
            return True
        if self.places['b'] == self.places['e'] == self.places['h'] == "O":
            return True
        if self.places['d'] == self.places['e'] == self.places['f'] == "O":
            return True
        if self.places['a'] == self.places['b'] == self.places['c'] == "O":
            return True
        if self.places['c'] == self.places['f'] == self.places['i'] == "O":
            return True
        if self.places['g'] == self.places['h'] == self.places['i'] == "O":
            return True
        if self.places['a'] == self.places['d'] == self.places['g'] == "O":
            return True
        else:
            return False

    def isboardfull(self):
        if self.places["a"] != 7 and self.places["b"] != 8 and self.places["c"] != 9:
            if self.places["d"] != 4 and self.places["e"] != 5 and self.places["f"] != 6:
                if self.places["g"] != 1 and self.places["h"] != 2 and self.places["i"] != 3:
                    self.boardfull = True
        else:
            self.boardfull = False

