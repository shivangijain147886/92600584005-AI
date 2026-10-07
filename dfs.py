goal = (1,2,3,
        4,5,6,
        7,8,0)

def print_board(state):
    for i in range(0,9,3):
        print(state[i:i+3])
    print()


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row,col=divmod(zero,3)

    moves=[(-1,0),(1,0),(0,-1),(0,1)]   #up,down,left,right

    for dr,dc in moves:
                new_row=row+dr
                new_col=col+dc

                if 0<=new_row<3 and 0<=new_col<3:
                        new_zero=new_row*3+new_col

                        new_state=list(state)
                        new_state[zero],new_state[new_zero] = new_state[new_zero],new_state[zero]

                        neighbors.append(tuple(new_state))

    return neighbors

#DFS Algorithm
def dfs(state):
        stack=[(state,[])] #simple queue
        visited=set()

        while stack:
            state,path=stack.pop() #remove first item

            if state ==goal:
              return path+[state]

            neighbors = get_neighbors(state)

            for neighbour in reversed(neighbors):
               if neighbour not in visited:
                   visited.add(neighbour)
                   stack.append((neighbour,path + [state]))

        return None

#example start state
start = (1,2,3,
         4,0,6,
         7,5,8)

solution = dfs(start)

if solution:
        print("Solution found in",len(solution)-1,"move:\n")
        for step in solution:
            print_board(step)
else:
        print("No solution found")





