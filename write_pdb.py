#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# ----------------------------------------
# USAGE:


# ----------------------------------------
# PREAMBLE:

import numpy as np
import sys
import MDAnalysis
from MDAnalysis.analysis.align import *

pdb1 = sys.argv[1]
output = sys.argv[2]

selection = 'protein and chain A' # CORRECT THIS...

flush = sys.stdout.flush

# ----------------------------------------
# SUBROUTINES:

def ffprint(string):
	print '%s' %(string)
        flush()

# ----------------------------------------
# MAIN PROGRAM:

u = MDAnalysis.Universe('%s' %(pdb1))
u_select = u.select_atoms(selection)

u_select.write(output)

