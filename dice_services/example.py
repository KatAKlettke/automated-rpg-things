import utilities as utils
import dnd_functions as dnd

# DND features
# Generating DND stats with verbose = True:
print(dnd.roll_dnd_stats(True))
# Generating DND stats with verbose = False:
print(dnd.roll_dnd_stats(False))

# Generating a single DND ability score with verbose = True:
print(dnd.roll_dnd_ability_score(True))
# Generating a single DND ability score with verbose = False:
print(dnd.roll_dnd_ability_score(False))

# Die Rolls
# Rolling 1 six-sided die:
print(next(utils.roll_die(6)))
# Rolling a 12-sided die:
print(next(utils.roll_die(12)))
# Rolling 2 100-sided dice:
# Careful: the function generates an iterator and therefore needs to be called with the same parameters as many times
# as dice rolls are desired
print(next(utils.roll_die(100, 2)))
print(next(utils.roll_die(100, 2)))