__author__ = 'LC'

"""
Author: Lipisha Chaudhary

This is a demo program that solves the Ice
Maze Problem.
"""

from collections import defaultdict


class Vertex:
    """
    An individual vertex in the graph.
    slots: key:  The identifier for this vertex
    sots: connected_to:  A dictionary of adjacent neighbors, where the key is
        the neighbor (Vertex), and the value is the edge cost (int)
    """

    __slots__ = "key", "connected_to"

    def __init__( self, key ):
        """
        Initialize a vertex
        param: key: The identifier for this vertex
        return: None
        """
        self.key = key
        self.connected_to = dict( )

    def add_neighbor( self, nbr, weight=0 ):
        """
        Connect this vertex to a neighbor with a given weight (default is 0).
        param: nbr (Vertex): The neighbor vertex
        param: weight (int): The edge weight (cost)
        return: None
        """
        self.connected_to[ nbr ] = weight

    def __str__( self ):
        """
        Return a string representation of the vertex and its direct neighbors
        return: The string
        """
        return str( self.key ) + "->" + str(
            [ str( x.key ) for x in self.connected_to ] )

    def get_connections( self ):
        """
        Get the neighbor vertices.
        return: A list of Vertex neighbors
        """
        return self.connected_to.keys( )

    def get_weight( self, nbr ):
        """
        Get the edge cost to a neighbor.
        param: nbr: The neighbor vertex
        return: The weight (int)
        """
        return self.connected_to[ nbr ]

    def __eq__( self, other ):
        """
        To check whether the vertices are equal or not by checking it's key.
        param: other: the vertex to which this one is being compared
        return: true iff both vertices have the same key.
        """
        return self.key == other.key


    def __hash__( self ):
        """
        Since vertices are compared only by their keys, the hash code is
        only based on the key.
        return: the hash of the vertex's key
        """
        return hash( self.key )

class Graph:
    """
    A graph implemented as an adjacency list of vertices.
    slot: vertList: A dictionary that maps a vertex key to a Vertex object
    slot: numVertices:  The total number of vertices in the graph
    """
    __slots__ = 'vertList', 'numVertices'

    def __init__( self, dataFile = None ):
        """
        Initialize the graph
        param: dataFile: a text file of 'name name dist' lines to create
                         a directed graph. If dataFile is None, create
                         an empty graph and use addVertex and add_edge
                         to fill it.
        return: None
        """
        self.vertList = dict()
        self.numVertices = 0
        if dataFile is not None:
            with open( dataFile, "r" ) as graphData:
                for line in graphData.readlines():
                    v1Name, v2Name, weight = line.strip().split()
                    self.add_edge( v1Name, v2Name, weight )

    def addVertex( self, key ):
        """
        Add a new vertex to the graph, or replace an existing one if the
        key is a duplicate.
        param: key: The identifier for the vertex (typically a string)
        return: Vertex
        """
        if key not in self.vertList:
            self.numVertices += 1
        vtx = Vertex( key )
        self.verList[ key ] = vtx
        return vtx

    def getVertex( self, key ):
        """
        Retrieve the vertex from the graph.
        param: key: The vertex identifier
        return: The Vertex in this graph with the given key if it is present,
                 otherwise None
        """
        return self.vertList[ key ]

    def __contains__( self, key ):
        """
        Returns whether the vertex labeled with the key is in the graph or not.
        param: key: The vertex label
        return: True if the vertex is present, and False if not
        """
        return key in self.vertList

    def add_edge( self, src, dest, cost=0 ):
        """
        Add a new directed edge from a source to a destination of an edge cost.
        param: src: The source vertex key
        param: dest: The destination vertex key
        param: cost: The edge cost 
        return: None
        """
        if src not in self.vertList:
            self.numVertices += 1
            self.vertList[ src ] = Vertex( src )
        if dest not in self.vertList:
            self.numVertices += 1
            self.vertList[ dest ] = Vertex( dest )
        self.vertList[ src ].add_neighbor( self.vertList[ dest ], cost )


    def get_vertex_keys( self ):
        """
        Return the collection of keys of the vertices in the graph.
        return: A list of vertex identifiers
        """
        return self.vertList.keys()

    def __str__( self ):
        return "Graph(" + str(self.numVertices) + "):" + \
               str( list( self.vertList.keys() ) )

    def __iter__( self ):
        """
        Return an iterator over the vertices in the graph.
        return: A list iterator over Vertex objects
        """
        return iter( self.vertList.values() )

