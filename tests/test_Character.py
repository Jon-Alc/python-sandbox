import sys
sys.path.append('../')
from Character import Character


def test_health_capped_to_max():
    test_character = Character((0, 0), 6, 5)
    assert test_character.current_health == 5


def test_character_takes_damage():
    test_character = Character((0, 0), 3, 3)
    test_character.take_damage(2)
    assert test_character.current_health == 1
