from Piece import Piece


class King(Piece):

    def __init__(self, isBlack, drawID = None, space=None):
        Piece.__init__(self, isBlack, drawID, space)
        self.name = "King"
        if isBlack:
            self.code = int("265A", 16)
        else:
            self.code = int("2654", 16)

    def legalMoves(self):
        controlledSquares = self.getTeam().getOppTeam().getControlledSquares()
        moves = []
        for space in self.std_moves[1]:
            if not(space in controlledSquares):
                moves.append(space)
        return moves



    def computeStandardMoves(self):
        print('compute')
        board = self.space.getBoard().getSpaces()
        loc = self.getSpace().getLoc()
        function = [-1,0,1]
        for i in range(len(function)):
            for j in range(len(function)):
                try:
                    temp = (loc[0] + function[i],loc[1] + function[j])
                    if loc[0] + function[i] < 0 or loc[1] + function[j]<0:
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