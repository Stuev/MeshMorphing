from SVector import *

class PIPVertex:
    
    def __init__(self, vertA, vertB):
        self.vertA = vertA
        self.vertB = vertB

    def evaluateAtT(self, t):
        return self.vertA * (1.0-t) + self.vertB * t