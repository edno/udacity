def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename, 'r') as f:
        for line in f:
            credit = line.split(',', maxsplit=1)
            cast_list.append(credit[0])
    return cast_list

print(create_cast_list('flying_circus_cast.txt'))
