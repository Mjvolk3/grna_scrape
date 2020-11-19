# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:35:07 2020

@author: michaelvolk
"""

def lethality(ranked_list_file_name = 'top_ranked_2020-11-11.txt',
              start = 0,
              end = 3,
              write_file = False,
              file_name = 'new'):
    
    import pandas as pd
    from null_mutant import null_mutant
    from synthetic_lethal import synthetic_lethal
    
    df = pd.read_csv(ranked_list_file_name, 
                sep = '\t', 
                nrows = end, 
                header = None, 
                names = ['index', 'gene_1', 'gene_2', 'gene_3', 'score'])
    df = df[start:end]
    #check for null mutants
    df_null = pd.DataFrame(index = df.index, columns = ('gene_1_null', 'gene_2_null', 'gene_3_null'))
    for i in range(df.shape[0]):
        df_null.loc[i + start, 'gene_1_null'] = null_mutant(df.loc[i + start, 'gene_1'])
        df_null.loc[i + start, 'gene_2_null'] = null_mutant(df.loc[i + start, 'gene_2'])
        df_null.loc[i + start, 'gene_3_null'] = null_mutant(df.loc[i + start, 'gene_3'])
    
    #check for synthetic lethal mutants
    df_synth_lethal = pd.DataFrame(index = df.index, columns = ('genes_1,2_synth', 'genes_1,3_synth', 'genes_2,3_synth'))
    for i in range(df.shape[0]):
        df_synth_lethal.loc[i + start, 'genes_1,2_synth'] = synthetic_lethal(df.loc[i + start, 'gene_1'], df.loc[i + start, 'gene_2'])
        df_synth_lethal.loc[i + start, 'genes_1,3_synth'] = synthetic_lethal(df.loc[i + start, 'gene_1'], df.loc[i + start, 'gene_3'])
        df_synth_lethal.loc[i + start, 'genes_2,3_synth'] = synthetic_lethal(df.loc[i + start, 'gene_2'], df.loc[i + start, 'gene_3'])
    
    #combine all tables
    df_lethal = pd.concat((df, df_null, df_synth_lethal), axis = 1)
    
    file_path = './' + file_name + '_lethality.xlsx'
    if write_file == True:
        df_lethal.to_excel(file_path)
    
    return df_lethal

 


