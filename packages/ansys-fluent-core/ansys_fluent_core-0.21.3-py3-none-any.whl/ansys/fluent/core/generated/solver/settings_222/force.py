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

from .force_child import force_child


class force(NamedObject[force_child], CreatableNamedObjectMixin[force_child]):
    """
    'force' child.
    """

    fluent_name = "force"

    child_object_type: force_child = force_child
    """
    child_object_type of force.
    """
    return_type = "<object object at 0x7f0e47c00f70>"
