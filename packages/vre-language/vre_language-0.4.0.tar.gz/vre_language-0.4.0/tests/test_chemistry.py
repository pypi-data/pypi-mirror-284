"""
tests for chemistry objects and operations
"""
from textx import get_children_of_type


def test_chemistry_chem_reaction(meta_model, model_kwargs):
    """test chemical reactions and chemical species"""
    inp = (
        "h2o_energy = 0. [eV];"
        "h2_energy  = 0. [eV];"
        "orr_free = -4.916 [eV];"
        "orr = Reaction 2 H2 + O2 = 2 H2O: ((temperature: 298.15) [K]);"
        "H2O = Species H2O ("
        "    (energy: h2o_energy),"
        "    (entropy: 2.1669e-3) [eV/K],"
        "    (zpe: 0.558) [eV],"
        "    (temperature: 298.15) [K]"
        ");"
        "H2 = Species H2 ("
        "    (energy: h2_energy),"
        "    (zpe: 0.270) [eV],"
        "    (entropy: 1.3613e-3) [eV/K],"
        "    (temperature: 298.15) [K]"
        ");"
        "O2 = Species O2 ("
        "    (free_energy: 2.*H2O.free_energy[0] - 2.*H2.free_energy[0] - orr_free),"
        "    (entropy: 2.1370e-3) [eV/K],"
        "    (zpe: 0.098) [eV],"
        "    (temperature: 298.15) [K]"
        ");"
        "orr_free_energy_correct = orr.free_energy[0] == orr_free"
    )
    prog = meta_model.model_from_str(inp, **model_kwargs)
    var_list = get_children_of_type('Variable', prog)
    assert next(v for v in var_list if v.name == 'orr_free_energy_correct').value


def test_chemistry_property_table(meta_model, model_kwargs):
    """test property table from chemical reactions and chemical species"""
    inp = (
        "H2O = Species H2O ("
        "   (free_energy: -14.739080832009071, -14.994145508249682) [eV],"
        "   (temperature: 500., 600.) [K]);"
        "water_props = H2O.properties;"
        "q1 = water_props select free_energy where temperature == 500. [K];"
        "q2 = water_props where free_energy < -14.8 [eV];"
        "MO = Species MO; M = Species M; H2 = Species H2;"
        "R1 = Reaction MO + H2 = M + H2O : ("
        "   (free_energy: -1., -2.) [eV],"
        "   (temperature: 500., 600.) [K]);"
        "q3 = R1.properties where temperature > 550 [kelvin];"
        "print(q1, q2, q3)"
    )
    ref = ("((free_energy: -14.739080832009071) [electron_volt]) ((free_energy: "
           "-14.994145508249682) [electron_volt], (temperature: 600.0) [kelvin])"
           " ((free_energy: -2.0) [electron_volt], (temperature: 600.0) [kelvin])")
    prog = meta_model.model_from_str(inp, **model_kwargs)
    assert prog.value == ref
