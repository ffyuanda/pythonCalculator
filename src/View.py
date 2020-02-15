

def drawDisplayPanel(canvas, data):

    canvas.create_rectangle(data.margin, data.margin, data.displayWidth -
                            data.margin, data.margin + data.displayHeight,
                            fill=data.displayColor, width=data.borderWidth)

    # canvas.create_text()
    pass


def drawCell(canvas, data, row, col):

    x0 = data.margin + data.cellWidth * col
    y0 = data.margin + row * data.cellHeight + data.displayHeight
    x1 = (col + 1) * data.cellWidth + data.margin
    y1 = (row + 1) * data.cellHeight + data.margin + data.displayHeight

    canvas.create_rectangle(x0, y0, x1, y1, fill=data.cellColor, width=2)

    canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2,
                       text=data.signs[row][col],
                       fill="white",
                       font="Times 30 bold")

    pass


def drawControlPanel(canvas, data):

    for i in range(data.controlRow):
        for j in range(data.controlCol):

            drawCell(canvas, data, i, j)
    pass


def drawNumbers(canvas, data):

    canvas.create_text(data.displayWidth - data.numWidth
                       * len(data.currNum) - 4,
                       data.displayHeight - data.numWidth - 10,
                       text=data.currNum, fill='white',
                       font="Times 32 bold")

    pass
