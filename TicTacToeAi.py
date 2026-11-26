import random

# I have removed the docstring format comming from docstring extension


class DumbAi:
    """
    This is the heart of the program
    Contains the basic working of tic tac toe computer


    Contains two AI. One is totally dumb and other is slithly smarter
    """

    def GetAvailableValues(self, board: list) -> list:
        """The function returns the sorted list of all the available move to make"""

        sortedBoard: list[int] = []

        for items in board:
            if items == "X" or items == "O":
                continue
            sortedBoard.append(items)

        return sortedBoard

    def GetPlayerValues(
        self, playerNumber: int, playerType: str, board: list, win: int
    ) -> list:
        """update the count of matching marks
        The functions simply looks at one cell of a line. If a cell has the same mark of one that is tracked then the count will increase by one. If not then it will reset
        """

        if board[win] == "X" or board[win] == "O":

            if playerNumber == 0:
                playerType = board[win]

            if board[win] == playerType:
                playerNumber += 1
            else:
                playerNumber = 0
                playerType = ""

        return [playerNumber, playerType]

    # This is one of the most important function for the smart AI
    def ExtractSignificantList(self, winning: list, board: list) -> list:
        """
        This function extract the most important numbers to get it's move
        """

        significantListOfValues: list = []

        for wins in winning:

            playerType = ""
            playerNumber = 0

            for win in wins:

                players = self.GetPlayerValues(
                    playerNumber=playerNumber,
                    playerType=playerType,
                    board=board,
                    win=win,
                )
                playerType = players[1]
                playerNumber = players[0]

            significantListOfValues.append([playerNumber, playerType, wins])

        return significantListOfValues

    def GetBestSignificant(self, significantList: list) -> int:
        """Choose the most userful winning for the smart computer
        this function works on that if the marks count of one line is the highest then it will pick that one
        """

        highestPlayerNumber = 0
        highestPlayerType = ""
        specials: list = [0, 2, 4, 6, 8]
        bestlist = [specials]

        for i in significantList:

            if highestPlayerNumber < i[0]:
                highestPlayerNumber = i[0]
                highestPlayerType = i[1]
                bestlist[0] = i[-1]

            if highestPlayerNumber == i[0] and highestPlayerType != i[1]:

                if i[1] == "O":
                    highestPlayerType = i[1]
                    bestlist[0] = i[-1]

        if highestPlayerNumber < 2:
            bestlist[0] = specials

        return bestlist

    def GetNotDumbComputerNumber(self, availableTries: list[int], bestlist: list[int], corner: bool = False):
        """Picks the best move from the bestlist"""

        bestlistssingular: list[int] = bestlist[0]

        probableValues: list[int] = []

        for values in availableTries:
            values -= 1

            if values in bestlistssingular:
                probableValues.append(values)

        if not corner:
            if len(probableValues) == 5:
                return 4

            if len(probableValues) == 4 and 4 in probableValues:
                return 4
        print(probableValues, availableTries[0] - 1)
        if len(probableValues) == 0:
            return availableTries[0] - 1
        return random.choice(probableValues)

    def LittleDumbAi(self, board: list[int]) -> int:
        """Gets a completelly random move"""

        computerChoices: list[int] = self.GetAvailableValues(board=board)
        computer: int = self.GetRandomComputerChoice(computerChoices)
        return computer

    def NotSoDumbAi(self, corner: bool = False) -> int:
        """returns the move of smart ai"""

        availableTries: list[int] = self.GetAvailableValues(board=self.board)
        bestList: list[int] = self.GetBestSignificant(
            self.ExtractSignificantList(self.wins, self.board)
        )
        computer: int = self.GetNotDumbComputerNumber(availableTries, bestList, corner)
    
        return computer

    def GetRandomComputerChoice(self, sortedBoard: list) -> int:
        computerChoice = random.choice(sortedBoard)
        
        return computerChoice - 1
