# Script to plot a cannon's range given its firing angle (theta) and muzzle velocity (v)

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib.ticker import MaxNLocator, LinearLocator

steps_per_variable = 101
theta_range = np.linspace(0, np.pi/2, num=steps_per_variable)  # theta is in radians
v_range = np.linspace(0, 100, num=steps_per_variable)  # v is in m/s

g = 9.81

# Characteristic equation: (2 / g) v^2 sin (theta) cos (theta)
t, v = np.meshgrid(theta_range, v_range)
sin = np.sin(theta_range)
cos = np.cos(theta_range)
# t_deg = np.rad2deg(t)
ra = 2 / g * v**2 * sin * cos

# plot graph
fig = plt.figure()
ax = plt.axes(projection='3d')

# Plot the surface.
surf = ax.plot_surface(t, v, ra, cmap=cm.coolwarm)  #,
                       # linewidth=0, antialiased=False)
ra_contour = ax.plot(t, v, 500)

# Customize axes limits
# ax.set_xlim(0, 90)      # theta
ax.set_ylim(0, 110)    # velocity
z_max = 1200
ax.set_zlim(0, z_max)    # range

ax.zaxis.set_major_locator(LinearLocator(int(z_max/100)+1))  # add tick marks to Z-axis

# # Add a color bar which maps values to colors
# fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_xlabel('theta (rad)')
ax.set_ylabel('v (m/s)')
ax.set_zlabel('range (m)')
ax.set_title('Cannon range')

plt.show()
