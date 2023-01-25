import matplotlib.pyplot as plt

distance = [15.69, 18.04, 24.29]
I_365 = [4.8, 4.3, 2.86]
I_405 = [6.1, 4.9, 3.3]
I_436 = [6.5, 5.3, 3.5]

plt.plot(distance, I_365, 'ro--', label="365 nm")
plt.plot(distance, I_405, 'go--', label="405 nm")
plt.plot(distance, I_436, 'bo--', label="436 nm")

plt.xlabel("Distance from Probe to Sensor (mm)")
plt.ylabel("Intensity (W/cm^2)")
plt.title("Probe UV Intensity")

plt.legend()
plt.grid(which='major')

plt.show()
