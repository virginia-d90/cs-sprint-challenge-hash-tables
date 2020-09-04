def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #make a dictionary to keep track of all of the different values in the main list
    # count the number of time each value occurs 
        #if a value occurs the same number of times as the length of the list add it to the result
    int_vals = {}
    result = []

    for arr in arrays:
        for i in arr:
            if i not in int_vals: #if not in dict
                int_vals[i] = 1 #add key and set to 1 to start count
            else: #int is in dict
                int_vals[i] += 1 #add a tally to the count
                if int_vals[i] == len(arrays): #if tally matches number of arrays add to result
                    result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
