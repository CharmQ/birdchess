from Piece import Piece
from King import King


class Knight(Piece):

    def __init__(self, isBlack, drawID = None, space=None):
        Piece.__init__(self, isBlack, drawID, space)
        self.name = "Knight"
        if isBlack:
            self.code = int("265E", 16)
        else:
            self.code = int("2658", 16)

    def computeStandardMoves(self):

        self.std_moves = [[],[]]
        board = self.space.getBoard().getSpaces()
        loc = self.space.getLoc()

        for i in [-1, -2, 1, 2]:
            j = 3 - abs(i)
            try:
                if loc[0]+i < 0 or loc[1]+j < 0:
                    raise IndexError
                self.std_moves[0].append(board[loc[0]+i][loc[1]+j])
                if isinstance(board[loc[0]+i][loc[1]+j].getPiece(), King) and self.canMoveTo(board[loc[0]+i][loc[1]+j]):
                    self.team.setCheckingLine([self.space])
                    self.team.addCheckingPiece(self)
                if self.canMoveTo(board[loc[0]+i][loc[1]+j]):
                    self.std_moves[1].append(board[loc[0]+i][loc[1]+j])
            except IndexError:
                pass

            try:
                if loc[0]+i < 0 or loc[1]-j < 0:
                    raise IndexError
                self.std_moves[0].append(board[loc[0]+i][loc[1]-j])
                if isinstance(board[loc[0]+i][loc[1]-j].getPiece(), King) and self.canMoveTo(board[loc[0]+i][loc[1]-j]):
                    self.team.setCheckingLine([self.space])
                    self.team.addCheckingPiece(self)
                if self.canMoveTo(board[loc[0]+i][loc[1]-j]):
                    self.std_moves[1].append(board[loc[0]+i][loc[1]-j])
            except IndexError:
                pass


