def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}    
    a =[]
    for i in range(len(arrays)):
        a += arrays[i]

    for n in a:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1

    res = [key for (key, value) in d.items() if value == len(arrays)]
    return res


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
