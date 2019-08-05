#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    # Changed route definition to eliminate another variable.
    route = []

    # Fill in the hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Find the starting destination (NONE)
    dest = hash_table_retrieve(hashtable, "NONE")
    
    # Adding initial append here for differences in readme vs tests
    route.append(dest)

    while dest is not "NONE":
        # route.append(dest)
        dest = hash_table_retrieve(hashtable, dest)
        # Moving append here to accommodate the difference between readme and tests
        # Readme shows route without "NONE", test expects it to be there.
        route.append(dest)

    return route
