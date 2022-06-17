class UIHandler:
    def __init__(self, canvas, board):
        self.canvas = canvas
        self.board = board
        self.canvas.bind('<Button-1>', lambda event: self.start_move(event))


    def start_move(self, event):
        x = event.x
        y = event.y
        if not self.board.getSpaces()[x // 90][y // 90].getPiece():
            return
        self.canvas.tag_raise(self.board.getSpaces()[x // 90][y // 90].getPiece().getDrawID())
        self.canvas.bind('<B1-Motion>', lambda event: self.update(event, self.board.getSpaces()[x // 90][y // 90].getPiece().getDrawID()))
        self.canvas.bind('<ButtonRelease-1>', lambda event: self.end_move(event, self.board.getSpaces()[x // 90][y // 90].getPiece().getDrawID(), (x // 90, y // 90)))

    def update(self, event, id):
        self.canvas.coords(id, event.x, event.y)

    def cancel_move(self, id, prev_ind):
        self.canvas.coords(id, (prev_ind[0])*90 + 45, (prev_ind[1])*90 + 45)
        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')


    def end_move(self, event, id, prev_ind):
        x = event.x
        y = event.y
        index = (x//90, y//90)
        if prev_ind == index:
            self.cancel_move(id, prev_ind)
            return
        spaces = self.board.getSpaces()
        if spaces[index[0]][index[1]].getPiece():
            spaces[index[0]][index[1]].getPiece().delete(self.canvas)
        spaces[index[0]][index[1]].setPiece(spaces[prev_ind[0]][prev_ind[1]].getPiece())
        spaces[index[0]][index[1]].getPiece().setSpace(spaces[index[0]][index[1]])
        spaces[prev_ind[0]][prev_ind[1]].setPiece(None)
        self.canvas.coords(id, (event.x // 90)*90 + 45, (event.y // 90)*90 + 45)
        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')
