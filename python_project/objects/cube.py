from typing import Self

import numpy as np
from python_project.pose import Pose


class Cube:
    def __init__(self, axes_length: np.ndarray, pose: Pose) -> None:

        self.axes_length = axes_length
        self._private_axes = axes_length  # NOT C++ (!!!)
        self.__hidden_axes = axes_length

    def __str__(self) -> str:
        my_str = ""
        my_str += str(self._private_axes)
        my_str += str(self.__hidden_axes)
        return my_str


class RedCube(Cube):
    def __str__(self):
        return new_cube._Cube__hidden_axes


def test_cube():
    new_cube = Cube(np.array([1, 0]), 0)
    breakpoint()
    print(new)
    print(new_cube._private_axes)
    print(new_cube._Cube__hidden_axes)
    breakpoint()


if __name__ == "__main__":
    test_cube()

    print("Execution successful")
