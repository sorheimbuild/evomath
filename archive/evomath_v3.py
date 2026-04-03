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
    XOR = "^"  # Bitwise XOR (crypto critical)
    AND = "&"  # Bitwise AND
    OR = "|"   # Bitwise OR
    SHL = "<<" # Left shift
    SHR = ">>" # Right shift
    ROT = "rot"  # Rotate bits
    NOT = "~"   # Bitwise NOT
    FLOOR = "floor"
    CEIL = "ceil"

class AntibodyClass(Enum):
    IGM = "IgM"      # Naive, broad response
    IGG = "IgG"      # Refined, high affinity

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
class Antibody:
    node: Node
    fitness: float = 0.0
    antibody_class: AntibodyClass = AntibodyClass.IGM
    affinity: float = 1.0
    age: int = 0
    mutations: int = 0
    lineage: str = ""
    
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


class ImmuneMemory:
    def __init__(self, decay_rate: float = 0.97):
        self.patterns: Dict[str, Node] = {}
        self.success_count: Dict[str, int] = {}
        self.last_used: Dict[str, int] = {}
        self.decay_rate = decay_rate
    
    def store(self, pattern_id: str, node: Node, generation: int):
        if pattern_id not in self.patterns or random.random() < 0.3:
            self.patterns[pattern_id] = node.clone()
        self.success_count[pattern_id] = self.success_count.get(pattern_id, 0) + 1
        self.last_used[pattern_id] = generation
    
    def get_diverse_patterns(self, n: int = 10, generation: int = 0) -> List[Tuple[str, Node, float]]:
        candidates = []
        for pid, node in self.patterns.items():
            usage = self.success_count.get(pid, 0)
            age_cost = self.decay_rate ** max(0, generation - self.last_used.get(pid, 0))
            weight = usage * age_cost
            candidates.append((pid, node, weight))
        
        candidates.sort(key=lambda x: x[2], reverse=True)
        return [(pid, node, weight) for pid, node, weight in candidates[:n]]
    
    def decay_all(self, generation: int):
        for pid in list(self.success_count.keys()):
            if generation - self.last_used.get(pid, 0) > 50:
                self.success_count[pid] = int(self.success_count[pid] * self.decay_rate)


