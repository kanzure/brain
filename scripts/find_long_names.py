#!/usr/bin/python
"""
find_long_names.py - find ridiculously long gene names used in the human brain
"""
import yaml
from len_sort import *

gene_names = []

genes = yaml.load(open("../allenbraininstitute/brain_genes.yaml"))
for (gene_id) in genes:
    gene = genes[gene_id]
    gene_name = gene["gene name"]
    gene_names.append(gene_name)

gene_names.sort(cmp=bylength)

for name in gene_names:
    print name

