from abc import ABC
from abc import abstractmethod
from Space import Space


class Piece(ABC):

    def __init__(self, isBlack, drawID = None, space=None):
        self.isBlack = isBlack
        self.space = space
        self.std_moves = [[],[]] #First index contains list if all controlled squares, second contains list of all space piece can move to
        self.drawID = drawID
        self.code = ""
        self.team = None
        self.name = ""
        self.pinningLine = []
        self.pinnedPieces = []
        self.moveCounter = 0

    def checkIsBlack(self):
        return self.isBlack

    def getSpace(self):
        return self.space

    def getStdMoves(self):
        return self.std_moves

    def getCode(self):
        return self.code

    def getName(self):
        return self.name

    def setSpace(self, space):
        self.space = space

    def getDrawID(self):
        return self.drawID

    def setDrawID(self, id):
        self.drawID = id

    def delete(self, canvas):
        self.getSpace().setPiece(None)
        canvas.delete(self.getDrawID())
        self.team.deletePiece(self)
    
    def isMoveLegal(self, targetSpace):
        return targetSpace in self.legalMoves()

    def getTeam(self):
        return self.team

    def setTeam(self, team):
        self.team = team

    def sameColorAs(self, piece):
        return piece.checkIsBlack() == self.isBlack

    def setPin(self, pinLine):
        self.pinningLine = pinLine
    
    def unPin(self):
        self.pinningLine = []

    def canMoveTo(self, space):
        if not(space.getPiece()):
            return True
        if not(space.getPiece().checkIsBlack() == self.isBlack):
            return True
        return False

    def move(self, targetSpace, canvas):

        if targetSpace.getPiece():
            targetSpace.getPiece().delete(canvas)
        self.space.setPiece(None)
        self.space = targetSpace 
        self.space.setPiece(self)
        canvas.coords(self.getDrawID(), self.getSpace().getLoc()[1]*90 + 45, self.getSpace().getLoc()[0]*90 + 45)
        canvas.tag_raise(self.getDrawID())
        self.moveCounter += 1

    def legalMoves(self):
        if len(self.team.getOppTeam().getCheckingPieces()) >= 2:
            return []
        moves = self.std_moves[1].copy()
        temp = []
        if len(self.pinningLine):
            for space in moves:
                if space in self.pinningLine:
                    temp.append(space)  
            moves = temp
        if len(self.team.getOppTeam().getCheckingPieces()) == 1:
            chk_line = self.team.getOppTeam().getCheckingLine()
            temp = []
            for space in moves:
                if space in chk_line:
                    temp.append(space)
            moves = temp
        return moves

    def getMoveCounter(self):
        return self.moveCounter
    
    @abstractmethod
    def computeStandardMoves(self):
        pass