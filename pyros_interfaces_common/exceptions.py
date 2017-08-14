from __future__ import absolute_import

import abc
import six

# TODO : move this out of interface, it should also be known by client since we transfer exceptions
# All Pyros Exception must be pickleable and have a message property

@six.add_metaclass(abc.ABCMeta)
class PyrosException(Exception):

    @abc.abstractproperty
    def message(self):
        return