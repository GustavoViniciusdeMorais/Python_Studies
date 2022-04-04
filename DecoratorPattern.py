# component interface
class Component():
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def operation(self) -> str:
        return "Concrete Component"

class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component
    
    def operation(self) -> str:
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"Concrete Decorator A operation: {self.component.operation()}"

component = ConcreteComponent()
decoratorA = ConcreteDecoratorA(component)
print(decoratorA.operation())