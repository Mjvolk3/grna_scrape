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
    import datetime
    from Bio.Seq import Seq
    
    gene_disruptions = len(gene_names)
    
    #generate IDT table
    df = pd.read_excel('template-paste-entry.xlsx')
    guides = []
    
    #fill table with proper oligos for scaffold PCR
    for gene_i in range(gene_disruptions):
        guides.append(gene_names[gene_i])
        if gene_i == 0:
            df.loc[gene_i,'Name'] = gene_names[gene_i] +'_sgtF_s52'
            df.loc[gene_i, 'Sequence'] = 'AAAGGTCTCAGATC' + gRNAs[gene_i] + 'GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGG'
            df.loc[gene_i * 2 + 1,'Name'] = gene_names[gene_i] + '_sgtR_s52'
            df.loc[gene_i * 2 + 1, 'Sequence'] = 'AAAGGTCTCA' + str(Seq(gRNAs[gene_i + 1][:4]).reverse_complement()) + 'TGCGCAAGCCCGGAATCGAAC'
        if (gene_i != gene_disruptions-1) & (gene_i != 0):
            df.loc[gene_i * 2, 'Name'] = gene_names[gene_i] + '_sgtF'
            df.loc[gene_i * 2, 'Sequence'] = 'AAAGGTCTCA' + gRNAs[gene_i] + 'GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGC'
            df.loc[gene_i * 2 + 1, 'Name'] = gene_names[gene_i] + '_sgtR'
            df.loc[gene_i * 2 + 1, 'Sequence'] =  'AAAGGTCTCA' + gRNAs[gene_i + 1] + 'TGCGCAAGCCCGGAATCGAACCGG'
        if gene_i == gene_disruptions-1:
            if optional_oligos == True:
                df.loc[gene_i * 2,'Name'] = gene_names[gene_i] + '_sgtF_URA3'
                #line with error - did not previously incorporate g3
                df.loc[gene_i * 2, 'Sequence'] = 'AAAGGTCTCA' + str(Seq(gRNAs[gene_i]).reverse_complement())[-4:] + 'GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGC'
                df.loc[gene_i * 2 + 1,'Name'] = gene_names[gene_i] + '_sgtR_URA3'
                df.loc[gene_i * 2 + 1, 'Sequence'] = 'AAAGGTCTCAAAACCTAGACACAGGGTAATAACTGATATAATTAAATTGAAGCTC'
                
    #set scale according to sequence length
    df = df.assign(Scale = ['25nm' if len(Sequence) <= 60 else '100nm' for Sequence in df['Sequence']])
    #set purification
    df = df.assign(Purification = "STD")
    
    if write_file == True:
        file_path = './' + file_name + '_oligos_' + str(datetime.datetime.now()).split(' ')[0] + '.xlsx'
        df.to_excel(file_path, index = False) 
        
    return df