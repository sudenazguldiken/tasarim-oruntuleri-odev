from abc import ABC, abstractmethod

class Discount(ABC):

    @abstractmethod
    def apply_discount(self, total):
        pass