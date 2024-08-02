#!/usr/bin/env python3
"""float annotation"""
from typing import Any


def floor(n: float) -> int:
    """REturn"""
    return int(n) if n >= 0 else int(n) - 1 if n != int(n) else int(n)
