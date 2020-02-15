def controlPanelClick(event, data):

    # Don't click outside of the control panel.
    if event.y < data.displayHeight:
        return

    row = (event.y - data.margin - data.displayHeight) // data.cellHeight
    col = (event.x - data.margin) // data.cellWidth
    row = int(row)
    col = int(col)
    # print(data.currNum, data.signs[row][col])

    data.currNum += data.signs[row][col]
    print(data.currNum)

    pass
