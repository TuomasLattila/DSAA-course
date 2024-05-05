class Graph:
    def __init__(self, n) -> None:
        self.graph = [[False]*n for i in range(n)]
        self.length = n
        self.paths = []
        self.shortest_paths = []

    def add(self, u, v, w):
        try:
            self.graph[u][v] = w
        except:
            pass
        return
    
    def remove(self, u, v):
        self.graph[u][v] = False
        return

    def all_paths(self):
        self.shortest_paths = [[-1]*self.length for i in range(self.length)]
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                self.all_paths_help(i, j, [], [False]*self.length, 0)
                if len(self.paths) > 0:
                    ans = sorted(self.paths, key=lambda path: path[1])[0][1]
                    self.shortest_paths[i][j] = ans
                    self.paths = [] #clear the old paths
        return self.shortest_paths
    
    def all_paths_help(self, start, end, list, visited, sum):
        if visited[start] == True:
            return
        visited[start] = True
        list.append(start)
        if start == end:
            self.paths.append((list, sum))
            return
        for i in range(len(self.graph[start])):
            if self.graph[start][i] != False:
                self.all_paths_help(i, end, list[:], visited[:], sum+self.graph[start][i])
        return


if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
             (2, 3, 1), (2, 5, 2), (3, 0, 6),
             (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in edges:
        graph.add(u, v, w)

    M = graph.all_paths()
    for weights in M:
        for weight in weights:
            print(f"{weight:3d}", end="")
        print()
    #  0 12  7  8  9  9
    # -1  0 -1 -1 -1 -1
    #  7  5  0  1 16  2
    #  6  8 13  0 15  2
    # -1  7 -1 -1  0  1
    # -1  6 -1 -1 -1  0