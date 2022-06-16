from Piece import Piece


class King(Piece):

    def __init__(self, isBlack, drawID = None, space=None):
        Piece.__init__(self, isBlack, drawID, space)
        if isBlack:
            self.code = int("265A", 16)
        else:
            self.code = int("2654", 16)