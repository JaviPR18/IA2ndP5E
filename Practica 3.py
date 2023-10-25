# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:52:51 2023

@author: javip
"""

import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Ejemplo de uso
grafo_ejemplo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 3, 'D': 2},
    'C': {'A': 4, 'B': 3, 'D': 5},
    'D': {'B': 2, 'C': 5, 'E': 1},
    'E': {'D': 1}
}

nodo_inicio = 'A'
resultados = dijkstra(grafo_ejemplo, nodo_inicio)
print(f"Distancias más cortas desde {nodo_inicio}: {resultados}")
