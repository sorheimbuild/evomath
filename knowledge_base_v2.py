"""
KnowledgeBase - COMPREHENSIVE Mathematical and Physics Prior Database

Version: 2.0 - Massive Expansion
Entries: 200+

Incorporates knowledge from:
- Number theory & combinatorics
- Algebraic identities
- Trigonometric relationships  
- Special functions
- Complex analysis
- Mathematical physics
- Quantum mechanics
- Particle physics
- Cosmology
- Thermodynamics
- Statistical mechanics
- Condensed matter
- Fluid dynamics
- Signal processing
- Control theory
- Information theory
- Cryptography
- Statistical patterns

This is a RESEARCH-GRADE knowledge base.
"""

import math
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Callable
from enum import Enum

class Domain(Enum):
    NUMBER_THEORY = "number_theory"
    COMBINATORICS = "combinatorics"
    ALGEBRA = "algebra"
    TRIGONOMETRY = "trigonometry"
    CALCULUS = "calculus"
    COMPLEX_ANALYSIS = "complex_analysis"
    SPECIAL_FUNCTIONS = "special_functions"
    DIFFERENTIAL_EQUATIONS = "differential_equations"
    APPROXIMATION_THEORY = "approximation_theory"
    INTEGRAL_CALCULUS = "integral_calculus"
    ANALYSIS = "analysis"
    INTEGRAL_TRANSFORMS = "integral_transforms"
    PHYSICS = "physics"
    QUANTUM_MECHANICS = "quantum_mechanics"
    PARTICLE_PHYSICS = "particle_physics"
    COSMOLOGY = "cosmology"
    THERMODYNAMICS = "thermodynamics"
    STATISTICAL_MECHANICS = "statistical_mechanics"
    CONDENSED_MATTER = "condensed_matter"
    FLUID_DYNAMICS = "fluid_dynamics"
    ELECTROMAGNETISM = "electromagnetism"
    OPTICS = "optics"
    RELATIVITY = "relativity"
    PLASMA_PHYSICS = "plasma_physics"
    ASTROPHYSICS = "astrophysics"
    SIGNAL_PROCESSING = "signal_processing"
    CONTROL_THEORY = "control_theory"
    INFORMATION_THEORY = "information_theory"
    CRYPTOGRAPHY = "cryptography"
    STATISTICS = "statistics"
    GRAPH_THEORY = "graph_theory"
    GROUP_THEORY = "group_theory"
    ALGEBRAIC_GEOMETRY = "algebraic_geometry"

@dataclass
class KnowledgeEntry:
    """A piece of mathematical or physics knowledge."""
    name: str
    expression: str
    description: str
    domain: Domain
    complexity: int
    applications: List[str]
    weight: float = 1.0
    source: str = "general"
    
    def __repr__(self):
        return f"KnowledgeEntry({self.name})"


