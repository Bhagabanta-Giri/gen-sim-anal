# gen-sim-anal — Genetic Simulation & Analysis Toolkit  
_master Branch_

### TL;DR

Simulate gene crossovers. Create theoretical children. Question biology. Repeat.

This branch contains a set of Python scripts designed to:

- Generate allele combinations from gene sequences
- Run bulk simulations of possible offspring gene pairs
- Eliminate duplicates and calculate occurrence stats

It's like Mendel meets Monte Carlo.

---

## 📁 What's in Here?

| File                | What It Does                                                         |
|---------------------|----------------------------------------------------------------------|
| `Simulation`        | Core script. Takes two genes, simulates child combos, outputs stats. |
| `DuplicateRemover`  | Utility to clean, split, and deduplicate gene strings.               |
| `AlleleCreator`     | Takes a single gene and returns all possible allele combinations.    |

All files play well together, even if they pretend not to.

---

## ⚙️ Requirements

- Python 3.x  
- No external libraries (just `random`)

---

## 🧪 Usage Flow

1. Input two matching gene strings (same characters, even length, alphabetic only).
2. Generate alleles via Cartesian crossover logic (Punnett Square).
3. Run as many simulations as needed.
4. Output: Unique gene combinations with their frequency percentages.

Not scientifically rigorous. Not biologically accurate. Surprisingly entertaining.

---

## 🗒️ Notes

- Scripts are modular. Mix and match as needed.
- Originally built for experimental fun. May or may not work on real DNA.
- Definitely works on imagination.

---

## License

None yet. It’s free-range code. Use responsibly—or irresponsibly, we won't judge.
