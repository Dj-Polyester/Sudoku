import sys
from copy import deepcopy

def output(a):
    sys.stdout.write(str(a))

N = 9

field = [[5,1,7,6,0,0,0,3,4],
         [2,8,9,0,0,4,0,0,0],
         [3,4,6,2,0,5,0,9,0],
         [6,0,2,0,0,0,0,1,0],
         [0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]

         |5|1|7|6|9|8|2|3|4| 0
 - - - - - - - - -
|2|8|9|1|3|4|7|5|6| 1
 - - - - - - - - -
|3|4|6|2|7|5|8|9|1| 2
 - - - - - - - - -
|6|7|2|8|4|9|3|1|5| 3
 - - - - - - - - -
|1|3|8|5|2|6|9|4|7| 4
 - - - - - - - - -
|9|5|4|7|1|3|6|8|2| 5
 - - - - - - - - -
|4|9|5|3|6|2|1|7|8| 6
 - - - - - - - - -
|7|2|3|4|8|1|5|6|9| 7
 - - - - - - - - -
|8|6|1|9|5|7|4|2|3| 8
"""
         [['5', '1', '7', '6', '9', '8', '2', '3', '4'],
         ['2', '8', '9', '1', '3', '4', '7', '5', '6'],
         ['3', '4', '6', '2', '7', '5', '8', '9', '1'],
         ['6', '7', '2', '8', '4', '9', '3', '1', '5'],
         ['1', '3', '8', '5', '2', '6', '9', '4', '7'],
         ['9', '5', '4', '7', '1', '3', '6', '8', '2'],
         ['4', '9', '5', '3', '6', '2', '1', '7', '8'],
         ['7', '2', '3', '4', '8', '1', '5', '6', '9'],
         ['8', '6', '1', '9', '5', '7', '4', '2', '3']]
"""
def print_field(field):
    if not field:
        output("No solution")
        return
    for i in range(N):
        for j in range(N):
            cell = field[i][j]
            if cell == 0 or isinstance(cell, set):
                output('.')
            else:
                output(cell)
            if (j + 1) % 3 == 0 and j < 8:
                output(' |')

            if j != 8:
                output(' ')
        output('\n')
        if (i + 1) % 3 == 0 and i < 8:
            output("- - - + - - - + - - -\n")

def read(field):
    """ Read field into state (replace 0 with set of possible values) """

    state = deepcopy(field)
    for i in range(N):
        for j in range(N):
            cell = state[i][j]
            if cell == 0:
                state[i][j] = set(range(1,10))

    return state

state = read(field)


def done(state):
    """ Are we done? """

    for row in state:
        for cell in row:
            if isinstance(cell, set):
                return False
    return True


def propagate_step(state):
    """
    Propagate one step.

    @return:  A two-tuple that says whether the configuration
              is solvable and whether the propagation changed
              the state.
    """

    new_units = False

    # propagate row rule
    for i in range(N):
        row = state[i]
        values = set([x for x in row if not isinstance(x, set)])
        for j in range(N):
            if isinstance(state[i][j], set):
                state[i][j] -= values
                if len(state[i][j]) == 1:
                    val = state[i][j].pop()
                    state[i][j] = val
                    values.add(val)
                    new_units = True
                elif len(state[i][j]) == 0:
                    return False, None

    # propagate column rule
    for j in range(N):
        column = [state[x][j] for x in range(N)]
        values = set([x for x in column if not isinstance(x, set)])
        for i in range(N):
            if isinstance(state[i][j], set):
                state[i][j] -= values
                if len(state[i][j]) == 1:
                    val = state[i][j].pop()
                    state[i][j] = val
                    values.add(val)
                    new_units = True
                elif len(state[i][j]) == 0:
                    return False, None

    # propagate cell rule
    for x in range(3):
        for y in range(3):
            values = set()
            for i in range(3 * x, 3 * x + 3):
                for j in range(3 * y, 3 * y + 3):
                    cell = state[i][j]
                    if not isinstance(cell, set):
                        values.add(cell)
            for i in range(3 * x, 3 * x + 3):
                for j in range(3 * y, 3 * y + 3):
                    if isinstance(state[i][j], set):
                        state[i][j] -= values
                        if len(state[i][j]) == 1:
                            val = state[i][j].pop()
                            state[i][j] = val
                            values.add(val)
                            new_units = True
                        elif len(state[i][j]) == 0:
                            return False, None

    return True, new_units

def propagate(state):
    """ Propagate until we reach a fixpoint """
    while True:
        solvable, new_unit = propagate_step(state)
        if not solvable:
            return False
        if not new_unit:
            return True


def solve(state):
    """ Solve sudoku """

    solvable = propagate(state)

    if not solvable:
        return None

    if done(state):
        return state

    for i in range(N):
        for j in range(N):
            cell = state[i][j]
            if isinstance(cell, set):
                for value in cell:
                    new_state = deepcopy(state)
                    new_state[i][j] = value
                    solved = solve(new_state)
                    if solved is not None:
                        return solved
                return None
def printSudoku(table,m,n):
	j=0
	for i in range(n):
		print(f" {i}",end="",flush=True)
	print()
	while(j < 2*m+1):
		if j%2==0:
			for i in range(n):
				print(" -",end="",flush=True)
		else:
			for i in range(n):
				index=int((j-1)/2)
				print(f"|{table[index][i]}",end="",flush=True)
			print(f"| {index}",end="",flush=True)
		print("\n",end="",flush=True)
		j+=1

printSudoku(solve(state),9,9)