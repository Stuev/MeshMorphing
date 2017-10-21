class SVector:
    
    def __init__(self, *args):
        self.vals = list(args)
        
    def __add__(self, v):
        if len(self.vals) == len(v.vals):
            new = [self.vals[i] + v.vals[i] for i in range(len(self.vals))]
        return SVector(*new)
    
    def __sub__(self, v):
        if len(self.vals) == len(v.vals):
            new = [self.vals[i] - v.vals[i] for i in range(len(self.vals))]
        return SVector(*new)
    
    def __iadd__(self, v):
        if len(self.vals) == len(v.vals):
            self.vals = [self.vals[i] + v.vals[i] for i in range(len(self.vals))]
        return self
    
    def __isub__(self, v):
        if len(self.vals) == len(v.vals):
            self.vals = [self.vals[i] - v.vals[i] for i in range(len(self.vals))]
        return self
    
    def __div__(self, v):
        new = [self.vals[i] / v for i in range(len(self.vals))]
        return SVector(*new)
    
    def __mul__(self, v):
        new = [self.vals[i] * v for i in range(len(self.vals))]
        return SVector(*new)
    
    def __idiv__(self, v):
        self.vals = [self.vals[i] / v for i in range(len(self.vals))]
        return self   
    
    def __imul__(self, v):
        self.vals = [self.vals[i] * v for i in range(len(self.vals))]
        return self

    def __getitem__(self, i):
        if (0 <= i < range(len(self.vals))):
            return self.vals[i]
        else:
            raise Exception("Invalid key to point")

        
    def __setitem__(self, i, val):
        if (0 <= i < range(len(self.vals))):
            self.vals[i] = val
        else:
            raise Exception("Invalid key to point")
            
    def __str__(self):
        returnVal = "(" + str("%.4f" % round(self.vals[0], 4))
        for i in range(1, len(self.vals)):
            returnVal += ", " + str("%.4f" % round(self.vals[i], 4))
        returnVal += ")"
        
        return returnVal
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.vals == other.vals
        return False
        
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.vals != other.vals
        return True
    
    def magSqd(self):
        return sum([pow(a, 2) for a in self.vals])
    
    def magnitude(self):
        return sqrt(self.magSqd())
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.magSqd() < other.magSqd()
        return False
                
    def normalizeV(self):
        self /= self.magnitude()
        
    def get_unit(self):
        if self.magnitude() == 0:
            return SVector(0.,0.,0.)
        return self / self.magnitude()
    
def distanceSqrd(v1, v2):
    return sum([pow(a - b, 2) for a, b in zip(v1.vals, v2.vals)])

def distance(v1, v2):
    return sqrt(distanceSqrd(v1, v2))

def normalized(v1):
    return v1 / v1.magnitude

def dotP(v1, v2):
    return sum([a * b for a, b in zip(v1.vals, v2.vals)])

def crossP3D(v1, v2):
    return SVector(v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0])
    
def angleDif(v1, v2):
    return acos(v1.dotV(v22) / (v1.magnitude() * v2.magnitude()))
    
def lerpV(v1, v2, t):
    return v1 + (v2 - v1) * t
    
def rand2D():
    pass
    
def rand3D():
    pass
    
def FromAngle2D(angle):
    return SVector(cos(angle), sin(angle))