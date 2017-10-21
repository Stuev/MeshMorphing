from SVector import *

class Face:
    
    def __init__(self, edges):
        self.edges = edges
        self.adjacentFaces = None
        self.N = edges[-1].reversed().X(edges[0]).get_unit()
        # self.infaceNormals = [crossP3D(edge.T, self.N).get_unit() for edge in self.edges]
        self.center = SVector(0,0,0)
        for e in self.edges:
            self.center += e.startVertex.vector
        self.center /= len(self.edges)
        for edge in self.edges:
            edge.addAdjFaces([self])
                    
    def addAdjacentFaces(self, adjacentFaces):
        self.adjacentFaces += adjacentFaces
        
    def drawSelf(self):
        beginShape()
        normal(self.N[0], self.N[1], self.N[2])
        for e in self.edges:
            val = e.startVertex.vector
            vertex(val[0], val[1], val[2])
        endShape(CLOSE)
        
    def drawSelfDebug(self):
        beginShape()
        normal(self.N[0], self.N[1], self.N[2])
        for e in self.edges:
            val = e.startVertex.vector
            vertex(val[0], val[1], val[2])
        endShape(CLOSE)
        
        # draw normals
        pushStyle()
        stroke(200, 0, 200)
        line(self.center[0], self.center[1], self.center[2], self.center[0] + self.N[0] * .1, self.center[1] + self.N[1] * .1, self.center[2] + self.N[2] * .1)
        popStyle()
        
        #draw inface normals
        pushStyle()
        stroke(0,200,0)
        for e in self.edges:
            Nes = [crossP3D(e.T, f.N).get_unit() for f in e.adjFaces]
            # for Ni in Nes:
            Ni = Nes[0] if len(Nes)>0 else None
            if Ni:
                line(e.center[0], e.center[1], e.center[2], e.center[0] + Ni[0] * .1, e.center[1] + Ni[1] * .1, e.center[2] + Ni[2] * .1)

        popStyle()
        
    def __str__(self):
        st = ''
        for e in self.edges:
            st += str(e) + " "
        return st