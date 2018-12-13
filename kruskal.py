#Oscar Tobanche
#Prof. Diego Aguirre
#manoj saha
#CS 2302
from graph import Graph, Vertex
collection = dict()
rank = dict()
def make_set(vertice):
    collection[vertice] = vertice

    rank[vertice] = 0


def find(vertice):
    if collection[vertice] != vertice:
        collection[vertice] = find(collection[vertice])

    return collection[vertice]


def union(vertice1, vertice2):
    root1 = find(vertice1)

    root2 = find(vertice2)

    if root1 != root2:

        if rank[root1] > rank[root2]:

            collection[root2] = root1

        else:

            collection[root1] = root2

        if rank[root1] == rank[root2]: rank[root2] += 1


def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

        minimum_spanning_tree = set()

        edges = list(graph['edges'])

        edges.sort()

    # print edges

    for edge in edges:

        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)

            minimum_spanning_tree.add(edge)

    return sorted(minimum_spanning_tree)
if __name__ == "__main__":
    graph = {

        'vertices': ['A', 'B', 'C'],
        'edges': set([
            (11,'A','B'),(13,'B','C'),(20,'A','C')

        ])
    }
    print(kruskal(graph))