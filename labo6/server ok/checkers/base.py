import abc

class BaseChecker(abc.ABC):
    """
    Abstract base class for checkers.
    """
    @abc.abstractclassmethod
    def check(cls, server):
        """
        Perform a check on the specified server and return the result.
        """
        pass
