from abc import ABC, abstractmethod

class Factory(ABC):
    @abstractmethod
    def factory_method(self):
        pass

class ConcreteFactory(Factory):
    def factory_method(self):
        return ConcreteProduct()

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProduct(Product):
    def operation(self):
        return "Product operation"
