from Piece import Piece


class King(Piece):

    def __init__(self, isBlack, drawID = None, space=None):
        Piece.__init__(self, isBlack, drawID, space)
        self.name = "King"
        if isBlack:
            self.code = int("265A", 16)
        else:
            self.code = int("2654", 16)

    def move(self, targetSpace, canvas, boardFlipped):
        board = self.space.getBoard().getSpaces()
        prev_space_loc = self.space.getLoc()
        super().move(targetSpace, canvas, boardFlipped)

        if abs(self.space.getLoc()[1] - prev_space_loc[1]) == 2:
            if self.space.getLoc() == (7,6):
                board[7][7].getPiece().move(board[7][5], canvas)
            elif self.space.getLoc() == (7,2):
                print(board[7][0].getPiece())
                board[7][0].getPiece().move(board[7][3], canvas)
            elif self.space.getLoc() == (0,6):
                board[0][7].getPiece().move(board[0][5], canvas)
            else:
                board[0][0].getPiece().move(board[0][3], canvas)
                pass


    def legalMoves(self):
        board = self.space.getBoard().getSpaces()
        controlledSquares = self.getTeam().getOppTeam().getControlledSquares()
        loc = self.getSpace().getLoc()
        inc = 1
        moves = []
        for space in self.std_moves[1]:
            if not(space in controlledSquares):
                moves.append(space)

        if not(self.isInCheck()):
            if self.getMoveCounter() == 0:
                while loc[1] + inc >= 0 and loc[1] + inc <= 7:
                    if board[loc[0]][loc[1] + inc].getPiece() and not (board[loc[0]][loc[1] + inc].getPiece().getName() == "Rook"):
                        break
                    elif board[loc[0]][loc[1] + inc] in controlledSquares:
                        break
                    elif board[loc[0]][loc[1] + inc].getPiece() and board[loc[0]][loc[1] + inc].getPiece().getName() == "Rook":
                        if board[loc[0]][loc[1] + inc].getPiece().getMoveCounter() == 0:
                            moves.append(board[loc[0]][loc[1] + 2])
                    else:
                        pass
                    inc+=1


                inc = 1
                while loc[1] - inc >= 0 and loc[1] - inc <= 7:
                    if board[loc[0]][loc[1] - inc].getPiece() and not (board[loc[0]][loc[1] - inc].getPiece().getName() == "Rook"):
                        break
                    elif board[loc[0]][loc[1] - inc] in controlledSquares:
                        break
                    elif board[loc[0]][loc[1] - inc].getPiece() and board[loc[0]][loc[1] - inc].getPiece().getName() == "Rook":
                        if board[loc[0]][loc[1] - inc].getPiece().getMoveCounter() == 0:
                            moves.append(board[loc[0]][loc[1] - 2])
                    else:
                        pass
                    inc+=1        
            
        return moves

    def isInCheck(self):
        controlledSquares = self.getTeam().getOppTeam().getControlledSquares()
        return self.space in controlledSquares

    def computeStandardMoves(self):
        self.std_moves = [[],[]]
        board = self.space.getBoard().getSpaces()
        loc = self.getSpace().getLoc()
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                try:
                    temp = (loc[0] + i,loc[1] + j)
                    if loc[0] + i < 0 or loc[1] + j < 0:
                        raise IndexError
                    if temp != loc:
                        self.std_moves[0].append(board[temp[0]][temp[1]])
                        if self.canMoveTo(board[temp[0]][temp[1]]):
                            self.std_moves[1].append(board[temp[0]][temp[1]])
                except IndexError:
                    pass
'''
0,0 | 0,1 | 0,2 | 0,3 | 0,4 | 0,5 | 0,6 | 0,7 |
1,0 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5 | 1,6 | 1,7 |
2,0 | 2,1 | 2,2 | 2,3 | 2,4 | 2,5 | 2,6 | 2,7 |
3,0 | 3,1 | 3,2 | 3,3 | 3,4 | 3,5 | 3,6 | 3,7 |
4,0 | 4,1 | 4,2 | 4,3 | 4,4 | 4,5 | 4,6 | 4,7 |
5,0 | 5,1 | 5,2 | 5,3 | 5,4 | 5,5 | 5,6 | 5,7 |
6,0 | 6,1 | 6,2 | 6,3 | 6,4 | 6,5 | 6,6 | 6,7 |
7,0 | 7,1 | 7,2 | 7,3 | 7,4 | 7,5 | 7,6 | 7,7 |
'''