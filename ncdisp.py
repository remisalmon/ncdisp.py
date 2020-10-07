# Remi Salmon
# salmon.remi@gmail.com
#
# October 6, 2020

# imports
import warnings

from netCDF4 import Dataset

# functions
def nowarnings(f):
    def wrapper(*args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')

            f(*args, **kwargs)

        return

    return wrapper

@nowarnings
def ncdisp(source):
    """
    Display contents of NetCDF data source.

    Parameters
    ----------
    source : str
        NetCDF data source.

    Returns
    -------
    None.
    """

    data = Dataset(source)

    print('Source:')
    print('\t{}'.format(source))

    print('Format:')
    print('\t{}'.format(data.file_format.lower()))

    ncdisp_group(data, level = 0)

    return

@nowarnings
def ncdisp_group(data, level = 0):
    if data.ncattrs():
        print('{}{}Attributes:'.format('\t'*level*2,
                                       'Global ' if level == 0 else ''))

        l = max(len(a) for a in data.ncattrs())

        for a in data.ncattrs():
            attribute = getattr(data, a)

            if type(attribute) is str:
                attribute = '\'{}\''.format(attribute)

            print('{}\t{}{}= {}'.format('\t'*level*2,
                                        a,
                                        ' '*(l-len(a)+1),
                                        attribute))

    if data.dimensions:
        print('{}Dimensions:'.format('\t'*level*2))

        l = max(len(d) for d in data.dimensions)

        for d in data.dimensions:
            print('{}\t{}{}= {}{}'.format('\t'*level*2,
                                          d,
                                          ' '*(l-len(d)+1),
                                          data.dimensions[d].size,
                                          '\t(UNLIMITED)' if data.dimensions[d].size == 0 else ''))

    if data.variables:
        print('{}Variables:'.format('\t'*level*2))

        for v in data.variables:
            print('{}\t{}'.format('\t'*level*2,
                                  v))

            if not data.variables[v].shape:
                size = '1x1'
            elif len(data.variables[v].shape) == 1:
                size = '{}x1'.format(data.variables[v].shape[0])
            else:
                size = 'x'.join(str(s) for s in data.variables[v].shape[::-1])

            print('{}\t\tSize:       {}'.format('\t'*level*2,
                                                size))

            dimension = ','.join(str(d) for d in data.variables[v].dimensions[::-1])

            print('{}\t\tDimensions: {}'.format('\t'*level*2,
                                                dimension))

            print('{}\t\tDatatype:   {}'.format('\t'*level*2,
                                                data.variables[v].dtype.name))

            if data.variables[v].ncattrs():
                print('{}\t\tAttributes:'.format('\t'*level*2))

                l = max(len(a) for a in data.variables[v].ncattrs())

                for a in data.variables[v].ncattrs():
                    attribute = getattr(data.variables[v], a)

                    if type(attribute) is str:
                        attribute = '\'{}\''.format(attribute)

                    print('{}\t\t            {}{}= {}'.format('\t'*level*2,
                                                              a,
                                                              ' '*(l-len(a)+1),
                                                              attribute))

    if data.groups:
        print('{}Groups:'.format('\t'*level*2))

        for g in data.groups:
            print('{}\t{}/'.format('\t'*level*2,
                                   data.groups[g].path))

            ncdisp_group(data.groups[g], level = level+1)

    else:
        return
