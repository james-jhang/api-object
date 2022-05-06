import os
from typing import List


def compare(l1: List, l2: List):
    assert l1.sort() == l2.sort()

def certificate():
    return [
        os.environ.get('HOST'),
        os.environ.get('USERNAME'),
        os.environ.get('PASSWORD')
    ]
