# Python_snippets_for_bioinformatics
Python code snippets for extracting PDB codes from .fasta files
If you have a single .fasta file for all protein sequence and need to extract PDB codes from the fasta file.
the fasta file is in the format "> PDB_ID | Chain_id | sequence
for example >5CCLA |PDBID|CHAIN|SEQUENCE ...... 
#here 5CCLA is the protein databank code (PDB) in which first 4 alpha_numeric characters 
#is the PDB ID and the fifth one is the CHAIN id an
RUN ext_pdb_2.py


#If you have a different .fasta file for each sequence and need to extract PDB codes from the fasta files
# the fasta file is in the format "> PDB_ID | Chain_id | sequence
# for example >5CCLA |PDBID|CHAIN|SEQUENCE ...... 
#here 5CCLA is the protein databank code (PDB) in which first 4 alpha_numeric characters 
#is the PDB ID and the fifth one is the CHAIN id an

RUN ext_pdb_2.py
