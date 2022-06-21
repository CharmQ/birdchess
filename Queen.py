from Piece import Piece


class Queen(Piece):

    def __init__(self, isBlack, drawID = None, space=None):
        Piece.__init__(self, isBlack, drawID, space)
        if isBlack:
            self.code = int("265B", 16)
        else:
            self.code = int("2655", 16)

    def legalMoves():
        pass

    def standardMoves(self):
        pass