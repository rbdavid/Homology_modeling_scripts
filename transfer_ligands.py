#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# ----------------------------------------
# USAGE:

# ./transfer_ligands.py homol_model.pdb template_ligands.pdb output.pdb

# ----------------------------------------
# PREAMBLE:

import numpy as np
import sys
import os
import MDAnalysis
from MDAnalysis.analysis.align import *

pdb1 = sys.argv[1]		# homology model structure
pdb2 = sys.argv[2]		# template structure W/ the ligands to be transfered
output = sys.argv[3]		# name of the pdb file to be created by this script

selection1 = 'protein'		# edit this line if you want to change the atom selection to be used for pdb 1
selection2 = 'not protein'	# edit this line if you want to change the atom selection to be used for pdb 2

# ----------------------------------------
# SUBROUTINES:

# ----------------------------------------
# MAIN PROGRAM:

u = MDAnalysis.Universe('%s' %(pdb1))			# Initialize a MDAnalysis.Universe, called u, that is from pdb1
u_selection = u.select_atoms(selection1)		# creating the AtomGroup object with the desired atom selection

v = MDAnalysis.Universe('%s' %(pdb2))			# Initialize a MDAnalysis.Universe, called v, that is from pdb2
v_selection = v.select_atoms(selection2)		# creating the AtomGroup object with the desired atom selection

merged = MDAnalysis.Merge(u_selection,v_selection)	# Merge AtomGroups from the two Universes; creates a Universe with all atoms that were merged
merged_all = merged.select_atoms('not (resname HOH and around 1.5 protein)')			# create a new AtomGroup that includes all atoms

merged_all.write(output)				# write a pdb file of the merged universe

