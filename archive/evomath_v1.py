import random
import math
from dataclasses import dataclass, field
from typing import List, Callable, Dict, Set, Any
from enum import Enum

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

@dataclass
class Node:
    op: str
    value: Any = None
    left: 'Node' = None
    right: 'Node' = None
    
    def evaluate(self, variables: Dict[str, float]) -> float:
        if self.op == "CONST":
            return self.value
        
        if self.op == "VAR":
            return variables.get(self.value, 0)
        
        if self.op == Operator.ADD.value:
            return self.left.evaluate(variables) + self.right.evaluate(variables)
        if self.op == Operator.SUB.value:
            return self.left.evaluate(variables) - self.right.evaluate(variables)
        if self.op == Operator.MUL.value:
            return self.left.evaluate(variables) * self.right.evaluate(variables)
        if self.op == Operator.DIV.value:
            denom = self.right.evaluate(variables)
            return self.left.evaluate(variables) / denom if denom != 0 else 1e10
        if self.op == Operator.POW.value:
            return self.left.evaluate(variables) ** self.right.evaluate(variables)
        if self.op == Operator.MOD.value:
            return self.left.evaluate(variables) % self.right.evaluate(variables)
        if self.op == Operator.SIN.value:
            return math.sin(self.left.evaluate(variables))
        if self.op == Operator.COS.value:
            return math.cos(self.left.evaluate(variables))
        if self.op == Operator.LOG.value:
            val = self.left.evaluate(variables)
            return math.log(abs(val) + 1e-10)
        if self.op == Operator.SQRT.value:
            return math.sqrt(abs(self.left.evaluate(variables)))
        
        return 0
    
    def complexity(self) -> int:
        if self.op in ("CONST", "VAR"):
            return 1
        return 1 + self.left.complexity() + self.right.complexity()
    
    def to_string(self) -> str:
        if self.op == "CONST":
            return str(self.value)
        if self.op == "VAR":
            return str(self.value)
        
        l, r = self.left.to_string(), self.right.to_string()
        
        if self.op == Operator.SIN.value:
            return f"sin({l})"
        if self.op == Operator.COS.value:
            return f"cos({l})"
        if self.op == Operator.LOG.value:
            return f"log({l})"
        if self.op == Operator.SQRT.value:
            return f"sqrt({l})"
        
        return f"({l}{self.op}{r})"

@dataclass
class TCell:
    chromosome: Node
    fitness: float = 0.0
    antigen_id: str = ""
    memory_marker: bool = False
    
@dataclass
class Antigen:
    inputs: Dict[str, float]
    target: float
    
@dataclass
class MemoryBank:
    patterns: Dict[str, Node] = field(default_factory=dict)
    success_count: Dict[str, int] = field(default_factory=dict)
    
    def store(self, pattern_id: str, node: Node):
        self.patterns[pattern_id] = node
        self.success_count[pattern_id] = self.success_count.get(pattern_id, 0) + 1
    
    def get_pattern(self, pattern_id: str) -> Node:
        return self.patterns.get(pattern_id)
    
    def get_top_patterns(self, n: int = 10) -> List[str]:
        return sorted(self.success_count.keys(), 
                     key=lambda x: self.success_count[x], 
                     reverse=True)[:n]

