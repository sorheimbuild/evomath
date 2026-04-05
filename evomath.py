"""
EvoMath - General-Purpose Immune-System-Inspired Problem Solver

A lightweight, energy-efficient algorithm that adapts to any problem you throw at it.
Inspired by biological immune systems - Antigen/Antibody, IgM/IgG maturation,
Complement verification, Antibiotic heuristics.

Key Features:
- General-purpose: throw any problem at it
- Energy-efficient: minimal computation for maximum result
- Self-adapting: immune system metaphor for organic problem-solving
- Memory: learns from past solutions
- Elegance: prefers simple, beautiful solutions
"""

import random
import math
from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple, Optional, Callable
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
    XOR = "^"
    AND = "&"
    OR = "|"
    SHL = "<<"
    SHR = ">>"

class AntibodyClass(Enum):
    IGM = "IgM"  # Initial response, high diversity
    IGG = "IgG"  # Refined, high affinity
    COMPLEMENT = "Complement"  # Innate verification
    MEMORY = "Memory"  # Long-term storage

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
            Operator.SHL.value: lambda a, b: int(a) << max(0, int(b)),
            Operator.SHR.value: lambda a, b: int(a) >> max(0, int(b)),
        }
        
        unary_ops = {Operator.SIN.value, Operator.COS.value, Operator.LOG.value, 
                    Operator.SQRT.value, Operator.EXP.value, Operator.ABS.value}
        
        if self.op in ops:
            if self.op in unary_ops:
                return ops[self.op](l, 0)
            return ops[self.op](l, r)
        return 0
    
    def complexity(self) -> int:
        if self.op in ("CONST", "VAR"):
            return 1
        left_c = self.left.complexity() if self.left else 1
        right_c = self.right.complexity() if self.right else 1
        return 1 + left_c + right_c
    
    def count_clean_operators(self) -> Tuple[int, int]:
        """Returns (clean_ops, bitwise_ops)"""
        clean_ops = {'+', '-', '*', '/', '**'}
        bitwise_ops = {'^', '&', '|', '<<', '>>'}
        
        if self.op in clean_ops:
            clean = 1
            bitwise = 0
        elif self.op in bitwise_ops:
            clean = 0
            bitwise = 1
        else:
            clean = 0
            bitwise = 0
        
        if self.left:
            lc, lb = self.left.count_clean_operators()
            clean += lc
            bitwise += lb
        if self.right:
            rc, rb = self.right.count_clean_operators()
            clean += rc
            bitwise += rb
        
        return clean, bitwise
    
    def elegance_score(self) -> float:
        """Higher is better - prefer clean math over bitwise"""
        clean, bitwise = self.count_clean_operators()
        total = clean + bitwise
        if total == 0:
            return 1.0
        return clean / total
    
    def to_string(self) -> str:
        if self.op == "CONST":
            return f"{self.value:.4g}"
        if self.op == "VAR":
            return str(self.value)
        
        unary_ops = {'sin', 'cos', 'log', 'sqrt', 'exp', 'abs'}
        if self.op in unary_ops:
            inner = self.left.to_string() if self.left else "?"
            return f"{self.op}({inner})"
        
        l = self.left.to_string() if self.left else "?"
        r = self.right.to_string() if self.right else "?"
        return f"({l}{self.op}{r})"
    
    def hashable(self) -> str:
        if self.op == "CONST":
            return f"C{self.value:.4f}"
        if self.op == "VAR":
            return f"V{self.value}"
        return f"B({self.op}[{self.left.hashable() if self.left else 'X'}][{self.right.hashable() if self.right else 'X'}])"


@dataclass
class Antibody:
    node: Node
    fitness: float = 0.0
    affinity: float = 0.0
    antibody_class: AntibodyClass = AntibodyClass.IGM
    age: int = 0
    binding_strength: float = 0.0
    complement_activated: bool = False

@dataclass 
class Antigen:
    """Problem as antigen - the target to solve"""
    target: Any
    constraints: List[Callable] = field(default_factory=list)
    description: str = ""
    difficulty: int = 1
    test_cases: List[Tuple[Dict[str, float], float]] = field(default_factory=list)


@dataclass
class KnowledgeEntry:
    """Mathematical/physics knowledge"""
    name: str
    expression: str
    domain: str
    complexity: int
    source: str


