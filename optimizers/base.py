from abc import ABC, abstractmethod

class BaseOptimizer(ABC):
    """Abstract base class defining the contract for all network optimizers."""

    @abstractmethod
    def apply_optimization(self) -> None:
        """Applies the specific network optimization."""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Returns the name of the optimizer."""
        pass
