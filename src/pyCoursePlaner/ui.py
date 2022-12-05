from tkinter import * #still unsure about tkinter but sticking with it for now (https://github.com/TomSchimansky/CustomTkinter looks cool)
#example
from dnd_res import *
from scrollable_widget import *
from tk_scroll import *
draggable_places_list = []
#TODO: highlighting dragable places when hovering over them with a dragable


def scroll_bar_init(root):
    scroll_bar_widget = Frame(root)
    scroll_bar = Scrollbar(scroll_bar_widget)
    scroll_bar.pack( side = LEFT,fill = Y )

    #scroll_content = Listbox(scroll_bar_widget, yscrollcommand  = scroll_bar.set)
    #scroll_content.insert(END, Label(scroll_content, bd=5, bg="black", height=5, width=5)) #without a listbox and instead ascrolable frame
    scroll_content = Label(scroll_bar_widget, width = 15, height = 15)
    scroll_content.pack( side = LEFT, fill = BOTH )
    #scroll_bar.config( command = scroll_content.yview )
    scroll_bar_widget.pack(side=LEFT, fill=Y)
    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(3, weight=1)

def scroll_bar_widget(root):
    scrollFrame = ScrollFrame(root)
    #scrollFrame.grid_rowconfigure(3, weight=1)
    f = []
    for row in range(40):
            a = row
            f.append(Label(scrollFrame.viewPort, bd=5, bg="black", height=5, width=5).grid(row=row, column=1,pady=3))#scrollFrame.viewport return NoneType
            
            t="this is the second column for row %s" %row
            #make_draggable(b)

            #tk.Button(scrollFrame.viewPort, text=t, command=lambda x=a: printMsg("Hello " + str(x))).grid(row=row, column=1)

        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
    testF = Label(scrollFrame, bd=5, bg="black", height=5, width=5).grid(row=2, column=3,pady=3)
    scrollFrame.pack(side="left", fill="y", expand=False)
    make_draggable(testF)
    def printMsg(msg):
        print(msg)
    #scrollFrame.pack(side="left", fill="both")








def planner_frame_init(root):
    planner_frame = Frame(root, bd=1, relief="solid")
    #planner_frame.pack(side=RIGHT, fill=BOTH)
    define_dragable_locations(root=planner_frame, xpos=50, ypos=50, height=100, width=100, xnum=2, ynum=2,xpadding=5, ypadding=5)
    #planner_frame.grid(column=4,row=4)
    frame = Label(planner_frame, bd=5, bg="black", height=5, width=5)
    
    #frame.place(x=10, y=10)
    make_draggable(frame)
    frame.pack(side=LEFT)
    planner_frame.pack(side=LEFT, fill="both", expand=True)
    planner_frame.update()

root = Tk()
root.geometry("1000x600")
scroll_bar_widget(root)
planner_frame_init(root)
#scroll_bar_widget(root)


root.update()
mainloop()