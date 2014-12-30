# -*- coding: utf-8 -*-

import abc


class BaseEuler(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def solve(self):
        raise NotImplementedError

    @abc.abstractproperty
    def problem(self):
        raise NotImplementedError

    @abc.abstractproperty
    def answer(self):
        raise NotImplementedError
