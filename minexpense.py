class Graph:
    def __init__(self, n) -> None:
        self.graph = [[False]*n for i in range(n)]
        self.length = n

    def add(self, u, v, w):
        try:
            self.graph[u][v] = w
            self.graph[v][u] = w
        except:
            pass
        return
    
    def remove(self, u, v):
        try:
            self.graph[u][v] = False
            self.graph[v][u] = False
        except:
            pass
        return
    
    def min_expense(self):
        length = self.length
        node = 0
        for i in range(len(self.graph)):
            if sum(self.graph[i]) == 0:
                if node == i:
                    node += 1
                length -= 1
        weight = 0
        visited =[0]*self.length
        path = []
        while True:
            visited[node] = 1
            if sum(visited) == length:
                break
            for i in range(len(self.graph[node])):
                if self.graph[node][i] != False:
                    if visited[i] == 0:
                        path.append({'node':i, 'weight':self.graph[node][i]})
            sorted_path = sorted(path, key=lambda x:x['weight'])
            for j in range(len(sorted_path)):
                if visited[sorted_path[j]['node']] == 0:
                    weight += sorted_path[j]['weight']
                    node = sorted_path[j]['node']
                    path = sorted_path[j+1:]
                    break
        return weight
    
if __name__ == "__main__":
    graph = Graph(6)

    connections = (( 1,  2, 17), ( 4,  6, 14), ( 2,  5, 15),
                ( 3,  4,  3), ( 0,  5, 18), ( 3,  5,  8),
                ( 2,  0,  9), ( 0,  2, 19), ( 0,  1, 10),
                ( 1,  0, 13), ( 4,  1, 12), ( 5,  1,  3))

    for u, v, w in connections:
        graph.add(u, v, w)

    print(graph.min_expense())

    graph.remove(3, 4)
    graph.remove(1, 0)
    graph.remove(4, 1)

    print(graph.min_expense())