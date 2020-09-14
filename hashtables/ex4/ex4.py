def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    for n in a:
        num = abs(n)
        if num not in d:
            d[num] = 1
        else: 
            d[num] += 1

    res = [key for (key, value) in d.items() if value > 1 ]
    return res


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
