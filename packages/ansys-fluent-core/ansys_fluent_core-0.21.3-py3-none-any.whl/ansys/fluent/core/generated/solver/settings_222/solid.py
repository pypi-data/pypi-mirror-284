#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import (
    _ChildNamedObjectAccessorMixin,
    CreatableNamedObjectMixin,
    _NonCreatableNamedObjectMixin,
    AllowedValuesMixin,
    _InputFile,
    _OutputFile,
    _InOutFile,
)

from .fluid_child import fluid_child


class solid(NamedObject[fluid_child], CreatableNamedObjectMixin[fluid_child]):
    """
    'solid' child.
    """

    fluent_name = "solid"

    child_object_type: fluid_child = fluid_child
    """
    child_object_type of solid.
    """
    return_type = "<object object at 0x7f0e80e2b390>"
