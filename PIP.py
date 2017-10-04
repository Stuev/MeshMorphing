from SVector import crossP3D, normalized
from PIPFace import *
from PIPVertex import *

class PIP:
    
    def __init__(self, A, B):
        self.A = A
        self.B = B
        
        # PIP vertices are in pairs, there is an A and B component
        self.faces = []
        # generate VF faces
        self.VFFaces()        
        # generate FV faces
        self.FVFaces()                    
        # generate EE faces
        self.EEFaces()
 
    def EEFaces(self):
        for edgeA in self.A.edges:
            for edgeB in self.B.edges:
                # calculate normal
                N = crossP3D(edgeA.T, edgeB.T)
                # generate tentative face
                
                # add to faces if LSD(N, V, Va)
                adjFacesA = edgeA.adjFaces
                adjFacesB = edgeB.adjFaces
                # construct list of inface normals
                Nes = [(crossP3D(f.N, edgeA.T)).get_unit() for f in adjFacesA]
                NeB = [(crossP3D(f.N, edgeB.T)).get_unit() for f in adjFacesB]
                Nes += NeB
                
                LSD = True
                isPositive = dotP(Nes[0], N) > 0
                for Ne in Nes:
                    if dotP(Ne, N) > 0 != isPositive:
                        LSD = False
                        break
                
                if (LSD):
                    N = N if isPositive else N * -1
                    verts = []
                    verts.append(PIPVertex(edgeA.startVertex, edgeB.endVertex))
                    verts.append(PIPVertex(edgeA.startVertex, edgeB.startVertex))
                    verts.append(PIPVertex(edgeA.endVertex, edgeB.startVertex))
                    verts.append(PIPVertex(edgeA.endVertex, edgeB.endVertex))
                    self.faces.append(PIPFace(verts, N))
                                        
    def VFFaces(self):
        for vert in self.A.vertices:
            for face in self.B.faces:
                # calculate normal
                N = face.N
                
                # add to faces if LSD(N, V, Va)
                adjEdges = vert.adjEdges
                LSD = True
                for edge in adjEdges:
                    if dotP(edge.T, N) < 0:
                        LSD = False
                        break
                    
                # generate face
                if LSD:
                    verts = []
                    for edge in face.edges:
                        verts.append(PIPVertex(vert, edge.startVertex))
                    self.faces.append(PIPFace(verts, N))
                    
    def FVFaces(self):
        for vert in self.B.vertices:
            for face in self.A.faces:
                # calculate normal
                N = face.N
                
                # add to faces if LSD(N, V, Va)
                adjEdges = vert.adjEdges
                LSD = True
                for edge in adjEdges:
                    if dotP(edge.T, N) < 0:
                        LSD = False
                        break
                    
                # generate face
                if LSD:
                    verts = []
                    for edge in face.edges:
                        verts.append(PIPVertex(edge.startVertex, vert))
                    self.faces.append(PIPFace(verts, N))
                    
    def drawSelf(self, t):
        for f in self.faces:
            f.drawSelf(t)