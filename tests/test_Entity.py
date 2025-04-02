import sys
sys.path.append('../')
from Entity import Entity


def test_move():
    test_entity = Entity((0, 0))
    test_entity.move((-5, 5))
    assert test_entity.position == (-5, 5)
