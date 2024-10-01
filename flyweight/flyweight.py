from __future__ import annotations
from typing import List, Dict


class Client:
    """Context"""

    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        # Extrinsic address data
        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)


class Address:
    """Flyweight"""

    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str) -> None:
        print(
            self._street, address_number, self._neighbourhood, address_details,
            self._zip_code
        )


class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Usando objeto já criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto')

        return address_flyweight


if __name__ == "__main__":
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street='Av Brasil',
        neighbourhood='Centro',
        zip_code='000000-000'
    )

    a2 = address_factory.get_address(
        street='Av Brasil ',
        neighbourhood='Centro',
        zip_code='000000-000'
    )

    iago = Client('Iago')
    iago.address_number = '50'
    iago.address_details = 'Casa'
    iago.add_address(a1)
    iago.list_addresses()

    diogo = Client('diogo')
    diogo.address_number = '250A'
    diogo.address_details = 'AP 555'
    diogo.add_address(a2)
    diogo.list_addresses()

    print(a1 == a2)