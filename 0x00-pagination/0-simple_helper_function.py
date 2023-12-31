#!/usr/bin/env python3
""" Simple Helper Function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The function returns a tuple of size two containing a start index.
    """
    return ((page - 1) * page_size, page * page_size)
