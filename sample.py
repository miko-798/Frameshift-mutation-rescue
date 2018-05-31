from Bio import SeqIO 
from StringIO import StringIO

result = []
gene = NM_032291
fa_file = 'chr1.fa'
read_fa = open(fa_file, 'r')
fa = read_fa.read()

for line in SeqIO.parse(StringIO(fa), 'fasta'):
    if gene
    in line.description:
        result.append(record)

print result[0].format('fasta')