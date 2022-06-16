from Piece import Piece


class Pawn(Piece):

    def __init__(self, isBlack, drawID = None, space=None):
        Piece.__init__(self, isBlack, drawID, space)
        if isBlack:
            self.code = int("265F", 16)
        else:
            self.code = int("2659", 16)