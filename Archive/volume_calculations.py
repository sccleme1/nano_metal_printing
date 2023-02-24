import numpy as np

def volume_sphere(R_sphere, theta):
    return (2/3)*np.pi*(R_sphere**3)*(1 - np.cos(theta))

def volume_cylinder(r_cylinder, height):
    return np.pi*height*r_cylinder**2

def total_volume(vol_sphere, vol_cylinder):
    return vol_sphere + vol_cylinder

if __name__ == "__main__":
    Vs = volume_sphere(0.0022, 
