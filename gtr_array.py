# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:25:58 2020

@author: michaelvolk
"""

def gtr_array(gene_names = ('a', 'b', 'c'),
              gRNAs = (('n' * 20) , ('n' * 20), ('n' * 20)),
              optional_oligos = True,
              write_file = False,
              file_name = 'new'):
        
    import pandas as pd
    import Bio
    from Bio.Seq import Seq
    
    gene_disruptions = len(gene_names)
    
    #generate IDT table
    df = pd.read_excel('template-paste-entry.xlsx')
    
    #fill table with proper oligos for scaffold PCR
    for gene_i in range(gene_disruptions):
        if gene_i == 0:
            df.loc[gene_i,'Name'] = gene_names[gene_i] +'_sgtF_s52'
            df.loc[gene_i, 'Sequence'] = 'AAAGGTCTCAGATC' + gRNAs[gene_i] + 'GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGG'
            df.loc[gene_i, 'Scale'] = '25nm'
            df.loc[gene_i, 'Purification'] = 'STD'
            df.loc[gene_i * 2 + 1,'Name'] = gene_names[gene_i] + '_sgtR_s52'
            df.loc[gene_i * 2 + 1, 'Sequence'] = 'AAAGGTCTCA' + str(Seq(gRNAs[gene_i + 1][:4]).reverse_complement()) + 'TGCGCAAGCCCGGAATCGAAC'
            df.loc[gene_i * 2 + 1, 'Scale'] = '25nm'
            df.loc[gene_i * 2 + 1, 'Purification'] = 'STD'
        if (gene_i != gene_disruptions-1) & (gene_i != 0):
            df.loc[gene_i * 2, 'Name'] = gene_names[gene_i] + '_sgtF'
            df.loc[gene_i * 2, 'Sequence'] = 'AAAGGTCTCA' + gRNAs[gene_i] + 'GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGC'
            df.loc[gene_i * 2, 'Scale'] = '25nm'
            df.loc[gene_i * 2, 'Purification'] = 'STD'
            df.loc[gene_i * 2 + 1, 'Name'] = gene_names[gene_i] + '_sgtR'
            df.loc[gene_i * 2 + 1, 'Sequence'] =  'AAAGGTCTCA' + gRNAs[gene_i + 1] + 'TGCGCAAGCCCGGAATCGAACCGG'
            df.loc[gene_i * 2 + 1, 'Scale'] = '25nm'
            df.loc[gene_i * 2 + 1, 'Purification'] = 'STD'
        if gene_i == gene_disruptions-1:
            if optional_oligos == True:
                df.loc[gene_i * 2,'Name'] = gene_names[gene_i] + '_sgtF_URA3F'
                df.loc[gene_i * 2, 'Sequence'] = 'AAAGGTCTCAATGCGTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGC'
                df.loc[gene_i * 2, 'Scale'] = '25nm'
                df.loc[gene_i * 2, 'Purification'] = 'STD'
                df.loc[gene_i * 2 + 1,'Name'] = gene_names[gene_i] + '_sgtR_URA3R'
                df.loc[gene_i * 2 + 1, 'Sequence'] = 'AAAGGTCTCAAAACCTAGACACAGGGTAATAACTGATATAATTAAATTGAAGCTC'
                df.loc[gene_i * 2 + 1, 'Scale'] = '25nm'
                df.loc[gene_i * 2 + 1, 'Purification'] = 'STD'
    
    if write_file == True:
        file_path = './' + file_name_name + '_oligos.xlsx'
        df.to_excel(file_path, index = False) 
    
    return(df)