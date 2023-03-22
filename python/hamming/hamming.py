def distance(strand_a, strand_b):
    """
    Calculates the Hamming distance between two strands of DNA.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    """ count = 0
    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            count += 1
    return count """

    return sum(nucleotide_a != nucleotide_b for nucleotide_a, nucleotide_b in zip(strand_a, strand_b))
