# 1. Understand the problem:

# What are the inputs?
# level = limit = non-negative integer,
# magical_items = multiples = list of non-negative integers, including 0 and an empty list

# What are the outputs?
# energy _points = integer = sum of all multiples of magical_items up to limit

# What are the rules?
# The energy points are awarded according to the following rules:

# 1. For each magical item, take the base value and find all the multiples of that value that are less than or equal to the level number.
# 2. Combine the sets of numbers.
# 3. Remove any duplicates.
# 4. Calculate the sum of all the numbers that are left.

# What is the goal:
# Write the code that calculates the energy points that get awarded to players when they complete a level.
# The points awarded depend on two things:
# The level(a number) that the player completed.
# The base value of each magical item collected by the player during that level.


# 2. Examples:

# The player completed level 20 and found two magical items with base values of 3 and 5.
# sum_of_multiples(20, [3, 5])

# To calculate the energy points earned by the player, we need to find all the unique multiples of these base values that are less than or equal to level 20.
# Multiples of 3 up to 20: {3, 6, 9, 12, 15, 18}
# Multiples of 5 up to 20: {5, 10, 15, 20}
# Combine the sets and remove duplicates: {3, 5, 6, 9, 10, 12, 15, 18, 20}
# Sum the unique multiples: 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20 = 98
# Therefore, the player earns 98 energy points for completing level 20 and finding the two magical items with base values of 3 and 5.


# 3. Steps for converting input to output (Algorithm):

# 1. Find all the multiples of each magical item up to the limit
# 2. Combine the sets of multiples and remove duplicates.
# 3. Calculate the sum of the multiples.
# 4. Return the sum.


# 4. Implementation:

def sum_of_multiples(limit, item_values):
    # Step 1: Find multiples of each value in item_values up to the limit
    multiples_sets = [set(range(v, limit, v))
                      for v in item_values if v != 0]

    # Step 2 and 3: Combine the sets and remove duplicates
    combined_multiples = set().union(*multiples_sets)

    # Step 4: Calculate the sum of all the numbers that are left
    result = sum(combined_multiples)

    return result

# 5. Refactoring:


def find_multiples(limit, values):
    return [set(range(v, limit + 1, v)) for v in values if v != 0]


def combine_sets(sets_list):
    return set().union(*sets_list)


def sum_of_multiples(limit, item_values):

    multiples_sets = find_multiples(limit, item_values)

    combined_multiples = combine_sets(multiples_sets)

    result = sum(combined_multiples)

    return result
