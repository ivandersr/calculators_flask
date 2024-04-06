from abc import ABC, abstractmethod
from typing import List

class DriverHandlerInterface(ABC):
    @abstractmethod
    def standard_deviation(numbers: List[float]) -> float: pass

    @abstractmethod
    def variance(numbers: List[float]) -> float: pass

    @abstractmethod
    def mean(numbers: List[float]) -> float: pass