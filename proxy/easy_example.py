import abc
import logging

logging.basicConfig(level=logging.INFO)

class IDivision(abc.ABC):
    @abc.abstractmethod
    def div(a: int | float, b: int | float) -> float: ...

class Division:
    def div(self, a: int | float, b: int | float) -> float:
        return a / b


class ProxyDivision:
    def __init__(self) -> None:
        self._klass = Division()

    def div(self, a: int | float, b: int | float) -> float:
        try:
            result = self._klass.div(a, b)
            return result

        except ZeroDivisionError:
            logging.error(f"Argument b cannot be {b}")

        except TypeError:
            logging.error(f"Arguments must be integers/floats")


klass = ProxyDivision()
print(klass.div(2, 0))