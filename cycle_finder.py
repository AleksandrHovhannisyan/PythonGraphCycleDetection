from graph import DirectedGraph


class CycleFinder:

    def __init__(self, graph):
        '''
        Initializes this CycleFinder.

        Parameters:
        graph - an instance of DirectedGraph
        '''
        self.graph = graph
        self.startingNode = None
        self.visitedCount = {}

 
    def findCycles(self):
        '''
        Modifies the underlying graph this CycleFinder represents by trimming away
        all non-cyclical nodes and leaving only the nodes that are part of a cycle.
        '''
        # Initial list of all nodes in the graph
        nodes = list(self.graph.keys())
        # Loop through each node in the graph
        for node in nodes:
            # We need this check because the dict is constantly being modified (node removal)
            if node in self.graph.keys():
                # If the node was not part of a cycle, remove it
                if not self.isPartOfCycle(node):
                    self.graph.remove(node)
        return self.graph


    def isPartOfCycle(self, startingNode):
        '''
        Returns True if the given node is part of a cycle and False otherwise.

        Parameters:
        startingNode - the node at which to start the search
        '''
        # Reset node visitation counters on each iteration of the algorithm
        self.visitedCount.clear()
        # Keep track of the starting node
        self.startingNode = startingNode
        # And initiate the helper algorithm
        return self.__partOfCycle(previousNode=None, currentNode=startingNode)


    def __partOfCycle(self, previousNode, currentNode):
        '''
        Private wrapper/helper function. See isPartOfCycle for usage.
        Returns True if self.startingNode is part of a cycle and False otherwise.

        Parameters:
        previousNode - the node that led us to currentNode
        currentNode - the node we're currently visiting
        '''
        # This is so we avoid tracking all graph nodes. Only do it for nodes in the current path.
        if currentNode not in self.visitedCount:
            self.visitedCount[currentNode] = 0

        # Mark the node as having been visited one more time
        self.visitedCount[currentNode] += 1

        # If the node was visited twice, it's part of a cycle only if we're back to starting node
        if self.__visitedTwice(currentNode):
            return currentNode == self.startingNode
        
        # If the current node hasn't been visited twice, move on to its neighbors
        for neighbor in self.graph[currentNode]:
            if (neighbor in self.visitedCount and self.__visitedTwice(neighbor)) or \
            self.__partOfCycle(currentNode, neighbor):
                return True
        
        # Non-cycle termination
        return False


    def __visitedTwice(self, node):
        ''' Returns True if the given node has been visited twice and False otherwise. '''
        return self.visitedCount[node] == 2



# =================================================================
# Brief test using string nodes
# =================================================================
if __name__ == '__main__':

    graph_dict = { 'D':['S', 'T'], 'R':['A'], 'A':['S'], 'C':['S'], 
                 'S':[], 'F':['S'], 'W':['F'], 'U':['D'], 'G':['U'],
                 'T':['E'], 'B':['T'], 'E':['V'],
                 'V' : ['G'] }

    dgraph = DirectedGraph(graph_dict)
    print("Original graph: {}\n".format(dgraph))
    cycleFinder = CycleFinder(dgraph)
    cycleFinder.findCycles()
    print("Cycle(s): {}".format(dgraph))