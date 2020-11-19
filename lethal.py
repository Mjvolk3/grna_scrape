# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:46:48 2020

@author: michaelvolk
"""
import requests
import pandas as pd

def null_mutant(gene = 'can1'):
    '''
    Parameters
    ----------
    gene : TYPE, optional
        queried gene for checking null mutant viability. The default is 'can1'.

    Returns
    -------
    str
        whether null mutant is viable, inviable, or NA for inconclusive phenotypic evidence on SGD.
    '''
    
    #query SGD api for sequence details
    SGD_baseurl = "https://yeastgenome.org/backend"
    parameter = '/locus/gene/phenotype_details'
    parameter_lst = parameter.split("/")
    parameter_lst[-2] = gene
    parameter_details = "/".join(parameter_lst)
    url = SGD_baseurl + parameter_details
    response = requests.get(url).json()   
    
    # check gene essentiality https://www.yeastgenome.org/observable/APO:0000113
    phenotype_check = [elem['phenotype']['display_name'] for elem in response]
    if ('viable' in phenotype_check):
        return ('viable')
    elif ('inviable' in phenotype_check):
        return ('inviable')
    else:
        return('unknown')
    
def synthetic_lethal(gene_1 = 'csl4', gene_2 = 'cbf1'):
    '''
    Parameters
    ----------
    gene_1 : TYPE, optional
        Gene queried for synthetic lethal interaction data.Any SGD name is accepted .The default is 'csl4'.
    gene_2 : TYPE, optional
        Gene queried compared against query. Any SGD gene name is accepted.The default is 'cbf1'.

    Returns
    -------
    str
        Synthetic lethal pair, or inconclusive as '-'.
    '''
    
    #query SGD api for interaction details
    SGD_baseurl = "https://yeastgenome.org/backend"
    parameter = '/locus/gene/interaction_details'
    parameter_lst = parameter.split("/")
    parameter_lst[-2] = gene_1
    parameter_details = "/".join(parameter_lst)
    url = SGD_baseurl + parameter_details
    response = requests.get(url).json()   
    
    # check synthetic lethality https://www.yeastgenome.org/blog/tag/synthetic-lethal
    synth_lethal = [elem for elem in response if elem['experiment']['display_name'] == 'Synthetic Lethality']
    neighbors_1 = [elem['locus1']['format_name'] for elem in synth_lethal]
    neighbors_2 = [elem['locus2']['format_name'] for elem in synth_lethal]
    
    # I am assuming these encompass all recorded genetic interactions. Total interaction number agrees with SGD frontend
    synth_lethal_genes = list(set(neighbors_1 + neighbors_2))
    
    #Find systematic name of gene 1
    SGD_baseurl = "https://yeastgenome.org/backend"
    parameter = '/locus/gene'
    parameter_lst = parameter.split("/")
    parameter_lst[-1] = gene_1
    parameter_details = "/".join(parameter_lst)
    url = SGD_baseurl + parameter_details
    response = requests.get(url).json()   
    gene_1_sys_name = response['format_name']
    
    #remove self from list gene list 
    if gene_1_sys_name in synth_lethal_genes:
        synth_lethal_genes.remove(gene_1_sys_name)
    
    #find systematic name of gene 2
    SGD_baseurl = "https://yeastgenome.org/backend"
    parameter = '/locus/gene'
    parameter_lst = parameter.split("/")
    parameter_lst[-1] = gene_2
    parameter_details = "/".join(parameter_lst)
    url = SGD_baseurl + parameter_details
    response = requests.get(url).json()   
    gene_2_sys_name = response['format_name']
    
    #check if two genes create a synthetic lethal pair
    synth_lethal_pair = gene_2_sys_name in synth_lethal_genes

    if synth_lethal_pair:
        return 'lethal'
    else:
        # unconfirmed lethality... need to check all other interactions first
        return '-'
    
def lethality(ranked_list_file_name = 'top_ranked_2020-11-11.txt',
              start = 0,
              end = 2,
              write_file = False,
              file_name = 'new'):
    '''
    Parameters
    ----------
    ranked_list_file_name : TYPE, optional
        trigenic mutant ranked list. The default is 'top_ranked_2020-11-11.txt'.
    start : TYPE, optional
        start of the ranked table. The default is 0.
    end : TYPE, optional
        end of the ranked table. The default is 3.
    write_file : TYPE, optional
        write table to file or not. The default is False.
    file_name : TYPE, optional
        file name where df_lethal is written to. The default is 'new'.

    Returns
    -------
    df_lethal : TYPE
        Dataframe that provides null mutant viablity and synthetic lethal viability.
    '''
    
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
    