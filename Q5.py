"""
Implement  a graph-based data  structure  that
allows new  nodes  and  edges  to  be inserted and deleted
"""

#import unittest
import unittest

edges = ['12', '24', '34', '35', '45']

# Undirected, unweighed graph with Adjency Lists
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbours = list() #adjacent are connected vertices

    def add_neighbours(self, node):
        if node not in self.neighbours:
                    self.neighbours.append(node) 
                    self.neighbours.sort()
        
        
class graph:
    Linked_vertices = {} #Linked_vertices is a dictionary, so 
    #checks if vertex passed in is actually a vertex object and doesn't exist in the dictionary yet.
    def add_node(self, node):
        if  (node,Vertex) and (node.name) not in self.Linked_vertices:
            self.Linked_vertices[node.name] = node
            return True
        else:
            return False
    
    #adding an edge means updating the adjency list of both nodes with the other one
    def add_edge(self, start, end):
        if start in self.Linked_vertices and end in self.Linked_vertices:
            self.Linked_vertices[start].add_neighbours(end)
            self.Linked_vertices[end].add_neighbours(start)  
            return True
        else:
            return False

    def delete_edge(self, start, end):
        try:
            if self != None:
                del self[start][end]
                del self[start][end]
                print ('deleted\n', start[1], end[4])
                return True
        except:
                return None 


    #c. Printing the graph.
    def print_graph(self):
        for key in sorted(list(self.Linked_vertices.keys())):
            print(key + str(self.Linked_vertices[key].neighbours))




#visualisation 
#g = graph(v,e)
g = graph()
a = Vertex('0')
g.add_node(a)
g.add_node(Vertex('1'))

for i in range(ord('0'), ord('6')): #it iterates the nodes in the graph
    g.add_node(Vertex(chr(i)))

for edge in edges:
    g.add_edge(edge[:1], edge[1:])
g.print_graph()


class graph(unittest.TestCase):
    self.assertEqual('12', '24')
if __name__ == '__main__':
    unittest.main

