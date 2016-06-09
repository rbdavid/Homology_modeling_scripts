#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# ----------------------------------------
# USAGE:


# ----------------------------------------
# PREAMBLE:

import numpy as np
import sys
import os
import MDAnalysis
from MDAnalysis.analysis.align import *

pdb1 = sys.argv[1]
pdb2 = sys.argv[2]
output = sys.argv[3]

selection1 = 'protein'
selection2 = 'not protein'

flush = sys.stdout.flush

# ----------------------------------------
# SUBROUTINES:

def ffprint(string):
	print '%s' %(string)
        flush()

# ----------------------------------------
# MAIN PROGRAM:

u = MDAnalysis.Universe('%s' %(pdb1))
u_selection = u.select_atoms(selection1)

v = MDAnalysis.Universe('%s' %(pdb2))
v_selection = v.select_atoms(selection2)

merged = MDAnalysis.Merge(u_selection,v_selection)

merged.write(output)

