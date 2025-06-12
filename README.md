# Gene Combination Simulator

A simple Python script to simulate all possible combinations of alleles between two parent genes, estimate offspring genotypes, and display the resulting probabilities based on simulation count. This isn’t just Punnett Squares—this is raw allele math powered by code.

---

## Description

This script performs a basic simulation of genetic inheritance. It takes two parent gene strings and calculates every possible gene pairing from those alleles. Then, it runs a specified number of simulations to determine the frequency of each unique genotype.

This is especially useful for mono-hybrid crosses (e.g., `Aa x Aa`), though it technically works for any equal-length gene strings.

---

## How to Use

### 1. Parent Gene Input

You will be prompted to input two gene strings:

- **Line 1:** Enter the *dad's gene* string (e.g., `Aa`).
- **Line 2:** Enter the *mom's gene* string (e.g., `Aa` again).

The gene strings must be of the same length and represent alleles at the same loci. The loop will continue until both inputs match (case-insensitive), enforcing consistency. This is genetics, not chaos.


### 2. Number of Simulations

- **Line 3:** After providing matching genes, enter the number of simulations to run.

## Notes

- The script generates all possible combinations of alleles (Cartesian product).
- The simulation pool is created by extending the base combinations for the number of simulations specified.
- Genotypes with the same alleles in different order are de-duplicated.
- This script is intended for basic simulation and does not model crossover, linkage, or multigenic inheritance. Keep it Mendel-simple.
- No external libraries are required.

---

## Limitations

- Only works properly when both parent genes have the same number of alleles.
- Works best for mono-hybrid or small-scale inheritance patterns.
- The script prints raw lists (e.g., `['A', 'a']`). For prettier genotype formatting like `Aa`, sorting and string conversion can be added.

---

## License

This is open for educational use. Use it, break it, rewrite it, or make it into a genetics-themed video game. Just don’t try to patent `['A', 'a']`.

---

## Credits

Built by someone who respects biology enough to simulate it, but not enough to do it on paper.