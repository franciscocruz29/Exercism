# Step 1: Understand the problem
#
# What are the inputs?
# Two strings representing DNA strands (strand_a and strand_b)
#
# What is the output?
# An integer representing the Hamming distance between the two DNA strands.
# An error if the strands are of different lengths.
#
# What are the rules?
# The Hamming distance is the number of positions at which the corresponding nucleotides are different.
# The two input strands must be of equal length.
#
# What is the mental model?
# Compare each nucleotide at the same position in both DNA strands. Count the number of positions where the nucleotides differ and return this count as the Hamming distance.


# Step 2: Examples
#
# Input: strand_a = "", strand_b = ""
# Output: 0
#
# Input: strand_a = "G", strand_b =  "T"
# Output: 1
#
# Input: strand_a = "GGACGGATTCTG", strand_b =  "AGGACGGATTCT"
# Output: 9
#
# Input: strand_a = "AATG", strand_b = "AAA""
# Output: Error "Strands must be of equal length."


# Step 3: Algorithm - Steps for converting the input to output
#
# 1. Check if the lengths of strand_a and strand_b are equal. If not, raise a ValueError with the message "Strands must be of equal length."
# 2. Initialize a counter to 0 to keep track of the Hamming distance.
# 3. Iterate through the nucleotides of both strands simultaneously.
# 4. For each pair of nucleotides, if they are different, increment the counter.
# 5. After the loop, return the counter as the Hamming distance.

# Step 4: Implementation
def distance(strand_a: str, strand_b: str) -> int:
    """
    Calculates the Hamming distance between two strands of DNA.

    The Hamming distance is the number of positions at which the corresponding nucleotides are different. The strands must be of equal length.

    Parameters:
    strand_a (str): The first DNA strand.
    strand_b (str): The second DNA strand.

    Returns:
    int: The Hamming distance between the two DNA strands.

    Raises:
    ValueError: If the strands are of different lengths.
    """

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    count = 0
    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            count += 1
    return count
