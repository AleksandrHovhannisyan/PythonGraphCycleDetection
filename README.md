# Python Graph Cycle Detection

A simple Python program to detect cycles in a directed graph. Below is a sample image of the graph used for testing [source: Modern Operating Systems, 4th ed]. The left image shows the original nodes in the graph. The right image shows the reduced graph with all identified cycles.

![Image of a graph from Modern Operating Systems, Chapter 6](graph.PNG)

### Using the Class

The `CycleFinder` class expects to be fed an instance of `DirectedGraph` or `UndirectedGraph` (see `graph.py` for definitions of both). Those Graph classes in turn accept a dictionary that maps a node to its neighbors. Optionally, you can avoid initializing them with any dictionary and manually `insert` your nodes into the graphs.

You'll need the following imports:

`from cycle_finder import CycleFinder`

`from graph import DirectedGraph, UndirectedGraph`

### Testing

See `test_graph.py` for an example unit test of the `Graph` classes utilizing the `unittest` library.

See the bottom of `cycle_finder.py` for an example usage of all these classes to identify the cycle in the image above. Note that CycleFinder *will* modify the underlying dictionary once the `findCycles` method is invoked.

Note: If a node does not have any edges originating from it (such as `S` in the sample image provided above), do one of the following:

- If you're initializing a `Graph` object with a dictionary, then specify that node's neighbors as the empty list (`[]`)
- If you're instead manually inserting start-end pairs, then specify `end` as `None`