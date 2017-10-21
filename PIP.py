from SVector import *
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
        before = len(self.faces)

        for edgeA in self.A.edges:
            for edgeB in self.B.edges:
                
                N = edgeA.X(edgeB)
                # Nes = []
                # for f in (edgeA.adjFaces + edgeB.adjFaces):
                #     Nes += f.infaceNormals
                # Nes = (Nes + f.infaceNormals) for f in (edgeA.adjFaces + edgeB.adjFaces)
                Nes = [crossP3D(edgeA.T, f.N).get_unit() for f in edgeA.adjFaces] + [crossP3D(edgeB.T, f.N).get_unit() for f in edgeB.adjFaces]
                LSD = all([dotP(Ni, N) > 0 for Ni in Nes]) or all([dotP(Ni, N) > 0 for Ni in Nes])
                # LSD = all([dotP(edge.T, N) <= 0 for edge in edgeA.startVertex.adjEdges]) and all([dotP(edge.T, N) <= 0 for edge in edgeB.startVertex.adjEdges]) and all([dotP(edge.T, N) <= 0 for edge in edgeA.endVertex.adjEdges]) and all([dotP(edge.T, N) <= 0 for edge in edgeB.endVertex.adjEdges])

                flipSign = (dotP(Nes[0], N) > 0)
                    
                if LSD:
                    N = N  * -1 if flipSign else N
                    verts = []
                    verts.append(PIPVertex(edgeA.startVertex, edgeB.endVertex))
                    verts.append(PIPVertex(edgeA.startVertex, edgeB.startVertex))
                    verts.append(PIPVertex(edgeA.endVertex, edgeB.startVertex))
                    verts.append(PIPVertex(edgeA.endVertex, edgeB.endVertex))
                    newFace = PIPFace(verts, N)
                    self.faces.append(newFace)
                    
        print(len(self.faces)-before)

                                        
    def VFFaces(self):
        for vert in self.A.vertices:
            for face in self.B.faces:
                # calculate normal
                N = face.N
                
                # add to faces if LSD(N, V, Va)
                LSD = all([dotP(edge.T, N) <= 0 for edge in vert.adjEdges])
                    
                # generate face
                if LSD:
                    verts = [PIPVertex(vert, edge.startVertex) for edge in face.edges]
                    self.faces.append(PIPFace(verts, N))
                    
    def FVFaces(self):
        for vert in self.B.vertices:
            for face in self.A.faces:
                # calculate normal
                N = face.N
                
                # add to faces if LSD(N, V, Va)
                LSD = all([dotP(edge.T, N) <= 0 for edge in vert.adjEdges])
                    
                # generate face
                if LSD:
                    verts = [PIPVertex(edge.startVertex, vert) for edge in face.edges]
                    self.faces.append(PIPFace(verts, N))
                    
    def drawSelf(self, t):
        for f in self.faces:
            f.drawSelf(t)