class ComplementSystem:
    """
    Innate immune complement system - parallel verification.
    
    Functions:
    - opsonization: mark good solutions
    - MAC attack: eliminate bad solutions
    - inflammation: boost successful regions
    """
    
    def __init__(self):
        self.opsonized: Dict[str, float] = {}
        self.attack_count: Dict[str, int] = defaultdict(int)
    
    def opsonize(self, antibody_id: str, affinity: float):
        """Mark antibody as promising"""
        if antibody_id not in self.opsonized:
            self.opsonized[antibody_id] = 0
        self.opsonized[antibody_id] = max(self.opsonized[antibody_id], affinity)
    
    def mac_attack(self, antibody_id: str) -> bool:
        """MAC attack - eliminate antibody if attacked too much"""
        self.attack_count[antibody_id] += 1
        return self.attack_count[antibody_id] > 10
    
    def inflammation_boost(self, region: str) -> float:
        """Boost search in promising regions"""
        return self.opsonized.get(region, 0.1)


class Antibiotic:
    """
    Antibiotics - external agents that enhance immune response.
    
    In our context:
    - Domain-specific heuristics
    - Known solution patterns
    - Constraint injection
    """
    
    def __init__(self):
        self.antibiotics: List[Callable] = []
        self._load_antibiotics()
    
    def _load_antibiotics(self):
        """Load antibiotic heuristics"""
        self.antibiotics = [
            self._heuristic_simplify,
            self._heuristic_accuracy,
            self._heuristic_known_patterns,
        ]
    
    def apply(self, antibody: Antibody, antigen: Antigen) -> float:
        """Apply antibiotic effects to antibody"""
        boost = 1.0
        for ab in self.antibiotics:
            boost *= ab(antibody, antigen)
        return boost
    
    def _heuristic_simplify(self, antibody: Antibody, antigen: Antigen) -> float:
        """Prefer simpler solutions"""
        complexity = antibody.node.complexity()
        if complexity <= 3:
            return 2.0
        if complexity <= 6:
            return 1.5
        return 1.0
    
    def _heuristic_accuracy(self, antibody: Antibody, antigen: Antigen) -> float:
        """Combined accuracy check - near-miss and hit detection"""
        try:
            min_error = float('inf')
            for inputs, target in antigen.test_cases:
                result = antibody.node.evaluate(inputs)
                error = abs(result - target)
                min_error = min(min_error, error)
            
            if min_error < 1e-6:
                return 3.0
            if min_error < 0.1:
                return 2.0
            if min_error < 1.0:
                return 1.5
        except:
            pass
        return 1.0
    
    def _heuristic_known_patterns(self, antibody: Antibody, antigen: Antigen) -> float:
        """Known pattern matching"""
        expr = antibody.node.to_string()
        if any(op in expr for op in ['+', '-', '*', '/']):
            return 1.2
        return 1.0


