class Face:
    
    def __init__(self, edges):
        self.edges = edges
        self.adjacentFaces = None
        self.N = edges[-1].reversed().X(edges[0]).get_unit()
        
    def setAdjacentFaces(self, adjacentFaces):
        self.adjacentFaces = adjacentFaces
        
    def drawSelf(self):
        beginShape()
        normal(self.N[0], self.N[1], self.N[2])
        for e in self.edges:
            val = e.startVertex.vector
            vertex(val[0], val[1], val[2])
        endShape(CLOSE)
        