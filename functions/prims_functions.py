
def cost(G,e):
    return G.edges()[e]['weight']

# Function that determines if the edges are incident from each other.
def valid_incident_edges(G, T):
    
    # Loop determines that the edges are incident.
    incident_edges = []
    for e in G.edges():
        for v in T.nodes():
            if v in e: 
                incident_edges.append(e)
     
    # Loop dertermines that the edges dont cycle.          
    valid_edges = []
    for e in incident_edges:
        if e[0] not in T.nodes() or e[1] not in T.nodes():
            valid_edges.append(e)
            
    # If edges are not cycling return valid edge.
    return valid_edges

# Function determines the minimum path to valid edge.
def min_prims_edge(G, T):
    
    # Loop detrmines that the valid edge is a low minimum cost.
    possible_edges = valid_incident_edges(G, T)
    min_cost_edge = possible_edges[0]
    for e in possible_edges:
        if cost(G, e) < cost(G, min_cost_edge):
            min_cost_edge  = e
    return min_cost_edge              
