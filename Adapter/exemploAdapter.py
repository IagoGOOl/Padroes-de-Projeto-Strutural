from abc import ABC, abstractmethod

# Interface Duck
class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass

# Classe concreta Duck
class MallardDuck(Duck):
    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm flying")

# Interface Turkey
class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass

# Classe concreta Turkey
class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble")

    def fly(self):
        print("I'm flying a short distance")

# Adapter
class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        # Turkeys can't fly as well as ducks
        for _ in range(5):
            self.turkey.fly()

# Cliente
def client_code(duck: Duck):
    duck.quack()
    duck.fly()

if __name__ == "__main__":
    print("Testando MallardDuck:")
    mallard = MallardDuck()
    client_code(mallard)

    print("\nTestando TurkeyAdapter:")
    wild_turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(wild_turkey)
    client_code(turkey_adapter)
