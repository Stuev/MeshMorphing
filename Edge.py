from SVector import crossP3D

class Edge:
    
    def __init__(self, vertices, direction, adjFaces = None):
        self.vertices = vertices
        #direction should be -1 or 1 ... 1->forward,  -1->backward
        self.direction = direction
        self.startVertex = vertices[0] if direction > 0 else vertices[1]
        self.endVertex = vertices[1] if direction > 0 else vertices[0]
        self.T = (self.startVertex - self.endVertex).get_unit()
        self.adjFaces = adjFaces
        
    def X(self, edge):
        return crossP3D(self.T, edge.T)
                                                              
    def reversed(self):
        return Edge(self.vertices, -self.direction, self.adjFaces)
    
    def setAdjFaces(self, faces):
        self.adjFaces = faces
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.startVertex == other.startVertex and self.endVertex == other.endVertex
        return False
        
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self == other
        return True        