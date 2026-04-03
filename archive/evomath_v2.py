import random
import math
from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple, Optional
from enum import Enum
from collections import defaultdict

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
        }
        
        if self.op in ops:
            if self.op in (Operator.SIN.value, Operator.COS.value, Operator.LOG.value, 
                          Operator.SQRT.value, Operator.EXP.value, Operator.ABS.value):
                return ops[self.op](l, 0)
            return ops[self.op](l, r)
        
        return 0
    
    def complexity(self) -> int:
        if self.op in ("CONST", "VAR"):
            return 1
        if self.op in (Operator.SIN.value, Operator.COS.value, Operator.LOG.value, 
                      Operator.SQRT.value, Operator.EXP.value, Operator.ABS.value):
            return 1 + self.left.complexity() if self.left else 2
        left_c = self.left.complexity() if self.left else 1
        right_c = self.right.complexity() if self.right else 1
        return 1 + left_c + right_c
    
    def count_ops(self) -> int:
        if self.op in ("CONST", "VAR"):
            return 0
        count = 1
        if self.left:
            count += self.left.count_ops()
        if self.right:
            count += self.right.count_ops()
        return count
    
    def to_string(self) -> str:
        if self.op == "CONST":
            return f"{self.value:.4g}"
        if self.op == "VAR":
            return str(self.value)
        
        l = self.left.to_string() if self.left else "?"
        r = self.right.to_string() if self.right else "?"
        
        unary_ops = {Operator.SIN.value, Operator.COS.value, Operator.LOG.value, 
                    Operator.SQRT.value, Operator.EXP.value, Operator.ABS.value}
        
        if self.op in unary_ops:
            return f"{self.op}({l})"
        return f"({l}{self.op}{r})"
    
    def hashable(self) -> str:
        if self.op == "CONST":
            return f"C{self.value:.6f}"
        if self.op == "VAR":
            return f"V{self.value}"
        if self.op in (Operator.SIN.value, Operator.COS.value, Operator.LOG.value, 
                      Operator.SQRT.value, Operator.EXP.value, Operator.ABS.value):
            return f"U{self.op}({self.left.hashable() if self.left else 'X'})"
        return f"B({self.op}[{self.left.hashable() if self.left else 'X'}][{self.right.hashable() if self.right else 'X'}])"


@dataclass
class TCell:
    node: Node
    fitness: float = 0.0
    origin: str = "naive"
    age: int = 0
    hits: int = 0
    memory_strength: float = 1.0
    
@dataclass
class Antigen:
    test_cases: List[Tuple[Dict[str, float], float]]
    description: str = ""


class SymbolicSimplifier:
    def simplify(self, node: Node) -> Node:
        node = self.dce(node)
        node = self.constant_fold(node)
        node = self.algebraic_simplify(node)
        return node
    
    def dce(self, node: Node) -> Node:
        if node.op in ("CONST", "VAR"):
            return node
        
        left = self.dce(node.left) if node.left else None
        right = self.dce(node.right) if node.right else None
        
        if node.op in (Operator.SIN.value, Operator.COS.value, Operator.LOG.value, 
                      Operator.SQRT.value, Operator.EXP.value, Operator.ABS.value):
            if left and left.op == "CONST":
                try:
                    val = node.evaluate({})
                    return Node(op="CONST", value=val)
                except:
                    pass
            return Node(op=node.op, left=left)
        
        if left and left.op == "CONST" and right and right.op == "CONST":
            try:
                val = node.evaluate({})
                return Node(op="CONST", value=val)
            except:
                pass
        
        return Node(op=node.op, left=left, right=right)
    
    def constant_fold(self, node: Node) -> Node:
        if node.op in ("CONST", "VAR"):
            return node
        
        left = self.constant_fold(node.left) if node.left else None
        right = self.constant_fold(node.right) if node.right else None
        
        if node.op == Operator.ADD.value:
            if left and left.op == "CONST" and left.value == 0:
                return right
            if right and right.op == "CONST" and right.value == 0:
                return left
            if left and right and left.op == "CONST" and right.op == "CONST":
                return Node(op="CONST", value=left.value + right.value)
        
        if node.op == Operator.SUB.value:
            if right and right.op == "CONST" and right.value == 0:
                return left
            if left and right and left.op == "CONST" and right.op == "CONST":
                return Node(op="CONST", value=left.value - right.value)
        
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
    
    def algebraic_simplify(self, node: Node) -> Node:
        if node.op in ("CONST", "VAR"):
            return node
        
        left = self.algebraic_simplify(node.left) if node.left else None
        right = self.algebraic_simplify(node.right) if node.right else None
        
        if node.op == Operator.ADD.value:
            if left and right:
                if left.op == "VAR" and right.op == "VAR" and left.value == right.value:
                    return Node(op=Operator.MUL.value, 
                              left=Node(op="CONST", value=2), 
                              right=Node(op="VAR", value=left.value))
        
        if node.op == Operator.MUL.value:
            if left and right:
                if left.op == Operator.POW.value and right.op == Operator.POW.value:
                    if left.left and right.left and left.left.op == "VAR" and right.left.op == "VAR":
                        if left.left.value == right.left.value:
                            new_exp = Node(op=Operator.ADD.value,
                                         left=left.right, right=right.right)
                            return Node(op=Operator.POW.value,
                                       left=Node(op="VAR", value=left.left.value),
                                       right=self.algebraic_simplify(new_exp))
        
        return Node(op=node.op, left=left, right=right)


