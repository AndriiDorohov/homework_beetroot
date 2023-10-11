# Task 1

# Modify the 'depth-first search' to produce strongly connected
# components (Strongly Connected Components ).

from typing import Dict, List, Tuple, Optional


class Vertex:
    def __init__(self, key: int) -> None:
        self._id = key
        self.adjacent: List[Vertex] = []
        self.visited = False

    def add_neighbor(self, nbr) -> None:
        self.adjacent.append(nbr)

    def __str__(self) -> str:
        return f"{self._id} connected to: {[x.get_id() for x in self.adjacent]}"

    def get_connections(self) -> List["Vertex"]:
        return self.adjacent

    def get_id(self) -> int:
        return self._id


class Graph:
    def __init__(self):
        self.vertices: Dict[int, Vertex] = {}

    def add_vertex(self, id: int):
        if id not in self.vertices:
            self.vertices[id] = Vertex(id)

    def add_edge(self, from_id: int, to_id: int):
        if from_id in self.vertices and to_id in self.vertices:
            self.vertices[from_id].adjacent.append(self.vertices[to_id])

    def dfs(self, start_id: int, stack: List[Vertex]):
        start_vertex = self.vertices[start_id]
        start_vertex.visited = True

        for neighbor in start_vertex.adjacent:
            if not neighbor.visited:
                self.dfs(neighbor.get_id(), stack)

        stack.append(start_vertex)

    def transpose(self):
        transposed_graph = Graph()

        for vertex_id in self.vertices:
            transposed_graph.add_vertex(vertex_id)

        for vertex_id in self.vertices:
            for neighbor in self.vertices[vertex_id].adjacent:
                transposed_graph.add_edge(neighbor.get_id(), vertex_id)

        return transposed_graph

    def get_scc(self) -> List[List[int]]:
        stack = []
        scc_list = []

        for vertex_id in self.vertices:
            if not self.vertices[vertex_id].visited:
                self.dfs(vertex_id, stack)

        transposed_graph = self.transpose()

        for vertex_id in self.vertices:
            self.vertices[vertex_id].visited = False

        while stack:
            current_vertex = stack.pop()
            scc = []

            if not current_vertex.visited:
                transposed_graph.dfs(current_vertex.get_id(), scc)
                scc_list.append([v.get_id() for v in scc])

        return scc_list


def print_scc_result(scc_result: List[List[int]]):
    print("SCCs in the graph:")
    for scc in scc_result:
        print(" ".join(map(str, scc)))


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 0)
    g.add_edge(5, 4)
    g.add_edge(5, 2)

    scc_result = g.get_scc()
    print_scc_result(scc_result)
