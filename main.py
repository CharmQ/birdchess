from tkinter import *
import GameEngine


window = Tk()
window.geometry("720x720")
window.title("Chess")
window.resizable(False, False)


Game = GameEngine.GameEngine(window)
Game.run()