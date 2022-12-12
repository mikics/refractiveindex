import numpy
import scipy

from .material import get_array


class CustomMaterial():

    def __init__(self, wavelengths=None, permittivity=None, refractiveIndex=None):

        if permittivity is not None and refractiveIndex is not None:
            raise Exception(
                'To define a custom material, either the permittivity or the refractive index must be defined')

        if permittivity is not None:
            if wavelengths is None:
                wavelengths = 0
                permittivity = numpy.array([permittivity])
            self.permittivity = TabulatedPermittivityData.\
                FromLists(wavelengths, permittivity)

            self.refractiveIndex = TabulatedRefractiveIndexData.\
                FromLists(wavelengths, numpy.sqrt(permittivity))

        if refractiveIndex is not None:
            if wavelengths is None:
                wavelengths = 0
                refractiveIndex = numpy.array([refractiveIndex])
            self.refractiveIndex = TabulatedRefractiveIndexData.\
                FromLists(wavelengths, refractiveIndex)

            self.permittivity = TabulatedPermittivityData.\
                FromLists(wavelengths, refractiveIndex**2)

        self.rangeMin = numpy.min(wavelengths)
        self.rangeMax = numpy.max(wavelengths)
        self.get_refractiveindex = self.refractiveIndex.get_refractiveindex
        self.get_complete_refractive = self.refractiveIndex.get_complete_refractive
        self.get_permittivity = self.permittivity.get_permittivity
        self.get_complete_permittivity = self.permittivity.get_complete_permittivity


class TabulatedPermittivityData:

    """Tabulated Permittivity class"""

    def __init__(self, wavelengths, values):
        """
        Crete a TabulatedPermittivityData from a list of
        wavelengths and values

        :param wavelengths:
        :param values:
        """
        self.rangeMin = numpy.min(wavelengths)
        self.rangeMax = numpy.max(wavelengths)

        if self.rangeMin == self.rangeMax:
            self.permittivityFunction = values
        else:
            self.permittivityFunction = scipy.interpolate.interp1d(wavelengths,
                                                                   values, axis=0)
        self.wavelengths = wavelengths
        self.coefficients = values

    @staticmethod
    def FromLists(wavelengths, values):
        """
        Crete a TabulatedRefractiveIndexData from a list of
        wavelengths and values
        """
        return TabulatedPermittivityData(wavelengths, values)

    @get_array
    def get_permittivity(self, wavelength):

        if self.rangeMin == self.rangeMax:
            return self.permittivityFunction
        elif self.rangeMin <= wavelength <= self.rangeMax and\
                self.rangeMin != self.rangeMax:
            return self.permittivityFunction(wavelength)
        else:
            raise Exception('Wavelength {} is out of bounds.'
                            'Correct range(um): ({}, {})'
                            .format(wavelength, self.rangeMin, self.rangeMax))

    def get_complete_permittivity(self):
        extlist = [[
            self.wavelengths[i], self.coefficients[i]]
            for i in range(len(self.wavelengths))]
        return extlist


class TabulatedRefractiveIndexData:
    """Tabulated RefractiveIndex class"""

    def __init__(self, wavelengths, values):
        """
        Crete a TabulatedRefractiveIndexData from a list of
        wavelengths and values

        :param wavelengths:
        :param values:
        """
        self.rangeMin = numpy.min(wavelengths)
        self.rangeMax = numpy.max(wavelengths)

        if self.rangeMin == self.rangeMax:
            self.refractiveFunction = values
        else:
            self.refractiveFunction = scipy.interpolate.interp1d(wavelengths,
                                                                 values, axis=0)
        self.wavelengths = wavelengths
        self.coefficients = values

    @staticmethod
    def FromLists(wavelengths, values):
        """
        Crete a TabulatedRefractiveIndexData from a list of
        wavelengths and values
        """
        return TabulatedRefractiveIndexData(wavelengths, values)

    @get_array
    def get_refractiveindex(self, wavelength):
        """
        Get the refractive index at a certain wavelength
        :param wavelength:
        :returns: The refractive at wavelength
        :raises Exception:
        """
        if self.rangeMin == self.rangeMax:
            return self.refractiveFunction
        elif self.rangeMin <= wavelength <= self.rangeMax and\
                self.rangeMin != self.rangeMax:
            return self.refractiveFunction(wavelength)
        else:
            raise Exception('Wavelength {} is out of bounds.'
                            'Correct range(um): ({}, {})'
                            .format(wavelength, self.rangeMin, self.rangeMax))

    def get_complete_refractive(self):
        """
        Geth the complete refractive inde data as a list of lists

        :returns: The refractive index data in the form [wavlenght, index]
        """
        extlist = [[
            self.wavelengths[i], self.coefficients[i]]
            for i in range(len(self.wavelengths))]
        return extlist
