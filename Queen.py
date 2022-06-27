from Piece import Piece
from Rook import Rook
from Bishop import Bishop


class Queen(Piece):

    def __init__(self, isBlack, drawID = None, space=None):

        Piece.__init__(self, isBlack, drawID, space)
        self.name = "Queen"
        if isBlack:
            self.code = int("265B", 16)
        else:
            self.code = int("2655", 16)

        self.rook= Rook(isBlack=isBlack, space=space)
        self.bishop = Bishop(isBlack=isBlack, space=space)

    def setSpace(self, space):
        super().setSpace(space)
        self.rook.setSpace(space)
        self.bishop.setSpace(space)

    def setTeam(self, team):
        super().setTeam(team)
        self.rook.setTeam(team)
        self.bishop.setTeam(team)

    def move(self, targetSpace, canvas, boardFlipped):
        super().move(targetSpace, canvas, boardFlipped)
        self.rook.setSpace(targetSpace)
        self.bishop.setSpace(targetSpace)

    def computeStandardMoves(self):
        self.rook.computeStandardMoves()
        self.bishop.computeStandardMoves()
        self.std_moves[0] = self.rook.getStdMoves()[0] + self.bishop.getStdMoves()[0]
        self.std_moves[1] = self.rook.getStdMoves()[1] + self.bishop.getStdMoves()[1]
        pass

