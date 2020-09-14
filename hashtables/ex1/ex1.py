def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    if length <= 1 : return None

    cache = {}
    for i in range(length):
        cache[weights[i]] = i

    for i in range(length):
        weight_needed = limit - weights[i]        

        if weight_needed in cache:
            return [cache[weight_needed], i]
        else:
            continue


