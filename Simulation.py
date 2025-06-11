sample = []
child_pool_init = []

while True:
    dad_gene = input()
    mom_gene = input()
    if dad_gene.lower() == mom_gene.lower():
        break
    else:
        print("DNA mismatch. Did someone cheat on Mendel? \nTRY AGAIN")


for gene_1 in dad_gene:
    for gene_2 in mom_gene:
        combination = []
        combination.append(gene_1)
        combination.append(gene_2)
        sample.append(combination)
        
simulations = int(input())

for i in range(simulations):
    child_pool_init.extend(sample)

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
    for child in child_pool_init:
        if set(comb) == set(child):
            unique += 1
    percent = (unique/len(child_pool_init)*100)
    print(comb, str(percent))