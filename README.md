# grna_scrape
![gRNA_scrape](/gRNA_scrape.png)

## TO DO MV:
- [x] scrape gRNAs from ATUM and download top 3 guide sequences.
- [x] extract sequence details from SGD API for ATUM.
- [x] create GTR arrays 3 gene knockouts.
- [x] create test file to verify that A3 plasmid is constructed correctly
- [x] function for testing null mutant 
- [x] funciton for testing synthetic lethality 
- [x] function for generating lethality table with ranked mutants
- [x] function ordering top x triple oligos for triple knockouts
- [x] order oligos for top 10 mutants
- [ ] select gg sticky ends based on data from single pot gg efficiency
- [ ] order oligos with improved sticky ends 
- [ ] function for full ORF deletion homology repair oligos
- [ ] Create oligos for double mutants from Onge et al.
- [ ] create historic refernce table in bulk order to check if oligos have already been ordered
- [ ] function for 8bp deltion homolgy repair oligos

## TO DO SP:
- [ ] generate primers with primer 3. Args: sequence and grna loci. Returns IDT order form to order oligos.
- [ ] Incorporate chopchop so we can choose between using chopchop or atum. This can be done similarly with a frontend scrape, which might make it more accessible to everyone since you won't need to download the source to get it working. Or it can be done with the backend.
- [ ] see if you can get the webdriver in atum_grna.py to be a headless browser. If the browser is made headless the .fasta file will not download. This region in the code is marked. This is not a priority.
- [ ] find better DNA art...
 
<pre>-._    _.--'"`'--._    _.--'"`'--._    _.--'"`'--._    _   dariusz szenfeld
    '-:`.'|`|"':-.  '-:`.'|`|"':-.  '-:`.'|`|"':-.  '.` : '.   
  '.  '.  | |  | |'.  '.  | |  | |'.  '.  | |  | |'.  '.:   '.  '.
  : '.  '.| |  | |  '.  '.| |  | |  '.  '.| |  | |  '.  '.  : '.  `.
  '   '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.'   `.
         `-..,..-'       `-..,..-'       `-..,..-'       `         `</pre>
