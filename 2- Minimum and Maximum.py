def get_min(array):
    min_value = array[0]
    for value in array:
        if value < min_value:
            min_value = value
    return min_value

def get_max(array):
    max_value = array[0]
    for value in array:
        if value > max_value:
            max_value = value
    return max_value


my_list = [2,3,4,5,3,4,5,-8,0,20]

output = get_max(my_list)
print(output)