@dataclass
class ImmuneMemory:
    patterns: Dict[str, Node] = field(default_factory=dict)
    success_count: Dict[str, int] = field(default_factory=dict)
    last_used: Dict[str, int] = field(default_factory=dict)
    decay_rate: float = 0.95
    
    def store(self, pattern_id: str, node: Node, generation: int):
        if pattern_id not in self.patterns or random.random() < 0.3:
            self.patterns[pattern_id] = node.clone()
        self.success_count[pattern_id] = self.success_count.get(pattern_id, 0) + 1
        self.last_used[pattern_id] = generation
    
    def get_diverse_patterns(self, n: int = 10, generation: int = 0) -> List[Tuple[str, Node, float]]:
        candidates = []
        for pid, node in self.patterns.items():
            usage = self.success_count.get(pid, 0)
            age_cost = self.decay_rate ** (generation - self.last_used.get(pid, 0))
            weight = usage * age_cost
            candidates.append((pid, node, weight))
        
        candidates.sort(key=lambda x: x[2], reverse=True)
        selected = []
        for pid, node, weight in candidates[:min(n * 2, len(candidates))]:
            selected.append((pid, node, weight))
            if len(selected) >= n:
                break
        return selected
    
    def decay_all(self, generation: int):
        for pid in list(self.success_count.keys()):
            if generation - self.last_used.get(pid, 0) > 50:
                self.success_count[pid] = int(self.success_count[pid] * self.decay_rate)


