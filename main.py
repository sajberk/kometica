import geom
import numpy as np
import math
from sys import exit
from visualization import plot_simulation
import kdtree
from numpy.random import default_rng


num_of_particles = int(1e2) #broj cestica

nucleus_radius = 2 #2e3
cloud_radius = 50 #50e3

star_coords = [100, 0, 0]
obs_coords = [-100, 31, 0]
obs_view_vec = [100, 0, 0]
comet_coords = [0, 0, 0]


# transformacije
comet_coords, star_coords, obs_coords, obs_view_vec = geom.translate_points(comet_coords, star_coords, obs_coords, obs_view_vec)
star_coords, obs_coords, obs_view_vec = geom.rotate_to_negative_x_axis(star_coords, obs_coords, obs_view_vec)
ray = geom.Ray(obs_coords, obs_view_vec)


intersections = ray.sphere_intersection(comet_coords, cloud_radius)
if(isinstance(intersections, float) and np.isnan(intersections)):
    print(":(")
    exit()

# dummy tačke, biće ih milijardu al generisemo drvo
print("Počinjem generisanje")
seed = 1245780
generated_points = kdtree.generate_triplets(num_of_particles, cloud_radius, nucleus_radius, seed)
sphere_tree = kdtree.SphereKDTree(points=generated_points)

print("Počinjem pretragu")
r = 30 # oko svake od tačaka na vektoru pogleda

intersection_length = np.linalg.norm((ray.parametric(intersections[0]) - ray.parametric(intersections[1])))
points_on_the_vector_to_sample = np.linspace(ray.parametric(intersections[0]), ray.parametric(intersections[1]), math.ceil(intersection_length/(r*2)))
print(f"Dust cloud volume: {int((4/3) * math.pi * cloud_radius**3)}")
print(f"Search bubbles total volume: {int(len(points_on_the_vector_to_sample) * (4/3) * math.pi * r**3)}")


results = sphere_tree.query(points_on_the_vector_to_sample, r)
print(f"Pronadjeno tačaka: {results}")

# vizualizacija
plot_simulation(star_coords, obs_coords, obs_view_vec, comet_coords, cloud_radius, generated_points)
exit()


##testici da vidim jel radi :) 
#TODO eventualno prebaci u zaseban tests.py
print("\nTestici\n")
ray = geom.Ray([0,0,0], [12,12,12])
intersections = ray.sphere_intersection([23,12,98], 10)
if(isinstance(intersections, float) and np.isnan(intersections)):
    print(":(")
else:
    print(ray.parametric(intersections[0]))
    print(ray.parametric(intersections[1]))

ray = geom.Ray([0,0,0], [12,12,12])
intersections = ray.sphere_intersection([23,12,98], 100)
if(isinstance(intersections, float) and np.isnan(intersections)):
    print(":(")
else:
    print(ray.parametric(intersections[0]))
    print(ray.parametric(intersections[1]))

