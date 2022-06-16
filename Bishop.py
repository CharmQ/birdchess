from Piece import Piece


class Bishop(Piece):

    def __init__(self, isBlack, drawID = None, space=None):
        Piece.__init__(self, isBlack, drawID, space)
        if isBlack:
            self.code = int("265D", 16)
        else:
            self.code = int("2657", 16)