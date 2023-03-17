import copy
import numpy as np

moves = "D R D L U"

def main(direction, grid):
    rows = board.split("\n")

    rows = rows[:len(rows) -1]

    parsedMap = []
    for row in rows:
        splitRow = row.split(" ")
        intRow = []
        for char in splitRow:
            #TODO: handle this properly incase of bad values
            intRow.append(int(char))

        parsedMap.append(intRow)

    
    mapToDownshift = parsedMap.copy()
    mapToMoveLeft = copy.deepcopy(parsedMap)

    unused = [[2,2,4,2],[4,2,4,4],[2,2,2,2],[2,4,0,2]]
    leftShiftGrid = [[4,4,2,0],[4,4,4,0],[4,4,0,0],[2,4,2,0]]

    resultingGridLeft = moveLeft(mapToMoveLeft)

    assert(resultingGridLeft == leftShiftGrid)


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

def shiftGridLeft(grid):
    newGrid = []
    for row in grid:
        newGrid.append(shiftArrayLeft(row))

    return newGrid

def shiftGridRight(grid):
    newGrid = []
    for row in grid:
        newGrid.append(shiftArrayRight(row))

    return newGrid


def untransposeGrid(grid):
    untransposedGrid = []
    for i in range(len(grid[0])):
        row =[]
        for item in grid:
            row.append(item[i])
        untransposedGrid.append(row)
    return untransposedGrid

def shiftGridDown(grid):
    
    #Get Number of columns
    numColumns = 0
    if len(grid) > 0:
        numColumns = len(grid[0])    

    #Turn Columns into rows
    transposedGrid = []
    for column in range(0, numColumns):
        row = [i[column] for i in grid]
        modifiedRow = shiftArrayDown(row)
        transposedGrid.append(modifiedRow)

    #turn each element in a row back into a column
    return untransposeGrid(transposedGrid)


def shiftGridUp(grid):
    
    #Get Number of columns
    numColumns = 0
    if len(grid) > 0:
        numColumns = len(grid[0])    

    #Turn Columns into rows
    transposedGrid = []
    for column in range(0, numColumns):
        row = [i[column] for i in grid]
        modifiedRow = shiftArrayUp(row)
        transposedGrid.append(modifiedRow)

    #turn each element in a row back into a column
    x = untransposeGrid(transposedGrid)
    return x


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



    
#assert([4,4,2,0] == shiftLeft([2,2,4,2]))
#assert([4,2,4,0] == shiftArrayLeft([2,2,2,4]))
#assert([] == shiftArrayRight([2,2,2,4]))
#assert([0,4,4,2] == shiftRight([2,2,4,2]))
#assert([0,2,4,4] == shiftDown([2,4,2,2]))

#Special Cases
#assert([0,2,4,4] == shiftArrayDown([2,2,2,4]))
#assert([4,2,4,0] == shiftArrayUp([2,2,2,4]))

#assert([0,2,4,4] == shiftArrayRight([2,2,2,4]))
#assert([4,2,4,0] == shiftArrayLeft[2,2,2,4])


#shiftArrayLeft([2,2,2,4])

OG = [[2,2,4,2],[4,2,2,4],[2,2,2,2],[2,4,0,2]]
#leftShiftGrid = [[4,4,2,0],[4,4,4,0],[4,4,0,0],[2,4,2,0]]
#rightShiftGrid = [[0,4,4,2],[0,4,4,4],[0,0,4,4],[0,2,4,2]]
upShiftGrid = [[2,4,4,2],[4,2,4,4],[4,4,0,4],[0,0,0,0]]
#downShiftGrid = [[0,0,0,0],[2,2,0,2],[4,4,4,4],[4,4,4,4]]

#assert(leftShiftGrid == shiftGridLeft(OG))
#assert(rightShiftGrid == shiftGridRight(OG))
#assert(downShiftGrid == shiftGridDown(OG))
assert(upShiftGrid == shiftGridUp(OG))

board = """2 2 4 2
4 2 2 4
2 2 2 2
2 4 0 2
"""