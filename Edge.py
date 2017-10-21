from SVector import crossP3D

class Edge:
    
    def __init__(self, vertices, adjFaces = []):
        self.startVertex = vertices[0]
        self.endVertex = vertices[1]
        self.T = (self.endVertex - self.startVertex).get_unit()
        self.adjFaces = adjFaces
        self.center = (self.startVertex + self.endVertex) / 2
        
    def X(self, edge):
        return crossP3D(self.T, edge.T)
                                                              
    def reversed(self):
        return Edge([self.endVertex, self.startVertex], self.adjFaces)
    
    def addAdjFaces(self, faces):
        self.adjFaces += faces
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.startVertex == other.startVertex and self.endVertex == other.endVertex
        return False
        
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self == other
        return True       
    
    def __str__(self):
        return str(self.startVertex.vector)