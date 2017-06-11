#TODO: Implement the nearest_square function
def nearest_square(limit):
    n = 0;
    square = 0;
    while n*n <= limit:
        square = n*n
        n += 1
    return square

test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))
