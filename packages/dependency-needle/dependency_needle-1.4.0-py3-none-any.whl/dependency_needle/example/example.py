from abc import ABC, abstractmethod

from requests import Request

from dependency_needle.container import Container
from dependency_needle.lifetime_enums import LifeTimeEnums


def main():
    class MockInterfaceOne(ABC):
        """Mock interface class."""
        @abstractmethod
        def mock_method(self):
            """Mock interface method."""
            pass

    class MockInterfaceTwo(ABC):
        """Mock interface class."""

        @abstractmethod
        def mock_method(self):
            """Mock interface method."""
            pass

    class MockInterfaceThree(ABC):
        """Mock interface class."""

        @abstractmethod
        def mock_method(self):
            """Mock interface method."""
            pass

    class MockInterfaceFour(ABC):
        """Mock interface class."""

        @abstractmethod
        def mock_method(self):
            """Mock interface method."""
            pass

    class ConcreteOne(MockInterfaceOne):
        def mock_method(self):
            pass

    class ConcreteTwo(MockInterfaceTwo):
        def __init__(self, dependency_one: MockInterfaceOne):
            pass

        def mock_method(self):
            pass

    class ConcreteThree(MockInterfaceThree):
        def __init__(self, dependency_one: MockInterfaceOne,
                     dependency_two: MockInterfaceTwo):
            pass

        def mock_method(self):
            pass

    class ConcreteFourA(MockInterfaceFour):
        def __init__(self, dependency_three: MockInterfaceThree):
            pass

        def mock_method(self):
            pass

    class ConcreteFourB(MockInterfaceFour):
        def __init__(self, dependency_three: MockInterfaceThree):
            pass

        def mock_method(self):
            pass

    container = Container()

    container.register_interface(
        MockInterfaceOne, ConcreteOne, LifeTimeEnums.SINGLETON)
    container.register_interface(
        MockInterfaceTwo, ConcreteTwo, LifeTimeEnums.SINGLETON)
    container.register_interface(
        MockInterfaceThree, ConcreteThree, LifeTimeEnums.TRANSIENT)

    @container.build_dependencies_decorator()
    def method_with_dependencies_kwarg(request: Request,
                                       dependency: MockInterfaceThree):
        return dependency

    @container.build_dependencies_decorator()
    def method_with_dependencies_arg(request,
                                     dependency: MockInterfaceThree):
        return dependency

    @container.build_dependencies_decorator(
        jit_interfaces=set(),
        get_jit_transient_interfaces=lambda *args, **kwargs: {
            MockInterfaceFour: ConcreteFourB
        }
    )
    def method_with_jit_registery(request,
                                  dependency: MockInterfaceFour):
        dependency.mock_method()
        return dependency

    dependency_array = [
        method_with_dependencies_kwarg(request=Request()),
        method_with_dependencies_arg(Request()),
        method_with_jit_registery(Request()),
    ]

    return dependency_array


if __name__ == "__main__":
    main()
