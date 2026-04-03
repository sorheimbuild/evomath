# EvoMath

**A general-purpose immune-system-inspired problem solver.**

Throw any problem at it. It adapts.

---

## What is EvoMath?

EvoMath is a lightweight algorithm inspired by biological immune systems. Like the immune system recognizes and adapts to any pathogen, EvoMath adapts to any problem you give it.

**Core Philosophy:** Instead of specialized algorithms for each problem type, one general system that learns and adapts.

---

## Key Concepts

| Biology | EvoMath | Role |
|---------|--------|------|
| Antigen | Problem | The challenge to solve |
| Antibody | Solution | A candidate solution |
| B-cells | Population | Pool of candidate solutions |
| IgM → IgG | Antibody Class | Naive → Refined evolution |
| Complement | Verification | Parallel checking mechanisms |
| Memory | Learned Patterns | Successful solutions remembered |
| Antibiotics | Heuristics | External guidance |
| Clonal Selection | Affinity-based mutation | Better solutions mutate less |

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

- **General-Purpose**: Works on any problem definable with input/output pairs
- **Energy-Efficient**: Lightweight design, runs on Raspberry Pi
- **Self-Adaptive**: Immune metaphor means automatic adaptation
- **Memory**: Remembers successful patterns
- **Elegance**: Prefers simple, beautiful solutions over complex ones
- **Multi-Target**: Validates against multiple test cases

---

## Proof of Concept Benchmarks

| Problem | Description | Success Rate | Avg Time |
|---------|-------------|-------------|----------|
| Linear: `2x` | `f(x) = 2x` | 100% (3/3) | 0.03s |
| Quadratic: `x²` | `f(x) = x²` | 100% (3/3) | 0.03s |
| Cubic: `x³` | `f(x) = x³` | 100% (3/3) | 2.57s |

**Test conditions:** Population=100, Generations=30-50

**Benchmark code:** See `benchmark()` function in `evomath.py`

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

## Future Directions

- [ ] Test on physics/chemistry problems
- [ ] Real-world dataset symbolic regression
- [ ] Multi-objective optimization
- [ ] Distributed population (parallel computing)
- [ ] Self-tuning parameters

---

## Comparison to Alternatives

| Approach | Elegance | Efficiency | Adaptability |
|----------|----------|-----------|--------------|
| Brute Force | ❌ | ❌ | ❌ |
| Neural Networks | ❌ | ✓ | ✓ |
| GP/Genetic Programming | ✓ | ✓ | ✓ |
| **EvoMath** | ✓✓ | ✓✓ | ✓✓✓ |

---

## Status

**v0.8.0** - Core immune system implemented, benchmarks passing.

Active development. Throw problems at it, see what happens.

---

## License

MIT License

---

*"What if elegance itself could be evolved?"*
