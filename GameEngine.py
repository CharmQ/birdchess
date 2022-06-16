from tkinter import *
from UIHandler import UIHandler
from ChessBoard import ChessBoard


class GameEngine:
    def __init__(self, window):
        self.window = window
        self.canvas = Canvas(window, bg="white", width=self.window.winfo_screenwidth(), height=self.window.winfo_screenheight())
        self.canvas.pack()
        self.Board = ChessBoard.FEN_BoardGenerator("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
        self.printBoard()
        self.UIHandler = UIHandler(self.canvas, self.Board)

    def run(self):
        self.window.mainloop()


    def printBoard(self):

        spaces = self.Board.getSpaces()

        for i in range(len(spaces)):

            xtopleft = (i * (90) % 720)
            yTopLeft = ((i * 90)//720) * 90

            if spaces[i].checkIfDark():
                color = "green"
            else:
                color = "white"

            self.canvas.create_rectangle(xtopleft, yTopLeft, xtopleft+90, yTopLeft+90, fill=color)
            if spaces[i].getPiece():
                spaces[i].getPiece().setDrawID(self.canvas.create_text(xtopleft + 45, yTopLeft + 45, font=("Arial", 66), text=chr(spaces[i].getPiece().getCode())))






