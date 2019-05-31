print("Import modules, please wait...")
import os,sys,time
localtime = time.asctime(time.localtime(time.time()))
print("PRAP start time: ",localtime)
import CDSex
import ArKmer,ArBlastn,ArBlastp,ArMatrix
import ResKmer,ResBlastn,ResBlastp,ResMatrix
import Pangenome
import PanAccess

install = (os.getcwd()+"/").replace("\\","/")
file = ""

print("""
==================================================================
=================Pan Resistome Analysis Pipeline==================
==================================================================
If you choose one of RUN ALL MODULES, 
you don't need to RUN SEPARATE MODULE;
If you just want to run one module,
please see RUN SEPARATE MODULE
------------------------------------------------------------------

==================================================================
RUN ALL MODULES:
------------------------------------------------------------------
# Raw reads as input files (files with a ".fastq" extension):
------------------------------------------------------------------
[R1] analysis with CARD nucleotide database
[R2] analysis with ResFinder nucleotide database
------------------------------------------------------------------
# Genbank files as input files (files with a ".gb" extension):
------------------------------------------------------------------
[G1-1] analysis with CARD nucleotide database
[G1-2] analysis with CARD protein database
[G2-1] analysis with ResFinder nucleotide database
[G2-2] analysis with ResFinder protein database
------------------------------------------------------------------
# Nucleotide seq as input files (files with a ".fna" extension):
------------------------------------------------------------------
[N1] analysis with CARD nucleotide database
[N2] analysis with ResFinder nucleotide database
------------------------------------------------------------------
# Protein seq as input files (files with a ".faa" extension):
------------------------------------------------------------------
[P1] analysis with CARD protein database
[P2] analysis with ResFinder protein database
------------------------------------------------------------------
==================================================================

==================================================================
RUN SEPARATE MODULE:
------------------------------------------------------------------
# Preprocessing module:
------------------------------------------------------------------
[a] "CDSex.py": extract coding sequence from genbank files;
	form both protein and nucleotide fasta files;
------------------------------------------------------------------
# Gene identification modules:
------------------------------------------------------------------
## Modules using CARD database------------------------------------
[b-1] "ArKmer.py": find resistance genes from raw reads;
[b-2] "ArBlastn.py": find resistance genes from ".fna" files;
[b-3] "ArBlastp.py": find resistance genes from ".faa" files;
## Modules using ResFinder database-------------------------------
[c-1] "ResKmer.py": find resistance genes from raw reads;
[c-2] "ResBlastn.py": find resistance genes from ".fna" files;
[c-3] "ResBlastn.py": find resistance genes from ".fna" files;
------------------------------------------------------------------
# Analysis modules:
# Input files of Analysis modules are annotation files (files 
# with "_ar.csv" suffixes) formed by gene identification modules
------------------------------------------------------------------
[d] "Pangenome.py": pan-resistome analysis
	(mainly analyze for pan-genome features)
[e] "PanAccess.py": pan & accessory resistome analysis
	(mainly classify and statistical analysis for ARGs)
## Module using CARD database-------------------------------------
[f-1] "ArMatrix.py": analysis associated genes for each kind of 
	  antibiotics in CARD database
## Module using ResFinder database--------------------------------
[f-2] "ResMatrix.py": analysis associated ARGs for each kind of 
	  antibiotics in ResFinder database
==================================================================
""")

choose = input("Your choice: ").upper().replace(" ","")
ar_module = ["R1","G1-1","G1-2","N1","P1"]
res_module = ["R2","G2-1","G2-2","N2","P2"]
if choose in ar_module or choose in res_module:
	if choose in ar_module:
		if choose == "R1":
			file = ArKmer.main(install,"")
		elif choose == "G1-1":
			file = CDSex.main("")
			ArBlastn.main(install,file)
		elif choose == "G1-2":
			file = CDSex.main("")
			ArBlastp.main(install,file)
		elif choose == "N1":
			file = ArBlastn.main(install,"")
		elif choose == "P1":
			file = ArBlastp.main(install,"")
		else:
			print("Please input the write number!!!")
			sys.exit(0)
		Pangenome.main(install,file)
		PanAccess.main(install,file)
		ArMatrix.main(install,file)
	else:
		if choose == "R2":
			file = ResKmer.main(install,"")
		elif choose == "G2-1":
			file = CDSex.main("")
			ResBlastn.main(install,file)
		elif choose == "G2-2":
			file = CDSex.main("")
			ResBlastp.main(install,file)
		elif choose == "N2":
			file = ResBlastn.main(install,"")
		elif choose == "P2":
			file = ResBlastp.main(install,"")
		else:
			print("Please input the write number!!!")
			sys.exit(0)
		Pangenome.main(install,file)
		PanAccess.main(install,file)
		ResMatrix.main(install,file)

elif choose == "A":
	CDSex.main("")
elif choose == "B-1":
	ArKmer.main(install,"")
elif choose == "B-2":
	ArBlastn.main(install,"")
elif choose == "B-3":
	ArBlastp.main(install,"")
elif choose == "C-1":
	ResKmer.main(install,"")
elif choose == "C-2":
	ResBlastn.main(install,"")
elif choose == "C-3":
	ResBlastp.main(install,"")
elif choose == "D":
	Pangenome.main(install,"")
elif choose == "E":
	PanAccess.main(install,"")
elif choose == "F-1":
	ArMatrix.main(install,"")
elif choose == "F-2":
	ResMatrix.main(install,"")
else:
	print("Please input the write number!!!")
	sys.exit(0)

localtime = time.asctime(time.localtime(time.time()))
print("PRAP end time: ",localtime)