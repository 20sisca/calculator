from abc import ABC, abstractmethod
from numbers import Number


class AExpr(ABC):
    """ This class is abstract and serves as a superclass for all Arithmetic Expressions
    """

    @abstractmethod
    def eval(self) -> Number:
        pass


class Litteral(AExpr):
    """ This class represents the constant expressions. It inherits from AExpr and, unlike AExpr,
        it is a concrete class (because 'eval' is implemented).
    """
    def __init__(self, v: Number = 0) -> None:
        super().__init__()
        self._value = v

    def eval(self) -> Number:
        return self._value


class BExpr(AExpr):
    """ This class represents the binary expressions and, by inheritance, it is abstract.
        The reason is that the 'eval' abstract method is not yet implemented.
        This class has four concrete subclasses that represent 
        addition, subtraction, multiplication and division expressions.
    """

    def __init__(self, l: AExpr = None, r: AExpr = None) -> None:
        super().__init__()
        self._left = l
        self._right = r


class AddExpr(BExpr):
    """ Now come the concrete instances of binary expressions
    """

    def eval(self):
        return self._left.eval() + self._right.eval()


class SubExpr(BExpr):
    def eval(self):
        pass


class MulExpr(BExpr):
    def eval(self):
        pass


class DivExpr(BExpr):
    def eval(self):
        pass


## TODO 0: define the object representing the expression (2 + (2 + 2))
##         then, define the object representing the expression ((2 + 2) + 2)

## TODO 1: implement the eval methods of the SubExpr, MulExpr and DivExpr classes

## TODO 2: perform the test at line 81, and check that it passes. Add a few more tests.

## TODO 3: add an abstract class for unary expressions,
## and one concrete subclass for "Opposites" -1 will be represented as "OppExpr(Litteral(1))"

## TODO 4: add an abstract __str__ method to AExpr and implement it 
## for all concrete classes (add parentheses everywhere when it is necessary)

## TODO (Not now. Later) : add variables. What do you need to change?

if __name__ == "__main__":
    onePlusTwo = AddExpr(Litteral(1), Litteral(2))
    print(f"Hello, World {onePlusTwo.eval()}")
    e = MulExpr(AddExpr(Litteral(1),Litteral(2)),DivExpr(Litteral(2),Litteral(2)))
    # print(f"value should be 3 : {e.eval()}")