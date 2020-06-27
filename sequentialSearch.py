def sequentialSearch(array, term):
    for index in range(len(array)):
        if array[index] == term:
            print("Found, at " + str(index))


sequentialSearch([11,23,58,31,56,77,43,12,65,19],31)