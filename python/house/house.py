# Step 1 - Problem Understanding:

# What are the inputs?
# Two positive integers - start_verse and end_verse

# What are the outputs?
# A list of strings, each representing a verse from the rhyme

# What are the rules?
# - The rhyme must be generated from the specified verse range, starting from start_verse and ending at end_verse.
# - Verses are cumulative, meaning each subsequent verse builds upon the previous one, up to the 12th verse.

# What is the mental model?
# - Retrieve a slice of cumulative verses from a predefined rhyme based on given start and end positions.


# Step 2 - Examples and Test Cases

# Input: (1, 1)
# Output: ["This is the house that Jack built."]

# Input: (1, 3)
# Output: ["This is the house that Jack built.", "This is the malt that lay in the house that Jack built.", "This is the rat that ate the malt that lay in the house that Jack built."]

# Input: (12, 12)
# Output: ["This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."]


# Step 3 - Algorithm Design

# 1. Define the complete RHYME as a list of strings, where each string is a full verse
# 2. Create a function that takes start_verse and end_verse as parameters
# 3. Adjust the input parameters to be zero-indexed for list slicing
# 4. Return a slice of the RHYME list from (start_verse - 1) to end_verse


# Step 4 - Implementation

from typing import List

RHYME = [
    "This is the house that Jack built.",
    "This is the malt that lay in the house that Jack built.",
    "This is the rat that ate the malt that lay in the house that Jack built.",
    "This is the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "This is the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "This is the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "This is the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
]


def recite(start_verse: int, end_verse: int) -> List[str]:
    return RHYME[start_verse - 1: end_verse]
