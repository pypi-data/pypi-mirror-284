"""Custom classes for the chemistry objects"""
import numpy
import pandas
import pint_pandas
from virtmat.language.utilities.units import ureg
from virtmat.language.utilities.errors import RuntimeValueError


class ChemBase:
    """base class of all chemistry objects"""
    props_list = ['energy', 'enthalpy', 'entropy', 'free_energy', 'zpe', 'temperature']
    units_list = ['eV', 'eV', 'eV/K', 'eV', 'eV', 'K']
    prop_units = dict(zip(props_list, units_list))


class ChemReaction(ChemBase):
    """"custom chemical reaction class"""

    def __init__(self, terms, props=None):
        self.terms = terms
        self.props = props if props is not None else pandas.DataFrame()

    def __getitem__(self, key):
        if isinstance(key, int):
            dfr = self.props.iloc[[key]]
            return tuple(next(dfr.itertuples(index=False, name=None)))
        if isinstance(key, str):
            if key == 'properties':
                return self.props
            if key not in self.props:
                return self.prop_get(key)
            return self.props[key]
        if isinstance(key, slice):
            return self.__class__(self.terms, props=self.props[key])
        raise TypeError('unknown key type')

    def prop_get(self, prop):
        """compute a propery of reaction"""
        dtype = pint_pandas.PintType(self.prop_units[prop])
        self.props[prop] = pandas.Series([0.0], dtype=dtype)

        for term in self.terms:
            propval = getattr(term['species'], 'props')
            if prop in propval:
                if 'temperature' in propval and 'temperature' in self.props:
                    if any(propval['temperature'] != self.props['temperature']):
                        msg = 'temperatures of reaction and species must be equal'
                        raise RuntimeValueError(msg)
                self.props.loc[0, prop] += term['coefficient']*propval[prop][0]
            else:
                self.props.loc[0, prop] = ureg.Quantity(numpy.nan, self.prop_units[prop])
        return self.props[prop]


class ChemSpecies(ChemBase):
    """"custom chemical species class"""

    def __init__(self, name, props=None):
        self.name = name
        self.props = props if props is not None else pandas.DataFrame()
        if any(prop not in self.props for prop in self.props_list):
            self.set_props()

    def set_props(self):
        """calculate and set values of missing properties"""
        if 'ethalpy' not in self.props:
            if all(prop in self.props for prop in ['energy', 'zpe']):
                self.props['enthalpy'] = self.props['energy'] + self.props['zpe']
        if 'free_energy' not in self.props:
            if all(prop in self.props for prop in ['enthalpy', 'entropy', 'temperature']):
                self.props['free_energy'] = (self.props['enthalpy'] -
                                             self.props['temperature']*self.props['entropy'])
        if 'enthalpy' not in self.props:
            if all(prop in self.props for prop in ['free_energy', 'entropy', 'temperature']):
                self.props['enthalpy'] = (self.props['free_energy'] +
                                          self.props['temperature']*self.props['entropy'])
        if 'energy' not in self.props:
            if all(prop in self.props for prop in ['enthalpy', 'zpe']):
                self.props['energy'] = self.props['enthalpy'] - self.props['zpe']
        if 'entropy' not in self.props:
            if all(prop in self.props for prop in ['enthalpy', 'free_energy', 'temperature']):
                self.props['entropy'] = ((self.props['enthalpy'] - self.props['free_energy']) /
                                         self.props['temperature'])

    def __getitem__(self, key):
        if isinstance(key, int):
            dfr = self.props.iloc[[key]]
            return tuple(next(dfr.itertuples(index=False, name=None)))
        if isinstance(key, str):
            if key == 'name':
                return self.name
            if key == 'properties':
                return self.props
            if key in self.props:
                return self.props[key]
            dtype = pint_pandas.PintType(self.prop_units[key])
            return pandas.Series(numpy.nan, dtype=dtype, name=key)
        if isinstance(key, slice):
            return self.__class__(self.name, props=self.props[key])
        raise TypeError('unknown key type')
