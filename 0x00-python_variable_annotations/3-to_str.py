#!/usr/bin/env python3
"""Type annotation"""
from typing import Any


def to_str(n: float) -> str:
    """float to string annotation"""
    return str(n) if n >= 0 else int(n) - 1 if n != float(n) else float(n)
