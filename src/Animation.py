from View import *
from Control import *
from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.width = 400
    data.height = 500
    data.margin = 0

    # display area's config
    data.displayWidth = data.width
    data.displayHeight = 120
    data.displayColor = "grey"
    data.borderWidth = 3

    # control area's row and column
    data.controlRow = 4
    data.controlCol = 4
    data.cellWidth = data.width / data.controlCol
    data.cellHeight = (data.height - data.displayHeight) / data.controlRow
    data.cellColor = 'grey'
    data.signs = [['7', '8', '9', 'x'],
                  ['4', '5', '6', '-'],
                  ['1', '2', '3', '+'],
                  ["+/-", '0', '.', '=']
                  ]
    data.currNum = ""
    data.numWidth = 11


    pass


def mousePressed(event, data):
    # use event.x and event.y
    controlPanelClick(event, data)


    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    drawDisplayPanel(canvas, data)
    drawControlPanel(canvas, data)
    drawNumbers(canvas, data)
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")
