import geom
import numpy as np
from sys import exit
from visualization import plot_simulation
import kdtree
from numpy.random import default_rng


num_of_particles = int(1e6) #broj cestica
cloud_radius = 50e3
nucleus_radius = 2e3

star_coords = [-12222, 555, 111]
obs_coords = [0, 0, 0]
obs_view_vec = [125515, 125774, -15921]
comet_coords = [125510, 125770, -15920]
comet_radius = 3000

# transformacije
comet_coords, star_coords, obs_coords, obs_view_vec = geom.translate_points(comet_coords, star_coords, obs_coords, obs_view_vec)
star_coords, obs_coords, obs_view_vec = geom.rotate_to_negative_x_axis(star_coords, obs_coords, obs_view_vec)
ray = geom.Ray(obs_coords, obs_view_vec)

# vizualizacija
plot_simulation(star_coords, obs_coords, obs_view_vec, comet_coords, comet_radius)

intersections = ray.sphere_intersection(comet_coords, cloud_radius)
if(isinstance(intersections, float) and np.isnan(intersections)):
    print(":(")
    exit()

# dummy tačke, biće ih milijardu al generisemo drvo
print("Počinjem generisanje")
seed = 1245780
generated_points = kdtree.generate_triplets(num_of_particles, cloud_radius, nucleus_radius, seed)
sphere_tree = kdtree.SphereKDTree(points=generated_points)


intersection_length = np.linalg.norm((ray.parametric(intersections[0]), ray.parametric(intersections[1])))
points_on_the_vector_to_sample = np.linspace(ray.parametric(intersections[0]), ray.parametric(intersections[1]), int(intersection_length/2))

print("Počinjem pretragu")
r = 30 # oko svake od tačaka na vektoru pogleda
results = sphere_tree.query(points_on_the_vector_to_sample, r)
print(f"Pronadjeno tačaka: {results}")
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

