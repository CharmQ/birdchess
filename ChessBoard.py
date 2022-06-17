from Space import Space
from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from King import King
from Queen import Queen


class ChessBoard:
    def __init__(self, pieces=[None]*64):
        spaces = [[0]*8 for i in range(8)]
        temp = None
        temp_num = 0
        for i in range(0, 8):
            for j in range(0, 8):
                temp = Space((i + j) % 2 == 0, chr(ord('a') + j) + str(i), (i, j), pieces[i + j*8], self)
                spaces[i][j] = temp

        self.spaces = spaces

    def getSpaces(self):
        return self.spaces

    @classmethod
    def FEN_BoardGenerator(cls, FENString):

        FENString = FENString.replace("/", "")
        pieces=[None]*64
        index = 0
        for chara in FENString:
            if chara.isdigit():
                for i in range(int(chara) - 1):
                    index += 1
            elif chara == "p":
                pieces[index] = Pawn(True)
            elif chara == "P":
                pieces[index] = Pawn(False)

            elif chara == "b":
                pieces[index] = Bishop(True)
            elif chara == "B":
                pieces[index] = Bishop(False)

            elif chara == "n":
                pieces[index] = Knight(True)
            elif chara == "N":
                pieces[index] = Knight(False)

            elif chara == "r":
                pieces[index] = Rook(True)
            elif chara == "R":
                pieces[index] = Rook(False)

            elif chara == "k":
                pieces[index] = King(True)
            elif chara == "K":
                pieces[index] = King(False)

            elif chara == "q":
                pieces[index] = Queen(True)
            elif chara == "Q":
                pieces[index] = Queen(False)
            index += 1

        return ChessBoard(pieces)

