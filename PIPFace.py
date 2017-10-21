class PIPFace:
    
    def __init__(self, verts, N):
        self.vertices = verts
        self.N = N
        
    def drawSelf(self, t):
        beginShape()
        normal(self.N[0], self.N[1], self.N[2])
        for vert in self.vertices:
            val = vert.evaluateAtT(t)
            vertex(val[0], val[1], val[2])
        endShape(CLOSE)
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.N == other.N and set(self.vertices) == set(other.vertices)
        return False
    
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.N != other.N and set(self.vertices) != set(other.vertices)
        return True
    
    def __str__(self):
        returnVal = "["
        for v in self.vertices:
          returnVal += str(v) + ", "
        returnVal +="]"
        return returnVal
        
    def __lt__(self, other):
        return str(self) < str(other)