class EvoMath:
    def __init__(self, population_size: int = 1000, mutation_rate: float = 0.1):
        self.population: List[TCell] = []
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.memory = MemoryBank()
        self.generation = 0
        self.best_ever = None
        
        self.binary_ops = [op.value for op in [Operator.ADD, Operator.SUB, Operator.MUL, Operator.DIV, Operator.POW, Operator.MOD]]
        self.unary_ops = [op.value for op in [Operator.SIN, Operator.COS, Operator.LOG, Operator.SQRT]]
        self.all_ops = self.binary_ops + self.unary_ops
    
    def random_node(self, depth: int = 0, max_depth: int = 4) -> Node:
        if depth >= max_depth or random.random() < 0.3:
            if random.random() < 0.5:
                return Node(op="CONST", value=random.uniform(-10, 10))
            return Node(op="VAR", value=random.choice(['x', 'y', 'z', 'n']))
        
        if random.random() < 0.3:
            op = random.choice(self.unary_ops)
            return Node(op=op, left=self.random_node(depth + 1, max_depth))
        
        op = random.choice(self.binary_ops)
        return Node(op=op, 
                   left=self.random_node(depth + 1, max_depth),
                   right=self.random_node(depth + 1, max_depth))
    
    def initialize_population(self):
        self.population = [
            TCell(chromosome=self.random_node(max_depth=random.randint(2, 6)))
            for _ in range(self.population_size)
        ]
        
        for pattern_id in self.memory.get_top_patterns(100):
            pattern = self.memory.get_pattern(pattern_id)
            if pattern:
                self.population.append(TCell(chromosome=pattern, memory_marker=True))
    
    def fitness(self, cell: TCell, antigen: Antigen) -> float:
        try:
            result = cell.chromosome.evaluate(antigen.inputs)
            
            if math.isnan(result) or math.isinf(result):
                return 0.0
            
            error = abs(result - antigen.target)
            complexity = cell.chromosome.complexity()
            
            if error < 1e-6:
                return 10000.0 / (complexity ** 0.5)
            
            error_fitness = 1.0 / (error + 1e-10)
            elegance_bonus = math.log(complexity + 1) ** 0.5
            
            return error_fitness * elegance_bonus
        except:
            return 0.0
    
    def mutate(self, node: Node) -> Node:
        if random.random() < self.mutation_rate:
            return self.random_node(max_depth=random.randint(1, 4))
        
        if node.op == "CONST":
            return Node(op="CONST", value=node.value + random.gauss(0, 0.5))
        
        if node.op == "VAR":
            return Node(op="VAR", value=random.choice(['x', 'y', 'z', 'n']))
        
        if node.op in self.unary_ops:
            child = node.left if node.left else self.random_node()
            return Node(op=node.op, left=self.mutate(child))
        
        left = node.left if node.left else self.random_node()
        right = node.right if node.right else self.random_node()
        
        if random.random() < 0.5:
            return Node(op=node.op, left=self.mutate(left), right=right)
        return Node(op=node.op, left=left, right=self.mutate(right))
    
    def crossover(self, a: Node, b: Node) -> Node:
        if random.random() < 0.3 or a.complexity() < 2:
            return self.mutate(a)
        
        if random.random() < 0.5:
            return Node(op=a.op, left=a.left, right=b.right)
        return Node(op=a.op, left=b.left, right=a.right)
    
    def evolve_generation(self, antigen: Antigen):
        for cell in self.population:
            cell.fitness = self.fitness(cell, antigen)
        
        self.population.sort(key=lambda c: c.fitness, reverse=True)
        
        if self.population[0].fitness > (self.best_ever.fitness if self.best_ever else 0):
            self.best_ever = TCell(
                chromosome=self.population[0].chromosome,
                fitness=self.population[0].fitness
            )
        
        elite_count = max(2, self.population_size // 50)
        elites = self.population[:elite_count]
        
        new_population = list(elites)
        
        for _ in range(self.population_size - elite_count):
            parent1, parent2 = random.sample(elites, 2)
            child_chromosome = self.crossover(parent1.chromosome, parent2.chromosome)
            child_chromosome = self.mutate(child_chromosome)
            new_population.append(TCell(chromosome=child_chromosome))
        
        self.population = new_population
        self.generation += 1
        
        if self.generation % 100 == 0:
            pattern_id = f"gen_{self.generation}"
            self.memory.store(pattern_id, self.best_ever.chromosome)
    
    def solve(self, antigen: Antigen, max_generations: int = 1000, verbose: bool = True):
        self.initialize_population()
        
        for i in range(max_generations):
            self.evolve_generation(antigen)
            
            if verbose and i % 50 == 0:
                best = self.population[0]
                print(f"Gen {i}: fitness={best.fitness:.4f}, "
                      f"expr={best.chromosome.to_string()[:50]}...")
            
            if best.fitness > 5000:
                if verbose:
                    print(f"Solution found at generation {i}!")
                return best.chromosome
        
        if verbose:
            print(f"Best after {max_generations} generations: {self.population[0].chromosome.to_string()}")
        return self.population[0].chromosome

def demo():
    print("=== EvoMath Demo ===\n")
    
    evo = EvoMath(population_size=500, mutation_rate=0.15)
    
    print("Task 1: Find expression that equals 2x when x=3 (goal: find compact form)")
    inputs = {'x': 3.0, 'y': 0.0, 'z': 0.0, 'n': 0.0}
    target = 6.0
    antigen = Antigen(inputs=inputs, target=target)
    
    solution = evo.solve(antigen, max_generations=200)
    print(f"Result: {solution.to_string()}")
    print(f"Evaluates to: {solution.evaluate(inputs)}\n")
    
    print("Task 2: Find expression for e^pi (elegance search)")
    inputs = {'x': 0.0, 'y': 0.0, 'z': 0.0, 'n': 0.0}
    target = math.e ** math.pi
    antigen = Antigen(inputs=inputs, target=target)
    
    solution = evo.solve(antigen, max_generations=200)
    print(f"Result: {solution.to_string()}")
    print(f"Value: {solution.evaluate(inputs):.6f}")
    print(f"Target: {target:.6f}")
    print(f"Elegance (lower complexity = more elegant): {solution.complexity()}")

if __name__ == "__main__":
    demo()
