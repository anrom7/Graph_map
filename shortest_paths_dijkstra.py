# https://algotree.org/algorithms/single_source_shortest_path/dijkstras_shortest_path_python/ # O((E+V)Log(V))
import math

def dijkstras_shortest_path(graph, source):
    # Initialize the distance of all the nodes from the source node to infinity
    distances = {vertex: math.inf for vertex in graph.vertices()}
    previous_vertices = {vertex: None for vertex in graph.vertices()}
  
    # Distance of source node to itself is 0
    distances[source] = 0
    # Create a dictionary of { node, distance_from_source }
    dict_vertex_length = {source: 0}

    while dict_vertex_length :

        # Get the key for the smallest value in the dictionary
        # i.e Get the node with the shortest distance from the source
        current_vertex = min(dict_vertex_length, key = dict_vertex_length.get)
        del dict_vertex_length[current_vertex]
            
        for edge in graph.incident_edges(current_vertex):
            adj_vertex = edge.opposite(current_vertex)
            length_to_vertex = edge.element()

            if (distances[adj_vertex] > distances[current_vertex] +
                                       length_to_vertex) :
                distances[adj_vertex] = (distances[current_vertex] +
                                        length_to_vertex)
                dict_vertex_length[adj_vertex] = distances[adj_vertex]
                previous_vertices[adj_vertex] = current_vertex

    for vertex in graph.vertices():
        print(f"Source Node ({source}) -> Destination Node({vertex}) :"
              f"{distances[vertex]}")
        path, current_vertex = list(), vertex
        while previous_vertices[current_vertex] is not None:
            path.append(current_vertex.element())
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.append(current_vertex.element())
        print("Path:", list(reversed(path)))


if __name__ == '__main__':
    from graph_examples import figure_14_14
    graph = figure_14_14()
    for v in graph.vertices():
        if v.element() == "JFK":
            vertex = v
            break
    dijkstras_shortest_path(graph, vertex)
    print("______________________")
    from graph_examples import figure_14_15
    graph = figure_14_15()
    for v in graph.vertices():
        if v.element() == "BWI":
            vertex = v
            break
    dijkstras_shortest_path(graph, vertex)  