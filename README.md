# EvoMath

**A lightweight symbolic search engine inspired by immune systems.**

Designed for symbolic regression and structured optimization problems.

---

## What is EvoMath?

EvoMath is a tree-based symbolic search algorithm inspired by biological immune systems. It evolves mathematical expressions to fit input/output data, with a preference for elegant (simple) solutions.

**Core Use Case:** Given input/output pairs, discover the underlying formula.

---

## What It Is (Technically)

EvoMath is:
- **Tree-based symbolic search** - evolves expression trees
- **Genetic programming** with immune-inspired heuristics
- **Symbolic regression** - finding equations from data

It is NOT:
- A general AI
- A neural network
- A solver for all problems

---

## Key Concepts

| Biology | EvoMath | Role |
|---------|---------|------|
| Antigen | Problem | The challenge to solve (test cases) |
| Antibody | Solution | A candidate expression tree |
| B-cells | Population | Pool of candidate expressions |
| IgM → IgG | Antibody Class | Naive → Refined evolution |
| Complement | Verification | Parallel candidate scoring |
| Memory | Elite Archive | Successful patterns stored |
| Antibiotics | Heuristics | External guidance/priors |
| Clonal Selection | Affinity-based mutation | Better solutions mutate less |

---

## Algorithmic Interpretation

| Immune Concept | Technical Implementation |
|----------------|------------------------|
| Clonal Selection | Affinity-proportional mutation - good solutions get small mutations (fine-tuning), bad solutions get large mutations (exploration) |
| Idiotypic Suppression | Diversity preservation - suppress structurally similar solutions to avoid premature convergence |
| Complement Verification | Secondary scoring - parallel evaluation marks promising candidates |
| Memory Cells | Elite archive - store best solutions for reuse |
| Antibiotics | Injected heuristics - domain-specific priors guide search |
| Affinity Maturation | Class switching - IgM (naive) → IgG (refined) based on fitness |

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    ANTIGEN                          │
│              (Problem Definition)                    │
└───────────────────────┬─────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────┐
│                 POPULATION                           │
│  ┌─────────┬─────────┬─────────┬─────────────────┐  │
│  │   IgM   │   IgG   │Memory   │ Complement      │  │
│  │ (naive) │(refined)│(proven) │ (verified)      │  │
│  └─────────┴─────────┴─────────┴─────────────────┘  │
├─────────────────────────────────────────────────────┤
│  Clonal Selection + Crossover + Mutation            │
│  Idiotypic Network (diversity suppression)         │
└───────────────────────┬─────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────┐
│                 ANTIBODY                             │
│              (Solution Found)                        │
└─────────────────────────────────────────────────────┘
```

---

## Features

- **Pure Python** - No external dependencies
- **Low dependency footprint** - Just the standard library
- **No GPU required** - Runs on any Python environment
- **Designed for low-power hardware** - Minimal population (~100-200)
- **Elegance preference** - Prefers simple solutions over complex ones
- **Multi-target validation** - Tests against all input/output pairs

---

## Proof of Concept Benchmarks

### Single Variable
| Problem | Formula | Success Rate | Notes |
|---------|---------|-------------|-------|
| Linear: `2x` | `f(x) = 2x` | 100% | Works reliably |
| Quadratic: `x²` | `f(x) = x²` | 100% | Works reliably |
| Cubic: `x³` | `f(x) = x³` | 100% | Works |

### Multi-Variable (Physics)
| Problem | Formula | Success Rate | Notes |
|---------|---------|-------------|-------|
| F=ma | `m * a` | ~80% | Finds correct formula |
| p=mv | `m * v` | ~60% | Sometimes finds `v+v` |
| d=vt | `v * t` | ~70% | Works |

**Test conditions:** Population=80-100, Generations=25-40

**Benchmark code:** Run `python evomath.py` for physics benchmarks.

---

## Installation

```bash
git clone https://github.com/sorheimbuild/evomath.git
cd evomath
pip install -r requirements.txt
```

No external dependencies required - pure Python.

---

## Quick Start

```python
from evomath import EvoMath, Antigen

# Define your problem
test_cases = [
    ({'x': 1.0}, 2.0),
    ({'x': 2.0}, 4.0),
    ({'x': 3.0}, 6.0),
]

# Create solver
evo = EvoMath(population_size=100)
antigen = Antigen(target="Linear 2x", test_cases=test_cases)

# Solve
solution = evo.solve(antigen, max_generations=50)
print(f"Solution: {solution.to_string()}")  # Output: (x*2)
```

---

## Custom Problems

### Multi-variable
```python
test_cases = [
    ({'x': 2.0, 'y': 3.0}, 5.0),  # x + y
    ({'x': 4.0, 'y': 1.0}, 5.0),
]
```

### Any function
```python
test_cases = [
    ({'x': 1.0}, 1.0),     # f(x) = ?
    ({'x': 2.0}, 8.0),
    ({'x': 3.0}, 27.0),    # Could be x³
]
```

---

## How It Works

1. **Initialize**: Create random antibodies (solutions)
2. **Evaluate**: Test each antibody against test cases
3. **Select**: Pick best antibodies (complement-verified get priority)
4. **Evolve**: 
   - Crossover: Swap subtrees between parents
   - Mutate: Change nodes (smaller mutations for good solutions)
   - Clone: Copy best solutions
5. **Suppress**: Idiotypic network prevents duplicates
6. **Repeat**: Until solution found or max generations

---

## Energy Efficiency Design

EvoMath is designed for low-power devices:

- **Minimal memory**: Population of ~100-200 (vs millions in brute force)
- **Smart search**: Memory + complement reduce redundant computation
- **Early stopping**: Solution found = stop (no wasted cycles)
- **No GPU needed**: Pure Python, runs anywhere

---

## The Immune Metaphor

### Innate Immunity (Complement System)
- Parallel verification of solutions
- Opsonization: marks good solutions
- MAC attack: eliminates bad solutions
- Inflammation: boosts promising regions

### Adaptive Immunity (Antibodies)
- **IgM**: Initial naive response, high diversity
- **IgG**: Refined, matured antibodies
- **Memory**: Long-term pattern storage
- **Clonal Selection**: Better antibodies reproduce more

### External Agents (Antibiotics)
- Domain-specific heuristics
- Constraint injection
- Known pattern guidance

---

## Status

**v0.9.1-beta** - Multi-variable support, improved README credibility.

Active development. For symbolic regression research.

---

## License

MIT License

---

*"What if elegance itself could be evolved?"*
