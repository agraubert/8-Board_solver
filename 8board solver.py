import os
import sys
from math import copysign

def locator(grid, part):
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            if(grid[a][b]==part):
                return [a,b]
            
def boardpriority(_gameboard):
    locations=[]
    prios=[]
    for a in range(1,9):
        locations.append(locator(_gameboard, str(a)))
    locations.append(locator(_gameboard, " "))
    for a in range(len(locations)):
        x=a%3
        y=int(a/3)
        #print(locations[a])
        prios.append(abs(y-locations[a][0])+abs(x-locations[a][1]))
    return prios

def moves(gameboard, movesmade):
    loc=locator(gameboard, " ")
    newboards=[]
    workingboard=[thing[:] for thing in gameboard]
    templist=boardpriority(workingboard)
    if(loc[0]>0): #switch up
        workingboard[loc[0]][loc[1]]=workingboard[loc[0]-1][loc[1]]
        workingboard[loc[0]-1][loc[1]]=" "
        templist=boardpriority(workingboard)
        newboards.append([[thing[:] for thing in workingboard], templist, (sum(templist)+movesmade+1), movesmade+1])
        workingboard=[thing[:] for thing in gameboard]
    if(loc[0]<2): #switch down
        workingboard[loc[0]][loc[1]]=workingboard[loc[0]+1][loc[1]]
        workingboard[loc[0]+1][loc[1]]=" "
        templist=boardpriority(workingboard)
        newboards.append([[thing[:] for thing in workingboard], templist, (sum(templist)+movesmade+1), movesmade+1])
        workingboard=[thing[:] for thing in gameboard]
    if(loc[1]>0): #switch left
        workingboard[loc[0]][loc[1]]=workingboard[loc[0]][loc[1]-1]
        workingboard[loc[0]][loc[1]-1]=" "
        templist=boardpriority(workingboard)
        newboards.append([[thing[:] for thing in workingboard], templist, (sum(templist)+movesmade+1), movesmade+1])
        workingboard=[thing[:] for thing in gameboard]
    if(loc[1]<2): #switch right
        workingboard[loc[0]][loc[1]]=workingboard[loc[0]][loc[1]+1]
        workingboard[loc[0]][loc[1]+1]=" "
        templist=boardpriority(workingboard)
        newboards.append([[thing[:] for thing in workingboard], templist, (sum(templist)+movesmade+1), movesmade+1])
    
    return newboards

        
raw1=input("Row 1: ")
raw2=input("Row 2: ")
raw3=input("Row 3: ")
board=[]
endset=[["1", "2", "3"], ["4", "5", "6"], ["7", "8", " "]]
if(len(raw1)==3):
    board.append([thing[:] for thing in raw1])
if(len(raw2)==3):
    board.append([thing[:] for thing in raw2])
if(len(raw3)==3):
    board.append([thing[:] for thing in raw3])
priorities=[]
priorities=boardpriority(board) #has an array of the distances of each piece of the gameboard from its end place
gamestates=[]
history=[]
gamestates.append([[thing[:] for thing in board], priorities, sum(priorities), 0])
done=False
for a in range(len(board)):
    print("".join(board[a]))
print("Moves Required: 0")
print("Priority: ", sum(priorities))
while(not done):
    temp=[]
    print("Making Move")
    beststate=gamestates.pop(0)
    temp+=moves(beststate[0], beststate[3])
    gamestates+=temp
    
    #i know this part is innefficient, but i need this:
    remlist=[]
    if(len(history)>=1):
        for a in range(len(history)):
            for b in range(len(gamestates)):
                same=True
                for c in range(len(history[a][0])):
                    for d in range(len(history[a][0][c])):
                        if(history[a][0][c][d]!=gamestates[b][0][c][d]):
                            same=False
                if(same):
                    if(gamestates[b][2]>=history[a][2]):
                        remlist.append(b)
        remlist.sort()
        if(len(remlist)>=1):
            for a in range(len(remlist)):
                gamestates.pop(remlist[a]-a)
    
    history+=temp
    #print(gamestates[0])
    gamestates.sort(key=lambda x : x[2])

    
    print("New Board:")
    for a in range(len(gamestates[0][0])):
        print("".join(gamestates[0][0][a]))
    print("Moves Required: ", gamestates[0][3])
    print("Priority: ", gamestates[0][2])
    done=True
    for a in range(len(gamestates[0][0])):
        for b in range(len(gamestates[0][0][a])):
            if(gamestates[0][0][a][b]!=endset[a][b]):
                     done=False
    input("")
print("Done!")
for a in range(len(gamestates[0][0])):
    print("".join(gamestates[0][0][a]))
print("Moves Required: ", gamestates[0][3])
