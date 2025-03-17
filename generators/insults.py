"""
This module collects insult generators, starting with Shakespearean insults.
"""
import typing
import random

shakespeare_part_one_list: typing.List[str] = [
    "mewling",
    "paunchy",
    "pribbling",
    "puking",
    "puny",
    "qualling",
    "rank",
    "reeky",
    "roguish",
    "ruttish",
    "saucy",
    "spleeny",
    "spongy",
    "surly",
    "tottering",
    "unmuzzled",
    "vain",
    "venomed",
    "villainous",
    "warped",
    "wayward",
    "weedy",
    "yeasty",
    "brainsick",
    "bawdy",
    "fat",
    "false",
    "foul",
    "greasy",
    "infectious",
    "kindless",
    "lecherous",
    "remorseless",
    "rotten",
    "sanguine",
    "spherical",
    "starveling",
    "vile"
]

shakespeare_part_one_meaning: typing.Dict[str, str] = {
    "mewling": "cry feebly or querulously, whimper",
    "paunchy": "having a large or protruding belly",
    "pribbling": "pribble: a trivial dispute or discussion",
    "puking": "lit. vomiting -> disgusting",
    "puny": "small and weak"
}

shakespeare_part_two_list: typing.List[str] = [
    "idle-headed",
    "ill-breeding",
    "ill-nurtured",
    "knotty-pated",
    "milk-livered",
    "motley-minded",
    "onion-eyed",
    "plume-plucked",
    "pottle-deep",
    "pox-marked",
    "reeling-ripe",
    "rough-hewn",
    "rude-growing",
    "rump-fed",
    "shard-borne",
    "sheep-biting",
    "spur-galled",
    "swag-bellied",
    "tardy-gaited",
    "tickle-brained",
    "toad-spotted",
    "unchin-snouted",
    "weather-bitten",
    "sodden-witted",
    "bat-fowling",
    "beetle-brained",
    "dismal-dreaming",
    "elvish-mark'd",
    "fat-kidneyed",
    "folly-fallen",
    "hell-hated",
    "infant-like",
    "three-inch",
    "worsted-stocking"
]

shakespeare_part_three_list: typing.List[str] = [
    "lewdster",
    "lout",
    "maggot-pie",
    "malt-worm",
    "mammet",
    "measle",
    "minnow",
    "miscreant",
    "moldwarp",
    "mumble-news",
    "nut-hook",
    "pigeon-egg",
    "pignut",
    "puttock",
    "pumpion",
    "ratsbane",
    "scut",
    "skainsmate",
    "strumpet",
    "varlot",
    "vassal",
    "whey-face",
    "wagtail",
    "coward",
    "bed-presser",
    "biscuit",
    "boar pig",
    "bull's-pizzle",
    "carbuncle",
    "death-token",
    "eel-skin",
    "fustilarian",
    "harlot",
    "hog",
    "horseback-breaker",
    "knave",
    "madman",
    "neat's-tongue",
    "stock-fish",
    "whoreson",
    "worms-meat"
]


def shakespearean_insult(verbose: bool = False) -> str:
    """
    This generator randomly picks a number for each position, corresponding to one of the insult
    parts from the lists above, and returns the combined insult.
    :param verbose: bool Default: False. When set to True, adds the translation for the insult
    parts. This functionality is still WIP as the translations are not complete yet.
    :return: str The combined insult.
    """
    random_number_list_one: int = random.randint(0, len(shakespeare_part_one_list) - 1)
    random_number_list_two: int = random.randint(0, len(shakespeare_part_two_list) - 1)
    random_number_list_three: int = random.randint(0, len(shakespeare_part_three_list) - 1)

    cat_one_word: str = shakespeare_part_one_list[random_number_list_one]
    cat_two_word: str = shakespeare_part_two_list[random_number_list_two]
    cat_three_word: str = shakespeare_part_three_list[random_number_list_three]

    insult: str = "You " + cat_one_word + " " + cat_two_word + " " + cat_three_word + "!"

    # TODO: finish translating the lists, then uncomment this
    #if verbose:
    #    explanation_one: str = shakespeare_part_one_meaning[cat_one_word]
    #    insult = insult + "\n" + cat_one_word + ": " + explanation_one
    #    explanation_two: str = shakespeare_part_two_meaning[cat_two_word]
    #    insult = insult + "\n" + cat_two_word + ": " + explanation_two
    #    explanation_three: str = shakespeare_part_three_meaning[cat_three_word]
    #    insult = insult + "\n" + cat_three_word + ": " + explanation_three

    return insult
