def length_of_string(string):


    length = 0
    for char in string:
        length += 1
    return length


string = "Jumpwhere"
length = length_of_string(string)
print(length)
