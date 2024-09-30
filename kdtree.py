import numpy as np
from scipy.spatial import KDTree
from numpy.random import default_rng

class SphereKDTree:
    def __init__(self, points):
        self.points = np.array(points)
        self.tree = None
        self._build_tree()

    def _build_tree(self):
        self.tree = KDTree(self.points)

    def query(self, point, radius):
        res = self.tree.query_ball_point(point, radius, workers = -1)

        count = 0
        for r in res:
            count += len(r)
        return count
    
def generate_points_around_center(center, r, n):
    points = []
    for _ in range(n):
        theta = 2 * np.pi * np.random.random()
        phi = np.arccos(2 * np.random.random() - 1)
        rho = r * np.cbrt(np.random.random()) 

        x = rho * np.sin(phi) * np.cos(theta)
        y = rho * np.sin(phi) * np.sin(theta)
        z = rho * np.cos(phi)

        point = (center[0] + x, center[1] + y, center[2] + z)
        points.append(point)

    return points

def generate_triplets(size, r1, r2, seed = 1234):
    rng = default_rng(seed)
    triplets = np.empty((size, 3))

    for i in range(size):
        while True:
            r = (r1**3 * rng.random())**(1/3)
            if r < r2:
                continue
            
            if rng.random() < 0.9: 
                theta = rng.uniform(np.pi / 2, 3 * np.pi / 2) 
            else:
                theta = rng.uniform(-np.pi / 2, np.pi / 2) 

            phi = np.arccos(2 * rng.random() - 1)
            x = r * np.sin(phi) * np.cos(theta)
            y = r * np.sin(phi) * np.sin(theta)
            z = r * np.cos(phi)
            
            triplets[i] = [x, y, z]
            break
    
    return triplets