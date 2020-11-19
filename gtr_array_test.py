# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:07:17 2020

@author: michaelvolk
"""
def run_tests():
    
    from gtr_array import gtr_array
    import pandas as pd

    #can1 is YEL063C
    #ade2 is YOR128C
    #lyp1 is YNL268W
    
    #order_name = 'A3_plasmid'
    gene_names = ('YEL063C', 'YOR128C', 'YNL268W')
    gRNAs = ('GCTTACATGGAGACATCTAC', 'GATATCAAGAGGATTGGAAA', 'GCATGCTCTGTTCGCCAATG')
    #optional_sequences = True
    #gene_disruptions = len(gene_names)
    
    df = gtr_array(gene_names = gene_names, gRNAs = gRNAs)
    df_test = pd.read_excel('A3_test_oligos.xlsx')
    
    assert df.equals(df_test), ('A3 plasmid oligos are incorrect. Table equailty is printed to help debug', df == df_test)
    
    print('All tests passed!')
