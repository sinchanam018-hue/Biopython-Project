from Bio import SeqIO

# Read the GenBank file
record = SeqIO.read("protein_seq.gp", "genbank")

# Extract protein sequence
protein_seq = record.seq

print("Accession:", record.id)
print("Organism:", record.annotations.get("organism"))
print("Sequence length (aa):", len(protein_seq))
print("Description:", record.description)
print("Other annotations:",record.annotations)

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
