""" dna_to_rna = {
    "A": "U",
    "T": "A",
    "G": "C",
    "C": "G"
}


def to_rna(dna_strand):
    return "".join([dna_to_rna[nucleotide] for nucleotide in dna_strand]) """


dna_to_rna = str.maketrans('GCTA', 'CGAU')


def to_rna(dna_strand):
    return dna_strand.translate(dna_to_rna)
