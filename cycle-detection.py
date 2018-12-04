# Denotes our directed graph
neighbors = { 'D':['S', 'T'], 'R':['A'], 'A':['S'], 'C':['S'], 
                 'S':[], 'F':['S'], 'W':['F'], 'U':['D'], 'G':['U'],
                 'T':['E'], 'B':['T'], 'E':['V'],
                 'V' : ['G'] }

# Dict used by algorithm to keep track of how many times each node has been visited
visitedCount = {}

# Used by algorithm to compare the node in the current iteration to the starting node
startingNode = ''

#====================================================================
# This is the algorithm itself. Determines if startingNode is in cycle.
#====================================================================
def isPartOfCycle(previousNode, currentNode):
    # To avoid doing this at the start of the algorithm for all graph nodes.
    # That is, we only do this for nodes in the current "path" we're following.
    if currentNode not in visitedCount:
        visitedCount[currentNode] = 0

    # Mark the node as having been visited one more time
    visitedCount[currentNode] += 1

    # This stuff is for debugging purposes only and tracing the algorithm
    if previousNode == currentNode:
        print("Starting at {}. ".format(currentNode), end="")
    else:
        print("{} -> {}: ".format(previousNode, currentNode), end="")
    print("Node {} has been encountered {} times.".format(currentNode, visitedCount[currentNode]))

    # If the node was encountered twice...
    if visitedCount[currentNode] == 2:
        # Return True only if we're back to the starting node, in which case it's a cycle
        return currentNode == startingNode
    
    # Repeat for neighbors... and neighbors... and neighbors
    for neighbor in neighbors[currentNode]:
        if (neighbor in visitedCount and visitedCount[neighbor] == 2) or isPartOfCycle(currentNode, neighbor):
            return True
    
    # Non-cycle termination (anything but the situation like the one for 'B')
    return False


#====================================================================
# Encapsulates the underlying algorithm with some initial setup
#====================================================================
def runAlgorithm(node):
    # Reset L each time
    visitedCount.clear()
    # Keep track of the starting node
    global startingNode 
    startingNode = node
    # Initiate algo
    result = isPartOfCycle(node, node)
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
    print("Cycle(s): {}".format(neighbors))

main()