import geom
import numpy as np
import sys

##ulazni podaci
#koordinatni sistem u metrima
n = 1e9 #broj cestica
max_distance = 50e3

star_coords = [-12222, 555, 111]
obs_coords = [0, 0, 0]
obs_view_vec = [1255125, 12577, -1532]
comet_coords = [1255125, 12577, -1532]
comet_radius = 3000

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

