"""
@Sofi-mukhtar(Spyder)
"""

#If you have a single .fasta file for all protein sequence and need to extract PDB codes from the fasta file
# the fasta file is in the format "> PDB_ID | Chain_id | sequence
# for example >5CCLA |PDBID|CHAIN|SEQUENCE ...... 
#here 5CCLA is the protein databank code (PDB) in which first 4 alpha_numeric characters 
#is the PDB ID and the fifth one is the CHAIN id an
import pickle
import os
import string
import time
import math
import numpy as np
import subprocess 
import shutil
import numpy as np
fastafilefull= '/home/spyder/beta_turns/TR6614.txt'
#infile=os.listdir(fastadir)
#print(infile)
outfile=open('/home/spyder/beta_turns/TR6614_pdbcodes_2.txt','w')
count=0
fasta_file=open(fastafilefull,'r')
while True:
    z=fasta_file.readline()
    if z=='':
        break
    if z.startswith('>'):
        r1= z[1:6].strip()
        outfile.write(r1)
        outfile.write(',')
        count+=1
        
outfile.close()
print("total pdb codes are :  " + str(count))
    #z=read_file.readline()
