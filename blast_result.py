from Bio.Blast import NCBIXML

with open("blast_result.xml") as result_file:
    blast_record = NCBIXML.read(result_file)

# Closest homologs
for alignment in blast_record.alignments[:5]:
    print("Homolog:", alignment.title)
    print("Length:", alignment.length)

    # Conserved regions (HSPs)
    for hsp in alignment.hsps:
        print("E-value:", hsp.expect)
        print("Score:", hsp.score)
        print("Query:", hsp.query[:60])
        print("Match:", hsp.match[:60])
        print("Sbjct:", hsp.sbjct[:60])


from Bio.Blast import NCBIXML

# Open and read the entire BLAST result
with open("blast_result.xml") as B:
    blast_record = NCBIXML.read(B)

# Print total number of similar sequences (alignments/hits) found
print("Total Hits:", len(blast_record.alignments))

# Loop through all alignments to print titles
for alignment in blast_record.alignments:
    print("Homolog:", alignment.title)
    print("Length:", alignment.length)

    # Loop through HSPs (exact matching regions) inside each alignment
    for hsp in alignment.hsps:
        print("E-value:", hsp.expect) # Reliability
        print("Score:", hsp.score)   # Strength
        
        # Print the aligned sequences (Query, Match line, and Subject)
        print("Query:", hsp.query)
        print("Match:", hsp.match)
        print("Sbjct:", hsp.sbjct)
        
        # Print matching positions
        print("Query Range:", hsp.query_start, "to", hsp.query_end)
        print("Subject Range:", hsp.sbjct_start, "to", hsp.sbjct_end)