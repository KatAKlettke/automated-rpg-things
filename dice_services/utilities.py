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



