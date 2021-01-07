# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:03:34 2020

@author: michaelvolk
"""

def hr_donor(gene = 'can1', anneal_temp = 57):
    
    import requests
    from Bio.SeqUtils import MeltingTemp as mt
    from Bio.Seq import Seq
    
    #query SGD api for interaction details
    SGD_baseurl = "https://yeastgenome.org/backend"
    parameter = '/locus/gene/sequence_details'
    parameter_lst = parameter.split("/")
    parameter_lst[-2] = gene
    parameter_details = "/".join(parameter_lst)
    url = SGD_baseurl + parameter_details
    response = requests.get(url).json()   
    
    one_kb = [elem for elem in response['1kb'] if elem['strain']['format_name'] == 'S288C'][0]
    residues = one_kb['residues']
    plus_one_kb = residues[:1000]
    minus_one_kb = residues[-1000:]
    
    #homology donor needs to be 120 bp donor
    for i in range(1, 60):
        overlap = plus_one_kb[-i:] + minus_one_kb[:i]
        if mt.Tm_NN(overlap) >= anneal_temp:
            up_oh = plus_one_kb[-i:]
            down_oh = minus_one_kb[:i]
            break
        overlap = plus_one_kb[-i - 1:] + minus_one_kb[:i]
        if mt.Tm_NN(overlap) >= anneal_temp:
            up_oh = plus_one_kb[-i - 1:]
            down_oh = minus_one_kb[:i]
            break
        overlap = plus_one_kb[-i:] + minus_one_kb[:i + 1]
        if mt.Tm_NN(overlap) >= anneal_temp:
            up_oh = plus_one_kb[-i:]
            down_oh = minus_one_kb[:i + 1]
            break
        
    primer_F = plus_one_kb[-60:] + down_oh
    primer_R = up_oh + minus_one_kb[:60]
    primer_R = str(Seq(primer_R).reverse_complement())

    return (primer_F, primer_R)