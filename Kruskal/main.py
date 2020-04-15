import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    def union(self, parent, rank, x, y):
        x_ = self.find(parent, x)
        y_ = self.find(parent, y)
        if rank[x_] < rank[y_]:
            parent[x_] = y_
        elif rank[x_] > rank[y_]:
            parent[y_] = x_
        else:
            parent[y_] = x_
            rank[x_] += 1
    def Kruskal(self):
        result = []
        i = 0
        j = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [];
        rank = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        while j < self.vertices - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                j = j + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        print("Minimum spanning tree: ")
        mst = nx.Graph()
        w_sum = 0.
        weights_mst = []
        for u, v, weight in result:
            mst.add_edge(u, v, weight=weight)
            print(u,"->", v,", weight =", weight)
            weights_mst.append(weight)
            w_sum += weight
        print("Sum of all weights:", w_sum)
        return mst, weights_mst

plt.figure(figsize=(25,12))
print("Enter the number of vertices: ")
vertices = int(input())
print("Enter the number of edges: ")
edges = int(input())
graph = Graph(vertices)
graph_ = nx.Graph()
weights = []
print("Enter source vertex, destination vertex and weight for each edge:")
for i in range(edges):
    u, v , w = [int(j) for j in input().split()]
    graph.addEdge(u, v , w)
    graph_.add_edge(u, v, weight=w)
    weights.append(w)
mst, weights_mst = graph.Kruskal()
plt.subplot(121)
nx.draw_shell(graph_, node_color='deepskyblue', node_size=900, with_labels=True, width=3, edge_color='navy')
plt.subplot(122)
nx.draw_shell(mst, node_color='deepskyblue', node_size=900, with_labels=True, width=3, edge_color='navy')
plt.show()