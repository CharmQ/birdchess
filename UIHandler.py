class UIHandler:
    def __init__(self, canvas, board):
        self.canvas = canvas
        self.board = board
        self.canvas.bind('<Button-1>', lambda event: self.start_move(event))


    def start_move(self, event):
        x = event.x
        y = event.y
        index = x // 90 + 8 * (y // 90)
        if not self.board.getSpaces()[index].getPiece():
            return
        self.canvas.tag_raise(self.board.getSpaces()[index].getPiece().getDrawID())
        self.canvas.bind('<B1-Motion>', lambda event: self.update(event, self.board.getSpaces()[index].getPiece().getDrawID()))
        self.canvas.bind('<ButtonRelease-1>', lambda event: self.end_move(event, self.board.getSpaces()[index].getPiece().getDrawID(), index))

    def update(self, event, id):
        self.canvas.coords(id, event.x, event.y)

    def cancel_move(self, id, prev_ind):
        self.canvas.coords(id, (prev_ind % 8)*90 + 45, (prev_ind // 8)*90 + 45)
        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')


    def end_move(self, event, id, prev_ind):
        x = event.x
        y = event.y
        index = x // 90 + 8 * (y // 90)
        if prev_ind == index:
            self.cancel_move(id, prev_ind)
            return
        spaces = self.board.getSpaces()
        if spaces[index].getPiece():
            spaces[index].getPiece().delete(self.canvas)
        spaces[index].setPiece(spaces[prev_ind].getPiece())
        spaces[index].getPiece().setSpace(spaces[index])
        spaces[prev_ind].setPiece(None)
        self.canvas.coords(id, (event.x // 90)*90 + 45, (event.y // 90)*90 + 45)
        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')
