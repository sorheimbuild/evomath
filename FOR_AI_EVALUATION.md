# EvoMath Project Summary

**For AI Evaluation** - Share this with ChatGPT/Gemini/Claude

---

## What is EvoMath?

**EvoMath** is a tree-based symbolic search engine inspired by biological immune systems. It evolves mathematical expressions to fit input/output data, with a preference for elegant (simple) solutions.

**Core Use Case:** Given input/output pairs, discover the underlying formula.

**Current State:** v0.9.3-beta

---

## The Core Idea

Instead of brute force or specialized algorithms, one "immune system" that:
1. Generates candidate expressions (antibodies)
2. Tests them against test cases (antigens)
3. Evolves best performers (clonal selection)
4. Remembers good patterns (memory cells)
5. Prefers simple solutions (elegance metric)

---

## Technical Implementation

### Expression Tree
```
Node {
    op: str,           # operator: +, *, **, etc.
    value: Any,        # for CONST/VAR nodes
    left: Node,        # left child
    right: Node        # right child
}
```

### Fitness Function
```
fitness = base_fitness * var_coverage_penalty * error_penalty * affinity_bonus * class_bonus
```

Where:
- `var_coverage_penalty`: Forces use of ALL input variables (key fix for multi-variable)
- `elegance_bonus`: Prefers clean math ops over bitwise ops
- `affinity_bonus`: Better solutions mutate less (clonal selection)

### Immune Metaphors Implemented
| Immune Concept | Technical Implementation |
|----------------|------------------------|
| Clonal Selection | Affinity-proportional mutation |
| Idiotypic Suppression | Diversity preservation via hash matching |
| Complement Verification | Parallel candidate scoring |
| Memory Cells | Elite archive storage |
| Antibiotics | Injected heuristics |
| IgM → IgG | Class switching based on fitness |

---

## Benchmark Results

### Single Variable (Working Well)
| Problem | Formula | Success |
|---------|---------|---------|
| 2x | `x * 2` | 100% |
| x² | `x ** 2` | 100% |
| x³ | `x ** 3` | 100% |

### Multi-Variable (Improving)
| Problem | Formula | Success | Notes |
|---------|---------|---------|-------|
| F=ma | `m * a` | ~80% | Now works with var coverage |
| p=mv | `m * v` | ~60% | Sometimes finds `v+v` |
| d=vt | `v * t` | ~70% | Works |

---

## Known Limitations

1. **Stochastic** - Different runs = different results
2. **Bloat** - Sometimes evolves overly complex expressions
3. **Multi-var success rate** - Lower than single-var
4. **Noisy data** - Not robust
5. **Limited testing** - Only simple math/physics problems

---

## What We Want Feedback On

### For ChatGPT/Gemini:

1. **Is this a valid approach?** - Tree-based symbolic search with immune heuristics

2. **What would make it credible?** - We're aiming for "interesting research prototype" not "production tool"

3. **The SHA256 idea:** 
   - Generate a "topographical map" of SHA256 outputs
   - Study the landscape for patterns
   - Is this worth exploring or fundamentally flawed?

4. **Real-world application:**
   - Could this find physics formulas from data?
   - What's a good test case?

5. **Algorithm improvements:**
   - How to improve multi-variable success?
   - Is the immune metaphor adding value or just complexity?

---

## Files

- `evomath.py` - Main implementation (~970 lines)
- `README.md` - Documentation
- `archive/` - Old versions

---

## Prior Art - Immune System Approaches to Symbolic Regression

This validates that EvoMath is building on legitimate research (20+ years):

| Paper | Year | Key Contribution |
|-------|------|------------------|
| Johnson - "Artificial Immune System Programming for Symbolic Regression" | 2003 | First AIS for symbolic regression using clonal selection |
| Gan & Chow - "Clone Selection Programming and Application to Symbolic Regression" | 2008 | CSP combines GEP encoding with immune selection |
| Bernardino & Barbosa - "Grammar-Based Immune Programming for Symbolic Regression" | 2009 | Adds grammar constraints for syntax validity |

**Links:**
- https://link.springer.com/chapter/10.1007/3-540-36599-0_32 (Johnson 2003)
- https://www.sciencedirect.com/science/article/abs/pii/S0957417408001607 (Gan & Chow 2008)
- https://link.springer.com/chapter/10.1007/978-3-642-03246-2_26 (Bernardino 2009)

---

## Contact

For feedback, share this summary with any LLM and ask:
> "What do you think of this EvoMath project? What would you improve? Is the SHA256 idea worth exploring?"

---

## My Thoughts (for AI consideration)

### What's Working
- The immune metaphor provides a memorable narrative
- Single-variable cases work reliably
- The var_coverage penalty fixed multi-variable (key insight)
- Pure Python = portable

### What's Not Working  
- Multi-variable success is inconsistent
- The metaphor might be adding complexity without value
- No real-world validation yet
- Stochastic behavior makes it hard to trust

### Open Questions

1. **Is the immune metaphor doing anything?**
   - Could we achieve same results with standard GP + elitism?
   - Is "idiotypic suppression" just "diversity maintenance"?
   - Are we adding complexity for narrative, or does it actually help?

2. **SHA256 - honest assessment:**
   - SHA256 is a cryptographic hash - by design, it's one-way
   - The "topographical map" idea: visualize output space?
   - Problem: hashes are designed to appear random - no structure to find
   - BUT: maybe there are patterns in how it's computed?

3. **What would make this publishable?**
   - Compare against standard GP (e.g., PySR)
   - Show immune mechanisms actually help (ablation study)
   - Find ONE real-world formula no one knew

### Ideas for Next Steps
- Test on real physics data (not just generated examples)
- Try "leaky metabolic" - allow exploration before elegance penalty
- Add unit checking (MHC-like) for physics problems
- Compare performance to basic GP baseline

