#class Bar:
#  def __init__(self, Foo):
#    self.foo = Foo

#def FooBar():

#https://www.codeabbey.com/index/task_view/game-of-2048





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
        
            #Potential continue loop?
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

        #Going through and removing all the 0's that now exist in the column
        #check if the array actually has N zero, removes all those zeros by index, and then add to the start the array the number of zeros
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

    








    #If values are the same we can combine them but if they are not the same we cannot combine them 

    #Look through each up to down, if there's a zero, expand the window, if not, and combine then we can combine them

    #Case is val1 + val2 = val1 || val1*2 -> combine them.



    #Case 1: can't do a combine
        #Situation: 2,4,2,0
        #output: same
    
    #Case 2: combine with no intermediary
        #Situation: 2,2,4,0
        #output: 








#    for element in board:
        
        

#    if direction == "D":



#def moveDown(grid):

main("d", board)