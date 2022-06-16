from Piece import Piece


class Rook(Piece):

    def __init__(self, isBlack, drawID = None, space=None):
        Piece.__init__(self, isBlack, drawID, space)
        if isBlack:
            self.code = int("265C", 16)
        else:
            self.code = int("2656", 16)