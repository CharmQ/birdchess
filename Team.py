from King import King

class Team:

    def __init__(self, pieces = []):
        self.pieces = pieces
        self.controlledSquares = {}
        self.checkingPieces = []
        self.checkingLine = []
        self.King = None

    def getPieces(self):
        return self.pieces
    
    def getControlledSquares(self):
        return self.controlledSquares
    
    def getCheckingPieces(self):
        return self.checkingPieces
    
    def getCheckingLine(self):
        return self.checkingLine
    
    def computeControlledSquares(self):
        pass

    def addPiece(self, piece):
        self.pieces.append(piece)
        if isinstance(piece, King):
            self.King = piece


    def deletePiece(self, piece):
        self.pieces.remove(piece)

    def getKing(self):
        return self.King