class EvoMathV3:
    """
    Immune-system-inspired evolutionary algorithm with antibody maturation.
    
    Phases:
    1. IgM Response: Initial broad exploration (large population, high mutation)
    2. Affinity Maturation: Selection + somatic hypermutation (reduced population, focused mutation)
    3. Class Switching: Best IgM antibodies switch to IgG (specialized, high affinity)
    """
    
    def __init__(self, 
                 population_size: int = 1000,
                 igm_ratio: float = 0.4,
                 igg_ratio: float = 0.3,
                 mutation_rate: float = 0.15,
                 maturation_threshold: float = 0.7,
                 memory_decay: float = 0.97):
        
        self.population_size = population_size
        self.igm_ratio = igm_ratio
        self.igg_ratio = igg_ratio
        self.mutation_rate = mutation_rate
        self.maturation_threshold = maturation_threshold
        self.memory_decay = memory_decay
        
        self.population: List[Antibody] = []
        self.memory = ImmuneMemory(decay_rate=memory_decay)
        self.simplifier = SymbolicSimplifier()
        
        self.generation = 0
        self.best_ever: Optional[Antibody] = None
        self.history: List[float] = []
        
        self.phase = "IgM"
        self.maturation_cycle = 0
        self.igm_to_igg_conversions = 0
        
        self.binary_ops = [op.value for op in [Operator.ADD, Operator.SUB, Operator.MUL, Operator.DIV, Operator.POW, Operator.MOD, Operator.XOR, Operator.AND, Operator.OR, Operator.SHL, Operator.SHR, Operator.ROT]]
        self.unary_ops = [op.value for op in [Operator.SIN, Operator.COS, Operator.LOG, Operator.SQRT, Operator.EXP, Operator.ABS, Operator.NOT, Operator.FLOOR, Operator.CEIL]]
    
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
                lineage="igm_pool"
            ))
        
        patterns = self.memory.get_diverse_patterns(n=igg_count, generation=self.generation)
        for pid, node, weight in patterns:
            self.population.append(Antibody(
                node=node.clone(),
                antibody_class=AntibodyClass.IGG,
                affinity=min(weight, 3.0),
                lineage=f"memory:{pid[:8]}"
            ))
        
        while len(self.population) < self.population_size:
            self.population.append(Antibody(
                node=self.random_node(max_depth=3),
                antibody_class=AntibodyClass.IGM,
                lineage="fill"
            ))
    
    def mutate_node(self, node: Node, intensity: float = 1.0, antibody_class: Optional[AntibodyClass] = None) -> Node:
        mutation_prob = self.mutation_rate * intensity
        
        if antibody_class == AntibodyClass.IGG:
            mutation_prob *= 0.5
        elif antibody_class == AntibodyClass.IGM:
            mutation_prob *= 1.2
        
        if random.random() < mutation_prob:
            if random.random() < 0.3:
                return self.random_node(max_depth=random.randint(1, 4))
            
            if node.op == "CONST":
                noise = random.gauss(0, 0.3 * abs(node.value + 0.01))
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
    
    def somatic_hypermutation(self, antibody: Antibody) -> Antibody:
        new_node = self.mutate_node(antibody.node.clone(), intensity=1.5)
        new_antibody = Antibody(
            node=new_node,
            antibody_class=antibody.antibody_class,
            affinity=antibody.affinity,
            age=0,
            mutations=antibody.mutations + 1,
            lineage=antibody.lineage
        )
        return new_antibody
    
    def class_switch(self, antibody: Antibody) -> Antibody:
        if antibody.antibody_class == AntibodyClass.IGM and antibody.affinity > self.maturation_threshold:
            self.igm_to_igg_conversions += 1
            return Antibody(
                node=self.simplifier.simplify(antibody.node.clone()),
                antibody_class=AntibodyClass.IGG,
                affinity=antibody.affinity * 1.5,
                age=0,
                mutations=antibody.mutations,
                lineage=f"switched:{antibody.lineage}"
            )
        return antibody
    
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
        
        affinity_bonus = 1 + antibody.affinity * 0.5
        
        if antibody.antibody_class == AntibodyClass.IGG:
            affinity_bonus *= 1.2
        
        class_bonus = 1.0
        if antibody.antibody_class == AntibodyClass.IGG:
            class_bonus = 1.2
        
        hit_bonus = hit_rate * 500
        
        return (base_fitness * affinity_bonus * class_bonus + hit_bonus)
    
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
            self.memory.store(pattern_id, self.best_ever.node, self.generation)
        
        self.history.append(best.fitness)
        
        elite_count = max(2, self.population_size // 20)
        elites = self.population[:elite_count]
        
        igm_count = int(self.population_size * self.igm_ratio)
        igg_count = int(self.population_size * self.igg_ratio)
        derived_count = self.population_size - igm_count - igg_count
        
        new_population = []
        
        for antibody in elites:
            if antibody.fitness > self.maturation_threshold * 100:
                switched = self.class_switch(antibody)
                new_population.append(switched)
            else:
                new_population.append(Antibody(
                    node=self.simplifier.simplify(antibody.node.clone()),
                    fitness=antibody.fitness,
                    antibody_class=antibody.antibody_class,
                    affinity=antibody.affinity,
                    age=0
                ))
        
        for _ in range(igm_count - len([a for a in new_population if a.antibody_class == AntibodyClass.IGM])):
            if len(elites) >= 2:
                p1, p2 = random.sample(elites, 2)
                parent = p1 if p1.fitness > p2.fitness else p2
                child = self.somatic_hypermutation(parent)
                new_population.append(child)
            else:
                new_population.append(Antibody(
                    node=self.random_node(max_depth=random.randint(2, 5)),
                    antibody_class=AntibodyClass.IGM
                ))
        
        for _ in range(igg_count - len([a for a in new_population if a.antibody_class == AntibodyClass.IGG])):
            patterns = self.memory.get_diverse_patterns(n=5, generation=self.generation)
            if patterns:
                pid, node, weight = random.choice(patterns)
                new_population.append(Antibody(
                    node=self.mutate_node(node.clone(), intensity=0.3),
                    antibody_class=AntibodyClass.IGG,
                    affinity=min(weight, 3.0),
                    lineage=f"memory:{pid[:8]}"
                ))
            else:
                new_population.append(Antibody(
                    node=self.random_node(max_depth=3),
                    antibody_class=AntibodyClass.IGM
                ))
        
        while len(new_population) < self.population_size:
            new_population.append(Antibody(
                node=self.random_node(max_depth=random.randint(1, 4)),
                antibody_class=AntibodyClass.IGM,
                lineage="fill"
            ))
        
        self.population = new_population[:self.population_size]
        self.generation += 1
        
        self.maturation_cycle += 1
        if self.maturation_cycle >= 50:
            self.maturation_cycle = 0
            self.memory.decay_all(self.generation)
    
    def solve(self, antigen: Antigen, max_generations: int = 500, verbose: bool = True) -> Node:
        self.initialize_population(antigen)
        
        for i in range(max_generations):
            self.evolve_generation(antigen)
            
            best = self.population[0]
            
            if verbose and i % 50 == 0:
                simplified = self.simplifier.simplify(best.node)
                igg_count = len([a for a in self.population if a.antibody_class == AntibodyClass.IGG])
                print(f"Gen {i:4d}: fitness={best.fitness:12.2f} | "
                      f"hits={sum(1 for inp, t in antigen.test_cases if abs(best.node.evaluate(inp) - t) < 1e-6)}/{len(antigen.test_cases)} | "
                      f"IgG={igg_count:3d}/{self.population_size} | "
                      f"expr={simplified.to_string()[:40]}")
            
            if best.fitness > 10000:
                if verbose:
                    print(f"\n*** SOLUTION at generation {i} ***")
                    print(f"Total IgM->IgG conversions: {self.igm_to_igg_conversions}")
                return self.simplifier.simplify(best.node)
        
        if verbose:
            best = self.population[0]
            simplified = self.simplifier.simplify(best.node)
            igg_count = len([a for a in self.population if a.antibody_class == AntibodyClass.IGG])
            print(f"\nBest at gen {max_generations}: {simplified.to_string()}")
            print(f"Fitness: {best.fitness:.4f} | IgG: {igg_count}")
        
        return self.simplifier.simplify(self.population[0].node)


def demo():
    print("=" * 75)
    print(" EvoMathV3 - Antibody Maturation & Class Switching")
    print("=" * 75)
    
    evo = EvoMathV3(population_size=400)
    
    print("\n--- Task 1: Find expression that equals 3x for various x ---")
    test_cases = [
        ({'x': 1, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 3),
        ({'x': 2, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 6),
        ({'x': 3, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 9),
        ({'x': 5, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 15),
        ({'x': 10, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 30),
    ]
    antigen = Antigen(test_cases=test_cases, description="3x")
    solution = evo.solve(antigen, max_generations=150)
    print(f"Solution: {solution.to_string()}")
    
    print("\n--- Task 2: Find expression for x³ ---")
    test_cases = [
        ({'x': 1, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 1),
        ({'x': 2, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 8),
        ({'x': 3, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 27),
        ({'x': 4, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 64),
        ({'x': 5, 'y': 0, 'z': 0, 'n': 0, 't': 0}, 125),
    ]
    antigen = Antigen(test_cases=test_cases, description="x^3")
    evo2 = EvoMathV3(population_size=400)
    solution = evo2.solve(antigen, max_generations=150)
    print(f"Solution: {solution.to_string()}")
    
    print("\n" + "=" * 75)


if __name__ == "__main__":
    demo()
