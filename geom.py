import numpy as np

class Ray:
    def __init__(self, start, vec):
        self.start = np.array(start)
        self.vec = np.array(vec)
        
    def parametric(self, t):
        return self.start + t*self.vec
    
    def sphere_intersection(self, center, radius):
        center = np.array(center)
        A = self.vec[0]**2 + self.vec[1]**2 + self.vec[2]**2
        B = 2*self.vec[0]*(self.start[0] - center[0]) + 2*self.vec[1]*(self.start[1] - center[1]) + 2*self.vec[2]*(self.start[2] - center[2]) 
        C = (self.start[0] - center[0])**2 + (self.start[1] - center[1])**2 + (self.start[2] - center[2])**2 - radius**2
        discriminant = B**2 - 4*A*C
        
        if(discriminant <= 0):
            return np.NAN
        else:
            return (-B - np.sqrt(discriminant))/(2*A), (-B + np.sqrt(discriminant))/(2*A)