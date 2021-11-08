from os import name
from typing import List
import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import neighbors
from networkx.classes.graph import Graph
from networkx.exception import NetworkXError
#from gbfs import gbfs

#create an empty graph
G = nx.Graph()

#add the nodes to the graph
nodes = ["SportsComplex","Siwaka","Ph.1A","Ph.1B","STC","Phase2","J1","Mada","Phase3","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()

#add edges and length of the edges
#length in this case is the distance between them in meters
G.add_edge("SportsComplex","Siwaka",length = "450")
G.add_edge("Siwaka","Ph.1A",length = "10")
G.add_edge("Siwaka","Ph.1B",length = "230")
G.add_edge("Ph.1A","Ph.1B",length  = "100")
G.add_edge("Ph.1B","STC",length    = "50")
G.add_edge("STC","Phase2",length   ="50")
G.add_edge("Ph.1B","Phase2",length ="112")
G.add_edge("Ph.1A","Mada",length   = "850")
G.add_edge("Phase2","J1",length    = "600")
G.add_edge("J1","Mada",length      = "200")
G.add_edge("STC","ParkingLot",length = "250")
G.add_edge("Phase2","Phase3",length  = "500")
G.add_edge("Phase3","ParkingLot",length = "350")
G.add_edge("Mada","ParkingLot",length   = "700")

#position the nodes to look like the graph
G.nodes["SportsComplex"]['pos'] = (0,0)
G.nodes["Siwaka"]['pos']        = (2,0)
G.nodes["Ph.1A"]['pos']         = (4,0)
G.nodes["Ph.1B"]['pos']         = (4,-2)
G.nodes["STC"]['pos']           = (4,-4)
G.nodes["Phase2"]['pos']        = (6,-2)
G.nodes["J1"]['pos']            = (8,-2)
G.nodes["Mada"]['pos']          = (10,-2)
G.nodes["Phase3"]['pos']        = (8,-4)
G.nodes["ParkingLot"]['pos']    = (8,-6)

#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')

#dictionary to store the heuristics for GBFS
heuristics = {}
heuristics['SportsComplex'] = 730
heuristics['Siwaka']        = 405
heuristics['Ph.1A']         = 380
heuristics['Ph.1B']         = 280
heuristics['STC']           = 213
heuristics['Phase2']        = 210
heuristics['J1']            = 500
heuristics['Mada']          = 630
heuristics['Phase3']        = 160
heuristics['ParkingLot']    = 0

#v = heuristics.get("Siwaka")
#print(v)

#n = list(G.neighbors("Mada"))
#print(n)

#Greedy bfs
#Step 1: Place the starting node into the OPEN list.
#Step 2: If the OPEN list is empty, Stop and return failure.
#Step 3: Remove the node n, from the OPEN list which has the lowest value of h(n), and places it in the CLOSED list.
#Step 4: Expand the node n, and generate the successors of node n.
#Step 5: Check each successor of node n, and find whether any node is a goal node or not. If any successor node is goal node, then return success and terminate the search, else proceed to Step 6.
#Step 6: For each successor node, algorithm checks for evaluation function f(n), and then check if the node has been in either OPEN or CLOSED list. If the node has not been in both list, then add it to the OPEN list.
#Step 7: Return to Step 2.

class Node:
    def __init__(self,name):
        self.name = name
        self.heuristics = 0

    def __lt__(self, other):
        return self.heuristics < other.heuristics

'''def __lt__(self, other):
    n = heuristics.get(self)
    m = heuristics.get(other)
    return n < m'''

open = []    #unvisited nodes
closed = []  #visited nodes
path = []    #path to destination

#sorted(mylist, key=lambda x: x % 2 == 0)


start_node = "SportsComplex"
goal_node = "ParkingLot"

open.append("SportsComplex")
open.append("Siwaka")
open.append("Mada")
open.append("Ph.1A")

print(open)
open.sort()
print(open)
open.sort(key=lambda x:heuristics)
print(open)

#Step 1
'''open.append(start_node)
path.append(start_node)
print(open)
print(path)

while len(open) > 0:
    open.sort()'''


# Run gbfs algorithm
#gbfs_path = gbfs(G, heuristics, 'SportsComplex', 'ParkingLot')
#print(gbfs_path)
#print()

#draw the graph and visualize
'''arc_length = nx.get_edge_attributes(G,'length')
nx.draw_networkx(G, node_pos, node_size = 450)
nx.draw_networkx_edges(G, node_pos,width = 2)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)
nx.draw_networkx_edge_labels(G, node_pos, edge_labels = arc_length)
plt.axis('off')
plt.show()'''












