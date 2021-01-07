# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:08:53 2020

@author: michaelvolk
"""

#######################
import primer3
primer3.bindings.calcTm(minus_one_kb[-29:-5])
primer3.bindings.calcHomodimer(minus_one_kb[-29:-5])
primer3.bindings.calcHeterodimer(minus_one_kb[-29:-5], minus_one_kb[-40:-20])

can1F = 'CTGTCGTCAATCGAAAGTTTATTTCAGAGTTCTTCAGACTTCTTAACTCCTGTAAAAACAATTACCTTTGATCAC'
can1R = 'CGGTGTATGACTTATGAGGGTGAGAATGCGAAATGGCGTGGAAATGTGATCAAAGGTAATTGTTTTTACAGGAG'
print(primer3.bindings.calcHeterodimer(can1F[:60], can1R[:60]))
print(primer3.bindings.calcHomodimer(can1F[:60]))
print(primer3.bindings.calcHomodimer(can1R[:60]))

#import Bio
#from Bio.Emboss.Applications import Primer3Commandline

