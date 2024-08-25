import numpy as np
from scipy.spatial import KDTree

class SphereKDTree:
    def __init__(self, points):
        self.points = np.array(points)
        self.tree = None
        self._build_tree()

    def _build_tree(self):
        self.tree = KDTree(self.points)

    def query(self, point, radius):
        res = self.tree.query_ball_point(point, radius)
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