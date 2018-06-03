import os
import pysam

def reverse_complement(sequence):
    
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = "".join(complement.get(base, base) for base in reversed(sequence))
    return reverse_complement;

def complement(sequence):
    
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = "".join(complement.get(base, base) for base in sequence)
    return reverse_complement;
    
ctnnb1_fasta = os.path.join('chr1.fa')
gene_fa = pysam.Fastafile(ctnnb1_fasta)
gs = GeneSequence(gene_fa, nuc_context=1)

reverse_complement(gs)