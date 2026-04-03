# EvoMath

An immune-system-inspired evolutionary algorithm for discovering elegant mathematical expressions.

## Core Philosophy

Inspired by T-cell diversity in biological immune systems — the body maintains millions of T-cell variations to theoretically handle any organic threat. This project applies the same principle to mathematical discovery: a vast population of candidate solution approaches explores problem space, with memory of successful patterns that fade if not reinforced (just as antibiotic resistance decays without antibiotic pressure).

## Key Features

- **Multi-track population**: Naive (random) + Memory (proven) + Derived (mutations of best) running in parallel
- **Elegance-weighted fitness**: Rewarded solutions that work *and* are compact
- **Symbolic simplification**: Discovered expressions are auto-simplified
- **Memory with decay**: Successful patterns stored, fade over time if unused
- **Multi-target validation**: Solutions must work across multiple test cases, not just one

## Architecture

```
┌─────────────────────────────────────┐
│           POPULATION                 │
├─────────────┬─────────────┬──────────┤
│    NAIVE    │   MEMORY    │ DERIVED  │
│  (random)   │  (proven)   │(mutated) │
│    20%      │     30%     │   50%    │
├─────────────┴─────────────┴──────────┤
│  Multi-target fitness + simplification│
└─────────────────────────────────────┘
```

## The Elegance Metric

```
Fitness = (error_fitness × elegance_bonus + hit_rate × 500) × memory_strength

elegance_bonus = log(complexity + 1) ^ 0.3
```

Lower complexity = more elegant = higher fitness bonus.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from evomath_v2 import EvoMathV2, Antigen

evo = EvoMathV2(population_size=800)

# Multi-target: must work for ALL inputs
test_cases = [
    ({'x': 1, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 2),
    ({'x': 2, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 4),
    ({'x': 3, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 6),
]

antigen = Antigen(test_cases=test_cases)
solution = evo.solve(antigen, max_generations=500)
print(f"Result: {solution.to_string()}")
```

## Future Applications

- Cryptomining: Finding compact mathematical shortcuts to reduce search space
- Theoretical physics: Discovering elegant relationships in data
- Symbolic regression: Finding equations from input/output pairs
- General optimization: Any problem where "elegant" beats "brute force"

## Motivation

Current approaches to mathematical discovery often rely on:
- Brute force search (expensive)
- Heuristic optimization (may miss elegant solutions)
- Neural networks (opaque, not "elegant" by default)

This project asks: What if we evolved *elegance* itself? What if the best solution wasn't the most accurate, but the most beautiful?

## Status

Early development. Working prototype demonstrates core concepts.

## License

Private. All rights reserved.
