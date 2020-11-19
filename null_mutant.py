# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:44:31 2020

@author: michaelvolk
"""

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

    '''l
    import requests
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
    
    