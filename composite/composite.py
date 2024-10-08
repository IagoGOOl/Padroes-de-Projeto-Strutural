from _future_ import annotations
from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    """ Component """
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass
    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    """ Composite """

    def _init_(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    """ Leaf """

    def _init_(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if _name_ == "_main_":
    # Leaf
    camiseta1 = Product('camiseta1', 10)
    camiseta2 = Product('camiseta2', 10)
    camiseta3 = Product('camiseta3', 10)

    # Composite
    caixa_camisetas = Box('Caixa de camiseta')
    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)

    # Leaf
    smartphone1 = Product('smartphone1', 10000)
    smartphone2 = Product('smartphone2', 10000)

    # Composite
    caixa_smartphones = Box('Caixa de Smartphones')
    caixa_smartphones.add(smartphone1)
    caixa_smartphones.add(smartphone2)

    # Composite
    caixa_grande = Box('Caixa grande')
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphones)
    caixa_grande.print_content()
    print(caixa_grande.get_price())