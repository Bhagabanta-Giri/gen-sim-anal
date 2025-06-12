#Getting right input
###############################################################################################
while True:
    dad_gene = input("Enter Father's Gene: ").replace(" ","")
    mom_gene = input("Enter Mother's Gene: ").replace(" ","")
    if dad_gene.lower() == mom_gene.lower() and dad_gene.isalpha() and len(dad_gene) % 2 == 0:
        break #Loop breaks here when input is alright (Even with spaces)
    else:
        print("DNA mismatch or wrong DNA type. Did someone cheat on Mendel? \nTRY AGAIN")
        #Loop continues for wrong input
###############################################################################################




#creating proper alleles
###############################################################
def allele_creation(given_gene):
    output_allele_set = []
    new_gene_loci1 = given_gene[:int(len(given_gene)/2)]
    new_gene_loci2 = given_gene[int(len(given_gene)/2):]
    for allele1 in new_gene_loci1:
        for allele2 in new_gene_loci2:
            req_allele = allele1
            req_allele += allele2
            output_allele_set.append(req_allele)
    return output_allele_set

dad_alleles = allele_creation(dad_gene)
mom_alleles = allele_creation(mom_gene)
###############################################################





#creating a single sample generation
####################################
sample = [] 

for gene_1 in dad_alleles:
    for gene_2 in mom_alleles:
        combination = []
        combination.append(gene_1)
        combination.append(gene_2)
        sample.append(combination)

####################################





#Getting right input
###############################################################################################
while True:
    simulations = input("How many simulations? ")
    if simulations.isdigit():
        simulations = int(simulations)
        break
    else:
        print("Enter a valid input.\n")
###############################################################################################





#Actual child-pool of all the simulations. (Considering parents have that high stamina -wink)
##########################################################################
child_pool = []
for i in range(simulations):
    child_pool.extend(sample)
##########################################################################





children = sample

def duplicate_remover(sample, children):
    for gene_up in sample:
        for gene_down in sample:
            if gene_up != gene_down and set(gene_up) == set(gene_down):
                children.pop(sample.index(gene_down))
    return children

children = duplicate_remover(sample, children)

for comb in children:
    unique = 0
    for child in child_pool:
        if set(comb) == set(child):
            unique += 1
    percent = (unique/len(child_pool)*100)
    print("".join(comb) + ":- " + str(percent), "%")

print(children)