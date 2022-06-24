from Piece import Piece
from King import King


class Rook(Piece):

    def __init__(self, isBlack, drawID = None, space=None):
        Piece.__init__(self, isBlack, drawID, space)
        self.name = "Rook"
        if isBlack:
            self.code = int("265C", 16)
        else:
            self.code = int("2656", 16)

    def computeStandardMoves(self):
        self.std_moves = [[],[]]
        board = self.space.getBoard().getSpaces()
        loc = self.space.getLoc()
        pathIsFinished = False
        distance = 1


        dir = [-1, 0, 1, 0, 0, -1, 0, 1]

        for i in range(4):

            temp = []
            temp.append(self.space)
            pathIsFinished = False
            KingEncountered = False
            distance = 1
            potPinnedPiece = None

            while not pathIsFinished:
                try:
                    if loc[0]+(dir[i*2])*distance < 0 or loc[1]+(dir[i*2+1])*distance < 0:
                        raise IndexError
                    self.std_moves[0].append(board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance])
                    temp.append(board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance])
                    if self.canMoveTo(board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance]):
                        self.std_moves[1].append(board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance])

                    if board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance].getPiece():
                        if isinstance(board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance].getPiece(), King) and self.canMoveTo(board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance]):
                            self.team.setCheckingLine(temp)
                            self.team.addCheckingPiece(self)
                            KingEncountered = True
                            break
                        if not(board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance].getPiece().checkIsBlack() == self.isBlack):
                            potPinnedPiece = board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance].getPiece()
                        pathIsFinished = True
                    distance += 1
            
                except IndexError:
                    break

            while not(KingEncountered) and potPinnedPiece:
                try:   
                    if loc[0]+dir[i*2]*distance < 0 or loc[1]+dir[i*2+1]*distance < 0:
                        raise IndexError
                    if board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance].getPiece():
                        if isinstance(board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance].getPiece(), King) and self.canMoveTo(board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance]):
                            potPinnedPiece.setPin(temp)
                            break
                        else:
                            break
                    else:
                        temp.append(board[loc[0]+(dir[i*2])*distance][loc[1]+(dir[i*2+1])*distance])
                        distance += 1
                    
                except IndexError:
                    break
                