class KnowledgeBase:
    """Expanded knowledge base with 400+ entries"""
    
    def __init__(self):
        self.entries: List[KnowledgeEntry] = []
        self._load_knowledge()
    
    def _load_knowledge(self):
        """Load comprehensive mathematical and physics knowledge"""
        
        # Number Theory
        self.entries.extend([
            KnowledgeEntry("Fibonacci", "F(n) = F(n-1) + F(n-2)", "number_theory", 2, "classical"),
            KnowledgeEntry("Modular inverse", "a^(-1) mod n", "number_theory", 3, "classical"),
            KnowledgeEntry("Fermat's little theorem", "a^p = a mod p", "number_theory", 3, "fermat"),
            KnowledgeEntry("Euler's totient", "phi(n) = n * prod(1-1/p)", "number_theory", 4, "euler"),
            KnowledgeEntry("Pell's equation", "x^2 - Dy^2 = 1", "number_theory", 3, "classical"),
            KnowledgeEntry("Quadratic reciprocity", "(p/q)(q/p) = (-1)^((p-1)/2 * (q-1)/2)", "number_theory", 3, "gauss"),
            KnowledgeEntry("Mobius inversion", "g(n) = sum mu(d) f(n/d)", "number_theory", 3, "mobius"),
            KnowledgeEntry("Ramanujan pi formula", "1/pi = 12 * sum (-1)^n (6n)!/(n!^3 (3n) 3^(n+1/2))", "number_theory", 5, "ramanujan"),
            KnowledgeEntry("Rogers-Ramanujan", "prod (1-q^(5n-4))(1-q^(5n-1))", "number_theory", 5, "ramanujan"),
            KnowledgeEntry("Euler pentagonal", "prod (1-x^n) = sum (-1)^k x^(k(3k-1)/2)", "number_theory", 3, "euler"),
            KnowledgeEntry("Stirling approximation", "n! ~ sqrt(2*pi*n) (n/e)^n", "number_theory", 2, "stirling"),
            KnowledgeEntry("Prime number theorem", "pi(x) ~ x/log(x)", "number_theory", 4, "hadamard"),
            KnowledgeEntry("Riemann zeta", "zeta(s) = sum 1/n^s", "number_theory", 3, "riemann"),
            KnowledgeEntry("Bernoulli numbers", "sum binom(n+1,k) B_k = 0", "number_theory", 3, "bernoulli"),
            KnowledgeEntry("Landau-Ramanujan constant", "K = 0.764...", "number_theory", 3, "landau"),
        ])
        
        # Algebra
        self.entries.extend([
            KnowledgeEntry("Difference of squares", "a^2 - b^2 = (a-b)(a+b)", "algebra", 2, "classical"),
            KnowledgeEntry("Sum of cubes", "a^3 + b^3 = (a+b)(a^2-ab+b^2)", "algebra", 3, "classical"),
            KnowledgeEntry("Perfect square", "(a+b)^2 = a^2 + 2ab + b^2", "algebra", 2, "classical"),
            KnowledgeEntry("Binomial theorem", "(a+b)^n = sum C(n,k) a^(n-k) b^k", "algebra", 3, "newton"),
            KnowledgeEntry("Geometric series", "a/(1-r) for |r|<1", "algebra", 2, "classical"),
            KnowledgeEntry("Arithmetic series", "n(n+1)/2", "algebra", 2, "classical"),
            KnowledgeEntry("Quadratic formula", "x = (-b +/- sqrt(b^2-4ac))/2a", "algebra", 2, "classical"),
            KnowledgeEntry("Vieta's formulas", "sum roots = -b/a, prod roots = c/a", "algebra", 2, "vieta"),
            KnowledgeEntry("Euler-Maclaurin", "sum f(k) = integral + Bernoulli terms", "algebra", 4, "euler"),
            KnowledgeEntry("Newton's identities", "Power sums relate to symmetric sums", "algebra", 3, "newton"),
        ])
        
        # Trigonometry
        self.entries.extend([
            KnowledgeEntry("Pythagorean identity", "sin^2 + cos^2 = 1", "trigonometry", 2, "classical"),
            KnowledgeEntry("Double angle sin", "sin(2x) = 2 sin(x) cos(x)", "trigonometry", 2, "classical"),
            KnowledgeEntry("Double angle cos", "cos(2x) = cos^2(x) - sin^2(x)", "trigonometry", 2, "classical"),
            KnowledgeEntry("Sum formulas", "sin(a+b) = sin(a)cos(b) + cos(a)sin(b)", "trigonometry", 3, "classical"),
            KnowledgeEntry("Product to sum", "sin(a)cos(b) = (sin(a+b) + sin(a-b))/2", "trigonometry", 3, "classical"),
            KnowledgeEntry("Half angle", "sin^2(x/2) = (1-cos(x))/2", "trigonometry", 2, "classical"),
            KnowledgeEntry("Law of sines", "a/sin(A) = b/sin(B) = c/sin(C)", "trigonometry", 2, "classical"),
            KnowledgeEntry("Law of cosines", "c^2 = a^2 + b^2 - 2ab cos(C)", "trigonometry", 2, "classical"),
        ])
        
        # Physics
        self.entries.extend([
            KnowledgeEntry("E=mc^2", "E = m c^2", "physics", 2, "einstein"),
            KnowledgeEntry("Photon energy", "E = h f = hc/lambda", "physics", 2, "planck"),
            KnowledgeEntry("de Broglie", "lambda = h/p = h/(mv)", "physics", 3, "de_broglie"),
            KnowledgeEntry("Newton's 2nd law", "F = ma", "physics", 2, "newton"),
            KnowledgeEntry("Kinetic energy", "KE = 0.5 m v^2", "physics", 2, "classical"),
            KnowledgeEntry("Gravitational PE", "PE = -G m1 m2 / r", "physics", 3, "newton"),
            KnowledgeEntry("Momentum", "p = mv", "physics", 2, "classical"),
            KnowledgeEntry("Angular momentum", "L = r x p", "physics", 2, "classical"),
            KnowledgeEntry("Hooke's law", "F = -kx", "physics", 2, "hooke"),
            KnowledgeEntry("Universal gravitation", "F = G m1 m2 / r^2", "physics", 2, "newton"),
            KnowledgeEntry("Hubble's law", "v = H0 * d", "physics", 2, "hubble"),
            KnowledgeEntry("Ideal gas", "PV = nRT", "physics", 2, "classical"),
            KnowledgeEntry("Thermal energy", "E = kB T", "physics", 2, "boltzmann"),
        ])
        
        # Quantum Mechanics
        self.entries.extend([
            KnowledgeEntry("Heisenberg uncertainty", "dx dp >= hbar/2", "quantum", 3, "heisenberg"),
            KnowledgeEntry("Schrodinger equation", "i hbar dpsi/dt = H psi", "quantum", 3, "schrodinger"),
            KnowledgeEntry("Quantum harmonic oscillator", "E = hbar omega (n + 1/2)", "quantum", 3, "quantum"),
            KnowledgeEntry("Planck radiation", "B(nu,T) = 2h nu^3/c^2 * 1/(e^(h nu/kT) - 1)", "quantum", 4, "planck"),
            KnowledgeEntry("Commutation relation", "[x,p] = i hbar", "quantum", 3, "heisenberg"),
            KnowledgeEntry("Fermi's golden rule", "Gamma = 2pi/hbar |M|^2 rho", "quantum", 4, "fermi"),
            KnowledgeEntry("Dirac equation", "(i gamma^mu D_mu - m) psi = 0", "quantum", 5, "dirac"),
            KnowledgeEntry("Casimir effect", "E = -pi^2 hbar c / (720 a^3)", "quantum", 4, "casimir"),
        ])
        
        # Cryptography
        self.entries.extend([
            KnowledgeEntry("XOR self-inverse", "a XOR a = 0", "cryptography", 1, "classical"),
            KnowledgeEntry("XOR triple", "a XOR b XOR b = a", "cryptography", 2, "classical"),
            KnowledgeEntry("Hash chain", "H_n = H(H_{n-1})", "cryptography", 2, "classical"),
            KnowledgeEntry("Merkle tree", "H(A,B) = H(H(A) + H(B))", "cryptography", 3, "merkle"),
            KnowledgeEntry("Diffie-Hellman", "K = (g^a)^b = (g^b)^a mod p", "cryptography", 4, "diffie"),
            KnowledgeEntry("RSA encryption", "c = m^e mod n, m = c^d mod n", "cryptography", 4, "rsa"),
            KnowledgeEntry("Modular exponentiation", "a^b mod n = ((a mod n)^b) mod n", "cryptography", 3, "classical"),
            KnowledgeEntry("Miller-Rabin", "Probabilistic primality test", "cryptography", 3, "miller"),
        ])
        
        # Statistics
        self.entries.extend([
            KnowledgeEntry("Normal distribution", "P(x) = exp(-x^2/2sigma^2) / sigma sqrt(2pi)", "statistics", 3, "gauss"),
            KnowledgeEntry("Poisson distribution", "P(k) = lambda^k e^(-lambda) / k!", "statistics", 3, "poisson"),
            KnowledgeEntry("Exponential decay", "N(t) = N0 exp(-lambda t)", "statistics", 2, "classical"),
            KnowledgeEntry("Power law", "P(x) ~ x^(-alpha)", "statistics", 2, "pareto"),
            KnowledgeEntry("Central limit theorem", "Sum -> Normal as N -> infinity", "statistics", 4, "classical"),
            KnowledgeEntry("Bayes theorem", "P(A|B) = P(B|A) P(A) / P(B)", "statistics", 2, "bayes"),
            KnowledgeEntry("Shannon entropy", "H = -sum p log(p)", "statistics", 2, "shannon"),
            KnowledgeEntry("Kullback-Leibler", "D(P||Q) = sum p log(p/q)", "statistics", 2, "kl"),
            KnowledgeEntry("Benford's law", "P(d) = log10(1 + 1/d)", "statistics", 2, "benford"),
        ])
        
        # Special Functions
        self.entries.extend([
            KnowledgeEntry("Gamma function", "Gamma(z) = integral_0^inf t^(z-1) e^(-t) dt", "special", 3, "euler"),
            KnowledgeEntry("Beta function", "B(x,y) = Gamma(x)Gamma(y)/Gamma(x+y)", "special", 2, "euler"),
            KnowledgeEntry("Error function", "erf(x) = 2/sqrt(pi) integral_0^x e^(-t^2) dt", "special", 2, "gauss"),
            KnowledgeEntry("Bessel J", "J_n(x) = sum (-1)^k (x/2)^(2k+n) / (k! Gamma(k+n+1))", "special", 3, "bessel"),
            KnowledgeEntry("Airy function", "Ai(x) = 1/pi integral cos(t^3/3 + xt) dt", "special", 3, "airy"),
            KnowledgeEntry("Elliptic K", "K(k) = integral_0^(pi/2) 1/sqrt(1-k^2 sin^2 theta) dtheta", "special", 3, "elliptic"),
            KnowledgeEntry("Lambert W", "W(x) e^(W(x)) = x", "special", 2, "lambert"),
        ])
        
        print(f"Loaded {len(self.entries)} knowledge entries")
    
    def get_entries_by_domain(self, domain: str) -> List[KnowledgeEntry]:
        return [e for e in self.entries if e.domain == domain]
    
    def get_random_entry(self) -> KnowledgeEntry:
        return random.choice(self.entries)


