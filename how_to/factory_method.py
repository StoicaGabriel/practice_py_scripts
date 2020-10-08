# Basic example of a factory method pattern implementation.
from abc import ABC, abstractmethod


class Bicycle:
    def __init__(self, factory):
        self.tires = factory().add_tires()
        self.frame = factory().add_frame()


class BaseFactory(ABC):
    @abstractmethod
    def add_tires(self):
        pass

    @abstractmethod
    def add_frame(self):
        pass


class BaseTires(ABC):
    def part_type(self):
        pass


class BaseFrame(ABC):
    def part_type(self):
        pass


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


class GenericTires(BaseTires):
    def part_type(self):
        return 'generic_tires'


class RuggedTires(BaseTires):
    def part_type(self):
        return 'rugged_tires'


class RoadTires(BaseTires):
    def part_type(self):
        return 'road_tires'


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