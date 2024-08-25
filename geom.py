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
            return np.nan
        else:
            return (-B - np.sqrt(discriminant))/(2*A), (-B + np.sqrt(discriminant))/(2*A)
        
        
def calculate_angles(x, y, z):
    # Calculate angle in y-z plane
    theta_yz = np.arctan2(abs(z), abs(y))
    
    # Calculate angle in x-y plane
    theta_xy = np.arctan2(abs(y), abs(x))
    
    # Convert angles to degrees
    theta_yz_deg = np.degrees(theta_yz)
    theta_xy_deg = np.degrees(theta_xy)
    
    return theta_xy_deg, theta_yz_deg 

def translate_points(A, B, C):
    #Prva je uvek kometica jer nju teramo u koordinatni centar, B i C su zvezda i posmatrac
    Ax, Ay, Az = A
    B_prime = (B[0] - Ax, B[1] - Ay, B[2] - Az)
    C_prime = (C[0] - Ax, C[1] - Ay, C[2] - Az)
    
    A_prime = (0, 0, 0)
    
    return A_prime, B_prime, C_prime