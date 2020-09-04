def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    #make a dictionary to cache matches return the keys
    #add all numbers to the dict as key and value
    #check to see if a opposite match exists
    # add matches to output list 
    
    int_dict = {}
    output = []
    for i in a:
        int_dict[i] = i #populate the dict

        if i != 0 and - i in int_dict: #check if a negative counterpart is there
            output.append(abs(i))



    return output


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
