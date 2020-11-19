# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:32:46 2020

@author: michaelvolk
"""

def synthetic_lethal(gene_1 = 'csl4', gene_2 = 'cbf1'):
    import requests
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

    return synth_lethal_pair


