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
        