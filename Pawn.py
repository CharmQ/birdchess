from Piece import Piece
from King import King


class Pawn(Piece):

    def __init__(self, isBlack, drawID = None, space=None):
        Piece.__init__(self, isBlack, drawID, space)
        self.name = "Pawn"
        if isBlack:
            self.code = int("265F", 16)
        else:
            self.code = int("2659", 16)

    def computeStandardMoves(self):

        self.std_moves = [[],[]]
        board = self.space.getBoard().getSpaces()
        loc = self.space.getLoc()

        direction = -1
        if self.checkIsBlack():
            direction = 1

        if not(board[loc[0]+direction][loc[1]].getPiece()):
            self.std_moves[1].append(board[loc[0]+direction][loc[1]])

            if self.moveCounter == 0 and not(board[loc[0]+direction+direction][loc[1]].getPiece()):
                self.std_moves[1].append(board[loc[0]+direction+direction][loc[1]])

        try:
            temp = board[loc[0]+direction][loc[1]-1]
            self.std_moves[0].append(temp)
            if isinstance(temp.getPiece(), King) and self.canMoveTo(temp):
                self.team.setCheckingLine([self.space])
                self.team.addCheckingPiece(self)
            if temp.getPiece() and self.canMoveTo(temp):
                self.std_moves[1].append(temp)

        except IndexError:
            pass
        
        try:
            temp = board[loc[0]+direction][loc[1]+1]
            self.std_moves[0].append(temp)
            if isinstance(temp.getPiece(), King) and self.canMoveTo(temp):
                self.team.setCheckingLine([self.space])
                self.team.addCheckingPiece(self)
            if temp.getPiece() and self.canMoveTo(temp):
                self.std_moves[1].append(temp)

        except IndexError:
            pass