class EvoMathV2:
    def __init__(self, 
                 population_size: int = 1000,
                 naive_ratio: float = 0.2,
                 memory_ratio: float = 0.3,
                 mutation_rate: float = 0.15,
                 memory_decay_rate: float = 0.97):
        self.population_size = population_size
        self.naive_ratio = naive_ratio
        self.memory_ratio = memory_ratio
        self.mutation_rate = mutation_rate
        self.memory_decay_rate = memory_decay_rate
        
        self.population: List[TCell] = []
        self.memory = ImmuneMemory(decay_rate=memory_decay_rate)
        self.simplifier = SymbolicSimplifier()
        
        self.generation = 0
        self.best_ever: Optional[TCell] = None
        self.history: List[float] = []
        
        self.binary_ops = [op.value for op in [Operator.ADD, Operator.SUB, Operator.MUL, Operator.DIV, Operator.POW, Operator.MOD]]
        self.unary_ops = [op.value for op in [Operator.SIN, Operator.COS, Operator.LOG, Operator.SQRT, Operator.EXP, Operator.ABS]]
    
    def random_node(self, depth: int = 0, max_depth: int = 5) -> Node:
        if depth >= max_depth or random.random() < 0.25:
            if random.random() < 0.6:
                val = random.choice([0, 1, 2, 3, 0.5, 0.1, 0.01, math.pi, math.e, 2.718, 1.414])
                if random.random() < 0.3:
                    val = random.uniform(-5, 5)
                return Node(op="CONST", value=val)
            return Node(op="VAR", value=random.choice(['x', 'y', 'z', 'n', 't']))
        
        if random.random() < 0.25:
            op = random.choice(self.unary_ops)
            return Node(op=op, left=self.random_node(depth + 1, max_depth))
        
        op = random.choice(self.binary_ops)
        return Node(op=op,
                   left=self.random_node(depth + 1, max_depth),
                   right=self.random_node(depth + 1, max_depth))
    
    def initialize_population(self, antigen: Antigen):
        self.population = []
        naive_count = int(self.population_size * self.naive_ratio)
        memory_count = int(self.population_size * self.memory_ratio)
        derived_count = self.population_size - naive_count - memory_count
        
        for _ in range(naive_count):
            self.population.append(TCell(
                node=self.random_node(max_depth=random.randint(2, 6)),
                origin="naive"
            ))
        
        patterns = self.memory.get_diverse_patterns(n=memory_count, generation=self.generation)
        for pid, node, weight in patterns:
            tcell = TCell(node=node.clone(), origin="memory", memory_strength=min(weight, 2.0))
            self.population.append(tcell)
        
        while len(self.population) < naive_count + memory_count:
            self.population.append(TCell(
                node=self.random_node(max_depth=3),
                origin="naive"
            ))
        
        if self.best_ever and self.best_ever.node:
            for _ in range(derived_count):
                tcell = TCell(
                    node=self.mutate_node(self.best_ever.node.clone()),
                    origin="derived"
                )
                self.population.append(tcell)
        else:
            for _ in range(derived_count):
                self.population.append(TCell(
                    node=self.random_node(max_depth=random.randint(3, 5)),
                    origin="naive"
                ))
    
    def mutate_node(self, node: Node, intensity: float = 1.0) -> Node:
        if random.random() < self.mutation_rate * intensity:
            if random.random() < 0.3:
                return self.random_node(max_depth=random.randint(1, 4))
            
            if node.op == "CONST":
                noise = random.gauss(0, 0.5 * abs(node.value + 0.01))
                return Node(op="CONST", value=node.value + noise)
            
            if node.op == "VAR":
                return Node(op="VAR", value=random.choice(['x', 'y', 'z', 'n', 't']))
            
            if node.op in self.unary_ops:
                child = node.left.clone() if node.left else self.random_node()
                return Node(op=node.op, left=self.mutate_node(child, intensity * 0.8))
            
            left = node.left.clone() if node.left else self.random_node()
            right = node.right.clone() if node.right else self.random_node()
            
            if random.random() < 0.5:
                return Node(op=node.op, left=self.mutate_node(left, intensity * 0.8), right=right)
            return Node(op=node.op, left=left, right=self.mutate_node(right, intensity * 0.8))
        
        return node
    
    def recombine(self, a: Node, b: Node) -> Node:
        if random.random() < 0.4 or a.complexity() < 2:
            return self.mutate_node(a.clone(), intensity=1.5)
        
        a = a.clone()
        b = b.clone()
        
        if random.random() < 0.5:
            return Node(op=a.op if a.op not in ("CONST", "VAR") else b.op,
                       left=a.left if a.left else b.left,
                       right=b.right if b.right else a.right)
        return Node(op=b.op if b.op not in ("CONST", "VAR") else a.op,
                    left=b.left if b.left else a.left,
                    right=a.right if a.right else b.right)
    
    def fitness(self, cell: TCell, antigen: Antigen) -> float:
        node = cell.node
        
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
                    total_error += 0
                else:
                    total_error += error
            except:
                total_error += 1e10
        
        if total_error > 1e9:
            return 0.0
        
        avg_error = total_error / len(antigen.test_cases)
        hit_rate = hits / len(antigen.test_cases)
        complexity = node.complexity()
        op_count = node.count_ops()
        
        if avg_error < 1e-6 and hit_rate == 1.0:
            error_fitness = 10000
            elegance_bonus = 10000 / (complexity ** 0.7)
        else:
            error_fitness = 1.0 / (avg_error + 1e-15)
            elegance_bonus = math.log(complexity + 1) ** 0.3
        
        multi_target_bonus = hit_rate * 500
        
        return (error_fitness * elegance_bonus + multi_target_bonus) * cell.memory_strength
    
    def evolve_generation(self, antigen: Antigen):
        for cell in self.population:
            cell.fitness = self.fitness(cell, antigen)
            cell.age += 1
        
        self.population.sort(key=lambda c: c.fitness, reverse=True)
        
        best = self.population[0]
        if not self.best_ever or best.fitness > self.best_ever.fitness:
            self.best_ever = TCell(
                node=self.simplifier.simplify(best.node.clone()),
                fitness=best.fitness,
                origin="best"
            )
            pattern_id = self.best_ever.node.hashable()
            self.memory.store(pattern_id, self.best_ever.node, self.generation)
        
        self.history.append(best.fitness)
        
        naive_count = int(self.population_size * self.naive_ratio)
        memory_count = int(self.population_size * self.memory_ratio)
        derived_count = self.population_size - naive_count - memory_count
        
        elites = self.population[:max(3, self.population_size // 30)]
        
        new_population = []
        
        for cell in elites:
            new_cell = TCell(
                node=self.simplifier.simplify(cell.node.clone()),
                fitness=cell.fitness,
                origin=cell.origin,
                age=0
            )
            new_population.append(new_cell)
        
        patterns = self.memory.get_diverse_patterns(n=memory_count, generation=self.generation)
        for pid, node, weight in patterns:
            tcell = TCell(node=node.clone(), origin="memory", memory_strength=min(weight, 2.0), age=0)
            new_population.append(tcell)
        
        while len(new_population) < naive_count + memory_count:
            new_population.append(TCell(
                node=self.random_node(max_depth=random.randint(2, 5)),
                origin="naive",
                age=0
            ))
        
        derived_needed = derived_count - len(new_population) + self.population_size
        if derived_needed > 0:
            for _ in range(derived_needed):
                p1, p2 = random.sample(elites, 2)
                child_node = self.recombine(p1.node, p2.node)
                child_node = self.mutate_node(child_node)
                new_population.append(TCell(node=child_node, origin="derived", age=0))
        
        while len(new_population) < self.population_size:
            new_population.append(TCell(
                node=self.random_node(max_depth=random.randint(1, 4)),
                origin="naive",
                age=0
            ))
        
        self.population = new_population[:self.population_size]
        self.generation += 1
        
        if self.generation % 100 == 0:
            self.memory.decay_all(self.generation)
    
    def solve(self, antigen: Antigen, max_generations: int = 500, verbose: bool = True) -> Node:
        self.initialize_population(antigen)
        
        for i in range(max_generations):
            self.evolve_generation(antigen)
            
            best = self.population[0]
            
            if verbose and i % 50 == 0:
                simplified = self.simplifier.simplify(best.node)
                print(f"Gen {i:4d}: fitness={best.fitness:12.2f} | "
                      f"hits={sum(1 for inp, t in antigen.test_cases if abs(best.node.evaluate(inp) - t) < 1e-6)}/{len(antigen.test_cases)} | "
                      f"complexity={simplified.complexity():3d} | "
                      f"expr={simplified.to_string()[:45]}")
            
            if best.fitness > 10000:
                if verbose:
                    print(f"\n*** SOLUTION at generation {i} ***")
                return self.simplifier.simplify(best.node)
        
        if verbose:
            best = self.population[0]
            simplified = self.simplifier.simplify(best.node)
            print(f"\nBest at gen {max_generations}: {simplified.to_string()}")
            print(f"Fitness: {best.fitness:.4f} | Complexity: {simplified.complexity()}")
        
        return self.simplifier.simplify(self.population[0].node)


def demo():
    print("=" * 70)
    print(" EvoMathV2 - Immune-Inspired Mathematical Evolution")
    print("=" * 70)
    
    evo = EvoMathV2(population_size=800, naive_ratio=0.2, memory_ratio=0.3)
    
    print("\n--- Task 1: Find expression that equals 2x for various x ---")
    test_cases = [
        ({'x': 1, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 2),
        ({'x': 2, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 4),
        ({'x': 3, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 6),
        ({'x': 5, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 10),
        ({'x': 10, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 20),
    ]
    antigen = Antigen(test_cases=test_cases, description="2x")
    solution = evo.solve(antigen, max_generations=300)
    print(f"Solution: {solution.to_string()}")
    for inp, target in test_cases:
        print(f"  x={inp['x']}: {solution.evaluate(inp):.4f} (target: {target})")
    
    print("\n--- Task 2: Find expression for x² ---")
    test_cases = [
        ({'x': 1, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 1),
        ({'x': 2, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 4),
        ({'x': 3, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 9),
        ({'x': 4, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 16),
        ({'x': 5, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 25),
    ]
    antigen = Antigen(test_cases=test_cases, description="x^2")
    evo2 = EvoMathV2(population_size=800, naive_ratio=0.2, memory_ratio=0.3)
    solution = evo2.solve(antigen, max_generations=300)
    print(f"Solution: {solution.to_string()}")
    
    print("\n--- Task 3: Find elegant expression for golden ratio ---")
    test_cases = [
        ({'x': 0, 'y': 0, 'z': 0, 'n': 0, 't': 0}, (1 + math.sqrt(5)) / 2),
    ]
    antigen = Antigen(test_cases=test_cases, description="(1+sqrt(5))/2")
    evo3 = EvoMathV2(population_size=800, naive_ratio=0.2, memory_ratio=0.3)
    solution = evo3.solve(antigen, max_generations=200)
    print(f"Solution: {solution.to_string()}")
    print(f"Value: {solution.evaluate({'x': 0, 'y': 0, 'z': 0, 'n': 0, 't': 0}):.10f}")
    print(f"Target: {(1 + math.sqrt(5)) / 2:.10f}")
    
    print("\n" + "=" * 70)
    print(" Multi-run: Does memory help?")
    print("=" * 70)
    
    times_to_solution = []
    for run in range(3):
        evo_test = EvoMathV2(population_size=600)
        test_cases = [
            ({'x': 1, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 2),
            ({'x': 3, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 6),
            ({'x': 7, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 14),
        ]
        antigen = Antigen(test_cases=test_cases)
        solution = evo_test.solve(antigen, max_generations=200, verbose=False)
        times_to_solution.append(evo_test.generation)
        print(f"  Run {run + 1}: Solved in {evo_test.generation} generations")
    
    print(f"\nAverage: {sum(times_to_solution)/len(times_to_solution):.1f} generations")


if __name__ == "__main__":
    demo()
