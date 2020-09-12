def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    if length <= 1 : return None
    if length == 2 : return [1, 0]

    cache = {}
    for i in range(length-1):
        cache[weights[i]] = i

    for i in range(length-1):
        weight_needed = limit - weights[i]        

        if weight_needed in cache:
            print([i,cache[weight_needed]])
            return [cache[weight_needed], i]
        else:
            continue


get_indices_of_item_weights([10,20,15,5], 4, 30)