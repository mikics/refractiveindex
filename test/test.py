import numpy as np

from refractiveindex import material

au = material.Material(
    filename="data/main/Au/Olmon-sc")

wl0 = np.linspace(400e-9, 500e-9, 20)

print(au.get_permittivity(wavelength=wl0))
print(au.get_permittivity(400e-9))
