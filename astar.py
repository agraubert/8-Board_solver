def history_recall(singlestate, previous_states):
    #print(singlestate)
    current_state=previous_states[singlestate]
    state_history=[]
    state_history.append(current_state)
    if(current_state!="ORIGIN"):
        state_history+=history_recall(current_state, previous_states)
    return state_history

def solve(original, goal, generate_sequence, get_priority):
    history={}
    gamestates=[]
    gamestates.append([original, get_priority(original, goal)])
    history[original]="ORIGIN"
    exploredstates=1
    Done=False
    
    while(not Done):
        lead_state=gamestates.pop(0)
        pics=generate_sequence(lead_state[0])
        exploredstates+=1
        new_states=[]
        for pic in pics:
            if(not(pic in history)):
                history[pic]=lead_state[0]
                new_states.append([pic, get_priority(pic, goal)])            
        gamestates+=new_states
        gamestates.sort(key=lambda x : x[1])
        if(gamestates[0][0]==goal):
            Done=True
        statelength=len(gamestates)
        if(((exploredstates/1000)==(int(exploredstates/1000))) and exploredstates>999):
            print("\n Program is not frozen.  Has currently checked: ", exploredstates, " states")
            print("(", statelength," states in que)")
        if(statelength==0):
            print("No solution detected.  Press Ctrl+c to abort")
            
    final_solution=history_recall(gamestates[0][0], history)
    final_solution.reverse()
    final_solution.pop(0)
    final_solution.append(gamestates[0][0])
    #print(final_solution)
    exploredstates+=1
    return final_solution, exploredstates
