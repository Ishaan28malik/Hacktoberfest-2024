

import sys
#from heapq import heappop,heappush

class Edge:
    
    def __init__(self, weight, startVertex, endVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.endVertex = endVertex

class Node:
    
    def __init__(self, name):
        
        self.name = name
        self.predecessor = None
        self.minDistance = sys.maxsize
        self.adjList = []
        self.visited = False
    
class bellman:
    
    cycle = False
    def cal_short_path(self, startVertex,vertexList,edgeList):
        
        startVertex.minDistance = 0
        for vertex in vertexList:
            
            for edge in edgeList:
                
                u = edge.startVertex
                v = edge.endVertex
                
                if v.minDistance > u.minDistance + edge.weight:
                    v.minDistance = u.minDistance + edge.weight
                    v.predecessor = u
                
        for edge in edgeList:
            if edge.startVertex.minDistance + edge.weight < edge.endVertex.minDistance:
                bellman.cycle = True
        
    def print_short_path(self, targetVertex):
            
        if bellman.cycle is not True:
            print(targetVertex.minDistance)
            while targetVertex is not None:
                print(targetVertex.name,end=" ")
                targetVertex = targetVertex.predecessor
        else:
            print("Negative cycle detected")
                
n1 = Node("a")
n2 = Node("b")
n3 = Node("c")
n4 = Node("d")
n5 = Node("e")
n6 = Node("f")
n7 = Node("g")
n8 = Node("h")

e1 = Edge(5,n1,n2)
e2 = Edge(8,n2,n3)
e3 = Edge(-20,n3,n1)
e4 = Edge(15,n3,n5)
e5 = Edge(12,n3,n6)
e6 = Edge(-4,n4,n2)
e7 = Edge(9,n5,n4)
e8 = Edge(7,n6,n6)

n1.adjList.append(e1)
n1.adjList.append(e2)
n1.adjList.append(e3)
n2.adjList.append(e4)
n2.adjList.append(e5)
n3.adjList.append(e6)

vertexList = [n1,n2,n3,n4,n5,n6]
#edgeList = [e1,e2,e3,e4,e5,e6,e7,e8]
edgeList = [e1,e2,e3]
algo = bellman()
algo.cal_short_path(n1,vertexList,edgeList)
algo.print_short_path(n8)



            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            