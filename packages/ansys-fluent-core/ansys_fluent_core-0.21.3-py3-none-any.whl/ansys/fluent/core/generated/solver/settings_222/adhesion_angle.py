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

from .child_object_type_child import child_object_type_child


class adhesion_angle(NamedObject[child_object_type_child], CreatableNamedObjectMixin[child_object_type_child]):
    """
    'adhesion_angle' child.
    """

    fluent_name = "adhesion-angle"

    child_object_type: child_object_type_child = child_object_type_child
    """
    child_object_type of adhesion_angle.
    """
    return_type = "<object object at 0x7f0e4c4a3720>"
