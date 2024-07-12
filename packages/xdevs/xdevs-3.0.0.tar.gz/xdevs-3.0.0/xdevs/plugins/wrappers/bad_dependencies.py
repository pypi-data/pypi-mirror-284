from __future__ import annotations
from abc import ABC
from xdevs.models import Atomic


class BadDependenciesWrapper(Atomic, ABC):
    def __init__(self, **kwargs):
        """
        Template wrapper for using when dependencies are not installed.
        :param str wrapper_type: wrapper type.
        """
        super().__init__(**kwargs)
        wrapper_type = kwargs['wrapper_type']
        raise ImportError(f'{wrapper_type} wrapper specific dependencies are not installed')

    def deltint(self):
        pass

    def deltext(self, e: float):
        pass

    def lambdaf(self):
        pass

    def initialize(self):
        pass

    def exit(self):
        pass
