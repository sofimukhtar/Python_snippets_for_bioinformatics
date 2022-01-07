"""
@Sofi-mukhtar(Spyder)
"""

#If you have a different .fasta file for each sequence and need to extract PDB codes from the fasta files
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
fastadir= '/home/spyder/beta_turns/tr6614' # directory in which the fasta files exist
infile=os.listdir(fastadir)
#print(infile)
outfile=open('/home/spyder/beta_turns/TR6614_pdbcodes.txt','w') # create a new file 
count=0
for file1 in infile:
    temp= fastadir + os.sep+  file1
    #print(temp)
    fasta_file=open(temp,'r')
    while True:
        z=fasta_file.readline()
        if z.startswith('>'):
            r1= z[1:6].strip() # count the no. of characters in any one of the fasta files to get the PDB CODE
            outfile.write(r1)                                  # >5CCLA |PDBID|CHAIN|SEQUENCE ..>5CCLA means 1:6 characters
            outfile.write(',')
            count+=1
            break
outfile.close() 
print("total pdb codes are :  " + str(count))
    #z=read_file.readline()
