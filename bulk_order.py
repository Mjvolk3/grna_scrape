# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:44:37 2020

@author: michaelvolk
"""

##########################################
### todo:
# return table of guides along with gene names
# check against existing designs to prevent ordering duplicates
# check if guide sticky ends same
##########################################
def bulk_order(start = 0, 
    end = 1,
    write_file = False,
    file_name = 'ranked'):
    
    import datetime
    import pandas as pd
    from atum_grna import atum_grna
    from sequence_details import sequence_details
    from gtr_array import gtr_array
    from lethal import lethality
    
    df = lethality(start = start, end = end, write_file = True)
    df_oligos = pd.DataFrame()
    #loop is not very efficient since redundant genes are queried and later deleted... this is what came to mind first
    for i in range(df.shape[0]):
        gene_1_gRNAs = atum_grna(sequence_details = sequence_details(df.loc[i + start, 'gene_1']))
        gene_2_gRNAs = atum_grna(sequence_details = sequence_details(df.loc[i + start, 'gene_2']))
        gene_3_gRNAs = atum_grna(sequence_details = sequence_details(df.loc[i + start, 'gene_3']))
        
    return(gene_1_gRNAs, gene_2_gRNAs, gene_3_gRNAs)
        
        #df_triple = gtr_array(gene_names = ((df.loc[i + start, 'gene_1']), (df.loc[i + start, 'gene_2']), (df.loc[i + start, 'gene_3'])),
                      #gRNAs = (gene_1_gRNAs[0] , gene_2_gRNAs[0], gene_3_gRNAs[0]),
                      #optional_oligos = True,
                      #write_file = False)
        #df_oligos = df_oligos.append(df_triple)
    
    if write_file == True:
        file_path = './' + file_name + '_oligos_' + str(datetime.datetime.now()).split(' ')[0] + '.xlsx'
        df_oligos.drop_duplicates().to_excel(file_path, index = False) 
    
    return df_oligos.drop_duplicates()
