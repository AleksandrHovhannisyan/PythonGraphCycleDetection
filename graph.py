from abc import ABC, abstractmethod


class Graph(ABC):

    def __init__(self, graph = dict()):
        '''
        Initializes this Graph. A graph is represented
        as a dictionary mapping nodes to lists of neighbors.
        '''
        self.graph = graph
        super().__init__()

    @abstractmethod
    def insert(self, start, end):
        pass

    @abstractmethod
    def remove(self, nodeToRemove):
        pass

    def __str__(self):
        ''' Returns the contents of this graph in string form. '''
        return self.graph.__str__()

    def __getitem__(self, node):
        ''' Returns the list of neighbors for node or None if node does not exist '''
        if node not in self.graph:
            return None
        return self.graph[node]

    def keys(self):
        ''' Returns a list of this Graph's keys '''
        return self.graph.keys()



class DirectedGraph(Graph):

    def insert(self, start, end):
        '''
        Inserts the given nodes into the graph as a directional mapping of start -> end

        Parameters:
        start - the initial vertex/node
        end - the terminal vertex/node

        Returns: None
        '''
        if start not in self.graph:
            self.graph[start] = list()
        elif end in self.graph[start]:
            return
        self.graph[start].append(end)


    def remove(self, nodeToRemove):
        '''
        Removes the given node from the graph, as well as any of its outgoing
        edges to other nodes, if that node exists.

        Parameters:
        nodeToRemove - the node to remove from the graph

        Returns:
        The neighbors for nodeToRemove, or None if the node did not exist.
        '''
        if nodeToRemove not in self.graph:
            return False
        self.graph.pop(nodeToRemove)
        return True



class UndirectedGraph(Graph):

    def insert(self, start, end):
        '''
        Inserts the given nodes into the graph in a non-directed manner. In other words,
        start -> end and end -> start.

        Parameters:
        start - the initial vertex/node
        end - the terminal vertex/node
        '''
        if start not in self.graph:
            self.graph[start] = list()
        if end not in self.graph:
            self.graph[end] = list()
        if end in self.graph[start]:
            return
        self.graph[start].append(end)
        self.graph[end].append(start)


    def remove(self, nodeToRemove):
        '''
        Removes the given node from the graph, as well as any references to it
        by other nodes. Effectively, the node and all of its undirected edges
        are deleted.

        Parameters:
        nodeToRemove - the node to remove from the graph

        Returns:
        True if the node was successfully removed and False if it wasn't found.
        '''
        if nodeToRemove not in self.graph:
            return False

        # Remove the starting node itself and its outgoing edges
        self.graph.pop(nodeToRemove)

        # And now remove all edges leading to that node from other nodes
        for node, neighbors in self.graph.items():
            self.graph[node] = [neighbor for neighbor in neighbors if neighbor != nodeToRemove]
        return True