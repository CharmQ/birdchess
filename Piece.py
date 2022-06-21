from abc import ABC
from abc import abstractmethod
from Space import Space


class Piece(ABC):

    def __init__(self, isBlack, drawID = None, space=None):
        self.isBlack = isBlack
        self.space = space
        self.moves = []
        self.drawID = drawID
        self.code = ""

    def checkIsBlack(self):
        return self.isBlack

    def getSpace(self):
        return self.space

    def getMoves(self):
        return self.moves

    def getCode(self):
        return self.code

    def setSpace(self, space):
        self.space = space

    def getDrawID(self):
        return self.drawID

    def setDrawID(self, id):
        self.drawID = id

    def delete(self, canvas):
        self.getSpace().setPiece(None)
        canvas.delete(self.getDrawID())
    
    def isMoveLegal(self, targetSpace):
        return True
        #return targetSpace in self.legalMoves()

    @abstractmethod
    def legalMoves(self):
        pass
    
    @abstractmethod
    def standardMoves(self):
        pass