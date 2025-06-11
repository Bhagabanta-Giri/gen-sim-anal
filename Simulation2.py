#This was an experiment. It will be removed. It is wrong code.

from random import choice, randint

def combine_alleles(dad_gene, mom_gene, simulations):
    """Simulates genetic combinations and outputs percentage occurrence."""
    if len(dad_gene) != len(mom_gene):
        print("Genes must be the same length! Biology has some rules too.")
        return

    gene_length = len(dad_gene)
    sample_pool = []

    for _ in range(simulations):
        child = ""
        for i in range(gene_length):
            allele = choice([dad_gene[i], mom_gene[i]])
            child += allele
        sample_pool.append(child)

    # Count occurrences
    unique_children = set(sample_pool)
    for child in unique_children:
        count = sample_pool.count(child)
        percent = (count / simulations) * 100
        print(f"{child} --> {percent:.2f}%")

# --- Main ---
print("Enter gene pairs (same length). Example: AaBb")

while True:
    dad = input("Enter dad gene: ").strip()
    mom = input("Enter mom gene: ").strip()

    if dad.lower() == mom.lower():
        print("Genes matched. Time for simulation.")
        break
    else:
        print("Genes must be identical in length and loci. Try again.\n")

sim_count = int(input("How many children to simulate? "))

combine_alleles(dad, mom, sim_count)
