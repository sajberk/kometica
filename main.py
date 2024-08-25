import geom
import numpy as np
import sys
from visualization import plot_simulation
import kdtree
from numpy.random import default_rng

def generate_triplets(size, r1, r2, seed=12):
    rng = default_rng(seed)
    triplets = np.empty((size, 3))
    
    for i in range(size):
        while True:
            x, y, z = rng.uniform(-r1, r1, size=3)
            distance_squared = x**2 + y**2 + z**2
            if r2**2 < distance_squared < r1**2:
                triplets[i] = [x, y, z]
                break
    
    return triplets

##ulazni podaci
#koordinatni sistem u metrima
n = 1e4 #broj cestica
max_distance = 50e3

star_coords = [-12222, 555, 111]
obs_coords = [0, 0, 0]
obs_view_vec = [125510, 125770, -15920]
comet_coords = [125510, 125770, -15920]
comet_radius = 3000

# transformacije
comet_coords, star_coords, obs_coords, obs_view_vec = geom.translate_points(comet_coords, star_coords, obs_coords, obs_view_vec)
star_coords, obs_coords, obs_view_vec = geom.rotate_to_negative_x_axis(star_coords, obs_coords, obs_view_vec)

#izlaz
column_density = 0
note = "neinicijalizovano"


#ovde umetni transformacije tkd kometa bude u (0 0 0) a zvezdica na negativnom delu x ose 
#potrebne dve translacije, jedna u y-z ravni (da bi se dovela zvezda u x-y ravan) i jedna u x-y ravni da se dovede na x osu 



ray = geom.Ray(obs_coords, obs_view_vec)
#Finding parameter limits
#tj samo gledamo jel prolazimo celu max_dist sferu ili idemo od max_dist do kometice

intersections_max_dist = ray.sphere_intersection(comet_coords, max_distance)
if(isinstance(intersections_max_dist, float) and np.isnan(intersections_max_dist)):
    note = "Nema preseka sa max_dist sferom"
    print("U ovom trenutku kod treba da umre ali nisam stavio sys.exit da bi mogli testici na kraju da prodju, ovo je strahovito odvratno i treba biti napravljeno lepse :lmao:")
    #sys.exit(1)
else:
    t_min, t_max = intersections_max_dist

intersections_comet = ray.sphere_intersection(comet_coords, comet_radius)
if(isinstance(intersections_comet, float) and np.isnan(intersections_comet)):
    #nema preseka sa kometicom ali ako smo vec presekli max_dist sferu onda nas nije ni briga
    pass
else:
    t_max = intersections_comet[0]


# KD BLEJA ############

# dummy tačke, biće ih milijardu al generisemo drvo
generated_points = kdtree.generate_points_around_center(comet_coords, max_distance, int(n))
sphere_tree = kdtree.SphereKDTree(points=generated_points)

ray = geom.Ray(obs_coords, obs_view_vec)
intersections = ray.sphere_intersection(comet_coords, max_distance)
if(isinstance(intersections, float) and np.isnan(intersections)):
    print(":(")
    exit()

# ovo dole ima preseke
#ray = geom.Ray([0,0,0], [12,12,12])
#intersections = ray.sphere_intersection([23,12,98], 100)

intersection_length = np.linalg.norm((ray.parametric(intersections[0]), ray.parametric(intersections[1])))
points_on_the_vector_to_sample = np.linspace(ray.parametric(intersections[0]), ray.parametric(intersections[1]), int(intersection_length/2))


r = 1 # oko svake od tačaka na vektoru pogleda
results = sphere_tree.query(points_on_the_vector_to_sample, r)

exit()
############ KD BLEJA ###########


# da ga vidimo
#plot_simulation(star_coords, obs_coords, obs_view_vec, comet_coords, comet_radius)



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

