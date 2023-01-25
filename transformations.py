import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# 0 < Theta < Pi/2 (quarter circle)
# 0 < Phi < 2Pi
Theta = np.arange(0, np.pi/2, (np.pi/2/100))
Phi = np.arange(0, 2*np.pi, (2*np.pi/100))

def sph_to_cart(R, theta, phi):
    x = R*np.sin(theta)*np.cos(phi)
    y = R*np.sin(theta)*np.sin(phi)
    z = R*np.cos(theta)
    return x, y, z

def cart_to_sph(x, y, z):
    R = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arctan(np.sqrt(x**2 + y**2)/z)
    phi = np.arctan(y/x)
    return R, theta, phi

def make_coordinates(R, theta, phi):
    ''' Make a numpy array with x, y, z coordinates '''
    X, Y, Z = sph_to_cart(R, Theta, Phi)
    coordinates = np.array([X, Y, Z])
    #print("Coordinates", coordinates)
    ax = plt.axes(projection = "3d")
    ax.scatter(X, Y, Z)
    #plt.plot(Theta, Phi, "k")
    plt.show()
    pass

if __name__ == "__main__":
    make_coordinates(8.66, 0.63, 1.37)
    # convert from cartesian to spherical coordinates:
    print("Theta shape", np.shape(Theta))
    print("Phi shape", np.shape(Phi))
    x, y, z = 1, 5, 7
    R, theta, phi = cart_to_sph(x, y, z)
    print("Cartesian to spherical")
    print("x:", x, "y:", y, "z:", z)
    print("R:", round(R, 2), "theta:", round(theta, 2), "phi:", round(phi, 2))
    print()
    print("Spherical to cartesian (using above R, theta, phi)")
    x, y, z = sph_to_cart(R, theta, phi)
    print("x:", round(x, 2), "y:", round(y, 2), "z:", round(z, 2))
