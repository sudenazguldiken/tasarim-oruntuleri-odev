# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, event, data):
        pass
