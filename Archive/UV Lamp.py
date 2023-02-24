import matplotlib.pyplot as plt

distance = [9, 10, 13, 24]
intensity = [9.2, 8.9, 4.5, 2.2]

plt.plot(distance, intensity, 'r.')
plt.xlabel("Distance (mm)")
plt.ylabel("Intensity (W/cm^2)")
plt.title("Probe UV Intensity")

plt.show()
