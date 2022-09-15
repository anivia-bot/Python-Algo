from collections import defaultdict
 
# Function to build the graph
def build_graph():
    edges = [
        ["A", "B","W"], ["A", "E"],
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F", "W"],
        ["C", "G"], ["D", "E"]
    ]
    graph = defaultdict(list)
     
    # Loop to iterate over every
    # edge of the graph
    for edge in edges:
        for e in edge[1:]:
            
            
            # Creating the graph
            # as adjacency list
            graph[edge[0]].append(e)
            graph[e].append(edge[0])
    return graph
 

graph = build_graph()   
print(graph)
