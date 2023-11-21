import tkinter as tk
import Grid as Grid

def show_box():
    grid_instance.Grid().printStr()
    canvas.create_rectangle(50, 50, 200, 200, fill="blue")

window  = tk.Tk()
window.title('Box Demo')

canvas = tk.Canvas(window, width = 500, height = 500)
canvas.pack()

grid_instance = Grid()

show_box()

window.mainloop()