from tkinter import *
import GameEngine


window = Tk()
window.geometry("1080x720")
window.title("Chess")
window.resizable(False, False)


Game = GameEngine.GameEngine(window)
Game.run()