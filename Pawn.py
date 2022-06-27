from http.client import OK
from Piece import Piece
from King import King
from Queen import Queen
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from tkinter import *


class Pawn(Piece):

    def __init__(self, isBlack, drawID = None, space=None):
        self.var = IntVar()
        self.var.set(1)
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

        try:

            if not(board[loc[0]+direction][loc[1]].getPiece()):
                self.std_moves[1].append(board[loc[0]+direction][loc[1]])

                if self.moveCounter == 0 and not(board[loc[0]+direction+direction][loc[1]].getPiece()):
                    self.std_moves[1].append(board[loc[0]+direction+direction][loc[1]])

        except IndexError:
            pass
        
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

    def move(self, targetSpace, canvas, boardFlipped):
        super().move(targetSpace, canvas, boardFlipped)
        if self.checkIsBlack() and self.getSpace().getLoc()[0] == 7 or not(self.checkIsBlack()) and self.getSpace().getLoc()[0] == 0:
            self.promote()

    def promote(self):
        sel_wind = Toplevel(self.getTeam().getGameEng().getWindow())
        sel_wind.geometry("250x130+575+333")
        #sel_wind.protocol("WM_DELETE_WINDOW", lambda: None)
        sel_wind.grab_set()
        r1 = Radiobutton(sel_wind, text="Queen", variable=self.var, value=1)
        r2 = Radiobutton(sel_wind, text="Bishop", variable=self.var, value=2)
        r3 = Radiobutton(sel_wind, text="Knight", variable=self.var, value=3)
        r4 = Radiobutton(sel_wind, text="Rook", variable=self.var, value=4)
        call_back = lambda window:self.replacePiece(window)
        okButton = Button(sel_wind, text="OK", command=lambda: call_back(sel_wind))
        r1.pack(side="top")
        r2.pack(side="top")
        r3.pack(side="top")
        r4.pack(side="top")
        okButton.pack(side="top")

    def replacePiece(self, window):
        if self.var.get() == 1:
            piece = Queen(self.checkIsBlack())
        elif  self.var.get() == 2:
            piece = Bishop(self.checkIsBlack())
        elif  self.var.get() == 3:
            piece = Knight(self.checkIsBlack())
        elif  self.var.get() == 4:
            piece = Rook(self.checkIsBlack())

        piece.setSpace(self.space)
        self.space.setPiece(piece)
        self.team.deletePiece(self)
        self.team.addPiece(piece)
        piece.setTeam(self.team)
        self.getTeam().getGameEng().printBoard()
        window.destroy()


