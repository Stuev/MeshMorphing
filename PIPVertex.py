from SVector import *

class PIPVertex:
    
    def __init__(self, vertA, vertB):
        self.vertA = vertA
        self.vertB = vertB

    def evaluateAtT(self, t):
        return self.vertA * (1.0-t) + self.vertB * t
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.vertA == other.vertA and self.vertB == other.vertB
        return False
    
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.vertA != other.vertA and self.vertB != other.vertB
        return True
    
    def __hash__(self):
        return hash(self.vertA)
    
    def __str__(self):
        return "[" + str(self.vertA) + ", " + str(self.vertB) + "]"
    
    def __lt__(self, other):
        return self.vertA < other.vertA or (self.vertA == self.vertA and self.vertB < other.vertB)