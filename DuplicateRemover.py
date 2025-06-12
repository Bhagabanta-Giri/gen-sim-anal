children = sample = [['A', 'A'], ['A', 'a'], ['A', 'b'], ['A', 'b'], ['a', 'a'], ['a', 'b'], ['a', 'b'], ['B', 'A'], ['B', 'a'], ['B', 'b'], ['B', 'b'], ['b', 'b'], ['b', 'b']]
def duplicate_remover(sample, children):
    for gene_up in sample:
        for gene_down in sample:
            if gene_up != gene_down and set(gene_up) == set(gene_down):
                children.pop(sample.index(gene_down))
    return children