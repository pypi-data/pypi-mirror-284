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

from .lift_child import lift_child


class drag(NamedObject[lift_child], CreatableNamedObjectMixin[lift_child]):
    """
    'drag' child.
    """

    fluent_name = "drag"

    child_object_type: lift_child = lift_child
    """
    child_object_type of drag.
    """
    return_type = "<object object at 0x7f0e47bc8180>"
