#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# ----------------------------------------
# USAGE:

# ./write_pdb.py pdb1.pdb output_file.pdb

# ----------------------------------------
# PREAMBLE:

import numpy as np
import sys
import MDAnalysis

pdb1 = sys.argv[1]		# pdb file with multi-mer structures
output = sys.argv[2]		# output name for the pdb to be written

selection = 'segid A or segid C' 	# change this selection depending on the pdb and the chains wanted to be used in simulation

# ----------------------------------------
# SUBROUTINES:

# ----------------------------------------
# MAIN PROGRAM:

u = MDAnalysis.Universe(pdb1)			# Initialize a MDAnalysis.Universe object, called u, that is the structure from pdb1
u_select = u.select_atoms(selection)		# Initialize the AtomGroup object with the atoms determined from the selection variable

u_select.write(output)				# Write the pdb file of the AtomGroup

