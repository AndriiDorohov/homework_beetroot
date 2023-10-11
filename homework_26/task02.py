# Task 2

# Using breadth-first search write an algorithm that can
# determine the shortest path from each vertex to every other vertex.
# This is called the all-pairs shortest path problem.

from collections import deque
import math


def find_all_shortest_paths(graph):
    num_vertices = len(graph)
    distance_matrix = [[math.inf] * num_vertices for _ in range(num_vertices)]

    for source in range(num_vertices):
        queue = deque()
        queue.append((source, 0))
        distances = {source: 0}

        while queue:
            vertex, distance = queue.popleft()
            for neighbor, weight in graph[vertex]:
                new_distance = distance + weight
                if new_distance < distances.get(neighbor, math.inf):
                    distances[neighbor] = new_distance
                    queue.append((neighbor, new_distance))

        for target, distance in distances.items():
            distance_matrix[source][target] = distance

    return distance_matrix


edges = [(0, 1, 3), (0, 2, 1), (1, 2, 2), (1, 3, 1), (2, 3, 4), (3, 0, 2)]
num_vertices = max(max(src, dest) for src, dest, _ in edges) + 1

graph = {i: [] for i in range(num_vertices)}
for src, dest, weight in edges:
    graph[src].append((dest, weight))

shortest_paths = find_all_shortest_paths(graph)
for row in shortest_paths:
    print(row)
