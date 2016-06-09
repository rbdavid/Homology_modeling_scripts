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
system1 = sys.argv[2]
pdb2 = sys.argv[3]
system2 = sys.argv[4]

alignment = 'protein and name CA and (resid 20:25 or resid 50:55 or resid 73:75 or resid 90:94 or resid 112:116 or resid 142:147 or resid 165:169 or resid 190:194 or resid 214:218 or resid 236:240 or resid 253:258 or resid 303:307)'

flush = sys.stdout.flush

# ----------------------------------------
# SUBROUTINES:

def ffprint(string):
	print '%s' %(string)
        flush()

# ----------------------------------------
# MAIN PROGRAM:

u = MDAnalysis.Universe('%s' %(pdb1))
u_align = u.select_atoms(alignment)
u_all = u.select_atoms('all')
u_backbone = u.select_atoms('backbone')
u_all.translate(-u_backbone.center_of_mass())
pos0 = u_align.coordinates()

v = MDAnalysis.Universe('%s' %(pdb2))
v_align = v.select_atoms(alignment)
v_all = v.select_atoms('all')
v_backbone = v.select_atoms('backbone')
v_all.translate(-v_backbone.center_of_mass())

if len(v_align) != len(v_align):
	ffprint('Alignment atom selections do not have the same number of atoms.')
	sys.exit()

R, rmsd = rotation_matrix(v_align.coordinates(),pos0)
v_all.rotate(R)

u_all.write('aligned.%s.pdb' %(system1))
v_all.write('aligned.%s.pdb' %(system2))

