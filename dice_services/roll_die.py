import random
from typing import Iterator, Tuple, List


def roll_die(side_count: int, dice_count: int = 1) -> Iterator[int]:
    """
    Generates a random number in the range between 1 and side_count, dice_count number of times.
    Default argument for dice_count is 1.
    :param side_count: int number of sides the die has
    :param dice_count: int number of dice to be rolled, default: 1
    :return: Iterator[int] giving out the results one by one
    """
    for i in range(dice_count):
        yield random.randint(1, side_count)

def roll_dnd_stats() -> Tuple[int, int, int, int, int, int]:
    """
    Creates a tuple of six D&D ability scores to use for creating a level 1 character
    :return: Tuple[int, int, int, int, int, int]
    """
    stat_roll: List[int] = []
    for i in range(1, 7):
        stat_roll.append(roll_dnd_ability_score())
    return tuple(stat_roll)

def roll_dnd_ability_score() -> int:
    """
    Rolls a single D&D ability score
    :return: int An ability score calculated from random dice rolls
    """
    dice_rolls: List[int] = []
    for i in range(1, 5):
        dice_rolls.append(next(roll_die(6, 4)))

    print(dice_rolls)

    roll_to_discard: int = min(dice_rolls)
    dice_rolls.remove(roll_to_discard)

    ability_score: int = sum(dice_rolls)

    return ability_score

print(roll_dnd_stats())

