# refractiveindex.info-sqlite

Fork of the [Python 3 + SQLite wrapper](https://github.com/HugoGuillen/refractiveindex.info-sqlite)
for the [refractiveindex.info database](http://refractiveindex.info/), by [Hugo Guillen](https://github.com/HugoGuillen).

The fork adds some functionalities that are not available in the original project, such as
the possibility to get refractive indices and extinction coefficients for multiple
wavelengths, the possibility to calculate the optical permittivity, and a direct
access to the refractiveindex.info database.

## Features

- Create SQLite database from refractiveindex yml folder.
- Create SQLite database from refractiveindex.zip url.
- Search database pages by approximate or exact terms.
- Search material data (refractiveindex, extinctioncoefficient) by intervals.
- Execute custom SQL queries on the database.
- Export material data (refractiveindex, extinctioncoefficient) to numpy arrays or csv files.
- Get data (refractiveindex, extinctioncoefficient) at single or multiple wavelengths.
- Calculate optical permittivity at single or multiple wavelengths.
