class UIHandler:
    def __init__(self, canvas, board, gameEng):
        self.canvas = canvas
        self.board = board
        self.canvas.bind('<Button-1>', lambda event: self.start_move(event))
        self.gameEng = gameEng

    def start_move(self, event):
        x = event.x
        y = event.y
        if not self.board.getSpaces()[y // 90][x // 90].getPiece():
            return
        self.canvas.tag_raise(self.board.getSpaces()[y // 90][x // 90].getPiece().getDrawID())
        self.canvas.bind('<B1-Motion>', lambda event: self.update(event, self.board.getSpaces()[y // 90][x // 90].getPiece().getDrawID()))
        self.canvas.bind('<ButtonRelease-1>', lambda event: self.end_move(event, self.board.getSpaces()[y // 90][x // 90].getPiece().getDrawID(), (y // 90, x // 90)))

    def update(self, event, id):
        self.canvas.coords(id, event.x, event.y)

    def cancel_move(self, id, prev_ind):
        self.canvas.coords(id, (prev_ind[1])*90 + 45, (prev_ind[0])*90 + 45)
        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')


    def end_move(self, event, id, prev_ind):
        x = event.x
        y = event.y
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

        prev_space.getPiece().move(space, self.canvas)
        #self.canvas.coords(id, (event.x // 90)*90 + 45, (event.y // 90)*90 + 45)
        self.gameEng.turnEnd()
        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')
