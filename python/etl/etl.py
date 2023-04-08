# Understand the problem:
    # What are the inputs? 
        # A dictionary of scores and letters, where the key is a number (score) and the value is a list of letters that correspond to that score.
        # {1: ["A", "E"], 2: ["D", "G"]}    
    
    # What are the outputs?
        # A new dictionary, where the key is a letter and the value is the corresponding score.
        # {"a": 1, "d": 2, "e": 1, "g": 2}
        
    # What are the rules of the problem?
        # The old system stored a list of letters per score:
            # {1: ["A", "E"], 2: ["D", "G"]}
        # The new system stores a list of scores per letter. It also stores the letters in lower-case regardless of the case of the input letters:
            # {"a": 1, "d": 2, "e": 1, "g": 2}
        # The goal is to transform the legacy data format to the new format.

# What is the pseudo-code for the problem?
    # Initialize an empty dictionary to store the new format data
    # new_format_data = {}

    # Iterate over each score-letter pair in the old format data
    # for score, letters in old_format_data.items():
    
        # Iterate over each letter in the list of letters
        # for letter in letters:
        
         # Add a new key-value pair to the new format data dictionary
         # where the key is the lower-case version of the letter
         # and the value is the corresponding score
        #new_format_data[letter.lower()] = score


# def transform(legacy_data: {int: list}) -> {str: int}:
#     new_format_data = {}
#     for score, letters in legacy_data.items():
#         for letter in letters:
#             new_format_data[letter.lower()] = score
#     return new_format_data

def transform(in_dict: {}) -> {}:
    return {m.lower(): n for n in in_dict for m in in_dict[n]}
