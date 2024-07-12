"""
Register model processors

Model processors are callables that are called at the end of the parsing when
the whole model is instantiated. These processors accept the model and metamodel
as parameters.

Do not register object processors here
"""
import warnings
from textx import get_children_of_type, get_parent_of_type, textx_isinstance
from virtmat.language.utilities.errors import VaryError
from .cyclic import check_cycles_processor
from .duplicates import check_duplicates_processor
from .functions import check_functions_processor
from .imports import check_imports_processor
from .typechecks import check_types_processor
from .parallel import check_parallelizable_processor
from .amml import check_task_property_processor


def check_vary_processor(model, metamodel):
    """check if vary statements exist and whether they are referenced"""
    if get_children_of_type('Vary', model):
        warnings.warn('vary statement has no effect', UserWarning)
    for gref in get_children_of_type('GeneralReference', model):
        if textx_isinstance(gref.ref, metamodel['Series']):
            if get_parent_of_type('Vary', gref.ref):
                msg = f'reference to series \"{gref.ref.name}\" in vary statement'
                raise VaryError(msg)


def add_constraints_processors(metamodel):
    """register the constraints processors on the metamodel instance"""
    metamodel.register_model_processor(check_duplicates_processor)
    metamodel.register_model_processor(check_cycles_processor)
    metamodel.register_model_processor(check_imports_processor)
    metamodel.register_model_processor(check_functions_processor)
    metamodel.register_model_processor(check_types_processor)
    metamodel.register_model_processor(check_parallelizable_processor)
    metamodel.register_model_processor(check_vary_processor)
    metamodel.register_model_processor(check_task_property_processor)