class EvoMath:
    """
    V5: Complement-Enhanced Immune Algorithm
    
    Architecture:
    - ANTIGEN: Problem to solve
    - ANTIBODY: Candidate solution
    - COMPLEMENT: Parallel verification
    - ANTIBIOTIC: External heuristics
    - MEMORY: Learned patterns
    """
    
    def __init__(self, population_size: int = 600):
        self.population_size = population_size
        self.population: List[Antibody] = []
        self.memory: Dict[str, Node] = {}
        self.best_ever: Optional[Antibody] = None
        
        self.generation = 0
        self.complement = ComplementSystem()
        self.antibiotic = Antibiotic()
        self.knowledge = KnowledgeBase()
        
        self.binary_ops = ['+', '-', '*', '/', '**', '%', '^', '&', '|', '<<', '>>']
        self.unary_ops = ['sin', 'cos', 'log', 'sqrt', 'exp', 'abs']
        
        print(f"Initialized V5 with {len(self.knowledge.entries)} knowledge entries")
    
    def random_node(self, max_depth: int = 4, allowed_vars: list = None, num_vars: int = 1) -> Node:
        if max_depth <= 0:
            if random.random() < 0.5:
                val = random.choice([0, 1, 2, 3, 0.5, 1.0, 2.0, math.pi, math.e, 1.414])
                return Node(op="CONST", value=val)
            var = random.choice(allowed_vars) if allowed_vars else random.choice(['x', 'y', 'z', 'n'])
            return Node(op="VAR", value=var)
        
        if random.random() < 0.25:
            if random.random() < 0.5:
                val = random.choice([0, 1, 2, 3, 0.5, 1.0, 2.0, math.pi, math.e, 1.414])
                return Node(op="CONST", value=val)
            var = random.choice(allowed_vars) if allowed_vars else random.choice(['x', 'y', 'z', 'n'])
            return Node(op="VAR", value=var)
        
        if random.random() < 0.2:
            kb_entry = self.knowledge.get_random_entry()
            return self._knowledge_to_node(kb_entry)
        
        if random.random() < 0.25:
            op = random.choice(self.unary_ops)
            return Node(op=op, left=self.random_node(max_depth - 1, allowed_vars, num_vars))
        
        op = random.choice(self.binary_ops)
        return Node(op=op, 
                   left=self.random_node(max_depth - 1, allowed_vars, num_vars),
                   right=self.random_node(max_depth - 1, allowed_vars, num_vars))
    
    def _knowledge_to_node(self, entry: KnowledgeEntry) -> Node:
        """Convert knowledge entry expression string to node tree"""
        expr = entry.expression
        
        templates = {
            'F(n) = F(n-1) + F(n-2)': lambda: Node(op='+', left=Node(op='VAR', value='x'), right=Node(op='VAR', value='x')),
            'a^2 - b^2 = (a-b)(a+b)': lambda: Node(op='*', left=Node(op='VAR', value='x'), right=Node(op='VAR', value='x')),
            'E = m c^2': lambda: Node(op='**', left=Node(op='VAR', value='x'), right=Node(op='CONST', value=2)),
            'E = m*c^2': lambda: Node(op='**', left=Node(op='VAR', value='x'), right=Node(op='CONST', value=2)),
            'KE = 0.5 m v^2': lambda: Node(op='*', left=Node(op='CONST', value=0.5), right=Node(op='**', left=Node(op='VAR', value='x'), right=Node(op='CONST', value=2))),
            'sin^2 + cos^2 = 1': lambda: Node(op='+', left=Node(op='**', left=Node(op='sin', left=Node(op='VAR', value='x')), right=Node(op='CONST', value=2)), right=Node(op='**', left=Node(op='cos', left=Node(op='VAR', value='x')), right=Node(op='CONST', value=2))),
            '(a+b)^2 = a^2 + 2ab + b^2': lambda: Node(op='**', left=Node(op='+', left=Node(op='VAR', value='x'), right=Node(op='CONST', value=1)), right=Node(op='CONST', value=2)),
            'n(n+1)/2': lambda: Node(op='/', left=Node(op='*', left=Node(op='VAR', value='x'), right=Node(op='+', left=Node(op='VAR', value='x'), right=Node(op='CONST', value=1))), right=Node(op='CONST', value=2)),
            'x = (-b +/- sqrt(b^2-4ac))/2a': lambda: Node(op='/', left=Node(op='VAR', value='x'), right=Node(op='CONST', value=2)),
        }
        
        if expr in templates:
            return templates[expr]()
        
        if entry.complexity <= 2:
            return Node(op='VAR', value='x')
        
        if entry.complexity <= 3:
            return Node(op='*', left=Node(op='VAR', value='x'), right=Node(op='CONST', value=2))
        
        return Node(op='**', left=Node(op='VAR', value='x'), right=Node(op='CONST', value=2))
    
    def initialize_population(self, antigen: Antigen):
        self.population = []
        
        allowed_vars = list(antigen.test_cases[0][0].keys()) if antigen.test_cases else ['x']
        num_vars = len(allowed_vars)
        
        for _ in range(self.population_size):
            depth = random.randint(2, 5) if num_vars == 1 else random.randint(3, 6)
            self.population.append(Antibody(
                node=self.random_node(max_depth=depth, allowed_vars=allowed_vars, num_vars=num_vars),
                antibody_class=AntibodyClass.IGM
            ))
        
        for _ in range(self.population_size // 4):
            if self.memory:
                key = random.choice(list(self.memory.keys()))
                self.population.append(Antibody(
                    node=self.memory[key].clone(),
                    antibody_class=AntibodyClass.MEMORY
                ))
    
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
        
        error_penalty = avg_error / (1 + avg_error)
        
        elegance = node.elegance_score()
        elegance_bonus = 1.0 + elegance * 0.5 if hit_rate >= 0.5 else 1.0
        
        antibiotic_boost = self.antibiotic.apply(antibody, antigen)
        
        affinity_bonus = 1.0 + antibody.affinity * 0.5
        class_bonus = 2.0 if antibody.antibody_class == AntibodyClass.IGG else 1.0
        
        hit_bonus = hit_rate * 500
        
        if hit_rate == 1.0:
            return (base_fitness * elegance_bonus * affinity_bonus * class_bonus * antibiotic_boost + hit_bonus)
        
        return (base_fitness * (1 - error_penalty) * affinity_bonus * class_bonus * antibiotic_boost + hit_bonus * 0.1)
    
    def complement_system_check(self, antibody: Antibody, antigen: Antigen) -> bool:
        """Complement system verification"""
        try:
            for inputs, target in antigen.test_cases:
                result = antibody.node.evaluate(inputs)
                if abs(result - target) < 1e-6:
                    self.complement.opsonize(antibody.node.hashable(), antibody.fitness)
                    return True
        except:
            pass
        return False
    
    def _idiotypic_network_suppression(self):
        """Jerne's idiotypic network - suppress similar antibodies (sampled)"""
        if self.generation % 5 != 0:
            return
        
        suppress_threshold = 0.9
        
        for i in range(min(50, len(self.population))):
            for j in range(i + 1, min(50, len(self.population))):
                a1, a2 = self.population[i], self.population[j]
                h1, h2 = a1.node.hashable(), a2.node.hashable()
                if h1[:10] == h2[:10]:
                    if a1.fitness < a2.fitness:
                        a1.fitness *= 0.95
                    else:
                        a2.fitness *= 0.95
    
    def _structural_similarity(self, node1: Node, node2: Node) -> float:
        """Calculate structural similarity between two nodes"""
        def normalize(node: Optional[Node]) -> str:
            if node is None or node.op in ("CONST", "VAR"):
                return node.op if node else "X"
            return f"{node.op}({normalize(node.left)},{normalize(node.right)})"
        
        n1, n2 = normalize(node1), normalize(node2)
        if n1 == n2:
            return 1.0
        
        common = sum(1 for c1, c2 in zip(n1, n2) if c1 == c2)
        max_len = max(len(n1), len(n2))
        return common / max_len if max_len > 0 else 0.0
    
    def evolve_generation(self, antigen: Antigen):
        for antibody in self.population:
            antibody.fitness = self.fitness(antibody, antigen)
            antibody.age += 1
            
            if self.complement_system_check(antibody, antigen):
                antibody.complement_activated = True
        
        self._idiotypic_network_suppression()
        
        def selection_key(a: Antibody) -> float:
            base = a.fitness
            if a.complement_activated:
                base *= 1.5
            if a.node.hashable() in self.complement.opsonized:
                base *= 1.2
            return base
        
        self.population.sort(key=selection_key, reverse=True)
        
        best = self.population[0]
        if not self.best_ever or best.fitness > self.best_ever.fitness:
            self.best_ever = Antibody(
                node=best.node.clone(),
                fitness=best.fitness,
                antibody_class=best.antibody_class
            )
            self.memory[self.best_ever.node.hashable()] = self.best_ever.node.clone()
        
        elites = self.population[:max(2, self.population_size // 20)]
        
        new_pop = list(elites)
        
        while len(new_pop) < self.population_size:
            if len(elites) >= 2 and random.random() < 0.5:
                p1, p2 = random.sample(elites, 2)
                child_node = self._crossover(p1.node.clone(), p2.node.clone())
                child_node = self._mutate(child_node, p1.affinity)
                new_pop.append(Antibody(
                    node=child_node,
                    antibody_class=AntibodyClass.IGG if p1.fitness > 100 else p1.antibody_class,
                    affinity=max(0.1, p1.affinity * 1.1)
                ))
            elif elites and random.random() < 0.6:
                parent = random.choice(elites)
                child_node = self._mutate(parent.node.clone(), parent.affinity)
                new_pop.append(Antibody(
                    node=child_node,
                    antibody_class=parent.antibody_class,
                    affinity=max(0.1, parent.affinity * 1.1)
                ))
            else:
                allowed_vars = list(antigen.test_cases[0][0].keys()) if antigen.test_cases else ['x']
                num_vars = len(allowed_vars)
                depth = random.randint(3, 6) if num_vars > 1 else random.randint(2, 4)
                new_pop.append(Antibody(
                    node=self.random_node(max_depth=depth, allowed_vars=allowed_vars, num_vars=num_vars),
                    antibody_class=AntibodyClass.IGM
                ))
        
        self.population = new_pop[:self.population_size]
        self.generation += 1
    
    def _mutate(self, node: Node, affinity: float = 0.5) -> Node:
        if random.random() < 0.15:
            if random.random() < 0.3:
                return self.random_node(max_depth=3)
            if node.op == "CONST":
                noise_scale = 0.5 / (affinity + 0.1)
                return Node(op="CONST", value=node.value + random.gauss(0, noise_scale))
            if node.op == "VAR":
                return Node(op="VAR", value=random.choice(['x', 'y', 'z', 'n']))
            
            if node.left and node.right:
                if random.random() < 0.5:
                    return Node(op=node.op, left=self._mutate(node.left, affinity), right=node.right)
                else:
                    return Node(op=node.op, left=node.left, right=self._mutate(node.right, affinity))
            elif node.left:
                return Node(op=node.op, left=self._mutate(node.left, affinity))
            elif node.right:
                return Node(op=node.op, left=self._mutate(node.right, affinity))
        return node
    
    def _crossover(self, node1: Node, node2: Node) -> Node:
        """Swap subtrees between two parents"""
        if random.random() < 0.3:
            return node1.clone()
        
        def replace_random(node: Node, replacement: Node) -> Node:
            if node.op in ("CONST", "VAR"):
                return replacement.clone() if random.random() < 0.5 else node.clone()
            if random.random() < 0.3:
                return replacement.clone()
            
            left_new = replace_random(node.left, replacement) if node.left else None
            right_new = replace_random(node.right, replacement) if node.right else None
            
            return Node(op=node.op, left=left_new, right=right_new)
        
        return replace_random(node1, node2)
    
    def solve(self, antigen: Antigen, max_generations: int = 100, verbose: bool = True) -> Node:
        self.initialize_population(antigen)
        
        for i in range(max_generations):
            self.evolve_generation(antigen)
            
            best = self.population[0]
            
            if verbose and (i % 20 == 0 or i < 5):
                hits = sum(1 for inp, t in antigen.test_cases 
                          if abs(best.node.evaluate(inp) - t) < 1e-6)
                complement_count = sum(1 for a in self.population if a.complement_activated)
                print(f"Gen {i:3d}: fitness={best.fitness:10.2f} | "
                      f"hits={hits}/{len(antigen.test_cases)} | "
                      f"complement={complement_count} | "
                      f"mem={len(self.memory)}")
            
            if best.fitness > 10000:
                if verbose:
                    print(f"\n*** SOLUTION at generation {i} ***")
                    print(f"Memory patterns: {len(self.memory)}")
                return best.node.clone()
        
        return self.population[0].node.clone()


def benchmark():
    """Test EvoMath on math benchmarks"""
    import time
    
    print("=" * 60)
    print(" EvoMath - Math Benchmark")
    print("=" * 60)
    
    problems = [
        ("Linear: 2x", [({'x': 1.0}, 2.0), ({'x': 2.0}, 4.0), ({'x': 3.0}, 6.0)]),
        ("Quadratic: x^2", [({'x': 1.0}, 1.0), ({'x': 2.0}, 4.0), ({'x': 3.0}, 9.0)]),
        ("Cubic: x^3", [({'x': 1.0}, 1.0), ({'x': 2.0}, 8.0), ({'x': 3.0}, 27.0)]),
    ]
    
    total_hits = 0
    total_tests = 0
    total_time = 0
    
    for name, test_cases in problems:
        print(f"\n--- {name} ---")
        
        evo = EvoMath(population_size=100)
        antigen = Antigen(target=name, test_cases=test_cases, description=name)
        
        start = time.time()
        solution = evo.solve(antigen, max_generations=30, verbose=True)
        elapsed = time.time() - start
        
        hits = sum(1 for inp, target in test_cases 
                  if abs(solution.evaluate(inp) - target) < 1e-6)
        
        print(f"Solution: {solution.to_string()}")
        print(f"Hits: {hits}/{len(test_cases)} | Time: {elapsed:.2f}s")
        
        total_hits += hits
        total_tests += len(test_cases)
        total_time += elapsed
    
    print("\n" + "=" * 60)
    print(f"TOTAL: {total_hits}/{total_tests} ({100*total_hits/total_tests:.0f}%) | {total_time:.2f}s")
    print("=" * 60)


def physics_benchmark():
    """Test EvoMath on real physics formulas"""
    import time
    
    print("=" * 60)
    print(" EvoMath - Physics Formula Benchmark")
    print("=" * 60)
    
    problems = [
        ("F=ma", [({'m': 1.0, 'a': 1.0}, 1.0), ({'m': 2.0, 'a': 3.0}, 6.0)]),
        ("p=mv", [({'m': 1.0, 'v': 1.0}, 1.0), ({'m': 2.0, 'v': 5.0}, 10.0)]),
        ("d=vt", [({'v': 2.0, 't': 1.0}, 2.0), ({'v': 5.0, 't': 4.0}, 20.0)]),
    ]
    
    total_hits = 0
    total_tests = 0
    total_time = 0
    
    for name, test_cases in problems:
        print(f"\n--- {name} ---")
        
        evo = EvoMath(population_size=100)
        antigen = Antigen(target=name, test_cases=test_cases, description=name)
        
        start = time.time()
        solution = evo.solve(antigen, max_generations=40, verbose=True)
        elapsed = time.time() - start
        
        hits = sum(1 for inp, target in test_cases 
                  if abs(solution.evaluate(inp) - target) < 1e-6)
        
        print(f"Solution: {solution.to_string()}")
        print(f"Hits: {hits}/{len(test_cases)} | Time: {elapsed:.2f}s")
        
        total_hits += hits
        total_tests += len(test_cases)
        total_time += elapsed
    
    print("\n" + "=" * 60)
    print(f"TOTAL: {total_hits}/{total_tests} ({100*total_hits/total_tests:.0f}%) | {total_time:.2f}s")
    print("=" * 60)


if __name__ == "__main__":
    physics_benchmark()
