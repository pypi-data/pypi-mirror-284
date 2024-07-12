"""
Test type checking and type inference
"""
import sys
from os import path
from textx import metamodel_from_file
from textx.export import model_export
from virtmat.language.metamodel.properties import add_properties
from virtmat.language.metamodel.processors import add_processors
from virtmat.language.utilities.textx import GRAMMAR_LOC

meta = metamodel_from_file(GRAMMAR_LOC, auto_init_attributes=False)
add_properties(meta)
add_processors(meta, constr_processors=True)

model_file = sys.argv[1]
model_dot_file = path.splitext(model_file)[0]+'.dot'
program = meta.model_from_file(model_file)
model_export(program, model_dot_file)
