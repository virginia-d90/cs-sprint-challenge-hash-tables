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
    #make a dict of tickets where source is key and destination is value
    #make a list for the route 
    cache = {}
    route = [None] * length #set equal to number of tickets

    for ticket in tickets: #populate the cache
        cache[ticket.source] = ticket.destination

    destination = cache["NONE"] #first ticket will have source = NONE so destination is set to the value

    for leg in range(length): #add destination of each ticket to the route list
        route[leg] = destination
        print(route)

        destination = cache[destination] #sets source of the route trip to the previous destination


  



    

      


    return route
