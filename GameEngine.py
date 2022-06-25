from tkinter import *
from tkinter import messagebox
from UIHandler import UIHandler
from ChessBoard import ChessBoard
from Team import Team


class GameEngine:
    def __init__(self, window):
        self.window = window
        self.canvas = Canvas(window, bg="white", width=self.window.winfo_screenwidth(), height=self.window.winfo_screenheight())
        self.canvas.pack()
        self.whitePieces = Team("White")
        self.blackPieces = Team("Black")
        self.Board = ChessBoard.FEN_BoardGenerator("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR", self.whitePieces, self.blackPieces)
        self.whitePieces.setOppTeam(self.blackPieces)
        self.blackPieces.setOppTeam(self.whitePieces)
        self.printBoard()
        self.UIHandler = UIHandler(self.canvas, self.Board, self)
        self.isBlackTurn = False
        self.turnToMove = None
        self.opp = None
        self.prev_color = None
        self.inCheck = False
        self.turnSetup()
        

    def run(self):
        self.window.mainloop()

    def turnSetup(self):
        if self.isBlackTurn:
            self.turnToMove = self.blackPieces
            self.opp = self.whitePieces
        else:
            self.turnToMove = self.whitePieces
            self.opp = self.blackPieces

        self.turnToMove.computeControlledSquares()
        self.opp.computeControlledSquares()
        self.inCheck = self.turnToMove.getKing().isInCheck()
        #if self.inCheck:
            #self.canvas.itemconfig(self.turnToMove.getKing().getSpace().getDrawID(), fill = "red")
        self.turnToMove.totalLegalMoves()
        if len(self.turnToMove.getTotalLegalMoves()) == 0:  
            if self.inCheck:
                self.checkMate()
            else:
                self.staleMate()
        self.turnToMove.printLegalMoves()
        print("\n")

    def turnEnd(self):
        #if self.inCheck:
            #self.canvas.itemconfig(self.turnToMove.getKing().getSpace().getDrawID(), fill = self.prev_color)
        self.inCheck=False
        self.toggleTurn()
        self.whitePieces.reset()
        self.blackPieces.reset()
        self.turnSetup()


    def checkMate(self):
        messagebox.showinfo("Checkmate", self.opp.getName() + " has won by checkmate")
        pass

    def staleMate(self):
        messagebox.showinfo("Stalemate", "Draw by stalemate")
        pass

    def getWhitePieces(self):
        return self.whitePieces
    
    def getBlackPieces(self):
        return self.blackPieces

    def toggleTurn(self):
        self.isBlackTurn = not(self.isBlackTurn)

    def moveIsLegal(self, piece, targetSpace):
        if piece.checkIsBlack() == self.isBlackTurn:
            if piece.isMoveLegal(targetSpace):
                return True
        return False

    def printBoard(self):

        spaces = self.Board.getSpaces()

        for i in range(len(spaces)):
            for j in range(len(spaces[0])):

                xtopleft = j * 90
                yTopLeft = i * 90

                if spaces[i][j].checkIfDark():
                    color = "green"
                else:
                    color = "white"

                self.canvas.create_rectangle(xtopleft, yTopLeft, xtopleft+90, yTopLeft+90, fill=color)
                if spaces[i][j].getPiece():
                    spaces[i][j].getPiece().setDrawID(self.canvas.create_text(xtopleft + 45, yTopLeft + 45, font=("Arial", 66), text=chr(spaces[i][j].getPiece().getCode())))






