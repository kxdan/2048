

#Handles removing and adding the 0's back into grid in the appropriate position depending on the shift
def handleEmpty(grid, isReverse):
    count = 0
    newArray = []
    for element in grid:
        if element == 0:
            count +=1
        else: 
            newArray.append(element)

    if not isReverse:
        for x in range(0, count):
            newArray.append(0)

    if isReverse:
        newArray.reverse()
        for x in range(0, count):
            newArray.insert(0, 0)

    return newArray

#Handles the shifting and addition of the values that are combined
def shiftHorizontal(array, isReverse):
    for x in range (0, len(array)):
        firstValue = array[x]

        #Case: We're at the last element in the array
        if x+1 < len(array):
            secondValue = array[x+1]
        else:
            secondValue = None

        if firstValue == secondValue:
            firstValue = firstValue*2
            array[x] = firstValue
            array[x+1] = 0

    filteredArray = handleEmpty(array, isReverse)
    return filteredArray

#Transposes a grid
def untransposeGrid(grid):
    untransposedGrid = []
    for i in range(len(grid[0])):
        row =[]
        for item in grid:
            row.append(item[i])
        untransposedGrid.append(row)
    return untransposedGrid

#Handles left and right shifting, copy row due to by ref passing (not hugely needed, but makes testing easier and grid is small enough that it's not a problem)
def shiftGridHorizontal(grid, isLeftShift):
    newGrid = []
    for row in grid:
        if isLeftShift:
            newGrid.append(shiftArrayLeft(row))
        else: 
            newGrid.append(shiftArrayRight(row))

    return newGrid

#Handles Up and Down shifting, copy row due to by ref passing
def shiftGridVertical(grid, isUpShift):
    numColumns = 0
    if len(grid) > 0:
        numColumns = len(grid[0])    

    #Turn Columns into rows
    transposedGrid = []
    for column in range(0, numColumns):
        row = [i[column] for i in grid]
        if isUpShift:
            modifiedRow = shiftArrayUp(row)
        else:
            modifiedRow = shiftArrayDown(row)
        transposedGrid.append(modifiedRow)

    #Turn rows back into columns
    return untransposeGrid(transposedGrid)


#Left and Up are the same. Maintaining two functions for readability
def shiftArrayLeft(array):
    return shiftHorizontal(array, False)

def shiftArrayUp(array):
    return shiftHorizontal(array, False)

#Right and Down are the same. Maintaining two functions for readability
def shiftArrayRight(array):
    array.reverse()
    return shiftHorizontal(array, True)

def shiftArrayDown(array):
    array.reverse()
    return shiftHorizontal(array, True)

#Test atomic array shifting, one row (or a column posing as a row)
def ArrayTests(): 
    assert([4,4,2,0] == shiftArrayLeft([2,2,4,2]))
    assert([4,2,4,0] == shiftArrayLeft([2,2,2,4]))
    assert([0,2,4,4] == shiftArrayRight([2,2,2,4]))
    assert([0,4,4,2] == shiftArrayRight([2,2,4,2]))
    assert([0,2,4,4] == shiftArrayDown([2,4,2,2]))
    #Special Cases
    assert([0,2,4,4] == shiftArrayDown([2,2,2,4]))
    assert([4,2,4,0] == shiftArrayUp([2,2,2,4]))
    assert([0,2,4,4] == shiftArrayRight([2,2,2,4]))
    assert([4,2,4,0] == shiftArrayLeft([2,2,2,4]))

#Test Grid shifts
def GridTests():
    start = [[2,2,4,2],[4,2,2,4],[2,2,2,2],[2,4,0,2]]
    leftShiftGrid = [[4,4,2,0],[4,4,4,0],[4,4,0,0],[2,4,2,0]]
    assert(leftShiftGrid == shiftGridHorizontal(start, isLeftShift=True))

    start = [[2,2,4,2],[4,2,2,4],[2,2,2,2],[2,4,0,2]]
    rightShiftGrid = [[0,4,4,2],[0,4,4,4],[0,0,4,4],[0,2,4,2]]
    assert(rightShiftGrid == shiftGridHorizontal(start, isLeftShift=False))

    start = [[2,2,4,2],[4,2,2,4],[2,2,2,2],[2,4,0,2]]
    upShiftGrid = [[2,4,4,2],[4,2,4,4],[4,4,0,4],[0,0,0,0]]
    assert(upShiftGrid == shiftGridVertical(start, isUpShift=True))

    start = [[2,2,4,2],[4,2,2,4],[2,2,2,2],[2,4,0,2]]
    downShiftGrid = [[0,0,0,0],[2,2,0,2],[4,4,4,4],[4,4,4,4]]
    assert(downShiftGrid == shiftGridVertical(start, isUpShift=False))

def PlayGame(gridAsString, movesAsString):
    rows = gridAsString.split("\n")
    rows = rows[:len(rows) -1]

    Grid = []
    for row in rows:
        splitRow = row.split(" ")
        intRow = []
        for char in splitRow:
            intRow.append(int(char))

        Grid.append(intRow)
    
    moveArray = movesAsString.split(" ")

    print("Your Start Grid:")
    for row in Grid:
        print(row)

    for move in moveArray:
        match move:
            case "D":
                Grid=shiftGridVertical(Grid,isUpShift=False)
            case "U":
                Grid=shiftGridVertical(Grid,isUpShift=True)
            case "R":
                Grid=shiftGridHorizontal(Grid,isLeftShift=False)
            case "L":
                Grid=shiftGridHorizontal(Grid,isLeftShift=True)
        
    print("Your Final Grid:")
    for row in Grid:
        print(row)

ArrayTests()
GridTests()

board = """2 2 4 2
4 2 2 4
2 2 2 2
2 4 0 2
"""
moves = "D R D L U"

PlayGame(board, moves)