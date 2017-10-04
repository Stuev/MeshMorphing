from Face import *
from Edge import *
from Vertex import *

class BREP:
    
    def __init__(self, faces, verts):
        self.vertices = [Vertex(verts[v], v) for v in range(len(verts))]
        
        self.edges = []
        self.faces = []

        # fill in faces and edges
        for face in faces:
            faceEdges = []
            for vert in range(len(face)):
                edge = Edge([self.vertices[face[vert - 1]], self.vertices[face[vert]]], 1)
                
                # check if edge already found   
                alreadyFound = False             
                for e in self.edges:
                    if (edge == e):
                        self.edges.append(e)
                        faceEdges.append(e)
                        alreadyFound = True
                        break
                    elif (edge == e.reversed()):
                        self.edges.append(e.reversed())
                        faceEdges.append(e.reversed())
                        alreadyFound = True
                        break
                        
                if (not alreadyFound):
                    self.edges.append(edge)
                    faceEdges.append(edge)
                    
            # make face
            self.faces.append(Face(faceEdges))

        # update edges leaving vertices
        for v in self.vertices:
            v.setAdjEdges(self.getEdgesLeavingVertex(v))
        
        # update faces adjacent to edges
        for edge in self.edges:
            edge.setAdjFaces(self.getAdjFaces(edge))
        
    def drawSelf(self):
        fill(255)
        for f in self.faces:
            f.drawSelf()
            
    def getEdgesLeavingVertex(self, v):
        adjEdges = []
        for edge in self.edges:
            if v == edge.startVertex:
                adjEdges.append(edge)    
        return adjEdges
    
    def getAdjFaces(self, edge):
        adjFaces = []
        for f in self.faces:
            for e in f.edges:
                if edge == e or edge == e.reversed():
                    adjFaces.append(f)
                    break
        return adjFaces