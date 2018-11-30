# Denotes our directed graph
neighbors = { 'D':['S', 'T'], 'R':['A'], 'A':['S'], 'C':['S'], 
                 'S':[], 'F':['S'], 'W':['F'], 'U':['D'], 'G':['U'],
                 'T':['E'], 'B':['T'], 'E':['V'],
                 'V' : ['G'] }


# For use by the algorithm
L = { node:0 for node in neighbors.keys() }


#====================================================================
# This is the algorithm itself. Determines if startingNode is in cycle.
#====================================================================
def isPartOfCycle(previousNode, currentNode, startingNode):
    # Mark the node as having been visited
    L[currentNode] += 1

    # Info, for debugging purposes
    print("{} -> {}: node {} has been encountered {} times.".format(previousNode, currentNode, currentNode, L[currentNode]))

    # If the node was encountered twice and it's the starting one, cycle
    if L[currentNode] == 2 and currentNode == startingNode:
        return True

    # If a node was encountered twice an it's not the starting one, no cycle
    elif L[currentNode] == 2 and currentNode != startingNode:
        return False
    
    # Repeat for neighbors... and neighbors... and neighbors
    for neighbor in neighbors[currentNode]:
        if L[neighbor] == 2 or isPartOfCycle(currentNode, neighbor, startingNode):
            return True
    
    # Non-cycle termination
    return False


#====================================================================
# Encapsulates the underlying algorithm with some initial setup
#====================================================================
def runAlgorithm(node):
    # Reset L each time
    for key in L.keys():
        L[key] = 0
    # Keep track of the starting node
    startingNode = node
    # Initiate algo
    result = isPartOfCycle(node, node, startingNode)
    print("{} is part of a cycle: {}".format(node, result))
    return result


#====================================================================
# Removes the given node from the graph (the "neighbors" dictionary)
#====================================================================
def removeNode(node):
    print("Removing node {} from the graph.".format(node))
    global neighbors

    # Remove the node itself from the graph's key list
    for key in neighbors.keys():
        if key == node:
            neighbors.pop(key, None)
            break
    
    # And now remove all appearances in values
    for key, value in neighbors.items():
        value = [x for x in value if x != node]
        neighbors[key] = value

    # Debugging only
    print(neighbors)


#====================================================================
# Main method, called first
#====================================================================
def main():
    # Initial list of all nodes in the graph
    nodes = list(neighbors.keys())
    # Loop through each node
    for node in nodes:
        # We need this check because the dict is constantly being modified
        if node in neighbors.keys():
            nodeIsPartOfCycle = runAlgorithm(node)
            # If the node was not part of a cycle, remove the ending node
            if not(nodeIsPartOfCycle):
                removeNode(node)
        # For readability
        print()

main()