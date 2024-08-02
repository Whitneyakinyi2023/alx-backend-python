#!/usr/bin/python3
"""g"""
from typing import List, Tuple


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

if __name__ == "__main__":
    print(zoom_array.__annotations__)
