# Score categories.

def YACHT(d): return 50 if len(set(d)) == 1 else 0
def ONES(d): return sum(x for x in d if x == 1)
def TWOS(d): return sum(x for x in d if x == 2)
def THREES(d): return sum(x for x in d if x == 3)
def FOURS(d): return sum(x for x in d if x == 4)
def FIVES(d): return sum(x for x in d if x == 5)
def SIXES(d): return sum(x for x in d if x == 6)


def FULL_HOUSE(d):
    return sum(d) if len(set(d)) == 2 and any(d.count(x) == 3 for x in set(d)) else 0


def FOUR_OF_A_KIND(d): return sum(x * 4 for x in set(d) if d.count(x) > 3)
def LITTLE_STRAIGHT(d): return 30 if sum(d) == 15 and len(set(d)) == 5 else 0
def BIG_STRAIGHT(d): return 30 if sum(d) == 20 and len(set(d)) == 5 else 0
def CHOICE(d): return sum(d)


def score(dice, category):
    return category(dice)
