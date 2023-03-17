def is_isogram(phrase):
    scrubbed = phrase.lower().replace(" ", "").replace("-", "") # remove spaces and dashes
    return len(scrubbed) == len(set(scrubbed)) # check if length of string is equal to length of set
