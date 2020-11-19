# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:07:17 2020

@author: michaelvolk
"""

#can1 is YEL063C
#ade2 is YOR128C
#lyp1 is YNL268W

#args order matters
order_name = 'A3_plasmid'
gene_names = ('YEL063C', 'YOR128C', 'YNL268W')
gRNAs = ('GCTTACATGGAGACATCTAC', 'GATATCAAGAGGATTGGAAA', 'GCATGCTCTGTTCGCCAATG')
optional_sequences = True
gene_disruptions = len(gene_names)





df_test = pd.read_excel('A3_scaffold_oligos.xlsx')
test = []
for i in range(df_test.shape[0]):
    seq = df.loc[i,'Sequence'] != df_test.loc[i,'Sequence']
    test.append(seq)

