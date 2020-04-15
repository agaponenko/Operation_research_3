import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    def find(self, parent, vertice):
        if parent[vertice] != vertice:
            return self.find(parent, parent[vertice])
        else:
            return vertice
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
        for vertice in range(self.vertices):
            parent.append(vertice)
            rank.append(0)
        while j < self.vertices - 1:
            u, v, w = self.graph[i]
            i = i + 1
            if self.find(parent, u) != self.find(parent, v):
                j = j + 1
                result.append([u, v, w])
                self.union(parent, rank, self.find(parent, u), self.find(parent, v))
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
    def Boruvka(self):
        mst_weights = 0
        number = self.vertices
        parent = []
        rank = []
        mst = []
        print("Minimum spanning tree: ")
        mst_graph = nx.Graph()
        for vertice in range(self.vertices):
            parent.append(vertice)
            rank.append(0)
            mst = [-1]*self.vertices
        while number > 1:
            for i in range(len(self.graph)):
                u, v, weight = self.graph[i]
                if self.find(parent, u) != self.find(parent, v):
                    if mst[self.find(parent, u)] == -1 or mst[self.find(parent, u)][2] > weight:
                        mst[self.find(parent, u)] = [u,v,weight]
                    if mst[self.find(parent, v)] == -1 or mst[self.find(parent, v)][2] > weight:
                        mst[self.find(parent, v)] = [u,v,weight]
            for vertice in range(self.vertices):
                if mst[vertice] != -1:
                    u, v, weight = mst[vertice]
                    if self.find(parent, u) != self.find(parent, v):
                        mst_weights += weight
                        self.union(parent, rank, self.find(parent, u), self.find(parent, v))
                        print(u, "->", v, ", weight =", weight)
                        mst_graph.add_edge(u, v, weight=weight)
                        number = number - 1
            mst = [-1] * self.vertices
        print("Sum of all weights:", mst_weights)
        return mst_weights, mst_graph


plt.figure(figsize=(25,15))
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
weights_mst, mst = graph.Boruvka()
plt.subplot(121)
nx.draw_shell(graph_, node_color='deepskyblue', node_size=1400, with_labels=True, width=3, edge_color='navy')
plt.subplot(122)
nx.draw_shell(mst, node_color='deepskyblue', node_size=1400, with_labels=True, width=3, edge_color='navy')
plt.show()