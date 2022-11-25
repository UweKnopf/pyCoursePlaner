from tkinter import * #still unsure about tkinter but sticking with it for now (https://github.com/TomSchimansky/CustomTkinter looks cool)
#example

draggable_places_list = []
def add_button():
    Button(root, text='New Button', command=add_button).pack()
#refractor this eventually into its own file or even module
def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start) #Button 1 is the edge of the widget(?)
    widget.bind("<B1-Motion>", on_drag_motion)
    widget.bind("<ButtonRelease-1>", on_drag_stop)

def on_drag_start(event):
    widget = event.widget
    #original mouse position
    widget._drag_start_x = event.x 
    widget._drag_start_y = event.y
    #original widget position
    widget._drag_start_x_stand = widget.winfo_x()
    widget._drag_start_y_stand = widget.winfo_y()

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)
    for draggable_widget in draggable_places_list:
        changeOnWidgetHover(widget, draggable_widget, "blue", "white")

def on_drag_stop(event):
    widget = event.widget
    for draggable_widget in draggable_places_list:
        if not draggable_place(widget, draggable_widget):
            widget.place(x=widget._drag_start_x_stand, y=widget._drag_start_y_stand)
        else:
            widget.place(x=draggable_widget.winfo_x(), y=draggable_widget.winfo_y())
            break


def draggable_place(widget, targetwidget):#probably in a for loop iterating over all possible locations
    if (targetwidget.winfo_x() < widget.winfo_x() < targetwidget.winfo_x() + targetwidget.winfo_width()) and (targetwidget.winfo_y() < widget.winfo_y() < targetwidget.winfo_x() + targetwidget.winfo_height()):
        return True
    return False

def changeOnWidgetHover(widget, targetwidget, colorOnHover, colorOnLeave):
    if draggable_place(widget, targetwidget):
        targetwidget.config(background=colorOnHover)
    else:
        targetwidget.config(background=colorOnLeave)

def changeOnHover(frame, colorOnHover, colorOnLeave):

    # adjusting backgroung of the widget
    # background on entering widget
    frame.bind("<Enter>", func=lambda e: frame.config(background=colorOnHover))

    # background color on leving widget
    frame.bind("<Leave>", func=lambda e: frame.config(background=colorOnLeave))

#TODO: highlighting dragable places when hovering over them with a dragable

root = Tk()
root.geometry("300x300")
#draggable_places_list.append(Label(root, bd=30, bg="white", height=10, width=12))
for num in range(0,15):
    draggable_places_list.append(Label(root, bd=10, bg="white", height=5, width=5))
    draggable_places_list[num].place(x=40+num*60, y=40)
    #changeOnHover(draggable_places_list[num], "blue", "white")
#changeOnHover(frame2, "red", "white")
#draggable_places_list.append(frame2)
frame = Label(root, bd=5, bg="black", height=5, width=5)
frame.place(x=10, y=10)
make_draggable(frame)

#notes = Label(frame)
#notes.pack()
root.update()
drag_x = draggable_places_list[0].winfo_x()
print(drag_x)
mainloop()