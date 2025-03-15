"""
This module uses utility functions to provide D&D specific functions, like generating a set of
character attributes or calculating a single attribute value.
"""

import typing
import utilities as utils


def roll_dnd_ability_score(verbose: bool = False) -> int:
    """
    Rolls a single D&D ability score
    :param: verbose bool if set to True, prints all dice rolls as well as the discarded roll
    :return: int An ability score calculated from random dice rolls
    """
    dice_rolls: typing.List[int] = []
    for i in range(1, 5):
        dice_rolls.append(next(utils.roll_die(6, 4)))

    if verbose:
        print('Rolls:', dice_rolls)

    roll_to_discard: int = min(dice_rolls)

    if verbose:
        print('Discard lowest:', roll_to_discard)

    dice_rolls.remove(roll_to_discard)

    ability_score: int = sum(dice_rolls)

    return ability_score


def roll_dnd_stats(verbose: bool = False) -> typing.Tuple[int, int, int, int, int, int]:
    """
    Creates a tuple of six D&D ability scores to use for creating a level 1 character
    :param: verbose bool if set to True, prints all dice rolls as well as the discarded rolls
    :return: Tuple[int, int, int, int, int, int]
    """
    stat_roll: typing.List[int] = []
    for i in range(1, 7):
        stat_roll.append(roll_dnd_ability_score(verbose))
    return tuple(stat_roll)
