class Graph:
    def __init__(self, n) -> None:
        self.graph = [[False]*n for i in range(n)]
        self.visited = [False]*n
        self.length = n

    def add(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True
        return
    
    def remove(self, u, v):
        self.graph[u][v] = False
        self.graph[v][u] = False
        return
    
    def dft(self, start):
        self.dft_help(start)
        print(end="\n")
        self.visited = [False]*self.length #clear the visited list for further use
        return

    def dft_help(self, start):
        if self.visited[start]:
            return
        self.visited[start] = True
        print(start, end=" ")
        for i in range(len(self.graph[start])):
            if self.graph[start][i]:
                self.dft_help(i)
        return
    
    def bft(self, start):
        queue = [start]
        self.visited[start] = True
        while len(queue) > 0:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            for i in range(len(self.graph[vertex])):
                if self.graph[vertex][i]:
                    if self.visited[i]:
                        continue
                    self.visited[i] = True
                    queue.append(i)
        print(end="\n")
        self.visited = [False]*self.length #clear the visited list for further use
        return



if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2), (0, 4), (2, 1),
             (2, 3), (2, 5), (3, 0),
             (3, 5), (4, 5), (5, 1))
    
    for u, v in edges:
        graph.add(u, v)
        
    graph.dft(0)           # 0 2 1 5 3 4 
    graph.bft(0)           # 0 2 3 4 1 5 

    graph.remove(0, 2)
    graph.remove(2, 5)
    graph.remove(1, 4)

    graph.dft(0)           # 0 3 2 1 5 4 
    graph.bft(0)           # 0 3 4 2 5 1