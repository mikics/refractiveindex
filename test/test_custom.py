import numpy as np

from refractiveindex import custom_material


def test_custom_material():
    wl0 = np.linspace(400e-9, 500e-9, 20)

    eps = np.array([[4.0 + 0.1j, 0.0, 0.0],
                    [0.0, 4.0, 0.0],
                    [9.0, 0.0, 4.0]], dtype=np.complex128)

    eps_tiled = np.tile(eps, (len(wl0), 1, 1))
    custom_mat = custom_material.CustomMaterial(
        wavelengths=wl0, permittivity=eps_tiled)

    print(custom_mat.get_permittivity(401e-9))
    print(custom_mat.get_refractiveindex(401e-9))


def test_interpolation():
    wl0 = np.linspace(1, 4, 2)

    eps_0 = np.array([[1.0 + 1j, 0.0, 0.0],
                      [0.0, 1.0 + 1j, 0.0],
                      [9.0, 0.0, 1.0 + 1j]], dtype=np.complex128)

    eps_1 = np.array([[4.0 + 4j, 0.0, 0.0],
                      [0.0, 4.0 + 4j, 0.0],
                      [9.0, 0.0, 4.0 + 4j]], dtype=np.complex128)

    eps = np.array([eps_0, eps_1])
    custom_mat = custom_material.CustomMaterial(
        wavelengths=wl0, permittivity=eps)

    print(custom_mat.get_permittivity(3))
    print(custom_mat.get_refractiveindex(2))


def test_constant_permittivity():

    wl0 = np.linspace(1, 4, 20)
    eps = 1
    custom_mat = custom_material.CustomMaterial(permittivity=eps)

    print(custom_mat.get_permittivity(wl0))
    print(custom_mat.get_refractiveindex(wl0))


def test_constant_refractive():

    wl0 = np.linspace(1, 4, 20)
    n = 1
    custom_mat = custom_material.CustomMaterial(refractiveIndex=n)

    print(custom_mat.get_permittivity(wl0))
    print(custom_mat.get_refractiveindex(wl0))
