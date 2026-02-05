from Bio import SeqIO
from Bio.Blast import NCBIWWW

print("Reading protein sequence...")
record = SeqIO.read("protein_seq.fasta", "fasta")

print("Running BLAST... this may take a few minutes")
result_handle = NCBIWWW.qblast("blastp", "nr", record.seq)

with open("blast_result.xml", "w") as out_handle:
    out_handle.write(result_handle.read())

result_handle.close()

print("BLAST completed successfully. Results saved as blast_result.xml")
