class Graph:
    def __init__(self, n) -> None:
        self.graph = [[False]*n for i in range(n)]
        self.length = n
        self.paths = []

    def add(self, u, v, w):
        self.graph[u][v] = w
        return
    
    def remove(self, u, v):
        self.graph[u][v] = False
        return

    def shortest_path(self, start, end):
        self.shortest_path_help(start, end, [], [False]*self.length, 0)
        if len(self.paths) > 0:
            ans = sorted(self.paths, key=lambda path: path[1])[0][0]
            for i in range(len(ans)):
                print(ans[i], end=" ")
            print(end="\n")
            self.paths = [] #clear the old paths
        else:
            print("-1")
        return
    
    def shortest_path_help(self, start, end, list, visited, sum):
        if visited[start] == True:
            return
        visited[start] = True
        list.append(start)
        if start == end:
            self.paths.append((list, sum))
            return
        for i in range(len(self.graph[start])):
            if self.graph[start][i] != False:
                self.shortest_path_help(i, end, list[:], visited[:], sum+self.graph[start][i])
        return



if __name__ == "__main__":

    graph = Graph(10)
    edges = ((0, 1, 25), (0, 2,  6), (1, 3, 10),
             (1, 4,  3), (2, 3,  7), (2, 5, 25),
             (3, 4, 12), (3, 5, 15), (3, 6,  4),
             (3, 7, 15), (3, 8, 20), (4, 7,  2),
             (5, 8,  2), (6, 7,  8), (6, 8, 13),
             (6, 9, 15), (7, 9,  5), (8, 9,  1))
    for u, v, w in edges:
        graph.add(u, v, w)

    graph.shortest_path(0, 9)   # 0 2 3 6 7 9
    graph.remove(3, 6)
    graph.remove(5, 6)
    graph.shortest_path(0, 9)   # 0 2 3 5 8 9