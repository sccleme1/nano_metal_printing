"""
Printer UV Intensity measurement
"""

import numpy as np
import matplotlib.pyplot as plt

Z_values = np.array([85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95])

I_365_down_blank = np.array([820.3, 820.1, 811, 801, 789, 779, 770, 764, 750, 733, 716])
I_365_up_blank = np.array([802, 804, 800, 792, 783, 773, 766, 758, 746, 730, 715])
I_365_down_image = np.array([7.78, 7.77, 7.69, 7.58, 7.45, 7.35, 7.21, 7.09, 6.97, 6.84, 6.72])
I_365_up_image = np.array([7.65, 7.64, 7.58, 7.5, 7.4, 7.3, 7.18, 7.05, 6.94, 6.83, 6.71])

I_405_down_blank = np.array([996, 988, 987, 965, 949, 931, 919, 906, 885, 865, 842])
I_405_up_blank = np.array([977, 976, 966, 956, 940, 925, 913, 903, 884, 862, 839])
I_405_down_image = np.array([9.4, 9.35, 9.3, 9.05, 8.9, 8.73, 8.54, 8.36, 8.19, 8.02, 7.83])
I_405_up_image = np.array([9.26, 9.23, 9.13, 8.99, 8.83, 8.68, 8.49, 8.34, 8.18, 8.00, 7.84])


plt.figure(1)
plt.title("Printer Intensity, No Image\n(Green = 255)")
plt.xlabel("Z-Setting (mm)")
plt.ylabel("Intensity uW/cm^2")
plt.plot(Z_values, I_365_down_blank, 'b.', label="365 nm")
plt.plot(Z_values, I_365_up_blank, 'b.')
plt.plot(Z_values, I_405_down_blank, 'r.', label="405 nm")
plt.plot(Z_values, I_405_up_blank, 'r.')
plt.axvline(x=91.77, color='k', alpha=0.4, label='Focal Point', linestyle='--')
plt.legend()

plt.figure(2)
plt.title("Printer Intensity, Projecting Image 7\n(Green = 255)")
plt.xlabel("Z-Setting (mm)")
plt.ylabel("Intensity mW/cm^2")
plt.plot(Z_values, I_365_down_image, 'b.', label="365 nm")
plt.plot(Z_values, I_365_up_image, 'b.')
plt.plot(Z_values, I_405_down_image, 'r.', label="405 nm")
plt.plot(Z_values, I_405_up_image, 'r.')
plt.axvline(x=91.77, color='k', alpha=0.4, label='Focal Point', linestyle='--')
plt.legend()

'''
plt.figure(3)
plt.title("R, G, B, Tests")
'''

plt.show()
