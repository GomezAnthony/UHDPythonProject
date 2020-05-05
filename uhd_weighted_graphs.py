from algorithims.prims import prims_algorithim
import networkx as nx

# Use lib to read the graph coordinates into G
G = nx.read_weighted_edgelist('data/G1.txt', nodetype = int)

# Pass G starting point and call the algorithim to start the graph.
T = prims_algorithim(G, 3, draw = True, showG = True)



