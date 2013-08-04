import astar

def locate_points(picture, target):
    for row in range(len(picture)):
        for column in range(len(picture[row])):
            if(picture[row][column]==str(target)):
                return [row, column]
            
def atos(picture):
    final_string=""
    for row in picture:
        final_string+="".join(row)
    return final_string

def stoa(string):
    final_grid=[[string[0], string[1], string[2]], [string[3], string[4], string[5]], [string[6], string[7], string[8]]]
    return final_grid

def generate_offspring(parent):
    children=[]
    templateboard=[thing[:] for thing in stoa(parent)]
    coord=locate_points(stoa(parent), " ")
    if(coord[0]>=1): #move up
        templateboard[coord[0]][coord[1]]=templateboard[coord[0]-1][coord[1]]
        templateboard[coord[0]-1][coord[1]]=" "
        children.append(atos(templateboard))
        templateboard=[thing[:] for thing in stoa(parent)]

    if(coord[1]>=1): #move left
        templateboard[coord[0]][coord[1]]=templateboard[coord[0]][coord[1]-1]
        templateboard[coord[0]][coord[1]-1]=" "
        children.append(atos(templateboard))
        templateboard=[thing[:] for thing in stoa(parent)]

    if(coord[0]<=1): #move down
        templateboard[coord[0]][coord[1]]=templateboard[coord[0]+1][coord[1]]
        templateboard[coord[0]+1][coord[1]]=" "
        children.append(atos(templateboard))
        templateboard=[thing[:] for thing in stoa(parent)]

    if(coord[1]<=1): #move right
        templateboard[coord[0]][coord[1]]=templateboard[coord[0]][coord[1]+1]
        templateboard[coord[0]][coord[1]+1]=" "
        children.append(atos(templateboard))

    return children

def find_priority(current, goal):
    locations=[]
    state_priority=0
    goal_locations=[]
    for point in range(1,9):
        locations.append(locate_points(stoa(current), str(point)))
        goal_locations.append(locate_points(stoa(goal), str(point)))
    locations.append(locate_points(stoa(current), " "))
    goal_locations.append(locate_points(stoa(goal), " "))
    for point in range(len(locations)):
        state_priority+=(abs(goal_locations[point][0]-locations[point][0])+abs(goal_locations[point][1]-locations[point][1]))
    return state_priority                  



    
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

solution, explored=astar.solve(atos(board), atos(endset), generate_offspring, find_priority)
for state in solution:
    nstate=stoa(state)
    for a in range(len(nstate)):
        print("".join(nstate[a]))
    print("\n")
print("Moves Required: ", len(solution)-1)
print("States Checked: ", explored)
