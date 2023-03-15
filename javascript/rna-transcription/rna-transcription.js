export const toRna = (dna) => {
  const map = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
  };
  return dna.split('').map(nucleotide => map[nucleotide]).join('');
};
