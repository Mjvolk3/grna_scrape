# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:36:52 2020

@author: michaelvolk
"""

def sequence_details(gene = 'YEL063C'):
    
    import requests
    import roman
    
    #query SGD api for sequence details
    SGD_baseurl = "https://yeastgenome.org/backend"
    parameter = '/locus/gene/sequence_details'
    parameter_lst = parameter.split("/")
    parameter_lst[-2] = gene
    parameter_details = "/".join(parameter_lst)
    url = SGD_baseurl + parameter_details
    response = requests.get(url).json()
    
    #find start and end locations of gene
    for i in range(len(response['coding_dna'])): 
        if response['coding_dna'][i]['strain']['display_name'] == "S288C":
            strain_index  = i
    
    start_bp = response['coding_dna'][strain_index]['start']
    end_bp = response['coding_dna'][strain_index]['end']
    
    #find chromosome of gene
    for i in range(len(response['1kb'])): 
        if response['1kb'][i]['contig']['is_chromosome'] == True:
            chr_index  = i 
    
    chromosome = roman.fromRoman(response['1kb'][chr_index]['contig']['display_name'].split(" ")[-1])
    
    return(chromosome, start_bp, end_bp)
    
