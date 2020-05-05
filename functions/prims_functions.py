
def cost(G,e):
    return G.edges()[e]['weight']


def valid_incident_edges(G, T):
     
    incident_edges = []
    for e in G.edges():
        for v in T.nodes():
            if v in e: 
                incident_edges.append(e)
                
    valid_edges = []
    for e in incident_edges:
        if e[0] not in T.nodes() or e[1] not in T.nodes():
            valid_edges.append(e)

    return valid_edges

def min_prims_edge(G, T):
    
    possible_edges = valid_incident_edges(G, T)
    min_cost_edge = possible_edges[0]
    for e in possible_edges:
        if cost(G, e) < cost(G, min_cost_edge):
            min_cost_edge  = e
    return min_cost_edge              
