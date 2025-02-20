import numpy
import scipy

from .material import get_array


class CustomMaterial():

    def __init__(self, wavelengths=None, permittivity=None, refractive_index=None, permeability=None):

        if permittivity is not None and refractive_index is not None:
            raise Exception(
                'To define a custom material, either the permittivity or the refractive index must be defined')

        if permeability is None:
            if wavelengths is None:
                permeability = 1
            else:
                permeability = numpy.ones(len(wavelengths))

        if permittivity is None and refractive_index is None:
            if wavelengths is None:
                permittivity = 1
                refractive_index = 1
            else:
                permittivity = numpy.ones(len(wavelengths))
                refractive_index = numpy.ones(len(wavelengths))

        if permittivity is not None:
            if wavelengths is None:
                wavelengths = 0
            self.permittivity = TabulatedData.\
                FromLists(wavelengths, permittivity)

            self.refractive_index = TabulatedData.\
                FromLists(wavelengths, numpy.sqrt(permittivity))

        if refractive_index is not None:
            if wavelengths is None:
                wavelengths = 0
            self.refractive_index = TabulatedData.\
                FromLists(wavelengths, refractive_index)

            self.permittivity = TabulatedData.\
                FromLists(wavelengths, refractive_index ** 2)

        if permeability is not None:
            if wavelengths is None:
                wavelengths = 0
            self.permeability = TabulatedData.\
                FromLists(wavelengths, permeability)

        self.rangeMin = numpy.min(wavelengths)
        self.rangeMax = numpy.max(wavelengths)

        self.get_refractiveindex = self.refractive_index.get_data
        self.get_complete_refractive = self.refractive_index.get_complete_data

        self.get_permittivity = self.permittivity.get_data
        self.get_complete_permittivity = self.permittivity.get_complete_data

        self.get_permeability = self.permeability.get_data
        self.get_complete_permeability = self.permeability.get_complete_data


class TabulatedData:

    def __init__(self, wavelengths, values):
        self.rangeMin = numpy.min(wavelengths)
        self.rangeMax = numpy.max(wavelengths)

        if self.rangeMin == self.rangeMax:
            self.get_function = values
        else:
            self.get_function = scipy.interpolate.interp1d(wavelengths,
                                                           values, axis=0)
        self.wavelengths = wavelengths
        self.coefficients = values

    @staticmethod
    def FromLists(wavelengths, values):
        return TabulatedData(wavelengths, values)

    @get_array
    def get_data(self, wavelength):

        if self.rangeMin == self.rangeMax:
            return self.get_function
        elif self.rangeMin <= wavelength <= self.rangeMax and\
                self.rangeMin != self.rangeMax:
            return self.get_function(wavelength)
        else:
            raise Exception('Wavelength {} is out of bounds.'
                            'Correct range(um): ({}, {})'
                            .format(wavelength, self.rangeMin, self.rangeMax))

    def get_complete_data(self):
        extlist = [[
            self.wavelengths[i], self.coefficients[i]]
            for i in range(len(self.wavelengths))]
        return extlist
