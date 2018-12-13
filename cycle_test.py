from cycle_finder import CycleFinder

graph = { 'D':['S', 'T'], 'R':['A'], 'A':['S'], 'C':['S'], 
                 'S':[], 'F':['S'], 'W':['F'], 'U':['D'], 'G':['U'],
                 'T':['E'], 'B':['T'], 'E':['V'],
                 'V' : ['G'] }

print("Original graph: {}\n".format(graph))

cycleFinder = CycleFinder(graph)
cycles = cycleFinder.findCycles()

print("Cycle(s): {}".format(cycles))