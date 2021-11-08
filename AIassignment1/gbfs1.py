from os import name
from typing import List
import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import neighbors
from networkx.classes.graph import Graph
from networkx.exception import NetworkXError

graph = nx.Graph()

graph = {
'SportsComplex':[('Siwaka',405)],
'Siwaka':[('Ph.1A',380), ('Ph.1B',280)],
'Ph.1A':[('Mada',630), ('Ph.1B',280)],
'Ph.1B':[('STC',213), ('Phase2',210)],
'STC':[('Phase2',210), ('ParkingLot',0)],
'Phase2':[('STC',213), ('Phase3',160), ('J1',500)],
'Phase3':[('ParkingLot',0)],
'J1':[('Mada',630)],
'Mada':[('ParkingLot',0)]
}

def bfs(start, target, graph, queue=[], visited=[]):
    if start not in visited:
        print(start)
        visited.append(start)
    queue=queue+[x for x in graph[start] if x[0][0] not in visited]
    queue.sort(key=lambda x:x[1])
    if queue[0][0]==target:
        print(queue[0][0])
    else:
        processing=queue[0]
        queue.remove(processing)
        bfs(processing[0], target, graph, queue, visited)
bfs('SportsComplex', 'ParkingLot', graph)


