from dataclasses import dataclass
from typing import Protocol,runtime_checkable
from fuel_efficency.entities.position import Position


@runtime_checkable
@dataclass(slots=True)
class Node(Protocol):
    """ This is the Node class, that represents our Vertex in our Graph.

    Because our Vertex have the attribute weight Real number, we can calculate the
    Minimum distance between a source and another vertex. Bellman-Ford and Dijkstra algorithms
    are the most common to use in that situation. The Edge is the (NodeA, NodeB) tuple, the
    weight of the path is describe by the sum of them.

    Attributes:
        weight (float): Represents the weight to reach that node
        position (Position): Represent the coordinates of that Node


    """
    weight: float
    position: 'Position' = Position()

    def getHashables(self):
        return (self.weight, self.position)

    def __hash__(self):
        return hash(self.getHashables())

    def __lt__(self, other: 'Node'):
        if isinstance(other,Node):
            return self.weight < other.weight
        raise NotImplementedError("Missing `weight` attribute")

    def __gt__(self, other: 'Node'):
        if isinstance(other,Node):
            return self.weight > other.weight
        raise NotImplementedError(f"Cannot compare Node and {type(other)}")

    def __le__(self, other: 'Node'):
        if isinstance(other,Node):
            return self.weight <= other.weight
        raise NotImplementedError(f"Cannot compare Node and {type(other)}")

    def __ge__(self, other: 'Node'):
        if isinstance(other,Node):
            return self.weight >= other.weight
        raise NotImplementedError(f"Cannot compare Node and {type(other)}")

    def __eq__(self, other: 'Node'):
        if isinstance(other, Node):
            return self.weight == other.weight and self.position == other.position
        raise NotImplementedError("Missing `position` or `weight` attribute")

    def __ne__(self, other: 'Node'):
        if isinstance(other, Node):
            return self.weight != other.weight and self.position != other.position
        raise NotImplementedError(f"Cannot compare Node and {type(other)}")
