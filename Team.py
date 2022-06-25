from King import King

class Team:

    def __init__(self, name):
        self.name = name
        self.pieces = []
        self.controlledSquares = set()
        self.totLegalMoves = [] 
        self.checkingPieces = []
        self.checkingLine = []
        self.king = None
        self.oppTeam = None

    def getPieces(self):
        return self.pieces
    
    def getName(self):
        return self.name
    
    def getControlledSquares(self):
        return self.controlledSquares

    def clearControlledSquares(self):
        self.controlledSquares = set()

    def getCheckingPieces(self):
        return self.checkingPieces
    
    def clearCheckingPieces(self):
        self.checkingPieces = []
    
    def addCheckingPiece(self, piece):
        self.checkingPieces.append(piece)

    def getCheckingLine(self):
        return self.checkingLine

    def clearCheckingLine(self):
        self.checkingLine = []
    
    def setCheckingLine(self, line):
        self.checkingLine = line

    def addPiece(self, piece):
        self.pieces.append(piece)
        if isinstance(piece, King):
            self.king = piece

    def deletePiece(self, piece):
        self.pieces.remove(piece)

    def getKing(self):
        return self.king

    def getOppTeam(self):
        return self.oppTeam

    def setOppTeam(self, oppTeam):
        self.oppTeam = oppTeam

    def computeControlledSquares(self):
        for piece in self.pieces:
            piece.computeStandardMoves()
            for space in piece.getStdMoves()[0]:
                self.controlledSquares.add(space)

    def totalLegalMoves(self):
        for piece in self.pieces:
            for space in piece.legalMoves():
                self.totLegalMoves.append((piece,space))
    
    def printLegalMoves(self):
        for move in self.totLegalMoves:
            print(move[0].getName(), move[1].getID())
    
    def getTotalLegalMoves(self):
        return self.totLegalMoves

    def clearTotalLegalMoves(self):
        self.totLegalMoves = []
    
    def resetPins(self):
        for piece in self.pieces:
            piece.unPin()

    def reset(self):
        self.clearCheckingLine()
        self.clearCheckingPieces()
        self.clearControlledSquares()
        self.clearTotalLegalMoves()
        self.resetPins()
