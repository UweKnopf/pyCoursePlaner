from tkinter import *
draggable_places_list = []

def make_draggable(widget):
    """Makes a widget dragable"""
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
    #for draggable_widget in draggable_places_list:
        #changeOnWidgetHover(widget, draggable_widget, "blue", "white")

def on_drag_stop(event):
    widget = event.widget
    for draggable_widget in draggable_places_list:
        if not draggable_place(widget, draggable_widget):
            widget.place(x=widget._drag_start_x_stand, y=widget._drag_start_y_stand)
        else:
            widget.place(x=draggable_widget.winfo_x(), y=draggable_widget.winfo_y())
            break


def draggable_place(widget, targetwidget):#probably in a for loop iterating over all possible locations
    if (targetwidget.winfo_x() < widget.winfo_x() < targetwidget.winfo_x() + targetwidget.winfo_width()) and (targetwidget.winfo_y() < widget.winfo_y() < targetwidget.winfo_y() + targetwidget.winfo_height()):
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

def define_dragable_locations(root, xpos, ypos, xnum=1, ynum=1, height=50, width=50, xpadding=0, ypadding=0):
    """Main way to declare possible locations for a dragable object.
    xnum, ynum:  Size of a grid
    xpadding, ypadding: Distance between locations
    height, width: Units in pixels!
    """
    global draggable_places_list
    
    for y_grid in range(0,ynum):
        for x_grid in range(0,xnum):
            draggable_places_list.append(Label(root, bd=10, bg="white"))
            draggable_places_list[-1].place(x = xpos + x_grid*(width+xpadding), y = ypos + y_grid*(height+ypadding), height = height, width = width)

            root.update()
