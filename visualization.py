import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def set_axes_equal(ax):
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    y_range = abs(y_limits[1] - y_limits[0])
    z_range = abs(z_limits[1] - z_limits[0])

    max_range = max([x_range, y_range, z_range])

    x_middle = np.mean(x_limits)
    y_middle = np.mean(y_limits)
    z_middle = np.mean(z_limits)

    ax.set_xlim3d([x_middle - max_range/2, x_middle + max_range/2])
    ax.set_ylim3d([y_middle - max_range/2, y_middle + max_range/2])
    ax.set_zlim3d([z_middle - max_range/2, z_middle + max_range/2])

def plot_simulation(star_coords, obs_coords, obs_view_vec, comet_coords, comet_radius, dust_points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # plotujemo tri tela i vektor pogleda
    ax.scatter(obs_coords[0], obs_coords[1], obs_coords[2], color='blue', s=100, label='Observer')

    ax.scatter(star_coords[0], star_coords[1], star_coords[2], color='yellow', s=200, label='Star')

    ax.scatter(comet_coords[0], comet_coords[1], comet_coords[2], color='red', s=100, label='Comet')

    for dust in dust_points:
        ax.scatter(dust[0], dust[1], dust[2], color="grey", s=10)

    ax.plot([obs_coords[0], obs_coords[0] + 2*obs_view_vec[0]], [obs_coords[1], obs_coords[1] + 2*obs_view_vec[1]], [obs_coords[2], obs_coords[2] + 2*obs_view_vec[2]], linewidth=2)


    # kometica 3d sfera
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = comet_radius * np.cos(u) * np.sin(v) + comet_coords[0]
    y = comet_radius * np.sin(u) * np.sin(v) + comet_coords[1]
    z = comet_radius * np.cos(v) + comet_coords[2]
    ax.plot_wireframe(x, y, z, color="r", alpha=0.3)

  
    set_axes_equal(ax)

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    ax.set_title("kometicaaa")

    ax.legend()

    plt.show()
