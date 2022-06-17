class Space:

    def __init__(self, isDark, id, loc, piece, board, drawID=None):
        self.isDark = isDark
        self.id = id
        self.loc = loc
        self.piece = piece
        if self.piece:
            self.piece.setSpace(self)
        self.board = board
        self.drawID = drawID

    def checkIfDark(self):
        return self.isDark

    def getID(self):
        return self.id

    def getLoc(self):
        return self.loc

    def getDrawID(self):
        return self.drawID

    def getPiece(self):
        return self.piece

    def getBoard(self):
        return self.board

    def setPiece(self, piece):
        self.piece = piece

    def setDrawID(self, id):
        self.drawID = id