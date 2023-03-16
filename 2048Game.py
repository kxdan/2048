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

    
    move("d", parsedMap)

    print("x") 

board = """2 2 4 2
4 2 2 4
2 2 2 2
2 4 0 2
"""


boardWithEdits = """0 0 0 0
2 2 0 2
4 4 4 4
4 4 4 4
"""

def move(direction, grid):

    print(grid)

    gridlen = len(grid)

    previouslyCombined = [[False]*gridlen for _ in range(gridlen)]

    for j in range(len(grid[0])):

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