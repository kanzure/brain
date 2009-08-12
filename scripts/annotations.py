#!/usr/bin/python
#see http://biopython.org/wiki/Annotate_Entrez_Gene_IDs
import sys 
from Bio import Entrez
from copy import copy
 
# *Always* tell NCBI who you are
Entrez.email = "kanzure@gmail.com"
 
def retrieve_annotation(id_list): 
    """Annotates Entrez Gene IDs using Bio.Entrez, in particular epost (to
    submit the data to NCBI) and esummary to retrieve the information. 
    Returns a list of dictionaries with the annotations."""
 
    request = Entrez.epost("gene",id=",".join(id_list))
    try:
        result = Entrez.read(request)
    except RuntimeError, e:
        #FIXME: How generate NAs instead of causing an error with invalid IDs?
        print "An error occurred while retrieving the annotations."
        print "The error returned was %s" % e
        sys.exit(-1)
 
    webEnv = result["WebEnv"]
    queryKey = result["QueryKey"]
    data = Entrez.esummary(db="gene", webenv=webEnv, query_key =
            queryKey)
    annotations = Entrez.read(data)
 
    print "Retrieved %d annotations for %d genes" % (len(annotations),
            len(id_list))
 
    return annotations

def yaml_ref(name):
    '''goal: given the name of an attribute, come up with a reasonable name for the yaml reference for pointers to use later'''
    return_name = copy(str(name))
    return_name = return_name.replace(" ", "_")
    return_name = return_name.replace(",", "-")
    return_name = return_name.replace("'", "-")
    return_name = return_name.lower()
    return return_name

def print_data(annotation):
    for gene_data in annotation:
        gene_id = gene_data["Id"]
        gene_symbol = gene_data["NomenclatureSymbol"]
        gene_name = gene_data["Description"]
        print "%s: &%s\n\tentrez id: %s\n\tgene symbol: %s\n\tgene name: \"%s\"" % (gene_symbol, gene_symbol, gene_id, gene_symbol, gene_name)

if __name__ == "__main__":
    file_handler = open("../allenbraininstitute/entrez_geneid_list_human-cortices.txt")
    id_list = file_handler.read()
    id_list = id_list.split("\n")
    annotation = retrieve_annotation(id_list)
    print_data(annotation)
