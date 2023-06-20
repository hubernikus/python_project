from dataclasses import dataclass

@dataclass
class Pose:
    x: float
    y: float
    z: float
    
    @classmethod 
    def from_vector(cls, vector: list | tuple):
        return cls(vector[0], vector[1], vector[2])


