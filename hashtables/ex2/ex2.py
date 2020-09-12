#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    my_dict = {}
    for i in range(length - 1):
        my_dict[tickets[i].source] = tickets[i].destination

    route = [my_dict['NONE']]


    print(route)
    print(my_dict)
    for i in range(length):
        print(i)
        if route[i] in my_dict:
            route[i+1] = my_dict[route[i]]

    # print(route)

    return route


