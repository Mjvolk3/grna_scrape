# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 01:29:04 2020

@author: michaelvolk
"""
def atum_grna(sequence_details = (5, 31694, 33466),
              num = 10,
              chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe",
              download_base_path = "C:\\Users\\michaelvolk\\downloads\\",
              port = 51060):
    
    from selenium import webdriver
    import time
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    import os
    from Bio import SeqIO
    from selenium.webdriver.chrome.options import Options
    
    chromosome_num = str(sequence_details[0])
    start_bp = sequence_details[1]
    end_bp = sequence_details[2]
    options = Options()
    options.headless = False #For making browser headless https://github.com/TheBrainFamily/chimpy/issues/108
    driver = webdriver.Chrome(chrome_driver_path, options = options, port = port)
   
    driver.get("https://atum.bio/eCommerce/cas9/input")
    
    #Select Genome
    search = driver.find_element_by_id('genomeId')
    for option in search.find_elements_by_tag_name('option'):
            if option.text == 'Saccharomyces cerevisiae S288C (R64-1-1)':
                    option.click()
    
    #Wild-type Cas9
    wtcas9 = driver.find_element_by_id('cas9SearchType1')
    wtcas9.click()
    
    #Open Target Gene
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/form/div/div[1]/div[5]/div[2]/div[1]/a/h4'))).click()
    
    #Select Chromosome
    chromosome = driver.find_element_by_id('chromosomeId')
    for option in chromosome.find_elements_by_tag_name('option'):
        if option.text == chromosome_num:
                    option.click()
    
    #Select genomic region
    start_base = driver.find_element_by_name("startBase")      
    start_base.send_keys(start_bp)
    end_base = driver.find_element_by_name("endBase")
    end_base.send_keys(end_bp)
    
    #search for guides
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/form/div/div[1]/div[5]/div[2]/div[2]/div[4]/button'))).click()
    
    #select drop down to show more guides
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[(@id = "btnShowMore")]'))).click()
    
    for n in range(4,num):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "moreResults", " " )) and (((count(preceding-sibling::*) + 1) = ' + str(n) + ') and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "form-check-input", " " ))]'))).click()
    
    #Continue
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div[3]/div/form/div[3]/div[2]/button'))).click()
    
    #download gRNA fasta
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div/div/fieldset/legend/a'))).click()
    
    time.sleep(5) #if no download, increase sleep time
    driver.quit() 
    
    #get guides from fasta, and remove fasta
    file_name = "gRNA.fasta"
    file_path = download_base_path + file_name 
    
    guides = []
    with open(file_path, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            guides.append(str(record.seq))
    
    os.remove(file_path)
    return(guides)