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

    print("x") 

board = """2 2 4 2
4 2 2 4
2 2 2 2
2 4 0 2
"""

def handleEmpty(Direction, grid):
    count = 0
    newArray = []
    for element in grid:
        if element == 0:
            count +=1
        else: 
            newArray.append(element)

    if Direction == "left":
        for x in range(0, count):
            newArray.append(0)

    if Direction == "right":
        for x in range(0, count):
            newArray.insert(0, 0)

    return newArray

def shiftLeft(array):

    #[2,2,4,2]
    #[4,4,2,0]

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

    filteredArray = handleEmpty("left", array)
    return filteredArray

assert([4,4,2,0] == shiftLeft([2,2,4,2]))
assert([4,2,4,0] == shiftLeft([2,2,2,4]))


board = """2 2 4 2
4 2 2 4
2 2 2 2
2 4 0 2
"""

boardMovedLeft = """4 4 2 0
4 4 4 0
4 4 0 0
2 4 2 0
"""

boardMovedDown = """0 0 0 0
2 2 0 2
4 4 4 4
4 4 4 4
"""