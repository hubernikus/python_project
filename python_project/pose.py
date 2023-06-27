from dataclasses import dataclass
import copy


@dataclass
class Pose:
    x: float
    y: float

    @classmethod
    def from_vector(cls, vector: list | tuple):
        return cls(vector[0], vector[1])


class NormalPose:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> None:
        # print(self)
        # print(str(self))
        # print(self.__str__())
        return str(self)

    def __str__(self) -> str:
        new_str = "NormalPose with values \n"
        new_str += f"x = {self.x} \n"
        new_str += f"y = {self.y} \n"
        return new_str

    def __add__(self, other):
        new_pose = copy.deepcopy(self)
        new_pose.x = new_pose.x + other.x
        new_pose.y = new_pose.y + other.y

        return new_pose

    def __ge__(self, other) -> bool:
        raise NotImplementedError("not clearly defined.")

    def has_larger_distance_from_origin():
        pass


def main():
    new_pose = Pose(0, 0)
    print("Pose script done.")


def test_new_pose():
    new_pose = Pose(0, 0)

    old_pose = NormalPose(0, 0)

    breakpoint()
    print("test pose")


def test_add_poses():
    pose1 = NormalPose(0, 1)
    pose2 = NormalPose(2, 4)

    pose3 = pose1 + pose2

    breakpoint()

    print("test pose")


if (__name__) == "__main__":
    # main()
    # test_new_pose()
    test_add_poses()
