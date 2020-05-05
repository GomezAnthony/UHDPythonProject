from algorithims.prims import prims_algorithim
import networkx as nx

G = nx.read_weighted_edgelist('data/G1.txt', nodetype = int)

T = prims_algorithim(G, 2, draw = True, showG = True)



