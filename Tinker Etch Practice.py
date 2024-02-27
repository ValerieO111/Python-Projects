# myEtchASketch application from Coding Club: Python Basics
from tkinter import *

##### Set variables:
canvas_height = 1000
canvas_width = 1000
canvas_colour = "red"

##### main:
window = Tk()
window.title("Val'sEtchASketch")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width,highlightthickness=0)
canvas.pack()

p1_x = canvas_width / 2
p1_y = canvas_height
p1_colour = "black"
line_width = 15
line_length = 15

##### Functions:
# player controls
def p1_move_N():
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, (p1_y-line_length), width=line_width, fill=p1_colour)
    p1_y = p1_y - line_length

def p1_move_S():
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, p1_y+line_length, width=line_width, fill=p1_colour)
    p1_y = p1_y + line_length

def p1_move_E():
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x + line_length, p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_y + line_length

def p1_move_W():
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x - line_length, p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x - line_length

def erase_all():
    canvas.delete(ALL)

# bind movement to key presses
window.bind("<Up>", lambda event: p1_move_N())
window.bind("<Down>", lambda event: p1_move_S())
window.bind("<Left>", lambda event:p1_move_W())
window.bind("<Right>", lambda event:p1_move_E())
window.bind("u",lambda event: erase_all())
window.mainloop()
