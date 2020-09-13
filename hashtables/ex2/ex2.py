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
    for i in range(length):
        my_dict[tickets[i].source] = tickets[i].destination

    route = [None] * length

    route[0] = my_dict["NONE"]
    for i in range(1, length):
        cur_des = route[i-1]
        if my_dict[cur_des]:
            route[i] = my_dict[cur_des]

    return route


