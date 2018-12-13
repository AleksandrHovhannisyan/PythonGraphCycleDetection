class CycleFinder:

    #=============================================================================
    # Initializes the CycleFinder.
    # @param graph - a dictionary representing a directed graph (empty by default)
    #=============================================================================
    def __init__(self, graph=dict()):
        self.graph = graph
        self.startingNode = ''
        self.visitedCount = {}

    #=============================================================================
    # Returns a dictionary of any cycles it found in the given graph.
    #=============================================================================
    def findCycles(self):
        # Initial list of all nodes in the graph
        nodes = list(self.graph.keys())
        # Loop through each node in the graph
        for node in nodes:
            # We need this check because the dict is constantly being modified (node removal)
            if node in self.graph.keys():
                # Run the actual cycle detection algorithm
                nodeIsPartOfCycle = self.__runAlgorithm(node)
                print("{} is part of a cycle: {}".format(node, nodeIsPartOfCycle))
                # If the node was not part of a cycle, remove it
                if not nodeIsPartOfCycle:
                    self.__removeNode(node)
            print()
        return self.graph


    #=============================================================================
    # Wraps the underlying algorithm with some initial non-recursive setup.
    # @param startingNode - the node we're testing for cycles
    #=============================================================================
    def __runAlgorithm(self, startingNode):
        # Reset node visitation counters on each iteration of the algorithm
        self.visitedCount.clear()
        # Keep track of the starting node
        self.startingNode = startingNode
        # And initiate the algorithm
        return self.isPartOfCycle(previousNode=None, currentNode=startingNode)


    #=============================================================================
    # Determines if startingNode is part of a cycle.
    # @param previousNode - the node that led us to currentNode
    # @param currentNode - the node we're currently visiting
    #=============================================================================
    def isPartOfCycle(self, previousNode, currentNode):
        # This is so we avoid tracking all graph nodes. Only do it for nodes in the current path.
        if currentNode not in self.visitedCount:
            self.visitedCount[currentNode] = 0

        # Mark the node as having been visited one more time
        self.visitedCount[currentNode] += 1

        # This print stuff is for debugging purposes only
        if previousNode == None:
            print("Starting at {}. ".format(currentNode), end="")
        else:
            print("{} -> {}: ".format(previousNode, currentNode), end="")
        print("Node {} has been encountered {} times.".format(currentNode, self.visitedCount[currentNode]))

        # If the node was visited twice, it's part of a cycle only if we're back to starting node
        if self.visitedCount[currentNode] == 2:
            return currentNode == self.startingNode
        
        # If the current node hasn't been visited twice, move on to its neighbors
        for neighbor in self.graph[currentNode]:
            if (neighbor in self.visitedCount and self.visitedCount[neighbor] == 2) or \
            self.isPartOfCycle(currentNode, neighbor):
                return True
        
        # Non-cycle termination
        return False


    #=============================================================================
    # Removes the given node from the graph (dictionary).
    # @param nodeToRemove - the node to remove from the directed graph
    #=============================================================================
    def __removeNode(self, nodeToRemove):
        print("Removing node {} from the graph.".format(nodeToRemove))

        # Remove the node itself from the graph's key list
        for key in self.graph.keys():
            if key == nodeToRemove:
                self.graph.pop(key, None)
                break
        
        # And now remove all appearances in values
        for key, value in self.graph.items():
            value = [neighbor for neighbor in value if neighbor != nodeToRemove]
            self.graph[key] = value

        # Debugging only
        print("New graph: {}".format(self.graph))