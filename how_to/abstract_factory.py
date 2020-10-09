# Basic example of an abstract factory pattern implementation.
from abc import ABC, abstractmethod


class Bicycle:
    """Class for bicycle objects. The __init__ method is the actual interface."""
    def __init__(self, factory):
        self.tires = factory().add_tires()
        self.frame = factory().add_frame()


class BaseFactory(ABC):
    """Abstract Factory class. The two abstract methods are factory methods."""
    @abstractmethod
    def add_tires(self):
        pass

    @abstractmethod
    def add_frame(self):
        pass


class BaseTires(ABC):
    """Abstract class for tires component. This is part of the product."""
    def part_type(self):
        pass


class BaseFrame(ABC):
    """Abstract class for frame component. This is also part of the product."""
    def part_type(self):
        pass


# Factory methods for different types of bike.
class GenericFactory(BaseFactory):
    def add_tires(self):
        return GenericTires()

    def add_frame(self):
        return GenericFrame()


class MountainFactory(BaseFactory):
    def add_tires(self):
        return RuggedTires()

    def add_frame(self):
        return SturdyFrame()


class RoadFactory(BaseFactory):
    def add_tires(self):
        return RoadTires()

    def add_frame(self):
        return LightFrame()


# Products for different types of tires.
class GenericTires(BaseTires):
    def part_type(self):
        return 'generic_tires'


class RuggedTires(BaseTires):
    def part_type(self):
        return 'rugged_tires'


class RoadTires(BaseTires):
    def part_type(self):
        return 'road_tires'


# Products for different types of frames.
class GenericFrame(BaseFrame):
    def part_type(self):
        return 'generic_frame'


class SturdyFrame(BaseFrame):
    def part_type(self):
        return 'sturdy_frame'


class LightFrame(BaseFrame):
    def part_type(self):
        return 'light_frame'


if __name__ == '__main__':
    bike = Bicycle(GenericFactory)
    print(bike.tires.part_type())
    print(bike.frame.part_type())
    mountain_bike = Bicycle(MountainFactory)
    print(mountain_bike.tires.part_type())
    print(mountain_bike.frame.part_type())
    road_bike = Bicycle(RoadFactory)
    print(road_bike.tires.part_type())
    print(road_bike.frame.part_type())
