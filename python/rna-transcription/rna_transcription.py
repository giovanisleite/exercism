def to_rna(dna_strand):
    return (dna_strand
            .replace('C', 'g')
            .replace('G', 'c')
            .replace('T', 'a')
            .replace('A', 'u').upper())

