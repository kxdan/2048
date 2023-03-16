import copy
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

    downshiftGrid = [[0,0,0,0],[2,2,0,2],[4,4,4,4],[4,4,4,4]]

    resultingGridDown = moveDown(mapToDownshift)

    assert(resultingGridDown == downshiftGrid)

    leftShiftGrid = [[4,4,2,0],[4,4,4,0],[4,4,0,0],[2,4,2,0]]

    resultingGridLeft = moveLeft(mapToMoveLeft)

    assert(resultingGridLeft == leftShiftGrid)

    print("x") 

board = """2 2 4 2
4 2 2 4
2 2 2 2
2 4 0 2
"""

board1 = """2 2 4 2
2 2 2 4
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

def moveLeft(grid):
    gridlen = len(grid)

    previouslyCombined = [[False]*gridlen for _ in range(gridlen)]

    #Iterate through rows
    for row in range(gridlen):
        #Iterate through columns, do combination
        prevValue = grid[row][0]
        for column in range(1, gridlen):
            currentValue = grid[row][column]
        
            if (column+1 < gridlen):
                nextVal = grid[row][column+1]
                if(currentValue == prevValue and currentValue == nextVal):

                    allEqual = True
                    firstElement = grid[row]
                    for element in grid:
                        if element != firstElement:
                            allEqual = False

                    #check they're not all equal
                    if not allEqual:
                        continue

            if prevValue == currentValue and not previouslyCombined[row][column-1]:
                previouslyCombined[row][column] = True 
                currentValue=prevValue+currentValue 
                grid[row][column] = currentValue
                grid[row][column-1] = 0
            else:
                grid[row][column] = currentValue
            
            if currentValue == 0:
                currentValue = prevValue
                prevValue = 0
            
            prevValue = currentValue

        prevValue = grid[row][0]

        #Remove 0's in new row
        arrayToPop = []
        for column in range(0, gridlen):
            arrayToPop.append(grid[row][column])     

        countOfZeros = 0

        filteredArray = []
        for element in arrayToPop:
            if element != 0:
                filteredArray.append(element)
            else:
                countOfZeros+=1
        
        for j in range(0, countOfZeros):
            filteredArray.append(0)

        grid[row] = filteredArray

    return grid

def moveDown(grid):

    gridlen = len(grid)

    previouslyCombined = [[False]*gridlen for _ in range(gridlen)]

    for column in range(len(grid[0])):

        prevValue = grid[0][column]
        for row in range(1, gridlen):
            currentValue = grid[row][column]
        
            if (row+1 < gridlen):
                nextVal = grid[row+1][column]
                if(currentValue == prevValue and currentValue == nextVal):

                    allEqual = True
                    allElements = []
                    for index in range(0, gridlen):
                        allElements.append(grid[index][column])

                    firstElement = allElements[0]
                    for element in allElements:
                        if element != firstElement:
                            allEqual = False

                    #check they're not all equal
                    if not allEqual:
                        continue

            if prevValue == currentValue and not previouslyCombined[row-1][column]:
                previouslyCombined[row][column] = True 
                currentValue=prevValue+currentValue 
                grid[row][column] = currentValue
                grid[row-1][column] = 0
            else:
                grid[row][column] = currentValue
            
            if currentValue == 0:
                currentValue = prevValue
                prevValue = 0
            
            prevValue = currentValue

        prevValue = grid[0][column]
        arrayToPop = []

        for x in range(0, gridlen):
            arrayToPop.append(grid[x][column])     

        countOfZeros = 0

        filteredArray = []
        for element in arrayToPop:
            if element != 0:
                filteredArray.append(element)
            else:
                countOfZeros+=1
        
        for x in range(0, countOfZeros):
            filteredArray.insert(0,0)

        for x in range(0, len(filteredArray)):
            grid[x][column] = filteredArray[x]

    return grid

main("d", board)