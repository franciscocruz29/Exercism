def is_isogram(phrase):
    string = phrase.lower().replace(" ", "").replace("-", "") # remove spaces and dashes
    return len(string) == len(set(string)) # check if length of string is equal to length of set
