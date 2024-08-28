# Step 1: Understand the problem

# What are the inputs?
# A string representing a DNA sequence

# What are the outputs?
# A string representing the complementary RNA sequence

# What are the rules?
# Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
#   G -> C
#   C -> G
#   T -> A
#   A -> U

# What is the mental model?
# Iterate through each nucleotide in the DNA strand, replace it with the corresponding RNA nucleotide, and concatenate these to form the RNA strand.

# Step 2: Examples

# Input: ''
# OUtput: ''

# Input: 'G'
# Output: 'C'

# Input: 'ACGTGGTCTTAA'
# Output: 'UGCACCAGAAUU'

# Step 3: Convert the input to the output

# 1. Create a complement mapping:
#    Define a dictionary complement that maps DNA nucleotides to their corresponding RNA complements.
# 2. Build the RNA strand:
#    Use a list comprehension to iterate through each nucleotide in the DNA strand and look up its complement in the complement dictionary. The resulting list of RNA nucleotides is then joined into a single string using ''.join()

# Step 4: Implementation
def to_rna(dna_strand: str) -> str:
    """Convert a DNA strand to its RNA complement.

    Args:
        dna_strand (str): The DNA strand represented as a string.

    Returns:
        str: The RNA strand as a string.
    """
    # Mapping of DNA nucleotides to their RNA complements
    complement = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    # Use a list comprehension to build the RNA strand efficiently
    rna = ''.join(complement[nucleotide] for nucleotide in dna_strand)

    return rna