class ComprehensiveKnowledgeBase:
    """Massive knowledge base with 200+ entries."""
    
    def __init__(self):
        self._all_entries: Optional[List[KnowledgeEntry]] = None
    
    def get_all_entries(self) -> List[KnowledgeEntry]:
        if self._all_entries is None:
            self._all_entries = (
                self._number_theory() +
                self._combinatorics() +
                self._algebra() +
                self._trigonometry() +
                self._calculus() +
                self._complex_analysis() +
                self._special_functions() +
                self._differential_equations() +
                self._integral_calculus() +
                self._integral_transforms() +
                self._approximation_theory() +
                self._physics() +
                self._quantum_mechanics() +
                self._particle_physics() +
                self._cosmology() +
                self._thermodynamics() +
                self._statistical_mechanics() +
                self._condensed_matter() +
                self._fluid_dynamics() +
                self._electromagnetism() +
                self._optics() +
                self._relativity() +
                self._plasma_astrophysics() +
                self._signal_processing() +
                self._control_theory() +
                self._information_theory() +
                self._cryptography() +
                self._statistics()
            )
        return self._all_entries
    
    # ==================== NUMBER THEORY ====================
    
    def _number_theory(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Fibonacci sequence",
                expression="F(n) = F(n-1) + F(n-2), F(0)=0, F(1)=1",
                description="Golden ratio appears in nature, ratios converge to phi",
                domain=Domain.NUMBER_THEORY,
                complexity=2,
                applications=["sequence_prediction", "nature_patterns", "optimization"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Modular inverse",
                expression="(a * a^(-1)) mod n = 1",
                description="Modular multiplicative inverse - critical for RSA",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["cryptography", "RSA", "prime_testing"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Fermat's little theorem",
                expression="a^p mod p = a mod p",
                description="For prime p and any a not divisible by p",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["prime_testing", "cryptography"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Euler's totient",
                expression="phi(n) = n * prod(1 - 1/p) for prime p dividing n",
                description="Count of integers coprime to n",
                domain=Domain.NUMBER_THEORY,
                complexity=4,
                applications=["RSA", "number_theory"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Chinese remainder theorem",
                expression="x = a_i mod n_i has solution iff n_i coprime in pairs",
                description="System of congruences always solvable",
                domain=Domain.NUMBER_THEORY,
                complexity=4,
                applications=["cryptography", "error_correction", "distributed_computing"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Mobius inversion",
                expression="f(n) = sum_{d|n} g(d) implies g(n) = sum_{d|n} mu(d) f(n/d)",
                description="Inversion formula using Mobius function",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["cryptography", "combinatorics", "number_sieving"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Pell's equation",
                expression="x^2 - D*y^2 = 1",
                description="Indeterminate equation with infinite solutions for non-square D",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["cryptography", "approximation", "continued_fractions"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Legendre symbol",
                expression="(a/p) = a^((p-1)/2) mod p",
                description="Quadratic residue symbol, equals 1, -1, or 0",
                domain=Domain.NUMBER_THEORY,
                complexity=2,
                applications=["cryptography", "primality_testing", "quadratic_residues"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Quadratic reciprocity",
                expression="(p/q) * (q/p) = (-1)^((p-1)/2 * (q-1)/2)",
                description="Symmetry law relating Legendre symbols of p and q",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["cryptography", "computational_number_theory"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Gauss sum",
                expression="G(a,c) = sum_{x=0}^{c-1} exp(2*pi*i*a*x^2/c)",
                description="Quadratic exponential sum with deep number theory connections",
                domain=Domain.NUMBER_THEORY,
                complexity=4,
                applications=["analytic_number_theory", "algebraic_number_theory"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Euler's pentagonal number theorem",
                expression="prod_{n=1}^inf (1-x^n) = sum_{k=-inf}^{inf} (-1)^k x^(k(3k-1)/2)",
                description="Product expansion connecting partitions with pentagonal numbers",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["partition_theory", "generating_functions", "q_series"],
                source="ramanujan"
            ),
            KnowledgeEntry(
                name="Ramanujan's tau function",
                expression="Delta(z) = q * prod_{n=1}^inf (1-q^n)^24 = sum_{n=1}^inf tau(n)*q^n",
                description="Discriminant modular form with highly multiplicative coefficients",
                domain=Domain.NUMBER_THEORY,
                complexity=4,
                applications=["modular_forms", "cryptography", "integer_factorization"],
                source="ramanujan"
            ),
            KnowledgeEntry(
                name="Ramanujan's pi formulas",
                expression="1/pi = 12 * sum_{n=0}^inf (-1)^n * (6n)! / (n!^3 * (3n) * 3^(n+1/2))",
                description="Rapidly converging series for pi - one of Ramanujan's most famous results",
                domain=Domain.NUMBER_THEORY,
                complexity=4,
                applications=["high_precision_computation", "series_acceleration"],
                source="ramanujan"
            ),
            KnowledgeEntry(
                name="Rogers-Ramanujan identities",
                expression="1 + sum_{k=1}^inf q^(k(k-1)) / ((1-q)(1-q^2)...(1-q^k)) = prod_{n=1}^inf (1-q^(5n-4))(1-q^(5n-1))^-1",
                description="Identities relating partitions and hypergeometric series",
                domain=Domain.NUMBER_THEORY,
                complexity=5,
                applications=["partition_theory", "q_series", "modular_forms"],
                source="ramanujan"
            ),
            KnowledgeEntry(
                name="Ramanujan's congruences",
                expression="p(5k+4) = 0 mod 5, p(7k+5) = 0 mod 7, p(11k+6) = 0 mod 11",
                description="Beautiful congruence properties of partition function",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["pattern_recognition", "integer_sequences"],
                source="ramanujan"
            ),
            KnowledgeEntry(
                name="Hurwitz zeta function",
                expression="zeta(s,a) = sum_{n=0}^inf 1/(n+a)^s",
                description="Generalization of Riemann zeta with shift parameter",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["number_theory", "L_functions", "generalized_harmonic_series"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Lerch transcendent",
                expression="Phi(z,s,a) = sum_{n=0}^inf z^n/(n+a)^s",
                description="Generalization of polylogarithm and Hurwitz zeta",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["functional_equations", "analytic_number_theory"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Landau-Ramanujan constant",
                expression="K = 0.764223653589220662990698731250941...",
                description="Constant in asymptotic for sum of two squares",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["additive_number_theory", "representation_by_forms"],
                source="ramanujan"
            ),
            KnowledgeEntry(
                name="Bernoulli numbers recurrence",
                expression="sum_{k=0}^{m} binom(m+1,k) B_k = 0",
                description="Recursive definition of Bernoulli numbers",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["faulhaber_formula", "zeta_values", "calculus"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Pythagorean triples formula",
                expression="a = m^2 - n^2, b = 2mn, c = m^2 + n^2",
                description="Parametric formula for all primitive Pythagorean triples",
                domain=Domain.NUMBER_THEORY,
                complexity=2,
                applications=["geometry", "number_theory", "diophantine_equations"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Zeckendorf representation",
                expression="Every positive integer has unique representation as sum of non-consecutive Fibonacci numbers",
                description="Canonical representation using greedy algorithm",
                domain=Domain.NUMBER_THEORY,
                complexity=2,
                applications=["coding_theory", "data_compression"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Perfect number formula",
                expression="If 2^p - 1 is prime (Mersenne), then N = 2^(p-1) * (2^p - 1) is perfect",
                description="Euclid-Euler theorem for even perfect numbers",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["number_theory", "perfect_numbers"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Lagrange's four square theorem",
                expression="Every natural number n can be expressed as n = a^2 + b^2 + c^2 + d^2",
                description="Every integer is sum of four squares",
                domain=Domain.NUMBER_THEORY,
                complexity=4,
                applications=["additive_number_theory", "geometry_of_numbers"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Sum of two squares theorem",
                expression="n = sum of two squares iff prime factors of form (4k+3) have even exponent",
                description="Fermat's theorem characterizing representability",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["number_theory", "arithmetic_of_quadratic_forms"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Prime number theorem",
                expression="pi(x) ~ x/log(x)",
                description="Asymptotic distribution of primes",
                domain=Domain.NUMBER_THEORY,
                complexity=4,
                applications=["prime_distribution", "cryptography"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Riemann zeta functional equation",
                expression="zeta(s) = 2^s * pi^(s-1) * sin(pi*s/2) * Gamma(1-s) * zeta(1-s)",
                description="Symmetry relation extending zeta to entire complex plane",
                domain=Domain.NUMBER_THEORY,
                complexity=4,
                applications=["prime_number_theory", "quantum_physics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Stirling's approximation",
                expression="n! ~ sqrt(2*pi*n) * (n/e)^n",
                description="Asymptotic formula for factorial",
                domain=Domain.NUMBER_THEORY,
                complexity=2,
                applications=["combinatorics", "statistical_mechanics", "approximation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Euler's continued fraction for e",
                expression="e = [2;1,2,1,1,4,1,1,6,1,1,8,1,1,10,...]",
                description="Pattern in continued fraction for e",
                domain=Domain.NUMBER_THEORY,
                complexity=3,
                applications=["approximation_theory", "diophantine_approximation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Wallis product",
                expression="pi/2 = prod_{n=1}^inf (2n*2n)/((2n-1)(2n+1))",
                description="Infinite product representation of pi",
                domain=Domain.NUMBER_THEORY,
                complexity=2,
                applications=["numerical_computation", "pi_formulas"],
                source="classical"
            ),
        ]
    
    # ==================== COMBINATORICS ====================
    
    def _combinatorics(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Binomial theorem",
                expression="(a+b)^n = sum_{k=0}^n C(n,k) * a^(n-k) * b^k",
                description="General binomial expansion",
                domain=Domain.COMBINATORICS,
                complexity=2,
                applications=["polynomial_expansion", "combinatorics", "probability"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Pascal's identity",
                expression="C(n+1,k) = C(n,k) + C(n,k-1)",
                description="Recursive definition of binomial coefficients",
                domain=Domain.COMBINATORICS,
                complexity=2,
                applications=["combinatorics", "dynamic_programming"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Hockey-stick identity",
                expression="sum_{i=k}^{n} C(i,k) = C(n+1,k+1)",
                description="Sum of binomial coefficients along a diagonal",
                domain=Domain.COMBINATORICS,
                complexity=2,
                applications=["combinatorics", "counting_problems"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Catalan numbers",
                expression="C_n = (1/(n+1)) * C(2n,n)",
                description="Count of binary trees, Dyck paths, triangulations",
                domain=Domain.COMBINATORICS,
                complexity=3,
                applications=["data_structures", "combinatorial_objects"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Bell numbers",
                expression="B_{n+1} = sum_{k=0}^{n} C(n,k) * B_k",
                description="Number of ways to partition n-element set",
                domain=Domain.COMBINATORICS,
                complexity=3,
                applications=["combinatorics", "partition_theory"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Eulerian numbers",
                expression="A(n,k) = sum_{i=0}^{k} (-1)^i * C(n+1,i) * (k-i)^n",
                description="Number of permutations with exactly k descents",
                domain=Domain.COMBINATORICS,
                complexity=3,
                applications=["permutations", "sorting_algorithms"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Stirling numbers of first kind",
                expression="s(n+1,k) = s(n,k-1) - n * s(n,k)",
                description="Signed permutations, cycles in permutations",
                domain=Domain.COMBINATORICS,
                complexity=3,
                applications=["permutation_theory", "polynomial_factoring"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Stirling numbers of second kind",
                expression="S(n,k) = (1/k!) * sum_{i=0}^{k} (-1)^{k-i} * C(k,i) * i^n",
                description="Number of ways to partition n-element set into k nonempty subsets",
                domain=Domain.COMBINATORICS,
                complexity=3,
                applications=["combinatorics", "clustering", "set_partitions"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Multinomial theorem",
                expression="(x1+x2+...+xm)^n = sum_{k1+...+km=n} (n!/(k1!...km!)) * prod xi^ki",
                description="Generalization of binomial theorem",
                domain=Domain.COMBINATORICS,
                complexity=3,
                applications=["probability", "statistical_mechanics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Inclusion-exclusion principle",
                expression="|A1 U A2 U ... U An| = sum|Ai| - sum|Ai∩Aj| + sum|Ai∩Aj∩Ak| - ...",
                description="Counting elements in union of sets",
                domain=Domain.COMBINATORICS,
                complexity=3,
                applications=["counting", "probability", "derangements"],
                source="classical"
            ),
        ]
    
    # ==================== ALGEBRA ====================
    
    def _algebra(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Difference of squares",
                expression="a^2 - b^2 = (a-b)(a+b)",
                description="One of the most useful algebraic identities",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["factoring", "simplification", "crypto"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Sum/difference of cubes",
                expression="a^3 +/- b^3 = (a+/-b)(a^2 -/+ ab + b^2)",
                description="Factoring sum and difference of cubes",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["factoring", "simplification"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Perfect square trinomial",
                expression="(a+b)^2 = a^2 + 2ab + b^2",
                description="Binomial square expansion",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["completing_square", "optimization"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Geometric series",
                expression="sum_{k=0}^{n-1} a*r^k = a*(1-r^n)/(1-r)",
                description="Sum of finite geometric series",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["sequences", "interest_calculations", "physics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Infinite geometric series",
                expression="sum_{k=0}^{inf} a*r^k = a/(1-r) for |r| < 1",
                description="Sum of infinite geometric series",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["fractals", "series_evaluation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Arithmetic series",
                expression="sum_{k=1}^{n} k = n(n+1)/2",
                description="Sum of first n integers",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["summation", "triangular_numbers"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Sum of squares",
                expression="sum_{k=1}^{n} k^2 = n(n+1)(2n+1)/6",
                description="Sum of first n squares",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["statistics", "summation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Sum of cubes",
                expression="sum_{k=1}^{n} k^3 = (n(n+1)/2)^2",
                description="Sum of first n cubes - beautiful square of triangular number",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["number_theory", "summation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Log product rule",
                expression="log(a*b) = log(a) + log(b)",
                description="Logarithm of product equals sum of logs",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["logarithm_simplification", "information_theory"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Log quotient rule",
                expression="log(a/b) = log(a) - log(b)",
                description="Logarithm of quotient equals difference of logs",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["logarithm_simplification"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Log power rule",
                expression="log(a^b) = b*log(a)",
                description="Logarithm of power equals exponent times log",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["logarithm_simplification", "entropy"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Exponent product",
                expression="a^x * a^y = a^(x+y)",
                description="Same base exponents multiply add exponents",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["exponent_simplification", "growth_models"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Exponent of exponent",
                expression="(a^x)^y = a^(x*y)",
                description="Exponent of exponent multiplies",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["exponent_simplification"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Quadratic formula",
                expression="x = (-b +/- sqrt(b^2-4ac)) / 2a",
                description="Solutions to ax^2 + bx + c = 0",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["solving_quadratics", "roots"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Vieta's formulas",
                expression="For ax^2+bx+c: sum of roots = -b/a, product = c/a",
                description="Relate polynomial coefficients to roots",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["polynomial_roots", "algebra"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Discriminant",
                expression="Delta = b^2 - 4ac",
                description="Determines nature of quadratic roots",
                domain=Domain.ALGEBRA,
                complexity=2,
                applications=["root_classification", "quadratics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Euler-Maclaurin formula",
                expression="sum_{k=a}^{b} f(k) = integral + (f(a)+f(b))/2 + sum_{k=1}^{m} B_{2k}/(2k)! * (f^{(2k-1)}(b) - f^{(2k-1)}(a)) + R",
                description="Summation via integrals and Bernoulli numbers",
                domain=Domain.ALGEBRA,
                complexity=4,
                applications=["numerical_integration", "asymptotic_expansions"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Newton's identities",
                expression="e_k = (1/k) * sum_{i=1}^{k} (-1)^{i-1} * e_{k-i} * p_i",
                description="Relates power sums to elementary symmetric functions",
                domain=Domain.ALGEBRA,
                complexity=3,
                applications=["polynomial_roots", "invariant_theory"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Bernoulli polynomials",
                expression="B_n(x) = sum_{k=0}^{n} binom(n,k) * B_k * x^{n-k}",
                description="Polynomials generating Bernoulli numbers",
                domain=Domain.ALGEBRA,
                complexity=3,
                applications=["faulhaber_formulas", "zeta_values"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Faulhaber's formula",
                expression="sum_{k=1}^{n} k^p = (1/(p+1)) * sum_{k=0}^{p} binom(p+1,k) * B_k * n^{p+1-k}",
                description="Sum of p-th powers in terms of Bernoulli numbers",
                domain=Domain.ALGEBRA,
                complexity=4,
                applications=["summation_formulas"],
                source="classical"
            ),
        ]
    
    # ==================== TRIGONOMETRY ====================
    
    def _trigonometry(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Pythagorean identity",
                expression="sin^2(x) + cos^2(x) = 1",
                description="Fundamental trigonometric identity",
                domain=Domain.TRIGONOMETRY,
                complexity=2,
                applications=["trig_simplification", "geometry"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Double angle (sin)",
                expression="sin(2x) = 2*sin(x)*cos(x)",
                description="Double angle formula for sine",
                domain=Domain.TRIGONOMETRY,
                complexity=2,
                applications=["signal_processing", "wave_analysis"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Double angle (cos)",
                expression="cos(2x) = cos^2(x) - sin^2(x) = 2*cos^2(x) - 1 = 1 - 2*sin^2(x)",
                description="Multiple forms of cosine double angle",
                domain=Domain.TRIGONOMETRY,
                complexity=2,
                applications=["signal_processing", "wave_analysis"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Sum formulas",
                expression="sin(a+b) = sin(a)cos(b) + cos(a)sin(b), cos(a+b) = cos(a)cos(b) - sin(a)sin(b)",
                description="Sine and cosine of sum",
                domain=Domain.TRIGONOMETRY,
                complexity=3,
                applications=["wave_superposition", "oscillations"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Product to sum",
                expression="sin(x)cos(y) = 0.5*(sin(x+y) + sin(x-y)), cos(x)cos(y) = 0.5*(cos(x+y) + cos(x-y))",
                description="Product to sum formulas",
                domain=Domain.TRIGONOMETRY,
                complexity=3,
                applications=["signal_processing", "Fourier_analysis"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Sum to product",
                expression="sin(a) + sin(b) = 2*sin((a+b)/2)*cos((a-b)/2)",
                description="Sum to product formula",
                domain=Domain.TRIGONOMETRY,
                complexity=3,
                applications=["wave_interference", "signal_processing"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Half angle formulas",
                expression="sin^2(x/2) = (1 - cos(x))/2, cos^2(x/2) = (1 + cos(x))/2",
                description="Half angle formulas for squares",
                domain=Domain.TRIGONOMETRY,
                complexity=2,
                applications=["integration", "geometry"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Tangent half-angle (Weierstrass)",
                expression="sin(x) = 2t/(1+t^2), cos(x) = (1-t^2)/(1+t^2) where t = tan(x/2)",
                description="Universal trigonometric substitution",
                domain=Domain.TRIGONOMETRY,
                complexity=3,
                applications=["integration", "complex_analysis"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Law of sines",
                expression="a/sin(A) = b/sin(B) = c/sin(C)",
                description="Relates sides and angles in any triangle",
                domain=Domain.TRIGONOMETRY,
                complexity=2,
                applications=["triangulation", "surveying"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Law of cosines",
                expression="c^2 = a^2 + b^2 - 2ab*cos(C)",
                description="Generalization of Pythagorean theorem",
                domain=Domain.TRIGONOMETRY,
                complexity=2,
                applications=["triangles", "spherical_geometry"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Power reduction",
                expression="cos^2(x) = (1 + cos(2x))/2, sin^2(x) = (1 - cos(2x))/2",
                description="Reduce powers of trig functions",
                domain=Domain.TRIGONOMETRY,
                complexity=2,
                applications=["integration", "Fourier_analysis"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Cotangent identity",
                expression="1 + cot^2(x) = csc^2(x)",
                description="Pythagorean identity for cotangent",
                domain=Domain.TRIGONOMETRY,
                complexity=2,
                applications=["trig_identities"],
                source="classical"
            ),
        ]
    
    # ==================== CALCULUS ====================
    
    def _calculus(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Fundamental theorem of calculus",
                expression="d/dx * integral_a^x f(t)dt = f(x)",
                description="Derivative of integral equals integrand",
                domain=Domain.CALCULUS,
                complexity=3,
                applications=["integration", "antiderivatives"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Integration by parts",
                expression="integral u*dv = u*v - integral v*du",
                description="Product rule for integration",
                domain=Domain.CALCULUS,
                complexity=2,
                applications=["integration_techniques"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Chain rule",
                expression="d/dx f(g(x)) = f'(g(x)) * g'(x)",
                description="Derivative of composite functions",
                domain=Domain.CALCULUS,
                complexity=2,
                applications=["differentiation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Product rule",
                expression="d/dx (f*g) = f'*g + f*g'",
                description="Derivative of product",
                domain=Domain.CALCULUS,
                complexity=2,
                applications=["differentiation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Quotient rule",
                expression="d/dx (f/g) = (f'*g - f*g')/g^2",
                description="Derivative of quotient",
                domain=Domain.CALCULUS,
                complexity=2,
                applications=["differentiation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Taylor series",
                expression="f(x) = sum_{n=0}^inf f^{(n)}(a)/n! * (x-a)^n",
                description="Function as infinite polynomial",
                domain=Domain.CALCULUS,
                complexity=3,
                applications=["approximation", "analysis"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Maclaurin series",
                expression="f(x) = f(0) + f'(0)*x + f''(0)*x^2/2! + ...",
                description="Taylor series around x=0",
                domain=Domain.CALCULUS,
                complexity=3,
                applications=["series_expansion", "approximation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="L'Hopital's rule",
                expression="lim f(x)/g(x) = lim f'(x)/g'(x) when 0/0 or inf/inf",
                description="Limit evaluation via derivatives",
                domain=Domain.CALCULUS,
                complexity=2,
                applications=["limit_evaluation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Leibniz rule",
                expression="d^n/dx^n (f*g) = sum_{k=0}^n binom(n,k) * f^{(k)} * g^{(n-k)}",
                description="Generalized product rule",
                domain=Domain.CALCULUS,
                complexity=3,
                applications=["higher_derivatives", "combinatorics"],
                source="classical"
            ),
        ]
    
    # ==================== SPECIAL FUNCTIONS ====================
    
    def _special_functions(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Gamma function",
                expression="Gamma(z) = integral_0^inf t^{z-1} * e^{-t} dt",
                description="Factorial generalization for non-integers",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["factorial_extension", "statistics", "physics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Gamma reflection formula",
                expression="Gamma(z) * Gamma(1-z) = pi/sin(pi*z)",
                description="Relates gamma at complementary arguments",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["functional_equations", "number_theory"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Gamma multiplication theorem",
                expression="Gamma(nz) = (2*pi)^{(1-n)/2} * n^{nz-1/2} * prod_{k=1}^{n-1} Gamma(z + k/n)",
                description="Gamma function multiplication formula",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=4,
                applications=["functional_equations"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Beta function",
                expression="B(x,y) = Gamma(x)*Gamma(y)/Gamma(x+y)",
                description="Integral related to gamma",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=2,
                applications=["statistics", "integration"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Error function",
                expression="erf(x) = (2/sqrt(pi)) * integral_0^x e^{-t^2} dt",
                description="Integral of Gaussian, cumulative normal distribution",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=2,
                applications=["probability", "statistics", "diffusion"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Incomplete gamma function",
                expression="Gamma(s,x) = integral_x^inf t^{s-1} * e^{-t} dt",
                description="Upper incomplete gamma function",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["statistics", "counting_problems"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Bessel function of first kind",
                expression="J_n(x) = sum_{k=0}^inf (-1)^k * (x/2)^{2k+n} / (k!*Gamma(k+n+1))",
                description="Solutions to Bessel's differential equation",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["wave_propagation", "heat_conduction", "signal_processing"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Bessel function recurrence",
                expression="J_{nu-1}(x) - J_{nu+1}(x) = 2 * J_nu'(x)",
                description="Recurrence relations for Bessel functions",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["wave_equations", "cylindrical_coordinates"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Modified Bessel function",
                expression="I_nu(x) = i^{-nu} * J_nu(i*x)",
                description="Modified Bessel functions, exponentially growing",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["heat_equation", "electromagnetics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Airy function",
                expression="Ai(x) = (1/pi) * integral_0^inf cos(t^3/3 + x*t) dt",
                description="Solutions to Airy equation, oscillations and turning points",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["quantum_mechanics", "optics", "caustics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Elliptic integral (first kind)",
                expression="K(k) = integral_0^{pi/2} (1 - k^2*sin^2(theta))^{-1/2} d(theta)",
                description="Fundamental elliptic integral",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["pendulum_motion", "electromagnetics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Elliptic integral (second kind)",
                expression="E(k) = integral_0^{pi/2} sqrt(1 - k^2*sin^2(theta)) d(theta)",
                description="Arc length of ellipse",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["geometry", "mechanics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Theta function Jacobi",
                expression="theta_3(z,tau) = 1 + 2*sum_{n=1}^inf q^{n^2}*cos(2nz) where q = e^{pi*i*tau}",
                description="Fundamental Jacobi theta function",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=4,
                applications=["modular_forms", "quantum_field_theory"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Dilogarithm",
                expression="Li_2(z) = -integral_0^z log(1-t)/t dt",
                description="Special case of polylogarithm",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["number_theory", "quantum_field_theory"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Spence's functional equation",
                expression="Li_2(z) + Li_2(1-z) = pi^2/6 - log(z)*log(1-z)",
                description="Functional equation for dilogarithm",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["algebraic_K_theory"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Polylogarithm",
                expression="Li_s(z) = sum_{n=1}^inf z^n/n^s",
                description="Generalization of logarithm and dilogarithm",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["number_theory", "Feynman_diagrams"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Sine integral",
                expression="Si(x) = integral_0^x sin(t)/t dt",
                description="Integral of sinc function",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=2,
                applications=["signal_processing", "optics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Fresnel integrals",
                expression="C(x) = integral_0^x cos(pi*t^2/2) dt, S(x) = integral_0^x sin(pi*t^2/2) dt",
                description="Integrals related to Cornu spiral",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["optics", "diffraction"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Clausen function",
                expression="Cl_2(theta) = sum_{n=1}^inf sin(n*theta)/n^2",
                description="Trigonometric polylogarithm",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["magnetic_monopoles", "landau_levels"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Hypergeometric function",
                expression="_2F_1(a,b;c;z) = sum_{n=0}^inf (a)_n*(b)_n/(c)_n * z^n/n!",
                description="Generalized hypergeometric series",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=4,
                applications=["mathematical_physics", "differential_equations"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Gauss summation theorem",
                expression="_2F_1(a,b;c;1) = Gamma(c)*Gamma(c-a-b)/(Gamma(c-a)*Gamma(c-b))",
                description="Hypergeometric function at unit argument",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=4,
                applications=["series_evaluation", "mathematical_physics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Meijer G-function",
                expression="G_{p,q}^{m,n}(z) = very general expression",
                description="Most general special function encompassing most others",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=5,
                applications=["representation_of_special_functions"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Lambert W function",
                expression="W(x)*e^{W(x)} = x",
                description="Inverse of x*e^x function",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=2,
                applications=["exponential_equations", "delay_differential_equations"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Mittag-Leffler function",
                expression="E_alpha(x) = sum_{n=0}^inf x^n/Gamma(1 + alpha*n)",
                description="Generalization of exponential function",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["fractional_calculus", "anomalous_diffusion"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Gamma duplication formula",
                expression="Gamma(2z) = (2^{2z-1}/sqrt(pi)) * Gamma(z) * Gamma(z+1/2)",
                description="Duplication formula for gamma function",
                domain=Domain.SPECIAL_FUNCTIONS,
                complexity=3,
                applications=["computational_formulas"],
                source="classical"
            ),
        ]
    
    # ==================== COMPLEX ANALYSIS ====================
    
    def _complex_analysis(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Euler's identity",
                expression="e^{i*pi} + 1 = 0",
                description="Connects five fundamental constants",
                domain=Domain.COMPLEX_ANALYSIS,
                complexity=2,
                applications=["complex_analysis", "signal_processing"],
                source="classical"
            ),
            KnowledgeEntry(
                name="de Moivre's formula",
                expression="(cos(x) + i*sin(x))^n = cos(nx) + i*sin(nx)",
                description="Trigonometric functions in complex form",
                domain=Domain.COMPLEX_ANALYSIS,
                complexity=2,
                applications=["complex_numbers", "trigonometry"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Cauchy's integral formula",
                expression="f^{(n)}(a) = n!/(2*pi*i) * integral f(z)/(z-a)^{n+1} dz",
                description="Derivatives via contour integration",
                domain=Domain.COMPLEX_ANALYSIS,
                complexity=3,
                applications=["complex_analysis", "evaluation_of_integrals"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Residue theorem",
                expression="integral f(z) dz = 2*pi*i * sum residues",
                description="Contour integral equals 2*pi*i times sum of residues",
                domain=Domain.COMPLEX_ANALYSIS,
                complexity=3,
                applications=["integral_evaluation", "series_summation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Argument principle",
                expression="(1/(2*pi*i)) * integral f'(z)/f(z) dz = N - P",
                description="Number of zeros minus poles via contour integral",
                domain=Domain.COMPLEX_ANALYSIS,
                complexity=3,
                applications=["root_finding", "control_theory"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Rouché's theorem",
                expression="If |f-g| < |f| on contour, f and g have same zeros inside",
                description="Compare zeros of two functions",
                domain=Domain.COMPLEX_ANALYSIS,
                complexity=3,
                applications=["root_localization"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Laurent series",
                expression="f(z) = sum_{n=-inf}^{inf} a_n * (z-z0)^n",
                description="Series with negative powers for singularities",
                domain=Domain.COMPLEX_ANALYSIS,
                complexity=3,
                applications=["residue_calculus", "isolated_singularities"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Mittag-Leffler expansion",
                expression="f(z) = sum_{n=1}^{inf} z/(z^2 - a_n^2)",
                description="Partial fraction for meromorphic functions",
                domain=Domain.COMPLEX_ANALYSIS,
                complexity=3,
                applications=["residue_calculus"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Infinite product for sine",
                expression="sin(pi*x) = pi*x * prod_{n=1}^{inf} (1 - x^2/n^2)",
                description="Weierstrass factorization of sine",
                domain=Domain.COMPLEX_ANALYSIS,
                complexity=3,
                applications=["series_expansions", "product_formulas"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Weierstrass elliptic function",
                expression="P(z) = 1/z^2 + sum_{(m,n)!=(0,0)} 1/(z-omega_{mn})^2 - 1/omega_{mn}^2",
                description="Doubly periodic meromorphic function",
                domain=Domain.COMPLEX_ANALYSIS,
                complexity=5,
                applications=["elliptic_curves", "integrable_systems"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Joukowski transformation",
                expression="z = zeta + 1/zeta",
                description="Maps circles to airfoil shapes",
                domain=Domain.COMPLEX_ANALYSIS,
                complexity=3,
                applications=["aerodynamics", "conformal_mapping"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Schwarz-Christoffel mapping",
                expression="f(z) = A + integral_0^z prod (zeta - a_k)^{alpha_k} d(zeta)",
                description="Maps upper half-plane to polygons",
                domain=Domain.COMPLEX_ANALYSIS,
                complexity=4,
                applications=["electrostatics", "fluid_flow"],
                source="classical"
            ),
        ]
    
    # ==================== INTEGRAL CALCULUS ====================
    
    def _integral_calculus(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Frullani's integral",
                expression="integral_0^inf (f(ax) - f(bx))/x dx = (f(0) - f(inf)) * log(b/a)",
                description="Integral with logarithmic kernel",
                domain=Domain.INTEGRAL_CALCULUS,
                complexity=3,
                applications=["definite_integral_evaluation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Laplace transform",
                expression="L{f(t)} = integral_0^inf e^{-st} f(t) dt",
                description="Transform for solving differential equations",
                domain=Domain.INTEGRAL_CALCULUS,
                complexity=3,
                applications=["differential_equations", "control_systems"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Mellin transform",
                expression="M{f(x)} = integral_0^inf x^{s-1} * f(x) dx",
                description="Integral transform for multiplicative structures",
                domain=Domain.INTEGRAL_CALCULUS,
                complexity=3,
                applications=["number_theory", "signal_processing"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Hankel transform",
                expression="F_nu(k) = integral_0^inf f(r) * J_nu(k*r) * r dr",
                description="Transform using Bessel functions",
                domain=Domain.INTEGRAL_CALCULUS,
                complexity=4,
                applications=["image_processing", "optics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Abel's integral equation",
                expression="f(x) = integral_0^x g(t)/sqrt(x-t) dt",
                description="Integral equation with square root kernel",
                domain=Domain.INTEGRAL_CALCULUS,
                complexity=3,
                applications=["tomography", "seismology"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Mellin convolution",
                expression="(f * g)(s) = integral_0^inf f(x) * g(s/x)/x dx",
                description="Mellin convolution theorem",
                domain=Domain.INTEGRAL_CALCULUS,
                complexity=3,
                applications=["multiplicative_structres"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Poisson summation formula",
                expression="sum_{n=-inf}^{inf} f(n) = sum_{k=-inf}^{inf} F(2*pi*k)",
                description="Relates sum of function to sum of Fourier transform",
                domain=Domain.INTEGRAL_CALCULUS,
                complexity=4,
                applications=["number_theory", "signal_processing"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Watson's lemma",
                expression="integral_0^inf e^{-lambda*t} f(t) dt ~ sum_{n=0}^inf f^{(n)}(0)*Gamma(n+1)/lambda^{n+1}",
                description="Asymptotic expansion for Laplace transform",
                domain=Domain.INTEGRAL_CALCULUS,
                complexity=3,
                applications=["asymptotic_analysis"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Stationary phase",
                expression="integral_a^b e^{i*lambda*f(x)} dx ~ sum e^{i*lambda*f(x_k)} * sqrt(2*pi/|lambda*f''(x_k)|) * e^{i*pi/4*sgn(f''(x_k))}",
                description="Asymptotic evaluation of oscillatory integrals",
                domain=Domain.INTEGRAL_CALCULUS,
                complexity=4,
                applications=["wave_propagation", "optics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Method of steepest descent",
                expression="integral e^{lambda*f(z)} dz ~ sum contributions from saddle points",
                description="Asymptotic evaluation via saddle points",
                domain=Domain.INTEGRAL_CALCULUS,
                complexity=4,
                applications=["statistical_mechanics", "quantum_field_theory"],
                source="classical"
            ),
        ]
    
    # ==================== INTEGRAL TRANSFORMS ====================
    
    def _integral_transforms(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Fourier transform",
                expression="F(omega) = integral_{-inf}^{inf} f(t) * e^{-i*omega*t} dt",
                description="Decompose signal into frequencies",
                domain=Domain.INTEGRAL_TRANSFORMS,
                complexity=3,
                applications=["signal_processing", "quantum_mechanics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Inverse Fourier transform",
                expression="f(t) = (1/2*pi) * integral_{-inf}^{inf} F(omega) * e^{i*omega*t} d(omega)",
                description="Reconstruct signal from frequencies",
                domain=Domain.INTEGRAL_TRANSFORMS,
                complexity=3,
                applications=["signal_reconstruction"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Fourier convolution theorem",
                expression="F{f * g} = F{f} * F{g}",
                description="Fourier transform of convolution is product",
                domain=Domain.INTEGRAL_TRANSFORMS,
                complexity=2,
                applications=["signal_processing"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Parseval's theorem",
                expression="integral |f(t)|^2 dt = (1/2*pi) * integral |F(omega)|^2 d(omega)",
                description="Energy conservation in Fourier domain",
                domain=Domain.INTEGRAL_TRANSFORMS,
                complexity=2,
                applications=["signal_energy", "quantum_mechanics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Heisenberg uncertainty principle",
                expression="Delta(x) * Delta(p) >= hbar/2",
                description="Fundamental limit on position-momentum precision",
                domain=Domain.INTEGRAL_TRANSFORMS,
                complexity=3,
                applications=["quantum_mechanics", "signal_processing"],
                source="quantum"
            ),
            KnowledgeEntry(
                name="Short-time Fourier transform",
                expression="STFT{f}(tau, omega) = integral f(t) * w(t-tau) * e^{-i*omega*t} dt",
                description="Windowed Fourier transform for time-frequency analysis",
                domain=Domain.INTEGRAL_TRANSFORMS,
                complexity=3,
                applications=["time_frequency_analysis", "speech_processing"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Hilbert transform",
                expression="H{f}(t) = (1/pi) * P.V. integral f(tau)/(t-tau) dtau",
                description="90-degree phase shift",
                domain=Domain.INTEGRAL_TRANSFORMS,
                complexity=3,
                applications=["signal_envelope", "analytic_signal"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Hartley transform",
                expression="H(omega) = integral f(t) * (cos(omega*t) + sin(omega*t)) dt",
                description="Real-valued alternative to Fourier",
                domain=Domain.INTEGRAL_TRANSFORMS,
                complexity=2,
                applications=["signal_processing"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Radon transform",
                expression="Rf(theta,s) = integral f(s*theta + t*theta_perp) dt",
                description="Projection integrals for tomography",
                domain=Domain.INTEGRAL_TRANSFORMS,
                complexity=3,
                applications=["medical_imaging", "CT_scans"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Wavelet transform",
                expression="W_f(a,b) = (1/sqrt(a)) * integral f(t) * psi((t-b)/a) dt",
                description="Multi-scale analysis with localized basis",
                domain=Domain.INTEGRAL_TRANSFORMS,
                complexity=3,
                applications=["signal_analysis", "compression"],
                source="classical"
            ),
        ]
    
    # ==================== DIFFERENTIAL EQUATIONS ====================
    
    def _differential_equations(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Hypergeometric ODE",
                expression="x(1-x) y'' + [c - (a+b+1)x] y' - a*b*y = 0",
                description="Fuchsian ODE for hypergeometric function",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=4,
                applications=["mathematical_physics", "special_functions"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Bessel's differential equation",
                expression="x^2*y'' + x*y' + (x^2 - nu^2)*y = 0",
                description="Equation with Bessel function solutions",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=3,
                applications=["wave_propagation", "cylindrical_coordinates"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Legendre's differential equation",
                expression="(1-x^2)*y'' - 2x*y' + l(l+1)*y = 0",
                description="Orthogonal polynomials on [-1,1]",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=3,
                applications=["spherical_harmonics", "quantum_mechanics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Airy differential equation",
                expression="y'' - x*y = 0",
                description="Solutions oscillate then decay/grow",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=2,
                applications=["quantum_potential_barrier", "caustics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Hermite differential equation",
                expression="y'' - 2x*y' + 2n*y = 0",
                description="Quantum harmonic oscillator eigenfunctions",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=3,
                applications=["quantum_mechanics", "Gaussian_hermite_beams"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Laguerre differential equation",
                expression="x*y'' + (1-x)*y' + n*y = 0",
                description="Associated with Laguerre polynomials",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=3,
                applications=["quantum_hydrogen", "radial_functions"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Klein-Gordon equation",
                expression="(box + m^2)*phi = 0",
                description="Relativistic wave equation for spin-0 particles",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=4,
                applications=["quantum_field_theory", "particle_physics"],
                source="quantum"
            ),
            KnowledgeEntry(
                name="Dirac equation",
                expression="(i*gamma^mu*D_mu - m)*psi = 0",
                description="Relativistic wave equation for spin-1/2",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=5,
                applications=["quantum_mechanics", "electron_behavior"],
                source="quantum"
            ),
            KnowledgeEntry(
                name="Schrodinger equation",
                expression="i*hbar * d(psi)/dt = -hbar^2/(2m) * nabla^2*psi + V*psi",
                description="Fundamental quantum evolution equation",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=3,
                applications=["quantum_mechanics", "atomic_physics"],
                source="quantum"
            ),
            KnowledgeEntry(
                name="Heat equation",
                expression="del(u)/del(t) = alpha * nabla^2*u",
                description="Diffusion of heat over time",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=3,
                applications=["thermal_diffusion", "diffusion_processes"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Wave equation",
                expression="del^2(u)/del(t)^2 = c^2 * nabla^2*u",
                description="Wave propagation in space",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=3,
                applications=["acoustics", "electromagnetics"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Laplace equation",
                expression="nabla^2*phi = 0",
                description="Harmonic functions, no sources",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=2,
                applications=["electrostatics", "fluid_potential_flow"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Poisson equation",
                expression="nabla^2*phi = -rho/epsilon_0",
                description="Sources and sinks in potential theory",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=2,
                applications=["electrostatics", "gravity"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Burgers equation",
                expression="u_t + u*u_x = nu*u_{xx}",
                description="Shock waves and traffic flow",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=3,
                applications=["fluid_dynamics", "conservation_laws"],
                source="classical"
            ),
            KnowledgeEntry(
                name="KdV equation",
                expression="u_t + 6*u*u_x + u_{xxx} = 0",
                description="Soliton solutions",
                domain=Domain.DIFFERENTIAL_EQUATIONS,
                complexity=4,
                applications=["solitons", "water_waves"],
                source="classical"
            ),
        ]
    
    # ==================== APPROXIMATION THEORY ====================
    
    def _approximation_theory(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Weierstrass approximation theorem",
                expression="Every continuous function on [a,b] can be uniformly approximated by polynomials",
                description="Polynomial approximation is always possible",
                domain=Domain.APPROXIMATION_THEORY,
                complexity=3,
                applications=["numerical_analysis", "approximation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Bernstein polynomials",
                expression="B_n(f,x) = sum_{k=0}^n f(k/n) * C(n,k) * x^k * (1-x)^{n-k}",
                description="Constructive polynomial approximation",
                domain=Domain.APPROXIMATION_THEORY,
                complexity=3,
                applications=["probability", "approximation_algorithms"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Chebyshev polynomials",
                expression="T_n(x) = cos(n*arccos(x))",
                description="Minimax polynomial approximation",
                domain=Domain.APPROXIMATION_THEORY,
                complexity=3,
                applications=["numerical_analysis", "minimax_approximation"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Jackson's theorem",
                expression="Error <= C * omega(f, pi/n)",
                description="Approximation error bounds via modulus of continuity",
                domain=Domain.APPROXIMATION_THEORY,
                complexity=4,
                applications=["approximation_error_bounds"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Remez algorithm",
                expression="Iterative minimax polynomial approximation",
                description="Numerical algorithm for best uniform approximation",
                domain=Domain.APPROXIMATION_THEORY,
                complexity=4,
                applications=["numerical_algorithms", "filter_design"],
                source="classical"
            ),
            KnowledgeEntry(
                name="Legendre polynomials orthogonality",
                expression="integral_{-1}^{1} P_m(x)*P_n(x) dx = 0 for m != n",
                description="Orthogonal polynomials on [-1,1]",
                domain=Domain.APPROXIMATION_THEORY,
                complexity=2,
                applications=["numerical_integration", "series_expansion"],
                source="classical"
            ),
        ]
    
    # ==================== PHYSICS ====================
    
    def _physics(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Mass-energy equivalence",
                expression="E = m*c^2",
                description="Einstein's famous equation - mass and energy are equivalent",
                domain=Domain.PHYSICS,
                complexity=2,
                applications=["nuclear_physics", "energy_calculation"],
                weight=1.0,
                source="einstein"
            ),
            KnowledgeEntry(
                name="Photon energy",
                expression="E = h*f = h*c/lambda",
                description="Energy of photon from frequency or wavelength",
                domain=Domain.PHYSICS,
                complexity=2,
                applications=["quantum_physics", "spectroscopy"],
                weight=0.9,
                source="planck"
            ),
            KnowledgeEntry(
                name="de Broglie wavelength",
                expression="lambda = h/p = h/(m*v)",
                description="Wave nature of matter - wavelength from momentum",
                domain=Domain.PHYSICS,
                complexity=3,
                applications=["quantum_mechanics", "electron_diffraction"],
                weight=0.8,
                source="de_broglie"
            ),
            KnowledgeEntry(
                name="Newton's second law",
                expression="F = m*a",
                description="Force equals mass times acceleration",
                domain=Domain.PHYSICS,
                complexity=2,
                applications=["classical_mechanics", "force_calculation"],
                weight=1.0,
                source="newton"
            ),
            KnowledgeEntry(
                name="Kinetic energy",
                expression="KE = 0.5*m*v^2",
                description="Energy of motion",
                domain=Domain.PHYSICS,
                complexity=2,
                applications=["energy_calculation", "collisions"],
                weight=1.0,
                source="classical"
            ),
            KnowledgeEntry(
                name="Gravitational potential energy",
                expression="PE = -G*m1*m2/r",
                description="Potential energy from gravity",
                domain=Domain.PHYSICS,
                complexity=3,
                applications=["orbital_mechanics", "celestial_physics"],
                weight=0.9,
                source="newton"
            ),
            KnowledgeEntry(
                name="Momentum",
                expression="p = m*v",
                description="Linear momentum",
                domain=Domain.PHYSICS,
                complexity=2,
                applications=["collision_conservation", "motion"],
                weight=1.0,
                source="classical"
            ),
            KnowledgeEntry(
                name="Angular momentum",
                expression="L = r x p = m*r^2*omega",
                description="Rotational momentum",
                domain=Domain.PHYSICS,
                complexity=2,
                applications=["rotational_dynamics", "quantum_mechanics"],
                weight=0.9,
                source="classical"
            ),
            KnowledgeEntry(
                name="Hooke's law",
                expression="F = -k*x",
                description="Spring force proportional to displacement",
                domain=Domain.PHYSICS,
                complexity=2,
                applications=["oscillations", "elasticity"],
                weight=1.0,
                source="classical"
            ),
            KnowledgeEntry(
                name="Universal gravitation",
                expression="F = G*m1*m2/r^2",
                description="Newton's law of universal gravitation",
                domain=Domain.PHYSICS,
                complexity=2,
                applications=["celestial_mechanics", "orbits"],
                weight=1.0,
                source="newton"
            ),
        ]
    
    # ==================== QUANTUM MECHANICS ====================
    
    def _quantum_mechanics(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Heisenberg uncertainty principle",
                expression="Delta(x)*Delta(p) >= hbar/2",
                description="Fundamental limit on position-momentum precision",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=3,
                applications=["quantum_limits", "measurement"],
                weight=0.9,
                source="heisenberg"
            ),
            KnowledgeEntry(
                name="Schrodinger equation",
                expression="i*hbar*del(psi)/del(t) = -hbar^2/(2m)*nabla^2*psi + V*psi",
                description="Fundamental quantum evolution equation",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=3,
                applications=["quantum_mechanics", "atomic_physics"],
                weight=1.0,
                source="schrodinger"
            ),
            KnowledgeEntry(
                name="Time-independent Schrodinger equation",
                expression="-hbar^2/(2m)*nabla^2*psi + V*psi = E*psi",
                description="Stationary states in quantum mechanics",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=3,
                applications=["energy_eigenstates", "bound_systems"],
                weight=1.0,
                source="schrodinger"
            ),
            KnowledgeEntry(
                name="Quantum harmonic oscillator",
                expression="E_n = hbar*omega*(n + 1/2)",
                description="Energy levels of harmonic oscillator",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=3,
                applications=["vibrational_modes", "field_theory"],
                weight=0.9,
                source="quantum"
            ),
            KnowledgeEntry(
                name="Hydrogen atom energy levels",
                expression="E_n = -me^4/(2*(4*pi*epsilon_0)^2*hbar^2) * 1/n^2",
                description="Bohr model energy levels",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=4,
                applications=["atomic_physics", "spectroscopy"],
                weight=0.8,
                source="bohr"
            ),
            KnowledgeEntry(
                name="Planck radiation law",
                expression="B(nu,T) = (2*h*nu^3/c^2) * 1/(e^{h*nu/(k_B*T)} - 1)",
                description="Blackbody radiation spectral density",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=4,
                applications=["thermal_radiation", "cosmic_background"],
                weight=0.8,
                source="planck"
            ),
            KnowledgeEntry(
                name="Commutation relation",
                expression="[x,p_x] = x*p_x - p_x*x = i*hbar",
                description="Canonical commutation relation",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=3,
                applications=["quantum_mechanics", "phase_space"],
                weight=0.9,
                source="heisenberg"
            ),
            KnowledgeEntry(
                name="WKB approximation",
                expression="psi ~ C/p^{1/2} * exp(+/- i/hbar integral p dx)",
                description="Semiclassical approximation in quantum mechanics",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=4,
                applications=["tunneling", "adiabatic_approximation"],
                weight=0.7,
                source="quantum"
            ),
            KnowledgeEntry(
                name="Fermi's golden rule",
                expression="Gamma_{i->f} = (2*pi/hbar) * |M_{fi}|^2 * rho(E_f)",
                description="Transition rate in perturbation theory",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=4,
                applications=["decay_rates", "absorption"],
                weight=0.8,
                source="fermi"
            ),
            KnowledgeEntry(
                name="Aharonov-Bohm effect",
                expression="Phase shift = (q/hbar) * integral A*dl",
                description="Quantum effect from vector potential",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=4,
                applications=["magnetic_effects", "topological_phases"],
                weight=0.7,
                source="quantum"
            ),
            KnowledgeEntry(
                name="Landau-Zener formula",
                expression="P = exp(-2*pi*Delta^2/(hbar*v*|d(H_12)/dt|))",
                description="Transition probability at level crossing",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=4,
                applications=["adiabatic_passing", "molecular_passing"],
                weight=0.7,
                source="quantum"
            ),
            KnowledgeEntry(
                name="Wigner-Eckart theorem",
                expression="<alpha,J,M| T^{(k)}_q | alpha,J',M'> = <J',M'|k,q;J,M> * <alpha,J||T^{(k)}||alpha,J'>",
                description="Selection rules for matrix elements",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=5,
                applications=["angular_momentum", "selection_rules"],
                weight=0.6,
                source="quantum"
            ),
            KnowledgeEntry(
                name="Casimir effect",
                expression="E = -pi^2*hbar*c/(720*a^3) * A",
                description="Quantum vacuum energy between plates",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=4,
                applications=["quantum_vacuum", "nanotechnology"],
                weight=0.7,
                source="casimir"
            ),
            KnowledgeEntry(
                name="Lamb shift",
                expression="Delta E = (alpha^5*m*c^2)/(4*pi^3) * (something complex)",
                description="Energy level splitting from QED",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=5,
                applications=["quantum_electrodynamics", "precision_spectroscopy"],
                weight=0.6,
                source="qed"
            ),
            KnowledgeEntry(
                name="Bethe logarithm",
                expression="ln(k_0) = average of log(energy denominator)",
                description="Contributes to Lamb shift calculation",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=5,
                applications=["atomic_physics", "QED"],
                weight=0.5,
                source="bethe"
            ),
            KnowledgeEntry(
                name="Feynman path integral",
                expression="K(x_f,t_f;x_i,t_i) = integral D[x] exp(i*S[x]/hbar)",
                description="Sum over all possible paths",
                domain=Domain.QUANTUM_MECHANICS,
                complexity=5,
                applications=["quantum_field_theory", "statistical_mechanics"],
                weight=0.8,
                source="feynman"
            ),
        ]
    
    # ==================== PARTICLE PHYSICS ====================
    
    def _particle_physics(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Standard Model Lagrangian",
                expression="L = L_gauge + L_Higgs + L_Yukawa + L_lepton + L_quark",
                description="Fundamental particle physics Lagrangian",
                domain=Domain.PARTICLE_PHYSICS,
                complexity=5,
                applications=["particle_physics", "fundamental_forces"],
                weight=0.7,
                source="standard_model"
            ),
            KnowledgeEntry(
                name="Dirac equation",
                expression="(i*gamma^mu*D_mu - m)*psi = 0",
                description="Relativistic wave equation for spin-1/2 particles",
                domain=Domain.PARTICLE_PHYSICS,
                complexity=5,
                applications=["electron_physics", "quarks"],
                weight=0.8,
                source="dirac"
            ),
            KnowledgeEntry(
                name="Klein-Gordon equation",
                expression="(partial^2 + m^2)*phi = 0",
                description="Relativistic wave equation for spin-0 particles",
                domain=Domain.PARTICLE_PHYSICS,
                complexity=4,
                applications=["scalar_fields", "Higgs"],
                weight=0.7,
                source="classical"
            ),
            KnowledgeEntry(
                name="Proca equation",
                expression="partial_mu*F^{mu nu} + m^2*A^nu = 0",
                description="Massive vector field equation",
                domain=Domain.PARTICLE_PHYSICS,
                complexity=4,
                applications=["massive_bosons", "weak_interaction"],
                weight=0.6,
                source="particle"
            ),
            KnowledgeEntry(
                name="Yang-Mills theory",
                expression="L = -1/4*F^a_mu_nu*F^{a,mu_nu}",
                description="Non-abelian gauge theory",
                domain=Domain.PARTICLE_PHYSICS,
                complexity=5,
                applications=["QCD", "electroweak"],
                weight=0.7,
                source="yang_mills"
            ),
            KnowledgeEntry(
                name="QCD beta function",
                expression="beta(g) = -(b_0*g^3)/(16*pi^2) - ...",
                description="Running of strong coupling constant",
                domain=Domain.PARTICLE_PHYSICS,
                complexity=4,
                applications=["asymptotic_freedom", "confinement"],
                weight=0.6,
                source="qcd"
            ),
            KnowledgeEntry(
                name="Gell-Mann Low formula",
                expression="<0|T(q_1...q_n)|0> = sum_i (something complex)",
                description="Time-ordered product in perturbation theory",
                domain=Domain.PARTICLE_PHYSICS,
                complexity=4,
                applications=["QED", "perturbation_theory"],
                weight=0.6,
                source="quantum"
            ),
            KnowledgeEntry(
                name="Electroweak unification",
                expression="SU(2)_L x U(1)_Y -> U(1)_EM",
                description="Symmetry breaking in electroweak theory",
                domain=Domain.PARTICLE_PHYSICS,
                complexity=5,
                applications=["W_Z_bosons", "Higgs_mechanism"],
                weight=0.7,
                source="glashow"
            ),
        ]
    
    # ==================== COSMOLOGY ====================
    
    def _cosmology(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Friedmann equation",
                expression="H^2 = (8*pi*G/3)*rho - k*c^2/a^2 + Lambda*c^2/3",
                description="First Friedmann equation for expanding universe",
                domain=Domain.COSMOLOGY,
                complexity=4,
                applications=["cosmology", "expansion_of_universe"],
                weight=0.9,
                source="friedmann"
            ),
            KnowledgeEntry(
                name="Second Friedmann equation",
                expression="ddot(a)/a = -4*pi*G/3*(rho + 3p/c^2) + Lambda/3",
                description="Acceleration of cosmic expansion",
                domain=Domain.COSMOLOGY,
                complexity=4,
                applications=["dark_energy", "cosmic_acceleration"],
                weight=0.8,
                source="friedmann"
            ),
            KnowledgeEntry(
                name="Continuity equation",
                expression="dot(rho) + 3*(dot(a)/a)*(rho + p/c^2) = 0",
                description="Energy conservation in expanding universe",
                domain=Domain.COSMOLOGY,
                complexity=3,
                applications=["cosmological_fluid_dynamics"],
                weight=0.8,
                source="cosmology"
            ),
            KnowledgeEntry(
                name="Hubble's law",
                expression="v = H_0 * d",
                description="Velocity-distance relation for receding galaxies",
                domain=Domain.COSMOLOGY,
                complexity=2,
                applications=["expansion_rate", "galaxy_redshifts"],
                weight=1.0,
                source="hubble"
            ),
            KnowledgeEntry(
                name="Cosmological constant equation of state",
                expression="w = p/(rho*c^2) = -1",
                description="Dark energy has negative pressure",
                domain=Domain.COSMOLOGY,
                complexity=2,
                applications=["dark_energy", "accelerated_expansion"],
                weight=0.8,
                source="cosmology"
            ),
            KnowledgeEntry(
                name="Stefan's law (cosmological)",
                expression="rho_radiation ~ a*T^4",
                description="Radiation energy density scales with T^4",
                domain=Domain.COSMOLOGY,
                complexity=2,
                applications=["early_universe", "CMB"],
                weight=0.8,
                source="classical"
            ),
            KnowledgeEntry(
                name="Particle horizon",
                expression="d_H = c*integral_0^t dt'/a(t')",
                description="Maximum distance light could have traveled",
                domain=Domain.COSMOLOGY,
                complexity=4,
                applications=["observable_universe", "causality"],
                weight=0.7,
                source="cosmology"
            ),
        ]
    
    # ==================== THERMODYNAMICS ====================
    
    def _thermodynamics(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Ideal gas law",
                expression="PV = nRT",
                description="Equation of state for ideal gas",
                domain=Domain.THERMODYNAMICS,
                complexity=2,
                applications=["gas_laws", "thermodynamics"],
                weight=1.0,
                source="classical"
            ),
            KnowledgeEntry(
                name="First law of thermodynamics",
                expression="dU = dQ - dW",
                description="Energy conservation in thermodynamic systems",
                domain=Domain.THERMODYNAMICS,
                complexity=2,
                applications=["energy_conservation", "heat_engines"],
                weight=1.0,
                source="classical"
            ),
            KnowledgeEntry(
                name="Second law of thermodynamics",
                expression="dS >= dQ/T",
                description="Entropy never decreases",
                domain=Domain.THERMODYNAMICS,
                complexity=2,
                applications=["entropy", "arrow_of_time"],
                weight=1.0,
                source="classical"
            ),
            KnowledgeEntry(
                name="Carnot efficiency",
                expression="eta = 1 - T_c/T_h",
                description="Maximum efficiency of heat engine",
                domain=Domain.THERMODYNAMICS,
                complexity=2,
                applications=["heat_engines", "refrigerators"],
                weight=0.9,
                source="carnot"
            ),
            KnowledgeEntry(
                name="Clausius-Clapeyron relation",
                expression="dP/dT = L/(T*delta_V)",
                description="Phase boundary slope",
                domain=Domain.THERMODYNAMICS,
                complexity=3,
                applications=["phase_transitions", "clausius_clapeyron"],
                weight=0.8,
                source="classical"
            ),
            KnowledgeEntry(
                name="Gibbs free energy",
                expression="G = H - T*S",
                description="Spontaneity criterion at constant T,P",
                domain=Domain.THERMODYNAMICS,
                complexity=2,
                applications=["chemical_reactions", "phase_equilibrium"],
                weight=0.9,
                source="gibbs"
            ),
            KnowledgeEntry(
                name="Helmholtz free energy",
                expression="F = U - T*S",
                description="Spontaneity criterion at constant T,V",
                domain=Domain.THERMODYNAMICS,
                complexity=2,
                applications=["thermodynamic_potentials"],
                weight=0.8,
                source="classical"
            ),
            KnowledgeEntry(
                name="Chemical potential",
                expression="mu = (dG/dN)_{T,P}",
                description="Gibbs free energy per particle",
                domain=Domain.THERMODYNAMICS,
                complexity=3,
                applications=["phase_equilibrium", "mixtures"],
                weight=0.8,
                source="classical"
            ),
            KnowledgeEntry(
                name="Nernst heat theorem",
                expression="lim_{T->0} (dG/dT) = 0",
                description="Third law of thermodynamics",
                domain=Domain.THERMODYNAMICS,
                complexity=3,
                applications=["absolute_entropy", "low_temperature"],
                weight=0.7,
                source="nernst"
            ),
            KnowledgeEntry(
                name="Maxwell relations",
                expression="-(dS/dV)_T = (dP/dT)_V",
                description="Four Maxwell relations from exact differentials",
                domain=Domain.THERMODYNAMICS,
                complexity=3,
                applications=["thermodynamic_identities"],
                weight=0.8,
                source="classical"
            ),
        ]
    
    # ==================== STATISTICAL MECHANICS ====================
    
    def _statistical_mechanics(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Boltzmann distribution",
                expression="P(E) ~ exp(-E/(k_B*T))",
                description="Probability of energy state at temperature",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=3,
                applications=["statistical_mechanics", "thermodynamics"],
                weight=1.0,
                source="boltzmann"
            ),
            KnowledgeEntry(
                name="Partition function",
                expression="Z = sum_i exp(-E_i/(k_B*T))",
                description="Sum over all states weighted by Boltzmann factor",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=3,
                applications=["thermodynamic_properties", "statistical_mechanics"],
                weight=0.9,
                source="classical"
            ),
            KnowledgeEntry(
                name="Free energy from partition function",
                expression="F = -k_B*T*ln(Z)",
                description="Helmholtz free energy from partition function",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=3,
                applications=["free_energy_calculations"],
                weight=0.9,
                source="classical"
            ),
            KnowledgeEntry(
                name="Entropy (Boltzmann)",
                expression="S = k_B*ln(W)",
                description="Boltzmann's entropy formula",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=2,
                applications=["entropy", "statistical_mechanics"],
                weight=1.0,
                source="boltzmann"
            ),
            KnowledgeEntry(
                name="Entropy (Gibbs-Shannon)",
                expression="S = -k_B*sum_i P_i*ln(P_i)",
                description="Information-theoretic entropy",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=2,
                applications=["information_theory", "statistical_mechanics"],
                weight=0.9,
                source="shannon"
            ),
            KnowledgeEntry(
                name="Fermi-Dirac distribution",
                expression="f(E) = 1/(exp((E-E_F)/(k_B*T)) + 1)",
                description="Fermion occupation numbers",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=3,
                applications=["electrons_in_metals", "semiconductors"],
                weight=0.9,
                source="fermi"
            ),
            KnowledgeEntry(
                name="Bose-Einstein distribution",
                expression="n(E) = 1/(exp((E-mu)/(k_B*T)) - 1)",
                description="Boson occupation numbers",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=3,
                applications=["lasers", "BEC", "phonons"],
                weight=0.9,
                source="bose"
            ),
            KnowledgeEntry(
                name="Maxwell-Boltzmann distribution",
                expression="f(v) = 4*pi*(m/(2*pi*k_B*T))^{3/2}*v^2*exp(-m*v^2/(2*k_B*T))",
                description="Velocity distribution of gas molecules",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=3,
                applications=["kinetic_theory", "gas_dynamics"],
                weight=0.9,
                source="maxwell"
            ),
            KnowledgeEntry(
                name="Dulong-Petit law",
                expression="C_V = 3R per mole",
                description="Classical specific heat of solids",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=2,
                applications=["solid_state_physics", "specific_heat"],
                weight=0.7,
                source="classical"
            ),
            KnowledgeEntry(
                name="Debye model specific heat",
                expression="C_V ~ T^3 for T << T_D",
                description="Low temperature specific heat of solids",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=4,
                applications=["lattice_vibrations", "phonons"],
                weight=0.7,
                source="debye"
            ),
            KnowledgeEntry(
                name="Ising model Hamiltonian",
                expression="H = -J*sum_{<i,j>} S_i*S_j - h*sum_i S_i",
                description="Spin system with nearest neighbor interactions",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=4,
                applications=["magnetism", "phase_transitions"],
                weight=0.9,
                source="ising"
            ),
            KnowledgeEntry(
                name="Mean field approximation",
                expression="m = tanh(beta*(J*z*m + h))",
                description="Self-consistent equation for magnetization",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=3,
                applications=["magnetic_systems", "mean_field_theory"],
                weight=0.8,
                source="classical"
            ),
            KnowledgeEntry(
                name="Central limit theorem (statistical mechanics)",
                expression="Distribution of sum -> Gaussian as N -> infinity",
                description="Foundation of statistical mechanics",
                domain=Domain.STATISTICAL_MECHANICS,
                complexity=3,
                applications=["fluctuations", "statistical_foundation"],
                weight=0.9,
                source="classical"
            ),
        ]
    
    # ==================== CONDENSED MATTER ====================
    
    def _condensed_matter(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Drude model conductivity",
                expression="sigma = n*e^2*tau/m",
                description="DC conductivity in Drude model",
                domain=Domain.CONDENSED_MATTER,
                complexity=3,
                applications=["electrical_conductivity", "metals"],
                weight=0.8,
                source="drude"
            ),
            KnowledgeEntry(
                name="Hall effect",
                expression="R_H = -1/(n*e)",
                description="Transverse voltage in magnetic field",
                domain=Domain.CONDENSED_MATTER,
                complexity=3,
                applications=["carrier_density_measurement", "semiconductors"],
                weight=0.8,
                source="hall"
            ),
            KnowledgeEntry(
                name="Bloch theorem",
                expression="psi_k(r) = u_k(r)*exp(i*k*r)",
                description="Wavefunction in periodic potential",
                domain=Domain.CONDENSED_MATTER,
                complexity=4,
                applications=["band_theory", "solid_state"],
                weight=0.9,
                source="bloch"
            ),
            KnowledgeEntry(
                name="Kronig-Penney model",
                expression="cos(k*a) = P*sin(alpha*a)/(alpha*a) + cos(alpha*a)",
                description="Periodic potential model",
                domain=Domain.CONDENSED_MATTER,
                complexity=4,
                applications=["band_gaps", "crystal_momentum"],
                weight=0.7,
                source="quantum"
            ),
            KnowledgeEntry(
                name="Effective mass",
                expression="m* = hbar^2 / (d^2E/dk^2)",
                description="Electron mass in band structure",
                domain=Domain.CONDENSED_MATTER,
                complexity=3,
                applications=["semiconductor_physics"],
                weight=0.8,
                source="solid_state"
            ),
            KnowledgeEntry(
                name="BCS theory gap equation",
                expression="Delta = 2*hbar*omega_D*exp(-1/(N(0)*V))",
                description="Energy gap in superconducting state",
                domain=Domain.CONDENSED_MATTER,
                complexity=5,
                applications=["superconductivity", "BCS_theory"],
                weight=0.7,
                source="bcs"
            ),
            KnowledgeEntry(
                name="Josephson equations",
                expression="I = I_c*sin(phi), d(phi)/dt = 2*e*V/hbar",
                description="Superconducting tunnel junction",
                domain=Domain.CONDENSED_MATTER,
                complexity=3,
                applications=["SQUIDs", "superconducting_electronics"],
                weight=0.7,
                source="josephson"
            ),
            KnowledgeEntry(
                name="Anderson localization",
                expression="psi ~ exp(-r/xi)",
                description="Spatial decay of wavefunction in disordered systems",
                domain=Domain.CONDENSED_MATTER,
                complexity=4,
                applications=["disordered_systems", "insulator_transition"],
                weight=0.6,
                source="anderson"
            ),
            KnowledgeEntry(
                name="Landau Fermi liquid",
                expression="Quasiparticle lifetime ~ (E - E_F)^{-2}",
                description="Interactions renormalized as weakly interacting quasiparticles",
                domain=Domain.CONDENSED_MATTER,
                complexity=4,
                applications=["metals", "Fermi_liquids"],
                weight=0.7,
                source="landau"
            ),
            KnowledgeEntry(
                name="Quantum Hall conductivity",
                expression="sigma = n*e^2/h",
                description="Quantized Hall conductance",
                domain=Domain.CONDENSED_MATTER,
                complexity=4,
                applications=["quantum_Hall_effect", "topological_insulators"],
                weight=0.7,
                source="hall"
            ),
        ]
    
    # ==================== FLUID DYNAMICS ====================
    
    def _fluid_dynamics(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Navier-Stokes equation",
                expression="rho*(dv/dt + v*nabla*v) = -nabla*p + mu*nabla^2*v + rho*g",
                description="Fundamental fluid dynamics equation",
                domain=Domain.FLUID_DYNAMICS,
                complexity=4,
                applications=["fluid_mechanics", "weather", "aerodynamics"],
                weight=0.9,
                source="navier"
            ),
            KnowledgeEntry(
                name="Bernoulli's equation",
                expression="p + 0.5*rho*v^2 + rho*g*h = constant",
                description="Pressure-velocity relation along streamline",
                domain=Domain.FLUID_DYNAMICS,
                complexity=2,
                applications=["fluid_flow", "lift"],
                weight=1.0,
                source="bernoulli"
            ),
            KnowledgeEntry(
                name="Continuity equation (fluids)",
                expression="nabla*(rho*v) + d(rho)/dt = 0",
                description="Mass conservation in fluid flow",
                domain=Domain.FLUID_DYNAMICS,
                complexity=3,
                applications=["incompressible_flow", "mass_conservation"],
                weight=0.9,
                source="classical"
            ),
            KnowledgeEntry(
                name="Reynolds number",
                expression="Re = rho*v*L/mu = v*L/nu",
                description="Ratio of inertial to viscous forces",
                domain=Domain.FLUID_DYNAMICS,
                complexity=2,
                applications=["laminar_turbulent_transition", "scaling"],
                weight=1.0,
                source="reynolds"
            ),
            KnowledgeEntry(
                name="Poiseuille flow",
                expression="Q = (pi*r^4*dp)/(8*mu*L)",
                description="Laminar flow through pipe (Hagen-Poiseuille)",
                domain=Domain.FLUID_DYNAMICS,
                complexity=3,
                applications=["pipe_flow", "blood_flow"],
                weight=0.8,
                source="poiseuille"
            ),
            KnowledgeEntry(
                name="Euler equation (fluids)",
                expression="d(v)/dt + (v*nabla)*v = -nabla(p/rho) + g",
                description="Inviscid fluid dynamics",
                domain=Domain.FLUID_DYNAMICS,
                complexity=3,
                applications=["ideal_fluids", "conservative_flows"],
                weight=0.8,
                source="euler"
            ),
            KnowledgeEntry(
                name="Vorticity equation",
                expression="d(omega)/dt = (omega*nabla)*v + nu*nabla^2*omega",
                description="Evolution of vorticity in flow",
                domain=Domain.FLUID_DYNAMICS,
                complexity=4,
                applications=["vortex_dynamics", "turbulence"],
                weight=0.7,
                source="classical"
            ),
            KnowledgeEntry(
                name="Kelvin circulation theorem",
                expression="d(Gamma)/dt = 0 for barotropic, inviscid flow",
                description="Circulation conservation around closed curve",
                domain=Domain.FLUID_DYNAMICS,
                complexity=4,
                applications=["vortex_conservation", "fluid_conservation_laws"],
                weight=0.7,
                source="kelvin"
            ),
        ]
    
    # ==================== ELECTROMAGNETISM ====================
    
    def _electromagnetism(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Coulomb's law",
                expression="F = k*q1*q2/r^2",
                description="Electric force between charges",
                domain=Domain.ELECTROMAGNETISM,
                complexity=2,
                applications=["electric_fields", "static_charges"],
                weight=1.0,
                source="coulomb"
            ),
            KnowledgeEntry(
                name="Ohm's law",
                expression="V = I*R",
                description="Voltage, current, resistance relationship",
                domain=Domain.ELECTROMAGNETISM,
                complexity=2,
                applications=["circuits", "electronics"],
                weight=1.0,
                source="ohm"
            ),
            KnowledgeEntry(
                name="Maxwell's equations (differential)",
                expression="nabla*E = rho/epsilon_0, nabla*B = 0, nabla*E = -dB/dt, nabla*B = mu_0*J + mu_0*epsilon_0*dE/dt",
                description="Fundamental equations of electromagnetism",
                domain=Domain.ELECTROMAGNETISM,
                complexity=4,
                applications=["classical_electrodynamics", "light"],
                weight=1.0,
                source="maxwell"
            ),
            KnowledgeEntry(
                name="Lorentz force",
                expression="F = q*(E + v*B)",
                description="Force on charge in electromagnetic field",
                domain=Domain.ELECTROMAGNETISM,
                complexity=3,
                applications=["particle_accelerators", "mass_spectrometers"],
                weight=0.9,
                source="lorentz"
            ),
            KnowledgeEntry(
                name="Electric potential",
                expression="V = k*q/r",
                description="Potential from point charge",
                domain=Domain.ELECTROMAGNETISM,
                complexity=2,
                applications=["potential_theory", "capacitors"],
                weight=0.9,
                source="classical"
            ),
            KnowledgeEntry(
                name="Capacitance",
                expression="C = Q/V = epsilon_0*A/d",
                description="Charge stored per unit voltage",
                domain=Domain.ELECTROMAGNETISM,
                complexity=2,
                applications=["capacitors", "energy_storage"],
                weight=0.8,
                source="classical"
            ),
            KnowledgeEntry(
                name="Magnetic flux",
                expression="Phi = integral B*dA",
                description="Magnetic flux through surface",
                domain=Domain.ELECTROMAGNETISM,
                complexity=2,
                applications=["induction", "transformers"],
                weight=0.8,
                source="classical"
            ),
            KnowledgeEntry(
                name="Faraday's law",
                expression="emf = -d(Phi)/dt",
                description="Induced EMF from changing magnetic flux",
                domain=Domain.ELECTROMAGNETISM,
                complexity=3,
                applications=["generators", "transformers"],
                weight=0.9,
                source="faraday"
            ),
            KnowledgeEntry(
                name="Poynting vector",
                expression="S = (1/mu_0)*E*B",
                description="Energy flux in electromagnetic field",
                domain=Domain.ELECTROMAGNETISM,
                complexity=3,
                applications=["energy_transport", "radiation"],
                weight=0.8,
                source="poynting"
            ),
            KnowledgeEntry(
                name="EM wave impedance (vacuum)",
                expression="Z_0 = sqrt(mu_0/epsilon_0) = 377 ohms",
                description="Characteristic impedance of free space",
                domain=Domain.ELECTROMAGNETISM,
                complexity=2,
                applications=["transmission_lines", "optics"],
                weight=0.8,
                source="classical"
            ),
            KnowledgeEntry(
                name="Fine structure constant",
                expression="alpha = e^2/(4*pi*epsilon_0*hbar*c) ~ 1/137",
                description="Fundamental coupling constant for EM interaction",
                domain=Domain.ELECTROMAGNETISM,
                complexity=3,
                applications=["QED", "atomic_physics"],
                weight=0.8,
                source="sommerfeld"
            ),
        ]
    
    # ==================== OPTICS ====================
    
    def _optics(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Snell's law",
                expression="n1*sin(theta_1) = n2*sin(theta_2)",
                description="Refraction at interface",
                domain=Domain.OPTICS,
                complexity=2,
                applications=["refraction", "lenses"],
                weight=1.0,
                source="snell"
            ),
            KnowledgeEntry(
                name="Beer-Lambert law",
                expression="I = I_0*exp(-mu*x)",
                description="Absorption of light in medium",
                domain=Domain.OPTICS,
                complexity=2,
                applications=["spectroscopy", "absorption"],
                weight=0.9,
                source="classical"
            ),
            KnowledgeEntry(
                name="Diffraction grating equation",
                expression="d*sin(theta) = m*lambda",
                description="Maxima in diffraction pattern",
                domain=Domain.OPTICS,
                complexity=2,
                applications=["spectroscopy", "diffraction"],
                weight=0.9,
                source="classical"
            ),
            KnowledgeEntry(
                name="Rayleigh criterion",
                expression="theta_min = 1.22*lambda/D",
                description="Angular resolution limit",
                domain=Domain.OPTICS,
                complexity=2,
                applications=["telescopes", "resolution"],
                weight=0.8,
                source="rayleigh"
            ),
            KnowledgeEntry(
                name="Fresnel diffraction",
                expression="U(P) = (i*k/(2*pi))*integral U(xi)*exp(ik*r)/(r)*cos(theta) d(xi)",
                description="Near-field diffraction integral",
                domain=Domain.OPTICS,
                complexity=4,
                applications=["diffraction", "wave_optics"],
                weight=0.7,
                source="fresnel"
            ),
            KnowledgeEntry(
                name="Fabry-Perot interference",
                expression="I/I_0 = 1/(1 + F*sin^2(delta/2))",
                description="Multiple beam interference",
                domain=Domain.OPTICS,
                complexity=3,
                applications=["interferometers", "laser_cavities"],
                weight=0.8,
                source="optics"
            ),
            KnowledgeEntry(
                name="Brewster's angle",
                expression="tan(theta_B) = n2/n1",
                description="Angle for zero reflection of p-polarized light",
                domain=Domain.OPTICS,
                complexity=2,
                applications=["polarization", "anti-reflection"],
                weight=0.7,
                source="brewster"
            ),
            KnowledgeEntry(
                name="Compton scattering formula",
                expression="lambda' - lambda = h/(m_e*c)*(1 - cos(theta))",
                description="X-ray scattering from electrons",
                domain=Domain.OPTICS,
                complexity=3,
                applications=["X-ray_physics", "quantum_optics"],
                weight=0.8,
                source="compton"
            ),
            KnowledgeEntry(
                name="Rutherford scattering",
                expression="d(sigma)/d(Omega) = (Z_1*Z_2*e^2/(16*pi*epsilon_0*E))^2 * 1/sin^4(theta/2)",
                description="Alpha particle scattering cross section",
                domain=Domain.OPTICS,
                complexity=4,
                applications=["nuclear_physics", "scattering"],
                weight=0.6,
                source="rutherford"
            ),
        ]
    
    # ==================== RELATIVITY ====================
    
    def _relativity(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Lorentz factor",
                expression="gamma = 1/sqrt(1 - v^2/c^2)",
                description="Time dilation and length contraction factor",
                domain=Domain.RELATIVITY,
                complexity=3,
                applications=["special_relativity", "particle_physics"],
                weight=0.9,
                source="lorentz"
            ),
            KnowledgeEntry(
                name="Relativistic energy",
                expression="E = gamma*m*c^2",
                description="Total energy including relativistic effects",
                domain=Domain.RELATIVITY,
                complexity=3,
                applications=["particle_physics", "cosmic_rays"],
                weight=0.9,
                source="einstein"
            ),
            KnowledgeEntry(
                name="Mass-energy equivalence",
                expression="E^2 = (p*c)^2 + (m*c^2)^2",
                description="Relativistic energy-momentum relation",
                domain=Domain.RELATIVITY,
                complexity=3,
                applications=["particle_physics", "kinematics"],
                weight=0.9,
                source="einstein"
            ),
            KnowledgeEntry(
                name="Einstein field equations",
                expression="R_mu_nu - 0.5*g_mu_nu*R = (8*pi*G/c^4)*T_mu_nu",
                description="Fundamental equation of general relativity",
                domain=Domain.RELATIVITY,
                complexity=5,
                applications=["gravity", "cosmology", "black_holes"],
                weight=0.8,
                source="einstein"
            ),
            KnowledgeEntry(
                name="Schwarzschild radius",
                expression="r_s = 2*G*M/c^2",
                description="Radius of black hole event horizon",
                domain=Domain.RELATIVITY,
                complexity=3,
                applications=["black_holes", "gravitational_collapse"],
                weight=0.8,
                source="schwarzschild"
            ),
            KnowledgeEntry(
                name="Gravitational lensing",
                expression="alpha = 4*G*M/(c^2*b)",
                description="Light deflection by massive object",
                domain=Domain.RELATIVITY,
                complexity=3,
                applications=["astrophysics", "dark_matter"],
                weight=0.8,
                source="einstein"
            ),
            KnowledgeEntry(
                name="Time dilation",
                expression="Delta(t') = gamma*Delta(t)",
                description="Moving clocks run slower",
                domain=Domain.RELATIVITY,
                complexity=2,
                applications=["GPS", "particle_decay"],
                weight=0.9,
                source="einstein"
            ),
            KnowledgeEntry(
                name="Relativistic Doppler",
                expression="f' = f * sqrt((1+beta)/(1-beta))",
                description="Doppler shift for light",
                domain=Domain.RELATIVITY,
                complexity=2,
                applications=["redshift", "astronomy"],
                weight=0.8,
                source="relativity"
            ),
        ]
    
    # ==================== PLASMA & ASTROPHYSICS ====================
    
    def _plasma_astrophysics(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Debye length",
                expression="lambda_D = sqrt(epsilon_0*k_B*T/(n*e^2))",
                description="Screening length in plasma",
                domain=Domain.PLASMA_PHYSICS,
                complexity=3,
                applications=["plasma_physics", "screening"],
                weight=0.7,
                source="plasma"
            ),
            KnowledgeEntry(
                name="Plasma frequency",
                expression="omega_p = sqrt(n*e^2/(epsilon_0*m))",
                description="Natural frequency of plasma oscillations",
                domain=Domain.PLASMA_PHYSICS,
                complexity=3,
                applications=["plasma_diagnostics", "electronics"],
                weight=0.7,
                source="plasma"
            ),
            KnowledgeEntry(
                name="Chandrasekhar limit",
                expression="M_limit ~ 1.4*M_sun",
                description="Maximum mass of white dwarf",
                domain=Domain.ASTROPHYSICS,
                complexity=3,
                applications=["stellar_evolution", "supernovae"],
                weight=0.8,
                source="chandrasekhar"
            ),
            KnowledgeEntry(
                name="MHD equations",
                expression="d(rho*v)/dt = J*B - nabla*p + rho*g",
                description="Magnetohydrodynamics momentum equation",
                domain=Domain.PLASMA_PHYSICS,
                complexity=5,
                applications=["space_weather", "stellar_physics"],
                weight=0.6,
                source="mhd"
            ),
            KnowledgeEntry(
                name="Alfvén wave",
                expression="v_A = B/sqrt(mu_0*rho)",
                description="Waves in magnetized plasma",
                domain=Domain.PLASMA_PHYSICS,
                complexity=3,
                applications=["space_physics", "fusion"],
                weight=0.6,
                source="alfven"
            ),
            KnowledgeEntry(
                name="Eddington luminosity",
                expression="L_E = 4*pi*G*M*m_p*c/sigma_T",
                description="Maximum stable luminosity",
                domain=Domain.ASTROPHYSICS,
                complexity=4,
                applications=["accretion", "quasars"],
                weight=0.7,
                source="eddington"
            ),
            KnowledgeEntry(
                name="Jeans instability criterion",
                expression="lambda_J = c_s*sqrt(pi/(G*rho))",
                description="Minimum cloud size for gravitational collapse",
                domain=Domain.ASTROPHYSICS,
                complexity=3,
                applications=["star_formation", "nebulae"],
                weight=0.7,
                source="jeans"
            ),
            KnowledgeEntry(
                name="Salpeter IMF",
                expression="dN/dM ~ M^{-2.35}",
                description="Initial mass function for star formation",
                domain=Domain.ASTROPHYSICS,
                complexity=2,
                applications=["stellar_populations", "galaxies"],
                weight=0.6,
                source="salpeter"
            ),
            KnowledgeEntry(
                name="Tully-Fisher relation",
                expression="L ~ v^4",
                description="Luminosity-velocity relation for spirals",
                domain=Domain.ASTROPHYSICS,
                complexity=2,
                applications=["galaxy_rotation", "distance_scale"],
                weight=0.6,
                source="tully"
            ),
        ]
    
    # ==================== SIGNAL PROCESSING ====================
    
    def _signal_processing(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Fourier series",
                expression="f(t) = a_0 + sum_{n=1}^inf [a_n*cos(n*omega*t) + b_n*sin(n*omega*t)]",
                description="Periodic function as sum of sinusoids",
                domain=Domain.SIGNAL_PROCESSING,
                complexity=3,
                applications=["signal_analysis", "frequency_decomposition"],
                weight=1.0,
                source="fourier"
            ),
            KnowledgeEntry(
                name="Nyquist-Shannon sampling theorem",
                expression="f_s > 2*B for bandlimited signal",
                description="Minimum sampling rate for reconstruction",
                domain=Domain.SIGNAL_PROCESSING,
                complexity=2,
                applications=["digital_signal_processing", "communication"],
                weight=1.0,
                source="shannon"
            ),
            KnowledgeEntry(
                name="Convolution",
                expression="(f * g)(t) = integral f(tau)*g(t-tau) dtau",
                description="Signal smoothing and filtering",
                domain=Domain.SIGNAL_PROCESSING,
                complexity=2,
                applications=["filters", "system_response"],
                weight=0.9,
                source="classical"
            ),
            KnowledgeEntry(
                name="Z-transform",
                expression="X(z) = sum_{n=0}^inf x[n]*z^{-n}",
                description="Discrete-time signal analysis",
                domain=Domain.SIGNAL_PROCESSING,
                complexity=3,
                applications=["digital_filters", "control_systems"],
                weight=0.8,
                source="classical"
            ),
            KnowledgeEntry(
                name="Laplace transform (signal)",
                expression="X(s) = integral_0^inf x(t)*e^{-s*t} dt",
                description="Signal analysis in s-domain",
                domain=Domain.SIGNAL_PROCESSING,
                complexity=3,
                applications=["control_systems", "stability_analysis"],
                weight=0.9,
                source="classical"
            ),
            KnowledgeEntry(
                name="Transfer function",
                expression="H(s) = Y(s)/X(s)",
                description="System output over input in Laplace domain",
                domain=Domain.SIGNAL_PROCESSING,
                complexity=3,
                applications=["system_analysis", "filters"],
                weight=0.9,
                source="control"
            ),
            KnowledgeEntry(
                name="Aliasing condition",
                expression="omega_a = omega_s - omega",
                description="Alias frequency when undersampling",
                domain=Domain.SIGNAL_PROCESSING,
                complexity=2,
                applications=["undersampling", "frequency_overlap"],
                weight=0.8,
                source="signal"
            ),
            KnowledgeEntry(
                name="Parseval's theorem (signal)",
                expression="integral |x(t)|^2 dt = integral |X(f)|^2 df",
                description="Energy conservation in time and frequency domains",
                domain=Domain.SIGNAL_PROCESSING,
                complexity=2,
                applications=["signal_energy", "power_spectral_density"],
                weight=0.9,
                source="classical"
            ),
        ]
    
    # ==================== CONTROL THEORY ====================
    
    def _control_theory(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="PID controller",
                expression="u(t) = K_p*e(t) + K_i*integral e(t)dt + K_d*de/dt",
                description="Proportional-integral-derivative control",
                domain=Domain.CONTROL_THEORY,
                complexity=3,
                applications=["control_systems", "automation"],
                weight=1.0,
                source="control"
            ),
            KnowledgeEntry(
                name="Routh-Hurwitz criterion",
                expression="Conditions on Routh array for stability",
                description="Determine stability without finding roots",
                domain=Domain.CONTROL_THEORY,
                complexity=4,
                applications=["stability_analysis", "control_design"],
                weight=0.8,
                source="hurwitz"
            ),
            KnowledgeEntry(
                name="Nyquist stability criterion",
                expression="Z = P + N where N = encirclements of -1",
                description="Stability from Nyquist plot",
                domain=Domain.CONTROL_THEORY,
                complexity=4,
                applications=["feedback_stability", "control_design"],
                weight=0.8,
                source="nyquist"
            ),
            KnowledgeEntry(
                name="Bode plot magnitude",
                expression="|H(jw)|_dB = 20*log|H(jw)|",
                description="Frequency response magnitude in dB",
                domain=Domain.CONTROL_THEORY,
                complexity=2,
                applications=["frequency_analysis", "filter_design"],
                weight=0.8,
                source="bode"
            ),
            KnowledgeEntry(
                name="Phase margin",
                expression="PM = 180 + angle(H(jw_c))",
                description="Measure of relative stability",
                domain=Domain.CONTROL_THEORY,
                complexity=3,
                applications=["stability_margins", "control_design"],
                weight=0.8,
                source="control"
            ),
            KnowledgeEntry(
                name="Gain margin",
                expression="GM = -|H(jw_p)|_dB",
                description="Gain at phase crossover frequency",
                domain=Domain.CONTROL_THEORY,
                complexity=3,
                applications=["stability_margins", "control_design"],
                weight=0.8,
                source="control"
            ),
        ]
    
    # ==================== INFORMATION THEORY ====================
    
    def _information_theory(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Shannon entropy",
                expression="H(X) = -sum_i p_i*log_2(p_i)",
                description="Measure of information content",
                domain=Domain.INFORMATION_THEORY,
                complexity=2,
                applications=["information_theory", "compression"],
                weight=1.0,
                source="shannon"
            ),
            KnowledgeEntry(
                name="Channel capacity",
                expression="C = max_{p(x)} I(X;Y)",
                description="Maximum information rate through channel",
                domain=Domain.INFORMATION_THEORY,
                complexity=3,
                applications=["communication", "coding"],
                weight=1.0,
                source="shannon"
            ),
            KnowledgeEntry(
                name="Mutual information",
                expression="I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)",
                description="Information shared between X and Y",
                domain=Domain.INFORMATION_THEORY,
                complexity=2,
                applications=["correlation", "communication"],
                weight=0.9,
                source="shannon"
            ),
            KnowledgeEntry(
                name="Kullback-Leibler divergence",
                expression="D(P||Q) = sum p*log(p/q)",
                description="Relative entropy between distributions",
                domain=Domain.INFORMATION_THEORY,
                complexity=2,
                applications=["machine_learning", "statistics"],
                weight=0.9,
                source="kl"
            ),
            KnowledgeEntry(
                name="Hamming bound",
                expression="A_q(n,d) <= q^n / sum_{i=0}^{t} C(n,i)*(q-1)^i",
                description="Bound on code size for error correction",
                domain=Domain.INFORMATION_THEORY,
                complexity=3,
                applications=["coding_theory", "error_correction"],
                weight=0.7,
                source="hamming"
            ),
            KnowledgeEntry(
                name="Singleton bound",
                expression="d <= n - k + 1",
                description="Relationship between distance, length, dimension",
                domain=Domain.INFORMATION_THEORY,
                complexity=2,
                applications=["coding_theory", "MDS_codes"],
                weight=0.7,
                source="singleton"
            ),
            KnowledgeEntry(
                name="Gilbert-Varshamov bound",
                expression="A_q(n,d) >= q^n / sum_{i=0}^{d-1} C(n,i)*(q-1)^i",
                description="Lower bound on code size",
                domain=Domain.INFORMATION_THEORY,
                complexity=3,
                applications=["coding_theory", "lower_bounds"],
                weight=0.6,
                source="varshamov"
            ),
            KnowledgeEntry(
                name="Fano inequality",
                expression="H(P_X|Q_X) <= H(P_e) + P_e*log(|X|-1)",
                description="Uncertainty bound in terms of error probability",
                domain=Domain.INFORMATION_THEORY,
                complexity=3,
                applications=["information_theory", "converse_theorems"],
                weight=0.7,
                source="fano"
            ),
        ]
    
    # ==================== CRYPTOGRAPHY ====================
    
    def _cryptography(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="XOR property",
                expression="a XOR b XOR b = a",
                description="XOR with same value twice returns original",
                domain=Domain.CRYPTOGRAPHY,
                complexity=2,
                applications=["encryption", "error_detection"],
                weight=1.0,
                source="crypto"
            ),
            KnowledgeEntry(
                name="XOR cancellation",
                expression="a XOR a = 0",
                description="XOR of value with itself is zero",
                domain=Domain.CRYPTOGRAPHY,
                complexity=1,
                applications=["encryption", "hashing"],
                weight=1.0,
                source="crypto"
            ),
            KnowledgeEntry(
                name="Modular exponentiation",
                expression="a^b mod n = ((a mod n)^b) mod n",
                description="Optimization for large exponentiation",
                domain=Domain.CRYPTOGRAPHY,
                complexity=3,
                applications=["RSA", "Diffie-Hellman"],
                weight=1.0,
                source="classical"
            ),
            KnowledgeEntry(
                name="Hash chain",
                expression="H_n = H(H_{n-1})",
                description="Hash of previous hash - blockchain foundation",
                domain=Domain.CRYPTOGRAPHY,
                complexity=2,
                applications=["blockchain", "proof_of_work"],
                weight=1.0,
                source="crypto"
            ),
            KnowledgeEntry(
                name="Merkle tree",
                expression="hash(A,B) = H(H(A) + H(B))",
                description="Binary tree of hashes for efficient verification",
                domain=Domain.CRYPTOGRAPHY,
                complexity=3,
                applications=["blockchain", "data_verification"],
                weight=0.9,
                source="merkle"
            ),
            KnowledgeEntry(
                name="Double hash (Bitcoin)",
                expression="H_SHA256 = SHA256(SHA256(data))",
                description="Bitcoin's double SHA256 for security",
                domain=Domain.CRYPTOGRAPHY,
                complexity=2,
                applications=["bitcoin", "security"],
                weight=1.0,
                source="bitcoin"
            ),
            KnowledgeEntry(
                name="Diffie-Hellman key exchange",
                expression="K = (g^a)^b mod p = (g^b)^a mod p",
                description="Shared secret without transmitting private key",
                domain=Domain.CRYPTOGRAPHY,
                complexity=4,
                applications=["key_exchange", "TLS"],
                weight=0.8,
                source="diffie"
            ),
            KnowledgeEntry(
                name="RSA encryption",
                expression="c = m^e mod n, m = c^d mod n",
                description="Public key encryption using modular exponentiation",
                domain=Domain.CRYPTOGRAPHY,
                complexity=4,
                applications=["encryption", "digital_signatures"],
                weight=0.9,
                source="rsa"
            ),
            KnowledgeEntry(
                name="Elliptic curve group law",
                expression="P + Q = R, where R is reflection of intersection",
                description="Addition of points on elliptic curve",
                domain=Domain.CRYPTOGRAPHY,
                complexity=4,
                applications=["ECC", "modern_crypto"],
                weight=0.7,
                source="ecc"
            ),
            KnowledgeEntry(
                name="Miller-Rabin primality test",
                expression="Based on Fermat's little theorem with random bases",
                description="Probabilistic primality testing",
                domain=Domain.CRYPTOGRAPHY,
                complexity=3,
                applications=["prime_generation", "cryptography"],
                weight=0.8,
                source="miller"
            ),
            KnowledgeEntry(
                name="Lagrange's theorem (groups)",
                expression="|G| = |H| * [G:H] for subgroup H",
                description="Order of subgroup divides order of group",
                domain=Domain.CRYPTOGRAPHY,
                complexity=3,
                applications=["group_theory", "cryptography"],
                weight=0.7,
                source="group_theory"
            ),
            KnowledgeEntry(
                name="Chinese remainder theorem (crypto)",
                expression="Solve x = a_i mod n_i for coprime moduli",
                description="Efficient RSA decryption using CRT optimization",
                domain=Domain.CRYPTOGRAPHY,
                complexity=3,
                applications=["RSA_optimization", "efficient_computation"],
                weight=0.8,
                source="classical"
            ),
        ]
    
    # ==================== STATISTICS ====================
    
    def _statistics(self) -> List[KnowledgeEntry]:
        return [
            KnowledgeEntry(
                name="Normal distribution",
                expression="P(x) = (1/(sigma*sqrt(2*pi))) * exp(-(x-mu)^2/(2*sigma^2))",
                description="Gaussian distribution - ubiquitous in nature",
                domain=Domain.STATISTICS,
                complexity=3,
                applications=["statistics", "error_analysis", "nature"],
                weight=1.0,
                source="gauss"
            ),
            KnowledgeEntry(
                name="Poisson distribution",
                expression="P(k) = (lambda^k * e^{-lambda})/k!",
                description="Probability of rare events",
                domain=Domain.STATISTICS,
                complexity=3,
                applications=["queueing_theory", "radioactive_decay"],
                weight=0.9,
                source="poisson"
            ),
            KnowledgeEntry(
                name="Exponential decay",
                expression="N(t) = N_0 * exp(-lambda*t)",
                description="Radioactive decay, damped oscillations",
                domain=Domain.STATISTICS,
                complexity=2,
                applications=["decay_systems", "damping", "reliability"],
                weight=1.0,
                source="classical"
            ),
            KnowledgeEntry(
                name="Power law distribution",
                expression="P(x) = C * x^{-alpha}",
                description="Scale-free distributions - Zipf's law, Pareto",
                domain=Domain.STATISTICS,
                complexity=2,
                applications=["complex_systems", "wealth_distribution", "networks"],
                weight=0.9,
                source="pareto"
            ),
            KnowledgeEntry(
                name="Central limit theorem",
                expression="Sum of many variables -> Normal distribution",
                description="Independent random variables tend toward Gaussian",
                domain=Domain.STATISTICS,
                complexity=4,
                applications=["statistics_foundation", "data_analysis"],
                weight=1.0,
                source="classical"
            ),
            KnowledgeEntry(
                name="Bayes' theorem",
                expression="P(A|B) = P(B|A) * P(A) / P(B)",
                description="Inverse probability relationship",
                domain=Domain.STATISTICS,
                complexity=2,
                applications=["inference", "machine_learning"],
                weight=1.0,
                source="bayes"
            ),
            KnowledgeEntry(
                name="Maximum likelihood estimation",
                expression="theta_MLE = argmax sum log p(x_i|theta)",
                description="Parameter estimation by maximizing likelihood",
                domain=Domain.STATISTICS,
                complexity=3,
                applications=["parameter_estimation", "machine_learning"],
                weight=0.9,
                source="statistics"
            ),
            KnowledgeEntry(
                name="Chi-squared test",
                expression="chi^2 = sum (O_i - E_i)^2 / E_i",
                description="Goodness of fit test",
                domain=Domain.STATISTICS,
                complexity=2,
                applications=["hypothesis_testing", "goodness_of_fit"],
                weight=0.8,
                source="pearson"
            ),
            KnowledgeEntry(
                name="Cramér-Rao bound",
                expression="Var(theta_hat) >= 1/(n*I(theta))",
                description="Lower bound on parameter estimator variance",
                domain=Domain.STATISTICS,
                complexity=4,
                applications=["efficiency", "lower_bounds"],
                weight=0.7,
                source="cramer"
            ),
            KnowledgeEntry(
                name="Welch's t-test",
                expression="t = (x1 - x2) / sqrt(s1^2/n1 + s2^2/n2)",
                description="Compare means of two populations",
                domain=Domain.STATISTICS,
                complexity=2,
                applications=["hypothesis_testing", "A/B_testing"],
                weight=0.8,
                source="statistics"
            ),
            KnowledgeEntry(
                name="Kolmogorov-Smirnov statistic",
                expression="D_n = sup|F_n(x) - F(x)|",
                description="Maximum distance between empirical and theoretical CDF",
                domain=Domain.STATISTICS,
                complexity=3,
                applications=["goodness_of_fit", "two_sample_test"],
                weight=0.7,
                source="kolmogorov"
            ),
            KnowledgeEntry(
                name="Benford's law",
                expression="P(d) = log_10(1 + 1/d)",
                description="Distribution of first digits in many datasets",
                domain=Domain.STATISTICS,
                complexity=2,
                applications=["fraud_detection", "natural_datasets"],
                weight=0.7,
                source="benford"
            ),
            KnowledgeEntry(
                name="Zipf's law",
                expression="Rank ~ Frequency^{-1}",
                description="Frequency of words inversely proportional to rank",
                domain=Domain.STATISTICS,
                complexity=2,
                applications=["linguistics", "power_laws"],
                weight=0.8,
                source="zipf"
            ),
            KnowledgeEntry(
                name="Law of large numbers",
                expression="sample_mean -> true_mean as n -> infinity",
                description="Average converges to expectation",
                domain=Domain.STATISTICS,
                complexity=3,
                applications=["statistics_foundation", "convergence"],
                weight=0.9,
                source="classical"
            ),
            KnowledgeEntry(
                name="Skellam distribution",
                expression="P(k) = e^{-(mu1+mu2)} * (mu1/mu2)^{k/2} * I_k(2*sqrt(mu1*mu2))",
                description="Distribution of difference of two independent Poissons",
                domain=Domain.STATISTICS,
                complexity=4,
                applications=["Poisson_differences", "finance"],
                weight=0.5,
                source="skellam"
            ),
            KnowledgeEntry(
                name="Welch-Satterthwaite equation",
                expression="df = (s1^2/n1 + s2^2/n2)^2 / (s1^4/(n1^2*(n1-1)) + s2^4/(n2^2*(n2-1)))",
                description="Degrees of freedom for unequal variance t-test",
                domain=Domain.STATISTICS,
                complexity=4,
                applications=["t_test", "unequal_variances"],
                weight=0.6,
                source="statistics"
            ),
        ]
    
    # ==================== GETTERS ====================
    
    def get_all_entries(self) -> List[KnowledgeEntry]:
        """Get all knowledge entries from all domains."""
        if self._all_entries is None:
            self._all_entries = (
                self._number_theory() +
                self._combinatorics() +
                self._algebra() +
                self._trigonometry() +
                self._calculus() +
                self._complex_analysis() +
                self._special_functions() +
                self._differential_equations() +
                self._integral_calculus() +
                self._integral_transforms() +
                self._approximation_theory() +
                self._physics() +
                self._quantum_mechanics() +
                self._particle_physics() +
                self._cosmology() +
                self._thermodynamics() +
                self._statistical_mechanics() +
                self._condensed_matter() +
                self._fluid_dynamics() +
                self._electromagnetism() +
                self._optics() +
                self._relativity() +
                self._plasma_astrophysics() +
                self._signal_processing() +
                self._control_theory() +
                self._information_theory() +
                self._cryptography() +
                self._statistics()
            )
        return self._all_entries
    
    def get_entries_by_domain(self, domain: Domain) -> List[KnowledgeEntry]:
        """Get entries for a specific domain."""
        return [e for e in self.get_all_entries() if e.domain == domain]
    
    def get_entries_by_application(self, application: str) -> List[KnowledgeEntry]:
        """Get entries relevant to a specific application."""
        return [e for e in self.get_all_entries() 
                if application in e.applications]
    
    def get_weighted_entries(self, applications: List[str] = None) -> List[KnowledgeEntry]:
        """Get entries weighted by relevance to applications."""
        entries = self.get_all_entries()
        if applications:
            for app in applications:
                for entry in entries:
                    if app in entry.applications:
                        entry.weight *= 1.5
        return entries
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics about the knowledge base."""
        entries = self.get_all_entries()
        by_domain = {}
        for entry in entries:
            domain_name = entry.domain.value
            if domain_name not in by_domain:
                by_domain[domain_name] = 0
            by_domain[domain_name] += 1
        
        by_source = {}
        for entry in entries:
            if entry.source not in by_source:
                by_source[entry.source] = 0
            by_source[entry.source] += 1
        
        return {
            "total_entries": len(entries),
            "by_domain": by_domain,
            "by_source": by_source,
            "total_weight": sum(e.weight for e in entries)
        }
    
    def search(self, query: str) -> List[KnowledgeEntry]:
        """Search entries by name or description."""
        query = query.lower()
        return [e for e in self.get_all_entries() 
                if query in e.name.lower() or query in e.description.lower()]
    
    def __repr__(self):
        stats = self.get_statistics()
        return f"ComprehensiveKnowledgeBase({stats['total_entries']} entries)"


# Alias for backward compatibility
KnowledgeBase = ComprehensiveKnowledgeBase


# Quick test
if __name__ == "__main__":
    kb = ComprehensiveKnowledgeBase()
    print("=" * 70)
    print(" COMPREHENSIVE KNOWLEDGE BASE - Research Grade")
    print("=" * 70)
    print(f"\nTotal entries: {kb.get_statistics()['total_entries']}")
    print(f"Total weight: {kb.get_statistics()['total_weight']:.2f}")
    
    print("\n--- By Domain ---")
    by_domain = kb.get_statistics()['by_domain']
    for domain, count in sorted(by_domain.items(), key=lambda x: -x[1]):
        print(f"  {domain:30s}: {count:3d}")
    
    print("\n--- By Source ---")
    by_source = kb.get_statistics()['by_source']
    for source, count in sorted(by_source.items(), key=lambda x: -x[1]):
        print(f"  {source:15s}: {count:3d}")
    
    print("\n--- Sample Entries ---")
    samples = [
        "Ramanujan's pi formulas",
        "Einstein field equations",
        "Standard Model Lagrangian",
        "Shannon entropy",
        "XOR property",
    ]
    for name in samples:
        results = kb.search(name)
        if results:
            print(f"  {results[0].name}: {results[0].expression[:60]}...")
    
    print("\n" + "=" * 70)
