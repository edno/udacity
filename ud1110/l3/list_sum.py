def list_sum(input_list):
    sum = 0
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable
    for value in input_list:
        sum += value

    return sum



#These test cases check the list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))
