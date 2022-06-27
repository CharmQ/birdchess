class UIHandler:
    def __init__(self, canvas, board, gameEng):
        self.canvas = canvas
        self.board = board
        self.canvas.bind('<Button-1>', lambda event: self.start_move(event))
        self.gameEng = gameEng
        self.boardFlipped = False

    def start_move(self, event):
        x = event.x
        y = event.y
        if x <= 0 or x>=720 or y <= 0 or y >= 720: 
            return
        if self.boardFlipped:
            index = ((720-y)//90, (720-x)//90)
        else:  
            index = (y//90, x//90)
        if not self.board.getSpaces()[index[0]][index[1]].getPiece():
            return
        self.canvas.tag_raise(self.board.getSpaces()[index[0]][index[1]].getPiece().getDrawID())
        self.canvas.bind('<B1-Motion>', lambda event: self.update(event, self.board.getSpaces()[index[0]][index[1]].getPiece().getDrawID()))
        self.canvas.bind('<ButtonRelease-1>', lambda event: self.end_move(event, self.board.getSpaces()[index[0]][index[1]].getPiece().getDrawID(), (index[0], index[1])))

    def update(self, event, id):
        self.canvas.coords(id, event.x, event.y)

    def cancel_move(self, id, prev_ind):
        if self.boardFlipped:
            coords = (720-(prev_ind[1]*90) - 45, 720-(prev_ind[0]*90) - 45)
        else:
            coords = ((prev_ind[1])*90 + 45, (prev_ind[0])*90 + 45)
        self.canvas.coords(id, coords[0], coords[1])
        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')


    def end_move(self, event, id, prev_ind):
        x = event.x
        y = event.y
        if self.boardFlipped:
            index = ((720-y)//90, (720-x)//90)
        else:
            index = (y//90, x//90)



        if x <= 0 or x>=720 or y <= 0 or y >= 720: 
            self.cancel_move(id, prev_ind)
            return

        spaces = self.board.getSpaces()
        space = spaces[index[0]][index[1]]
        prev_space = spaces[prev_ind[0]][prev_ind[1]]
        
        if prev_ind == index:
            self.cancel_move(id, prev_ind)
            return
        if not self.gameEng.moveIsLegal(spaces[prev_ind[0]][prev_ind[1]].getPiece(), spaces[index[0]][index[1]]):
            self.cancel_move(id, prev_ind)
            return

        prev_space.getPiece().move(space, self.canvas, self.boardFlipped)
        self.gameEng.turnEnd()
        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')

    def setBoard(self, board):
        self.board = board

    def toggleBoardFlipped(self):
        self.boardFlipped = not(self.boardFlipped)