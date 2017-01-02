# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    change = True

    # first would locate the goal and set it to 0 
    # when going over each cell one by one, will look for its neighbours 
    # and set v2 = the value of the neighbours + cost per step
    # if ever one of the v2's is less than the current value of this cell
    # which means the v2 is not 99 
    # that means a change needs to be made
    # keep looping until no change is to make anymore
    # not very efficient algorithm
    
    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        change = True

                elif grid[x][y] == 0:
                    for i in range(len(delta)):
                        x2 = x + delta[i][0]
                        y2 = y + delta[i][1]
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:

                            v2 = value[x2][y2] + cost
                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2

    for i in range(len(value)):
        print value[i]


    return value 
compute_value(grid, goal, cost)
