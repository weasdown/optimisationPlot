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
t_deg = np.rad2deg(t)
r = 2 / g * v**2 * sin * cos

# plot graph
fig = plt.figure()
ax = plt.axes(projection='3d')

# Plot the surface.
surf = ax.plot_surface(t_deg, v, r, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize axes limits
ax.set_xlim(0, 90)      # theta
ax.set_ylim(0, 110)    # velocity
ax.set_zlim(0, 1200)    # range

ax.zaxis.set_major_locator(LinearLocator(13))  # add tick marks to Z-axis

# ax.contourf(t, v, r, offset=500, colors='k')
# ax.contour3D(t_deg, v, r, 3, colors='black')  # , colors='k')  # cmap='viridis')

# # Add a color bar which maps values to colors
# fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_xlabel('theta (°)')
ax.set_ylabel('v (m/s)')
ax.set_zlabel('range (m)')
ax.set_title('Cannon range')

plt.show()