def makeGraphFunction(maze, g_nodes):
    """
    Creates the graph of the matrix passed.
    param: maze: List of Nodes
    param: g_nodes: Dictionary of related Nodes
    return: Dictionary
    """
    for i in range(maze.__len__()):
        for j in range(maze[i].__len__()):
            k = j
            if maze[i][j] != 0:
             for k in range(k, maze[i].__len__()):
                if maze[i][k] == 0 or k == maze[i].__len__()-1:
                    break
             if k == maze[i].__len__()-1:
                if maze[i][k] == 0:
                     if maze[i][k-1] != maze[i][j]:
                      try:
                       g_nodes[maze[i][j]].append(maze[i][k-1])
                      except KeyError:
                       g_nodes[maze[i][j]] = [maze[i][k-1]]
                else:
                     if maze[i][j] != maze[i][k]:
                      try:
                       g_nodes[maze[i][j]].append(maze[i][k])
                      except KeyError:
                       g_nodes[maze[i][j]] = [maze[i][k]]
             if k < maze[i].__len__()-1:
                   if maze[i][j] != maze[i][k-1]:
                    try:
                      g_nodes[maze[i][j]].append(maze[i][k-1])
                    except KeyError:
                      g_nodes[maze[i][j]] = [maze[i][k-1]]
             k2 = j
             if maze[i][j] != 0:
              for k2 in range(j, -1, -1):
                if maze[i][k2] == 0 or k2 == 0:
                    break
              if k2 == 0:
                if maze[i][k2] == 0:
                   if maze[i][j] != maze[i][k2+1]:
                    try:
                        g_nodes[maze[i][j]].append(maze[i][k2+1])
                    except KeyError:
                        g_nodes[maze[i][j]] = [maze[i][k2+1]]
                else:
                   if maze[i][j] != maze[i][k2]:
                    try:
                      g_nodes[maze[i][j]].append(maze[i][k2])
                      #print('adding 222 ',maze[i][k2],'to ',maze[i][j])
                    except KeyError:
                      g_nodes[maze[i][j]] = [maze[i][k2]]
              if k2 > 0:
                  if maze[i][j] != maze[i][k2+1]:
                    try:
                      g_nodes[maze[i][j]].append(maze[i][k2+1])
                    except KeyError:
                      g_nodes[maze[i][j]] = [maze[i][k2+1]]
            k3 = i
            if maze[i][j] != 0:
             for k3 in range(k3, maze.__len__()):
                if maze[k3][j] == 0 or k3 == maze.__len__() - 1:
                    break
             if k3 == maze.__len__() - 1:
                 if maze[k3][j] == 0:
                    if maze[i][j] != maze[k3 - 1][j]:
                        try:
                         g_nodes[maze[i][j]].append(maze[k3 - 1][j])
                        except KeyError:
                         g_nodes[maze[i][j]] = [maze[k3 - 1][j]]
                 else:
                     if maze[i][j] != maze[k3][j]:
                        try:
                          g_nodes[maze[i][j]].append(maze[k3][j])
                        except KeyError:
                          g_nodes[maze[i][j]] = [maze[k3][j]]
             if k3 < maze.__len__() - 1:
                   if maze[i][j] != maze[k3-1][j]:
                    try:
                     g_nodes[maze[i][j]].append(maze[k3-1][j])
                    except KeyError:
                     g_nodes[maze[i][j]] = [maze[k3-1][j]]
            k4 = i
            if maze[i][j] != 0:
                       for k4 in range(i, -1,-1):
                           if maze[k4][j] == 0 or k4 == 0:
                               break
                       if k4 == 0:
                           if maze[k4][j] == 0:#if edge element is stone
                             if maze[i][j] != maze[k4 + 1][j]:
                               try:
                                   g_nodes[maze[i][j]].append(maze[k4 + 1][j])
                               except KeyError:
                                   g_nodes[maze[i][j]] = [maze[k4 + 1][j]]
                           else:
                              if maze[i][j] != maze[k4][j]:
                               try:
                                   g_nodes[maze[i][j]].append(maze[k4][j])
                               except KeyError:
                                   g_nodes[maze[i][j]] = [maze[k4][j]]
                       if (k4 > 0):
                          if maze[i][j] != maze[k4 + 1][j]:
                           try:
                               g_nodes[maze[i][j]].append(maze[k4 + 1][j])
                           except KeyError:
                               g_nodes[maze[i][j]] = [maze[k4 + 1][j]]
    return g_nodes


def search_path(graph, start, goal):
    """
    Gives the path with minimum number of
    steps required to reach the goal
    param: graph: Dictionary of related nodes
    param: start: starting node
    param: goal: Goal Node
    return: Shortest Path traversed
    """
    visited = []
    queue = [[start]]
    if start == goal:
        return "Start = goal", 0

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                g_path = list(path)
                g_path.append(neighbour)
                queue.append(g_path)
                if neighbour == goal:
                    return g_path, start
            visited.append(node)
    return "No Path", start


def main():
    """
    Open the test files and create a graph.
    Print out the number of steps along with
    the ice block co-ordinate pair.
    """
    with open("test3.txt") as file:
        data = [line.rstrip("\n").split(" ") for line in file]
    final_data = data[1:]
    alpha = ord("A")
    escape = data[0][2]
    m = int(data[0][0])
    n = int(data[0][1])
    for i in range(m):
        for j in range(n):
            if final_data[i][j] == '*':
                final_data[i][j] = 0
            else:
                final_data[i][j] = chr(alpha)
                alpha += 1

    escape_node = final_data[int(escape)][4]
    test_graph = {}
    test_list = []
    maze = makeGraphFunction(final_data, test_graph)
    final_graph = {}
    for keys in maze.keys():
        if keys != escape_node:
            path_result = search_path(maze, keys, escape_node)
            if path_result[0] != "No Path":
                final_graph[path_result[1]] = len(path_result[0]) - 1
            if path_result[0] == "No Path":
                test_list.append(path_result[1])

    if len(test_list) == 0:
        print("All Nodes reach the Escape Node!")
    else:
        print("No Path :", test_list)

    dict_graph = defaultdict(list)
    for keys, count in final_graph.items():
        dict_graph[count].append(keys)

    dict_graph = defaultdict(list)
    for keys, count in final_graph.items():
        dict_graph[count].append(keys)

    g_list = []
    g_nodes = dict()
    for key, value in dict_graph.items():
        # print(key, ':',value)
        for value_item in value:
            for i in range(m):
                for j in range(n):
                    if value_item is final_data[i][j]:
                        tempV = i, j,
                        tempK = str(key)
                        try:
                            g_nodes[tempK].append(tempV)
                        except KeyError:
                            g_nodes[tempK] = [tempV]

    for i in g_nodes:
        print(i, ':', g_nodes[i])


if __name__ == '__main__':
    main()
