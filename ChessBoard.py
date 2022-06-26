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
        for i in range(0, 8):
            for j in range(0, 8):
                temp = Space((i + j) % 2 == 1, chr(ord('a') + j) + str(8 - i), (i, j), pieces[i*8 + j], self)
                spaces[i][j] = temp
        self.spaces = spaces

    def getSpaces(self):
        return self.spaces

    def computeFENString(self):
        FEN_string = ""
        counter = 0
        for row in self.spaces:
            for space in row:
                piece = space.getPiece()
                if piece:
                    if counter > 0:
                        FEN_string += str(counter)
                        counter = 0

                    if isinstance(piece, Pawn):
                        if piece.checkIsBlack():
                            FEN_string += "p"
                        else:
                            FEN_string += "P"

                    if isinstance(piece, Bishop):
                        if piece.checkIsBlack():
                            FEN_string += "b"
                        else:
                            FEN_string += "B"

                    if isinstance(piece, Knight):
                        if piece.checkIsBlack():
                            FEN_string += "n"
                        else:
                            FEN_string += "N"

                    if isinstance(piece, Rook):
                        if piece.checkIsBlack():
                            FEN_string += "r"
                        else:
                            FEN_string += "R"

                    if isinstance(piece, King):
                        if piece.checkIsBlack():
                            FEN_string += "k"
                        else:
                            FEN_string += "K"

                    if isinstance(piece, Queen):
                        if piece.checkIsBlack():
                            FEN_string += "q"
                        else:
                            FEN_string += "Q"                                               

                else:
                    counter+=1
            if counter > 0:
                FEN_string += str(counter)
                counter = 0
            FEN_string +="/"

        FEN_string = FEN_string[:-1]


        return FEN_string


    @classmethod
    def FEN_BoardGenerator(cls, FENString, whitePieces, blackPieces):
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

            if pieces[index]:
                if pieces[index].checkIsBlack():
                    blackPieces.addPiece(pieces[index])
                    pieces[index].setTeam(blackPieces)
                else:
                    whitePieces.addPiece(pieces[index])
                    pieces[index].setTeam(whitePieces)
            index += 1
        return ChessBoard(pieces)


