class Graph:
    def __init__(self, n) -> None:
        self.graph = [[False]*n for i in range(n)]
        self.visited = [False]*n
        self.length = n
        self.subgraph_list = [None]*n

    def add(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True
        return
    
    def remove(self, u, v):
        self.graph[u][v] = False
        self.graph[v][u] = False
        return
    
    def subgraphs(self):
        for i in range(len(self.graph)):
            self.subgraphs_help(i, i)
        values = set(self.subgraph_list)
        self.subgraph_list = [None]*self.length
        return len(values)


    def subgraphs_help(self, node, substitute):
        if self.subgraph_list[node] != None:
            return
        self.subgraph_list[node] = substitute
        for i in range(len(self.graph[node])):
            if self.graph[node][i] != False:
                self.subgraphs_help(i, substitute)
        return



if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 4), (2, 1),
             (2, 5), (3, 0),
             (5, 1))
    for u, v in edges:
        graph.add(u, v)
    
    print(graph.subgraphs())  # 2
    
    more_connections = ((0, 2), (2, 3),
                        (3, 5), (4, 5))
    for u, v in more_connections:
        graph.add(u, v)

    print(graph.subgraphs())  # 1