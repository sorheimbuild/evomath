"""
EvoMathV4 - Knowledge-Enhanced Evolutionary Algorithm

Integrates the comprehensive KnowledgeBase (327+ entries) into the evolutionary process.
The algorithm now biases toward known mathematical patterns while maintaining diversity.
"""

import random
import math
from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple, Optional
from enum import Enum
from collections import defaultdict

# Import knowledge base
from knowledge_base_v2 import ComprehensiveKnowledgeBase, Domain, KnowledgeEntry

class Operator(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    POW = "**"
    MOD = "%"
    SIN = "sin"
    COS = "cos"
    LOG = "log"
    SQRT = "sqrt"
    EXP = "exp"
    ABS = "abs"
    XOR = "^"
    AND = "&"
    OR = "|"
    SHL = "<<"
    SHR = ">>"
    ROT = "rot"
    NOT = "~"
    FLOOR = "floor"
    CEIL = "ceil"

class AntibodyClass(Enum):
    IGM = "IgM"
    IGG = "IgG"

@dataclass
class Node:
    op: str
    value: Any = None
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    
    def clone(self) -> 'Node':
        if self.op in ("CONST", "VAR"):
            return Node(op=self.op, value=self.value)
        return Node(op=self.op, 
                    left=self.left.clone() if self.left else None,
                    right=self.right.clone() if self.right else None)
    
    def evaluate(self, variables: Dict[str, float]) -> float:
        if self.op == "CONST":
            return self.value
        if self.op == "VAR":
            return variables.get(self.value, 0)
        
        l = self.left.evaluate(variables) if self.left else 0
        r = self.right.evaluate(variables) if self.right else 0
        
        ops = {
            Operator.ADD.value: lambda a, b: a + b,
            Operator.SUB.value: lambda a, b: a - b,
            Operator.MUL.value: lambda a, b: a * b,
            Operator.DIV.value: lambda a, b: a / b if abs(b) > 1e-15 else 1e10,
            Operator.POW.value: lambda a, b: a ** b if a >= 0 or b == int(b) else abs(a) ** b,
            Operator.MOD.value: lambda a, b: a % b if b != 0 else 0,
            Operator.SIN.value: lambda a, b: math.sin(a),
            Operator.COS.value: lambda a, b: math.cos(a),
            Operator.LOG.value: lambda a, b: math.log(abs(a) + 1e-15),
            Operator.SQRT.value: lambda a, b: math.sqrt(abs(a)),
            Operator.EXP.value: lambda a, b: math.exp(a),
            Operator.ABS.value: lambda a, b: abs(a),
            Operator.XOR.value: lambda a, b: int(a) ^ int(b),
            Operator.AND.value: lambda a, b: int(a) & int(b),
            Operator.OR.value: lambda a, b: int(a) | int(b),
            Operator.SHL.value: lambda a, b: int(a) << int(b),
            Operator.SHR.value: lambda a, b: int(a) >> int(b),
            Operator.ROT.value: lambda a, b: ((int(a) << int(b)) | (int(a) >> (32 - int(b)))) % (2**32),
            Operator.NOT.value: lambda a, b: ~int(a),
            Operator.FLOOR.value: lambda a, b: math.floor(a),
            Operator.CEIL.value: lambda a, b: math.ceil(a),
        }
        
        unary_ops = {Operator.SIN.value, Operator.COS.value, Operator.LOG.value, 
                    Operator.SQRT.value, Operator.EXP.value, Operator.ABS.value,
                    Operator.NOT.value, Operator.FLOOR.value, Operator.CEIL.value}
        
        if self.op in ops:
            if self.op in unary_ops:
                return ops[self.op](l, 0)
            return ops[self.op](l, r)
        return 0
    
    def complexity(self) -> int:
        if self.op in ("CONST", "VAR"):
            return 1
        unary_ops = {Operator.SIN.value, Operator.COS.value, Operator.LOG.value, 
                    Operator.SQRT.value, Operator.EXP.value, Operator.ABS.value,
                    Operator.NOT.value, Operator.FLOOR.value, Operator.CEIL.value,
                    Operator.ROT.value}
        if self.op in unary_ops:
            return 1 + self.left.complexity() if self.left else 2
        left_c = self.left.complexity() if self.left else 1
        right_c = self.right.complexity() if self.right else 1
        return 1 + left_c + right_c
    
    def to_string(self) -> str:
        if self.op == "CONST":
            return f"{self.value:.4g}"
        if self.op == "VAR":
            return str(self.value)
        unary_ops = {Operator.SIN.value, Operator.COS.value, Operator.LOG.value, 
                    Operator.SQRT.value, Operator.EXP.value, Operator.ABS.value,
                    Operator.NOT.value, Operator.FLOOR.value, Operator.CEIL.value,
                    Operator.ROT.value}
        l = self.left.to_string() if self.left else "?"
        if self.op in unary_ops:
            return f"{self.op}({l})"
        r = self.right.to_string() if self.right else "?"
        return f"({l}{self.op}{r})"
    
    def hashable(self) -> str:
        if self.op == "CONST":
            return f"C{self.value:.6f}"
        if self.op == "VAR":
            return f"V{self.value}"
        unary_ops = {Operator.SIN.value, Operator.COS.value, Operator.LOG.value, 
                    Operator.SQRT.value, Operator.EXP.value, Operator.ABS.value,
                    Operator.NOT.value, Operator.FLOOR.value, Operator.CEIL.value,
                    Operator.ROT.value}
        if self.op in unary_ops:
            return f"U{self.op}({self.left.hashable() if self.left else 'X'})"
        return f"B({self.op}[{self.left.hashable() if self.left else 'X'}][{self.right.hashable() if self.right else 'X'}])"


@dataclass
class Antibody:
    node: Node
    fitness: float = 0.0
    antibody_class: AntibodyClass = AntibodyClass.IGM
    affinity: float = 1.0
    age: int = 0
    mutations: int = 0
    lineage: str = ""
    knowledge_boost: float = 1.0

@dataclass
class Antigen:
    test_cases: List[Tuple[Dict[str, float], float]]
    description: str = ""


class SymbolicSimplifier:
    def simplify(self, node: Node) -> Node:
        node = self.dce(node)
        node = self.constant_fold(node)
        return node
    
    def dce(self, node: Node) -> Node:
        if node.op in ("CONST", "VAR"):
            return node
        unary_ops = {Operator.SIN.value, Operator.COS.value, Operator.LOG.value, 
                    Operator.SQRT.value, Operator.EXP.value, Operator.ABS.value,
                    Operator.NOT.value, Operator.FLOOR.value, Operator.CEIL.value,
                    Operator.ROT.value}
        left = self.dce(node.left) if node.left else None
        right = self.dce(node.right) if node.right else None
        if node.op in unary_ops:
            if left and left.op == "CONST":
                try:
                    return Node(op="CONST", value=node.evaluate({}))
                except:
                    pass
            return Node(op=node.op, left=left)
        if left and left.op == "CONST" and right and right.op == "CONST":
            try:
                return Node(op="CONST", value=node.evaluate({}))
            except:
                pass
        return Node(op=node.op, left=left, right=right)
    
    def constant_fold(self, node: Node) -> Node:
        if node.op in ("CONST", "VAR"):
            return node
        unary_ops = {Operator.SIN.value, Operator.COS.value, Operator.LOG.value, 
                    Operator.SQRT.value, Operator.EXP.value, Operator.ABS.value,
                    Operator.NOT.value, Operator.FLOOR.value, Operator.CEIL.value,
                    Operator.ROT.value}
        left = self.constant_fold(node.left) if node.left else None
        right = self.constant_fold(node.right) if node.right else None
        
        if node.op == Operator.ADD.value:
            if left and left.op == "CONST" and left.value == 0:
                return right
            if right and right.op == "CONST" and right.value == 0:
                return left
            if left and right and left.op == "CONST" and right.op == "CONST":
                return Node(op="CONST", value=left.value + right.value)
        if node.op == Operator.MUL.value:
            if (left and left.op == "CONST" and left.value == 0) or \
               (right and right.op == "CONST" and right.value == 0):
                return Node(op="CONST", value=0)
            if left and left.op == "CONST" and left.value == 1:
                return right
            if right and right.op == "CONST" and right.value == 1:
                return left
            if left and right and left.op == "CONST" and right.op == "CONST":
                return Node(op="CONST", value=left.value * right.value)
        if node.op == Operator.SUB.value:
            if right and right.op == "CONST" and right.value == 0:
                return left
            if left and right and left.op == "CONST" and right.op == "CONST":
                return Node(op="CONST", value=left.value - right.value)
        if node.op == Operator.DIV.value:
            if left and left.op == "CONST" and left.value == 0:
                return Node(op="CONST", value=0)
            if right and right.op == "CONST" and right.value == 1:
                return left
            if left and right and left.op == "CONST" and right.op == "CONST":
                return Node(op="CONST", value=left.value / right.value if right.value != 0 else 0)
        if node.op == Operator.POW.value:
            if right and right.op == "CONST" and right.value == 0:
                return Node(op="CONST", value=1)
            if right and right.op == "CONST" and right.value == 1:
                return left
            if left and right and left.op == "CONST" and right.op == "CONST":
                return Node(op="CONST", value=math.pow(left.value, right.value))
        
        return Node(op=node.op, left=left, right=right)


class EvoMathV4:
    """
    Knowledge-Enhanced Evolutionary Algorithm
    
    Integrates 327+ mathematical and physics knowledge entries into:
    - Initial population seeding (bias toward known patterns)
    - Mutation guidance (prefer knowledge-relevant structures)
    - Fitness boosting (reward using known identities)
    """
    
    def __init__(self, 
                 population_size: int = 800,
                 igm_ratio: float = 0.35,
                 igg_ratio: float = 0.30,
                 mutation_rate: float = 0.12,
                 knowledge_bias: float = 0.3,
                 memory_decay: float = 0.97):
        
        self.population_size = population_size
        self.igm_ratio = igm_ratio
        self.igg_ratio = igg_ratio
        self.mutation_rate = mutation_rate
        self.knowledge_bias = knowledge_bias
        self.memory_decay = memory_decay
        
        self.population: List[Antibody] = []
        self.memory: Dict[str, Node] = {}
        self.success_count: Dict[str, int] = {}
        self.simplifier = SymbolicSimplifier()
        
        self.generation = 0
        self.best_ever: Optional[Antibody] = None
        self.history: List[float] = []
        
        self.igm_to_igg_conversions = 0
        
        # Load KnowledgeBase
        self.kb = ComprehensiveKnowledgeBase()
        self.knowledge_entries = self.kb.get_all_entries()
        print(f"Loaded {len(self.knowledge_entries)} knowledge entries")
        
        # Build knowledge patterns
        self._build_knowledge_patterns()
        
        self.binary_ops = [op.value for op in [Operator.ADD, Operator.SUB, Operator.MUL, Operator.DIV, Operator.POW, Operator.MOD, Operator.XOR, Operator.AND, Operator.OR, Operator.SHL, Operator.SHR]]
        self.unary_ops = [op.value for op in [Operator.SIN, Operator.COS, Operator.LOG, Operator.SQRT, Operator.EXP, Operator.ABS, Operator.NOT, Operator.FLOOR, Operator.CEIL]]
    
    def _build_knowledge_patterns(self):
        """Extract usable patterns from knowledge base."""
        self.knowledge_nodes: List[Node] = []
        
        for entry in self.knowledge_entries[:100]:
            try:
                node = self._parse_expression(entry.expression)
                if node:
                    self.knowledge_nodes.append(node)
            except:
                pass
        
        print(f"Built {len(self.knowledge_nodes)} knowledge patterns")
    
    def _parse_expression(self, expr: str) -> Optional[Node]:
        """Simple parser for common patterns."""
        import re
        
        # Handle simple cases
        expr = expr.replace(" ", "")
        
        # Constants
        if expr.replace(".", "").replace("-", "").isdigit():
            return Node(op="CONST", value=float(expr))
        
        # Simple binary operations
        for op in ["+", "-", "*", "/", "**"]:
            depth = 0
            for i in range(len(expr) - 1, -1, -1):
                if expr[i] == ')':
                    depth += 1
                elif expr[i] == '(':
                    depth -= 1
                if depth == 0 and expr[i] == op and i > 0:
                    left = self._parse_expression(expr[:i])
                    right = self._parse_expression(expr[i+1:])
                    if left and right:
                        return Node(op=op, left=left, right=right)
        
        # Parentheses
        if expr.startswith("(") and expr.endswith(")"):
            inner = self._parse_expression(expr[1:-1])
            if inner:
                return inner
        
        return None
    
    def random_node(self, depth: int = 0, max_depth: int = 5) -> Node:
        if depth >= max_depth or random.random() < 0.25:
            if random.random() < 0.5:
                val = random.choice([0, 1, 2, 3, 0.5, 0.1, 0.01, math.pi, math.e, 1.414, (1+5**0.5)/2])
                if random.random() < 0.3:
                    val = random.uniform(-5, 5)
                return Node(op="CONST", value=val)
            return Node(op="VAR", value=random.choice(['x', 'y', 'z', 'n', 't']))
        
        if random.random() < 0.2 and self.knowledge_nodes:
            return random.choice(self.knowledge_nodes).clone()
        
        if random.random() < 0.25:
            op = random.choice(self.unary_ops)
            return Node(op=op, left=self.random_node(depth + 1, max_depth))
        
        op = random.choice(self.binary_ops)
        return Node(op=op,
                   left=self.random_node(depth + 1, max_depth),
                   right=self.random_node(depth + 1, max_depth))
    
    def initialize_population(self, antigen: Antigen):
        self.population = []
        igm_count = int(self.population_size * self.igm_ratio)
        igg_count = int(self.population_size * self.igg_ratio)
        naive_count = self.population_size - igm_count - igg_count
        
        for _ in range(naive_count):
            self.population.append(Antibody(
                node=self.random_node(max_depth=random.randint(2, 6)),
                antibody_class=AntibodyClass.IGM,
                lineage="naive"
            ))
        
        for _ in range(igm_count):
            self.population.append(Antibody(
                node=self.random_node(max_depth=random.randint(3, 6)),
                antibody_class=AntibodyClass.IGM,
                knowledge_boost=1.0 + self.knowledge_bias,
                lineage="knowledge_guided"
            ))
        
        for _ in range(igg_count):
            if self.memory:
                pid = random.choice(list(self.memory.keys()))
                self.population.append(Antibody(
                    node=self.memory[pid].clone(),
                    antibody_class=AntibodyClass.IGG,
                    lineage=f"memory:{pid[:8]}"
                ))
            else:
                self.population.append(Antibody(
                    node=self.random_node(max_depth=3),
                    antibody_class=AntibodyClass.IGG,
                    lineage="igg_fill"
                ))
    
    def mutate_node(self, node: Node, intensity: float = 1.0, antibody_class: Optional[AntibodyClass] = None, use_knowledge: bool = False) -> Node:
        mutation_prob = self.mutation_rate * intensity
        
        if antibody_class == AntibodyClass.IGG:
            mutation_prob *= 0.5
        elif antibody_class == AntibodyClass.IGM:
            mutation_prob *= 1.1
        
        if random.random() < mutation_prob:
            if random.random() < 0.25 and self.knowledge_nodes:
                return random.choice(self.knowledge_nodes).clone()
            
            if node.op == "CONST":
                return Node(op="CONST", value=node.value + random.gauss(0, 0.3 * abs(node.value + 0.01)))
            
            if node.op == "VAR":
                return Node(op="VAR", value=random.choice(['x', 'y', 'z', 'n', 't']))
            
            if node.op in self.unary_ops:
                child = node.left.clone() if node.left else self.random_node()
                return Node(op=node.op, left=self.mutate_node(child, intensity * 0.8, antibody_class, use_knowledge))
            
            left = node.left.clone() if node.left else self.random_node()
            right = node.right.clone() if node.right else self.random_node()
            
            if random.random() < 0.5:
                return Node(op=node.op, left=self.mutate_node(left, intensity * 0.8, antibody_class, use_knowledge), right=right)
            return Node(op=node.op, left=left, right=self.mutate_node(right, intensity * 0.8, antibody_class, use_knowledge))
        
        return node
    
    def fitness(self, antibody: Antibody, antigen: Antigen) -> float:
        node = antibody.node
        
        total_error = 0
        hits = 0
        
        for inputs, target in antigen.test_cases:
            try:
                result = node.evaluate(inputs)
                if math.isnan(result) or math.isinf(result):
                    total_error += 1e10
                    continue
                error = abs(result - target)
                if error < 1e-6:
                    hits += 1
                else:
                    total_error += error
            except:
                total_error += 1e10
        
        if total_error > 1e9:
            return 0.0
        
        avg_error = total_error / len(antigen.test_cases)
        hit_rate = hits / len(antigen.test_cases)
        complexity = node.complexity()
        
        if avg_error < 1e-6 and hit_rate == 1.0:
            base_fitness = 10000 / (complexity ** 0.7)
        else:
            base_fitness = (1.0 / (avg_error + 1e-15)) * (math.log(complexity + 1) ** 0.3)
        
        affinity_bonus = 1 + antibody.affinity * 0.3
        class_bonus = 1.15 if antibody.antibody_class == AntibodyClass.IGG else 1.0
        knowledge_bonus = antibody.knowledge_boost
        
        hit_bonus = hit_rate * 500
        
        return (base_fitness * affinity_bonus * class_bonus * knowledge_bonus + hit_bonus)
    
    def evolve_generation(self, antigen: Antigen):
        for antibody in self.population:
            antibody.fitness = self.fitness(antibody, antigen)
            antibody.age += 1
        
        self.population.sort(key=lambda a: a.fitness, reverse=True)
        
        best = self.population[0]
        if not self.best_ever or best.fitness > self.best_ever.fitness:
            self.best_ever = Antibody(
                node=self.simplifier.simplify(best.node.clone()),
                fitness=best.fitness,
                antibody_class=best.antibody_class,
                affinity=best.affinity
            )
            pattern_id = self.best_ever.node.hashable()
            self.memory[pattern_id] = self.best_ever.node.clone()
            self.success_count[pattern_id] = self.success_count.get(pattern_id, 0) + 1
        
        self.history.append(best.fitness)
        
        elite_count = max(2, self.population_size // 20)
        elites = self.population[:elite_count]
        
        new_population = []
        
        for antibody in elites[:3]:
            if antibody.fitness > 70:
                self.igm_to_igg_conversions += 1
                new_population.append(Antibody(
                    node=self.simplifier.simplify(antibody.node.clone()),
                    antibody_class=AntibodyClass.IGG,
                    affinity=antibody.affinity * 1.5,
                    age=0
                ))
            else:
                new_population.append(Antibody(
                    node=self.simplifier.simplify(antibody.node.clone()),
                    fitness=antibody.fitness,
                    antibody_class=antibody.antibody_class,
                    age=0
                ))
        
        while len(new_population) < self.population_size:
            if len(elites) >= 2 and random.random() < 0.7:
                p1, p2 = random.sample(elites, 2)
                parent = p1 if p1.fitness > p2.fitness else p2
                child_node = self.mutate_node(parent.node.clone(), intensity=1.5, antibody_class=parent.antibody_class)
                new_population.append(Antibody(
                    node=child_node,
                    antibody_class=parent.antibody_class,
                    knowledge_boost=parent.knowledge_boost,
                    age=0
                ))
            else:
                new_population.append(Antibody(
                    node=self.random_node(max_depth=random.randint(2, 5)),
                    antibody_class=AntibodyClass.IGM,
                    age=0
                ))
        
        self.population = new_population[:self.population_size]
        self.generation += 1
    
    def solve(self, antigen: Antigen, max_generations: int = 300, verbose: bool = True) -> Node:
        self.initialize_population(antigen)
        
        for i in range(max_generations):
            self.evolve_generation(antigen)
            
            if verbose and (i % 50 == 0 or i < 5):
                best = self.population[0]
                simplified = self.simplifier.simplify(best.node)
                igg_count = len([a for a in self.population if a.antibody_class == AntibodyClass.IGG])
                kb_count = len([a for a in self.population if a.knowledge_boost > 1.0])
                print(f"Gen {i:4d}: fitness={best.fitness:12.2f} | "
                      f"hits={sum(1 for inp, t in antigen.test_cases if abs(best.node.evaluate(inp) - t) < 1e-6)}/{len(antigen.test_cases)} | "
                      f"IgG={igg_count:3d} | KB={kb_count:3d} | "
                      f"expr={simplified.to_string()[:35]}")
            
            if best.fitness > 10000:
                if verbose:
                    print(f"\n*** SOLUTION at generation {i} ***")
                return self.simplifier.simplify(best.node)
        
        if verbose:
            best = self.population[0]
            simplified = self.simplifier.simplify(best.node)
            print(f"\nBest at gen {max_generations}: {simplified.to_string()}")
            print(f"Fitness: {best.fitness:.4f}")
        
        return self.simplifier.simplify(self.population[0].node)


def benchmark():
    """Compare v4 (knowledge-enhanced) vs random search."""
    import time
    
    print("=" * 70)
    print(" EvoMathV4 - Knowledge-Enhanced Benchmark")
    print("=" * 70)
    
    problems = [
        ("Linear: 3x", [({'x': 1}, 3), ({'x': 2}, 6), ({'x': 3}, 9), ({'x': 5}, 15)]),
        ("Quadratic: x^2", [({'x': 1}, 1), ({'x': 2}, 4), ({'x': 3}, 9), ({'x': 4}, 16)]),
        ("Cubic: x^3", [({'x': 1}, 1), ({'x': 2}, 8), ({'x': 3}, 27), ({'x': 4}, 64)]),
        ("Fibonacci-ish: 2x+y", [({'x': 1, 'y': 1}, 3), ({'x': 2, 'y': 3}, 7), ({'x': 3, 'y': 5}, 11)]),
        ("Perfect square: (x+1)^2", [({'x': 1}, 4), ({'x': 2}, 9), ({'x': 3}, 16), ({'x': 4}, 25)]),
        ("Arithmetic: 2x+3", [({'x': 0}, 3), ({'x': 1}, 5), ({'x': 2}, 7), ({'x': 3}, 9)]),
    ]
    
    results = []
    
    for name, test_cases in problems:
        print(f"\n--- {name} ---")
        
        evo = EvoMathV4(population_size=500, knowledge_bias=0.3)
        antigen = Antigen(test_cases=test_cases, description=name)
        
        start = time.time()
        solution = evo.solve(antigen, max_generations=100, verbose=False)
        elapsed = time.time() - start
        
        hits = sum(1 for inp, target in test_cases 
                   if abs(solution.evaluate(inp) - target) < 1e-6)
        
        print(f"  Solution: {solution.to_string()}")
        print(f"  Hits: {hits}/{len(test_cases)}")
        print(f"  Time: {elapsed:.2f}s | Generations: {evo.generation}")
        
        results.append({
            "name": name,
            "solution": solution.to_string(),
            "hits": hits,
            "total": len(test_cases),
            "time": elapsed,
            "generations": evo.generation
        })
    
    print("\n" + "=" * 70)
    print(" Summary")
    print("=" * 70)
    
    total_hits = sum(r["hits"] for r in results)
    total_tests = sum(r["total"] for r in results)
    
    for r in results:
        status = "PASS" if r["hits"] == r["total"] else "PARTIAL"
        print(f"  {r['name']:25s}: {status} ({r['hits']}/{r['total']}) | {r['time']:.2f}s")
    
    print(f"\nTotal: {total_hits}/{total_tests} ({100*total_hits/total_tests:.1f}%)")


def demo():
    print("=" * 70)
    print(" EvoMathV4 - Knowledge-Enhanced Evolutionary Algorithm")
    print("=" * 70)
    
    evo = EvoMathV4(population_size=500)
    
    print("\n--- Test: Find expression that equals 2x for various x ---")
    test_cases = [
        ({'x': 1, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 2),
        ({'x': 2, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 4),
        ({'x': 3, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 6),
        ({'x': 5, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 10),
        ({'x': 10, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 20),
    ]
    antigen = Antigen(test_cases=test_cases, description="2x")
    solution = evo.solve(antigen, max_generations=150)
    print(f"Solution: {solution.to_string()}")
    
    print("\n--- Test: Find expression for x² ---")
    test_cases = [
        ({'x': 1, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 1),
        ({'x': 2, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 4),
        ({'x': 3, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 9),
        ({'x': 4, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 16),
        ({'x': 5, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 25),
    ]
    antigen = Antigen(test_cases=test_cases, description="x^2")
    solution = evo.solve(antigen, max_generations=150)
    print(f"Solution: {solution.to_string()}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    demo()
    print("\n")
    benchmark()
