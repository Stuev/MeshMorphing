class Vertex:
    
    def __init__(self, vector, index, adjEdges = None):
        self.index = index
        self.vector = vector
        self.adjEdges = adjEdges
        
    def setAdjEdges(self, adjEdges):
        self.adjEdges = adjEdges
        
    def __add__(self, v):    
        return self.vector + v.vector
    
    def __sub__(self, v):
        return self.vector - v.vector
    
    def __div__(self, v):
        return self.vector / v
        
    def __mul__(self, v):
        return self.vector * v
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.index == other.index
        return False
    
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.index != other.index
        return True
    
    def __str__(self):
        return str(self.vector)