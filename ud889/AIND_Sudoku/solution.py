assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    twins_list = []
    for box in boxes:
        if len(values[box]) == 2:
            v = values[box]
            for peer in peers[box]:
                if values[peer] == values[box]:
                    twins_list.append([box,peer])

    # Eliminate the naked twins as possibilities for their peers
    if twins_list:
        for twins in twins_list:
            # intersect list of twins' peers for common units
            twins_peers = set(peers[twins[0]]).intersection(set(peers[twins[1]]))
            for peer in twins_peers:
                for v in values[twins[0]]:
                    values = assign_value(values, peer, values[peer].replace(v,''))
    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

def diag(A, B):
    "Diagonals of A elements with elements in B."
    return [A[r]+B[c] for r in range(len(A)) for c in range(len(B)) if r == c]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    return dict((boxes[i], grid[i] if (grid[i] != '.') else '123456789') for i in range(len(boxes)))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    for box,value in values.items():
        if len(value) == 1:
            for peer in peers[box]:
                values = assign_value(values, peer, values[peer].replace(value,''))
    return values

def only_choice(values):
    for box,v in values.items():
        if len(v) > 1:
            for unit in units[box]:
                pval = str().join(values[key] for key in unit if key != box)
                d = [val for val in v if val not in pval]
                if len(d) == 1:
                    values = assign_value(values, box, d[0])
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        # Use the Naked Twins Strategy
        values = naked_twins(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
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

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    return search(grid_values(grid))

boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diag_units = [diag(rows, cols)] + [diag(rows, cols[::-1])]
unitlist = row_units + column_units + square_units + diag_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
