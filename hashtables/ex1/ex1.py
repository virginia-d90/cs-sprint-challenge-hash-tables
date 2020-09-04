def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #weights is a list while length and limit are int
    #looking for two items in "weights" that equal limit
        #return the indices of the two items
    #weights = keys ---> values = index ?i think?
    #check the dict to see the limit - weight is in the dict
        #if yes then return [index_item1, index_item2]


    weight_tbl = {}

    for i in range(length):#go through each index of weights

        if limit - weights[i] in weight_tbl:#check that second value needed is in table
            key = limit - weights[i] 
            index_2 = weight_tbl[key]
            return [i, index_2]

        weight_tbl[weights[i]] = i #add all weights to dict



    return None

