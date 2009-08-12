#!/usr/bin/python
import csv
from len_sort import *

gene_names = []
file_reader = csv.reader(open("../allenbraininstitute/mouse/all_brain_genes.csv"), delimiter=",", quotechar="\"")

for gene in file_reader:
    gene_name = gene[0]
    gene_names.append(gene_name)

gene_names.sort(cmp=bylength)

for name in gene_names:
    print name

