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

    
    moveLeft(parsedMap)

    moveDown(parsedMap)

    print("x") 

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

def moveLeft(grid):
    print(grid)

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
                            allEqual == False

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

    print(grid)


def moveDown(grid):

    print(grid)

    gridlen = len(grid)

    previouslyCombined = [[False]*gridlen for _ in range(gridlen)]

    #Iterate through columns
    for j in range(len(grid[0])):

        #Iterate through rows, do combination
        prevValue = grid[0][j]
        for x in range(1, gridlen):
            currentValue = grid[x][j]
        
            if (x+1 < gridlen):
                nextVal = grid[x+1][j]
                if(currentValue == prevValue and currentValue == nextVal):
                    continue

            if prevValue == currentValue and not previouslyCombined[x-1][j]:
                previouslyCombined[x][j] = True 
                currentValue=prevValue+currentValue 
                grid[x][j] = currentValue
                grid[x-1][j] = 0
            else:
                grid[x][j] = currentValue
            
            if currentValue == 0:
                currentValue = prevValue
                prevValue = 0
            
            prevValue = currentValue

        prevValue = grid[0][j]

        #Remove 0's in new row
        arrayToPop = []
        for x in range(0, gridlen):
            arrayToPop.append(grid[x][j])     

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
            grid[x][j] = filteredArray[x]

    print(grid)


main("d", board)