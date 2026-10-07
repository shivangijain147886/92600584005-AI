#capacities of the tow jugs
CAP_A = 6
CAP_B = 5

#GOAL AMOUNT
GOAL = 4

#FUNCTION TO PRINT STATE
def print_state(state):
    print("Jug A : ",state[0]," Liters")
    print("Jug B : ",state[1]," Liters")
    print()

#GENREATE ALL POSSIBLE MOVES
def get_neighbors(state):
    neighbors=[]

    a,b = state

    #1.Fill Jug A
    if a<CAP_A:
        neighbors.append(((CAP_A,b),"Fill Jug A"))

    #2. Fill Jug B
    if b<CAP_B:
        neighbors.append(((a,CAP_B),"Fill Jug B"))

    #3. Empty Jug A
    if a>0:
        neighbors.append(((0,b),"Empty Jug A"))

    #4. Empty Jug B
    if b>0:
        neighbors.append(((a,0),"Empty Jug B"))

    #5. Pour Jug A -> Jug B
    amount = min(a,CAP_B - b)

    if amount > 0:
        neighbors.append(((a-amount,b+amount),"Pour Jug A into Jug B"))

    #6. pour Jug B -> Jug A
    amount = min(b,CAP_A - a)

    if amount >0:
        neighbors.append(((a+amount,b-amount),"Pour Jug B into Jug A"))

    return neighbors

#BFS ALGORITHM
def bfs(state):
    queue = [(state,[])]
    visited = set()

    while queue:
        state,path = queue.pop(0)

        if state in visited:
            continue

        visited.add(state)

        #check goal
        if state[0] == GOAL or state[1] == GOAL:
            return path + [(state, "Goal Reached")]

        #Generate neighbors
        for neighbors, action in get_neighbors(state):

            if neighbors not in visited:
                queue.append((neighbors,path + [(neighbors,action)]))
    return None

#starting state
start = (0,0)

#run bfs
solution = bfs(start)

#print solution
if solution:
    print("Solution foubd in ",len(solution)," moves:\n")

    print("Initial State:")
    print_state(start)

    for state, action in solution:
        print(action)
        print_state(state)

else:
    print("No Solution found.")

    
