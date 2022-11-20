from tkinter import * #still unsure about tkinter but sticking with it for now (https://github.com/TomSchimansky/CustomTkinter looks cool)
#example
def add_button():
    Button(root, text='New Button', command=add_button).pack()
#refractor this eventually into its own file or even module
def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start) #Button 1 is the edge of the widget(?)
    widget.bind("<B1-Motion>", on_drag_motion)
    widget.bind("<ButtonRelease-1>", on_drag_stop)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

def on_drag_stop(event):
    widget = event.widget
    if not draggable_place(widget, 50, 10, 300, 100):#maybe checking for another third widget with is mouse inside more adaptable
        #widget.place(x=widget._drag_start_x, y=widget._drag_start_y)
        widget.place(x=10, y=10)#needs to be relative to on_drag_start location
    else:
        widget.place(x=50, y=10)

def draggable_place(widget, pX, pY, bufferX, bufferY):#probably in a for loop iterating over all possible locations
    if (pX < widget.winfo_x() < pX+bufferX) and (pY < widget.winfo_y() < pY+bufferY):
        return True
    return False

#TODO: highlighting dragable places when hovering over them with a dragable

root = Tk()
frame = Frame(root, bd=30, bg="#717378")
frame.place(x=10, y=10)
make_draggable(frame)

notes = Label(frame)
notes.pack()

mainloop()