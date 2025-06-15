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





#Getting right input again
###############################################################################################
while True:
    simulations = input("How many simulations? ")
    if simulations.isdigit():
        simulations = int(simulations)
        if not bool(simulations):
            print("No simulation for what?")
            print("Invalid input. Please try again.")
        else:
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




#Removing repeated gene code.
##################################################################

def duplicate_remover(sample):
    
    new_sample = []
    
    for _ in sample:
        new_sample.append(tuple(_))
    
    new_sample = set(new_sample)

    return new_sample
##################################################################






#Creation of spawnssss
##########################################################################

children = duplicate_remover(sample)

for comb in children:
    unique = 0
    for child in child_pool:
        if set(comb) == set(child):
            unique += 1
    percent = (unique/len(child_pool)*100)
    print("".join(comb) + ":- " + str(percent), "%")

print(children)
##########################################################################