# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:58:34 2020

@author: michaelvolk
"""    

def hr_donors (oligo_scaffold_file = 'top10_oligos_2020-11-19.xlsx',
               write_file = True, 
               file_name = 'new'):
    
    import pandas as pd
    from hr_donor import hr_donor
    import datetime
    
    df_scaffold = pd.read_excel(oligo_scaffold_file)
    scaffold_primers = list(df_scaffold['Name'])
    genes = list(set([elem.split('_')[0] for elem in scaffold_primers]))
    
    df_F = pd.read_excel('template-paste-entry.xlsx')
    df_F['Name'] = [gene + '_F' for gene in genes]
    df_F = df_F.assign(Sequence = [hr_donor(gene)[0] for gene in genes])
    
    df_R = pd.read_excel('template-paste-entry.xlsx')
    df_R['Name'] = [gene + '_R' for gene in genes]
    df_R = df_R.assign(Sequence = [hr_donor(gene)[1] for gene in genes])
    
    df = pd.concat([df_F, df_R])
    df = df.sort_values('Name')
    
    #set scale according to sequence length
    df = df.assign(Scale = ['25nm' if len(Sequence) <= 60 else '100nm' for Sequence in df['Sequence']])
    #set purification
    df = df.assign(Purification = "STD")
    
    if write_file == True:
        file_path = './' + file_name + '_hr-donors' + str(datetime.datetime.now()).split(' ')[0] + '.xlsx'
        df.to_excel(file_path, index = False) 
        
    return df