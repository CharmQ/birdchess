from Piece import Piece


class Knight(Piece):

    def __init__(self, isBlack, drawID = None, space=None):
        Piece.__init__(self, isBlack, drawID, space)
        if isBlack:
            self.code = int("265E", 16)
        else:
            self.code = int("2658", 16)