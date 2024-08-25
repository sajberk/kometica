import numpy as np

class Ray:
    def __init__(self, start, vec):
        vec_tmp = []
        for v in vec:
            vec_tmp.append(np.float128(v))
        start_tmp = np.float128(start)
        self.start = start_tmp
        self.vec = np.array(vec_tmp)
        
    def parametric(self, t):
        return self.start + t*self.vec
    
    def sphere_intersection(self, center, radius):
        center = np.array(center)
        A = self.vec[0]**2 + self.vec[1]**2 + self.vec[2]**2
        B = 2*self.vec[0]*(self.start[0] - center[0]) + 2*self.vec[1]*(self.start[1] - center[1]) + 2*self.vec[2]*(self.start[2] - center[2]) 
        C = (self.start[0] - center[0])**2 + (self.start[1] - center[1])**2 + (self.start[2] - center[2])**2 - radius**2
        discriminant = B**2 - 4*A*C
        
        print(A, B, C, discriminant)
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

def translate_points(A, B, C, D):
    #Prva je uvek kometica jer nju teramo u koordinatni centar, B i C su zvezda i posmatrac
    Ax, Ay, Az = A
    B_prime = (B[0] - Ax, B[1] - Ay, B[2] - Az)
    C_prime = (C[0] - Ax, C[1] - Ay, C[2] - Az)
    D_prime = (D[0] - Ax, D[1] - Ay, D[2] - Az)

    A_prime = (0, 0, 0)
    
    return A_prime, B_prime, C_prime, D_prime

def rotate_to_negative_x_axis(B, C, D):
    Bx, By, Bz = B
    
    # oko z ose 
    theta_z = np.arctan2(By, Bx)
    Rz = np.array([
        [np.cos(-theta_z), -np.sin(-theta_z), 0],
        [np.sin(-theta_z), np.cos(-theta_z), 0],
        [0, 0, 1]
    ])
    
    B_rotated_z = np.dot(Rz, B)
    C_rotated_z = np.dot(Rz, C)
    D_rotated_z = np.dot(Rz, D)
    
    # oko y ose
    Bx_rotated_z, _, Bz_rotated_z = B_rotated_z
    theta_y = np.arctan2(Bz_rotated_z, Bx_rotated_z)
    theta_y = -(theta_y - np.deg2rad(180))
    Ry = np.array([
        [np.cos(-theta_y), 0, np.sin(-theta_y)],
        [0, 1, 0],
        [-np.sin(-theta_y), 0, np.cos(-theta_y)]
    ])
    
    B_rotated = np.dot(Ry, B_rotated_z)
    C_rotated = np.dot(Ry, C_rotated_z)
    D_rotated = np.dot(Ry, D_rotated_z)
    
    return B_rotated, C_rotated, D_rotated