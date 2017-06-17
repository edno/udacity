from utils import *

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    return dict((boxes[i], grid[i] if (grid[i] != '.') else '123456789') for i in range(len(boxes)))

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    for box,value in values.items():
        if len(value) == 1:
            for peer in peers[box]:
                values[peer] = values[peer].replace(value,'')
    return values

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for k,v in values.items():
        if len(v) > 1:
            for unit in units[k]:
                pval = str().join(values[key] for key in unit if key != k)
                d = [val for val in v if val not in pval]
                if len(d) == 1:
                    values[k] = d[0]
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)
        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if not values:
        return False
    # Return solution if all box have unique value
    if all(len(v) == 1 for v in values.values()):
        return values
    # Choose one of the unfilled squares with the fewest possibilities
    _,box = min((len(v),k) for k,v in values.items() if len(v) > 1)
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    # If you're stuck, see the solution.py tab!
    for val in values[box]:
        new_values = values.copy()
        new_values[box] = val
        res = search(new_values)
        if res:
            return res

G = grid_values('2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3')
G = search(G)
display(G)
