def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    sorted_list = sorted(input_list, reverse=True)
    if len(sorted_list) < 3:
        return sorted_list
    else:
        return sorted_list[:3]

batch_sizes = ["Zorro", "Aria", "Goky"]
print(top_three(batch_sizes))
