"""
KnowledgeBase - Mathematical and Physics priors for EvoMath.

Incorporates knowledge from:
- Number theory
- Algebraic identities
- Trigonometric relationships
- Physics constants and equations
- Statistical patterns
- Special functions
"""

import math
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Callable
from enum import Enum

class Domain(Enum):
    NUMBER_THEORY = "number_theory"
    ALGEBRA = "algebra"
    TRIGONOMETRY = "trigonometry"
    CALCULUS = "calculus"
    PHYSICS = "physics"
    STATISTICS = "statistics"
    SPECIAL_FUNCTIONS = "special_functions"
    CRYPTOGRAPHY = "cryptography"

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
    
    def __repr__(self):
        return f"KnowledgeEntry({self.name}: {self.expression})"


class MathematicalPriors:
    """Known mathematical patterns and identities."""
    
    @staticmethod
    def get_all() -> List[KnowledgeEntry]:
        entries = []
        
        # === NUMBER THEORY ===
        
        entries.append(KnowledgeEntry(
            name="Fibonacci identity",
            expression="F(n) = F(n-1) + F(n-2)",
            description="Fibonacci sequence - appears in nature, golden ratio connections",
            domain=Domain.NUMBER_THEORY,
            complexity=2,
            applications=["sequence_prediction", "nature_patterns", "crypto"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Modular inverse",
            expression="(a * a^(-1)) mod n = 1",
            description="Modular multiplicative inverse - critical for RSA, cryptography",
            domain=Domain.NUMBER_THEORY,
            complexity=3,
            applications=["cryptography", "RSA", "prime_testing"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Fermat's little theorem",
            expression="a^p mod p = a mod p",
            description="For prime p and any a not divisible by p",
            domain=Domain.NUMBER_THEORY,
            complexity=3,
            applications=["prime_testing", "cryptography"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Euler's totient",
            expression="phi(n) = n * prod(1 - 1/p)",
            description="Count of integers coprime to n",
            domain=Domain.NUMBER_THEORY,
            complexity=4,
            applications=["RSA", "number_theory"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Chinese remainder theorem",
            expression="x = a_i mod n_i has solution if n_i coprime",
            description="System of congruences always has solution",
            domain=Domain.NUMBER_THEORY,
            complexity=4,
            applications=["cryptography", "error_correction"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Quadratic reciprocity",
            expression="(p/q) * (q/p) = (-1)^((p-1)/2 * (q-1)/2)",
            description="Relationship between two primes modulo each other",
            domain=Domain.NUMBER_THEORY,
            complexity=5,
            applications=["prime_theory", "crypto"]
        ))
        
        # === ALGEBRAIC IDENTITIES ===
        
        entries.append(KnowledgeEntry(
            name="Difference of squares",
            expression="a^2 - b^2 = (a-b)(a+b)",
            description="One of the most useful algebraic identities",
            domain=Domain.ALGEBRA,
            complexity=2,
            applications=["factoring", "simplification", "crypto"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Sum of cubes",
            expression="a^3 + b^3 = (a+b)(a^2 - ab + b^2)",
            description="Factoring sum of cubes",
            domain=Domain.ALGEBRA,
            complexity=3,
            applications=["factoring", "simplification"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Difference of cubes",
            expression="a^3 - b^3 = (a-b)(a^2 + ab + b^2)",
            description="Factoring difference of cubes",
            domain=Domain.ALGEBRA,
            complexity=3,
            applications=["factoring", "simplification"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Perfect square",
            expression="(a+b)^2 = a^2 + 2ab + b^2",
            description="Binomial square expansion",
            domain=Domain.ALGEBRA,
            complexity=2,
            applications=["completing_square", "optimization"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Binomial theorem",
            expression="(a+b)^n = sum C(n,k) * a^(n-k) * b^k",
            description="General binomial expansion",
            domain=Domain.ALGEBRA,
            complexity=4,
            applications=["polynomial_expansion", "combinatorics"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Geometric series",
            expression="sum a*r^n = a/(1-r) for |r|<1",
            description="Sum of infinite geometric series",
            domain=Domain.ALGEBRA,
            complexity=2,
            applications=["sequences", "interest", "physics"]
        ))
        
        # === TRIGONOMETRY ===
        
        entries.append(KnowledgeEntry(
            name="Pythagorean identity",
            expression="sin^2(x) + cos^2(x) = 1",
            description="Fundamental trig identity",
            domain=Domain.TRIGONOMETRY,
            complexity=2,
            applications=["trig_simplification", "geometry"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Double angle (sin)",
            expression="sin(2x) = 2*sin(x)*cos(x)",
            description="Double angle formula for sine",
            domain=Domain.TRIGONOMETRY,
            complexity=2,
            applications=["signal_processing", "wave_analysis"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Double angle (cos)",
            expression="cos(2x) = cos^2(x) - sin^2(x)",
            description="Double angle formula for cosine",
            domain=Domain.TRIGONOMETRY,
            complexity=2,
            applications=["signal_processing", "wave_analysis"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Sum formula (sin)",
            expression="sin(a+b) = sin(a)*cos(b) + cos(a)*sin(b)",
            description="Sine of sum",
            domain=Domain.TRIGONOMETRY,
            complexity=3,
            applications=["wave_superposition", "oscillations"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Sum formula (cos)",
            expression="cos(a+b) = cos(a)*cos(b) - sin(a)*sin(b)",
            description="Cosine of sum",
            domain=Domain.TRIGONOMETRY,
            complexity=3,
            applications=["wave_superposition", "oscillations"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Product to sum (sin*cos)",
            expression="sin(x)*cos(y) = 0.5*(sin(x+y) + sin(x-y))",
            description="Product to sum formula",
            domain=Domain.TRIGONOMETRY,
            complexity=3,
            applications=["signal_processing", "Fourier"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Half angle",
            expression="sin^2(x/2) = (1 - cos(x))/2",
            description="Half angle formula",
            domain=Domain.TRIGONOMETRY,
            complexity=2,
            applications=["integration", "geometry"]
        ))
        
        # === LOGARITHMS & EXPONENTS ===
        
        entries.append(KnowledgeEntry(
            name="Log product rule",
            expression="log(a*b) = log(a) + log(b)",
            description="Logarithm of product",
            domain=Domain.ALGEBRA,
            complexity=2,
            applications=["logarithm_simplification", "information_theory"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Log quotient rule",
            expression="log(a/b) = log(a) - log(b)",
            description="Logarithm of quotient",
            domain=Domain.ALGEBRA,
            complexity=2,
            applications=["logarithm_simplification"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Log power rule",
            expression="log(a^b) = b*log(a)",
            description="Logarithm of power",
            domain=Domain.ALGEBRA,
            complexity=2,
            applications=["logarithm_simplification", "entropy"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Exponent product",
            expression="a^x * a^y = a^(x+y)",
            description="Multiplying same base exponents",
            domain=Domain.ALGEBRA,
            complexity=2,
            applications=["exponent_simplification", "growth"]
        ))
        
        entries.append(KnowledgeEntry(
            name="Exponent of exponent",
            expression="(a^x)^y = a^(x*y)",
            description="Exponent of exponent",
            domain=Domain.ALGEBRA,
            complexity=2,
            applications=["exponent_simplification"]
        ))
        
        return entries


class PhysicsPriors:
    """Physics constants and equations."""
    
    # === FUNDAMENTAL CONSTANTS ===
    C = 299792458  # Speed of light (m/s)
    H = 6.62607015e-34  # Planck constant (J*s)
    HBAR = 1.054571817e-34  # Reduced Planck (J*s)
    G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
    K_B = 1.380649e-23  # Boltzmann constant (J/K)
    ALPHA = 7.2973525693e-3  # Fine structure constant (~1/137)
    PHI = (1 + 5**0.5) / 2  # Golden ratio
    E_MASS = 9.1093837015e-31  # Electron mass (kg)
    P_MASS = 1.67262192369e-27  # Proton mass (kg)
    
    @staticmethod
    def get_all() -> List[KnowledgeEntry]:
        entries = []
        
        # === MASS-ENERGY ===
        
        entries.append(KnowledgeEntry(
            name="Mass-energy equivalence",
            expression="E = m*c^2",
            description="Einstein's famous equation - mass and energy are equivalent",
            domain=Domain.PHYSICS,
            complexity=2,
            applications=["nuclear_physics", "energy_calculation"],
            weight=1.0
        ))
        
        entries.append(KnowledgeEntry(
            name="Photon energy",
            expression="E = h*f = h*c/lambda",
            description="Energy of a photon from its frequency or wavelength",
            domain=Domain.PHYSICS,
            complexity=2,
            applications=["quantum_physics", "spectroscopy"],
            weight=0.9
        ))
        
        entries.append(KnowledgeEntry(
            name="de Broglie wavelength",
            expression="lambda = h/p = h/(m*v)",
            description="Wave nature of matter - wavelength from momentum",
            domain=Domain.PHYSICS,
            complexity=3,
            applications=["quantum_mechanics", "electron_diffraction"],
            weight=0.8
        ))
        
        # === MECHANICS ===
        
        entries.append(KnowledgeEntry(
            name="Newton's second law",
            expression="F = m*a",
            description="Force equals mass times acceleration",
            domain=Domain.PHYSICS,
            complexity=2,
            applications=["classical_mechanics", "force_calculation"],
            weight=1.0
        ))
        
        entries.append(KnowledgeEntry(
            name="Kinetic energy",
            expression="KE = 0.5*m*v^2",
            description="Energy of motion",
            domain=Domain.PHYSICS,
            complexity=2,
            applications=["energy_calculation", "collisions"],
            weight=1.0
        ))
        
        entries.append(KnowledgeEntry(
            name="Gravitational potential energy",
            expression="PE = -G*m1*m2/r",
            description="Potential energy from gravity",
            domain=Domain.PHYSICS,
            complexity=3,
            applications=["orbital_mechanics", "celestial_physics"],
            weight=0.9
        ))
        
        entries.append(KnowledgeEntry(
            name="Momentum",
            expression="p = m*v",
            description="Linear momentum",
            domain=Domain.PHYSICS,
            complexity=2,
            applications=["collision_conservation", "motion"],
            weight=1.0
        ))
        
        # === QUANTUM MECHANICS ===
        
        entries.append(KnowledgeEntry(
            name="Heisenberg uncertainty",
            expression="dx*dp >= hbar/2",
            description="Fundamental limit on precision of position and momentum",
            domain=Domain.PHYSICS,
            complexity=3,
            applications=["quantum_limits", "measurement"],
            weight=0.9
        ))
        
        entries.append(KnowledgeEntry(
            name="Schrodinger relation",
            expression="E = hbar*omega",
            description="Energy in terms of angular frequency",
            domain=Domain.PHYSICS,
            complexity=2,
            applications=["quantum_mechanics", "wavefunctions"],
            weight=0.8
        ))
        
        entries.append(KnowledgeEntry(
            name="Compton scattering",
            expression="delta_lambda = h/(m*c) * (1 - cos(theta))",
            description="Photon wavelength shift in scattering",
            domain=Domain.PHYSICS,
            complexity=4,
            applications=["X-ray_physics", "quantum_optics"],
            weight=0.7
        ))
        
        # === THERMODYNAMICS & STATISTICS ===
        
        entries.append(KnowledgeEntry(
            name="Thermal energy",
            expression="E = k_B * T",
            description="Average thermal energy per degree of freedom",
            domain=Domain.PHYSICS,
            complexity=2,
            applications=["thermodynamics", "statistical_mechanics"],
            weight=0.9
        ))
        
        entries.append(KnowledgeEntry(
            name="Boltzmann distribution",
            expression="P(E) = exp(-E/(k_B*T))",
            description="Probability of energy state at temperature",
            domain=Domain.PHYSICS,
            complexity=3,
            applications=["statistical_mechanics", "thermodynamics"],
            weight=0.9
        ))
        
        entries.append(KnowledgeEntry(
            name="Stefan-Boltzmann law",
            expression="P = sigma*A*T^4",
            description="Blackbody radiation power",
            domain=Domain.PHYSICS,
            complexity=3,
            applications=["radiation", "astrophysics"],
            weight=0.8
        ))
        
        # === ELECTROMAGNETISM ===
        
        entries.append(KnowledgeEntry(
            name="Coulomb's law",
            expression="F = k*q1*q2/r^2",
            description="Electric force between charges",
            domain=Domain.PHYSICS,
            complexity=3,
            applications=["electromagnetism", "electric_fields"],
            weight=0.9
        ))
        
        entries.append(KnowledgeEntry(
            name="Fine structure constant",
            expression="alpha = e^2/(4*pi*epsilon_0*hbar*c) ~ 1/137",
            description="Fundamental constant coupling electromagnetic interaction",
            domain=Domain.PHYSICS,
            complexity=5,
            applications=["quantum_electrodynamics", "fundamental_physics"],
            weight=0.7
        ))
        
        entries.append(KnowledgeEntry(
            name="Ohm's law",
            expression="V = I*R",
            description="Voltage, current, resistance relationship",
            domain=Domain.PHYSICS,
            complexity=2,
            applications=["circuit_analysis", "electronics"],
            weight=1.0
        ))
        
        # === RELATIVITY ===
        
        entries.append(KnowledgeEntry(
            name="Lorentz factor",
            expression="gamma = 1/sqrt(1 - v^2/c^2)",
            description="Time dilation and length contraction factor",
            domain=Domain.PHYSICS,
            complexity=3,
            applications=["special_relativity", "particle_physics"],
            weight=0.9
        ))
        
        entries.append(KnowledgeEntry(
            name="Relativistic energy",
            expression="E = gamma*m*c^2",
            description="Total energy including relativistic effects",
            domain=Domain.PHYSICS,
            complexity=3,
            applications=["particle_physics", "cosmic_rays"],
            weight=0.9
        ))
        
        return entries


class CryptoPriors:
    """Cryptographic and number-theoretic patterns."""
    
    @staticmethod
    def get_all() -> List[KnowledgeEntry]:
        entries = []
        
        entries.append(KnowledgeEntry(
            name="XOR property",
            expression="a XOR b XOR b = a",
            description="XOR with same value twice returns original",
            domain=Domain.CRYPTOGRAPHY,
            complexity=2,
            applications=["encryption", "error_detection"],
            weight=1.0
        ))
        
        entries.append(KnowledgeEntry(
            name="XOR cancellation",
            expression="a XOR a = 0",
            description="XOR of value with itself is zero",
            domain=Domain.CRYPTOGRAPHY,
            complexity=1,
            applications=["encryption", "hashing"],
            weight=1.0
        ))
        
        entries.append(KnowledgeEntry(
            name="Modular exponentiation",
            expression="a^b mod n = ((a mod n)^b) mod n",
            description="Optimization for large exponentiation",
            domain=Domain.CRYPTOGRAPHY,
            complexity=3,
            applications=["RSA", "Diffie-Hellman", "cryptography"],
            weight=1.0
        ))
        
        entries.append(KnowledgeEntry(
            name="Prime sieve pattern",
            expression="Composite = n*p for n >= 2",
            description="Pattern for finding primes - all composites have prime factors",
            domain=Domain.CRYPTOGRAPHY,
            complexity=2,
            applications=["prime_generation", "RSA_key_creation"],
            weight=0.9
        ))
        
        entries.append(KnowledgeEntry(
            name="Diffie-Hellman",
            expression="K = (g^a)^b mod p = (g^b)^a mod p",
            description="Shared secret without transmitting private key",
            domain=Domain.CRYPTOGRAPHY,
            complexity=4,
            applications=["key_exchange", "TLS"],
            weight=0.8
        ))
        
        entries.append(KnowledgeEntry(
            name="Hash chain",
            expression="H_n = H(H_{n-1})",
            description="Hash of previous hash - blockchain foundation",
            domain=Domain.CRYPTOGRAPHY,
            complexity=2,
            applications=["blockchain", "proof_of_work"],
            weight=1.0
        ))
        
        entries.append(KnowledgeEntry(
            name="Merkle tree",
            expression="hash(A,B) = H(H(A) + H(B))",
            description="Binary tree of hashes for efficient verification",
            domain=Domain.CRYPTOGRAPHY,
            complexity=3,
            applications=["blockchain", "data_verification"],
            weight=0.9
        ))
        
        entries.append(KnowledgeEntry(
            name="Double hash",
            expression="H(H(data)) = HSHA(data)",
            description="Bitcoin's double SHA256 for security",
            domain=Domain.CRYPTOGRAPHY,
            complexity=2,
            applications=["bitcoin", "security"],
            weight=1.0
        ))
        
        return entries


class StatisticalPriors:
    """Statistical and probabilistic patterns."""
    
    @staticmethod
    def get_all() -> List[KnowledgeEntry]:
        entries = []
        
        entries.append(KnowledgeEntry(
            name="Normal distribution",
            expression="P(x) = exp(-x^2/(2*sigma^2)) / (sigma*sqrt(2*pi))",
            description="Gaussian distribution - ubiquitous in nature",
            domain=Domain.STATISTICS,
            complexity=3,
            applications=["statistics", "error_analysis", "nature"],
            weight=1.0
        ))
        
        entries.append(KnowledgeEntry(
            name="Poisson distribution",
            expression="P(k) = (lambda^k * e^(-lambda)) / k!",
            description="Probability of rare events",
            domain=Domain.STATISTICS,
            complexity=3,
            applications=["queueing_theory", "radioactive_decay"],
            weight=0.9
        ))
        
        entries.append(KnowledgeEntry(
            name="Exponential decay",
            expression="N(t) = N_0 * exp(-lambda*t)",
            description="Radioactive decay, damped oscillations",
            domain=Domain.STATISTICS,
            complexity=2,
            applications=["decay_systems", "damping"],
            weight=1.0
        ))
        
        entries.append(KnowledgeEntry(
            name="Power law",
            expression="P(x) = C * x^(-alpha)",
            description="Scale-free distributions - Zipf's law, Pareto",
            domain=Domain.STATISTICS,
            complexity=2,
            applications=["complex_systems", "wealth_distribution"],
            weight=0.9
        ))
        
        entries.append(KnowledgeEntry(
            name="Central limit theorem",
            expression="Sum of many variables -> Normal distribution",
            description="Independent random variables tend toward Gaussian",
            domain=Domain.STATISTICS,
            complexity=4,
            applications=["statistics_foundation", "data_analysis"],
            weight=1.0
        ))
        
        entries.append(KnowledgeEntry(
            name="Entropy",
            expression="H = -sum(p(x) * log(p(x)))",
            description="Information entropy - measure of uncertainty",
            domain=Domain.STATISTICS,
            complexity=3,
            applications=["information_theory", "compression", "cryptography"],
            weight=1.0
        ))
        
        return entries


class KnowledgeBase:
    """
    Combined knowledge base from all domains.
    
    Usage:
        kb = KnowledgeBase()
        entries = kb.get_entries_by_domain(Domain.PHYSICS)
        kb.apply_to_population(population)
    """
    
    def __init__(self):
        self.math = MathematicalPriors()
        self.physics = PhysicsPriors()
        self.crypto = CryptoPriors()
        self.statistics = StatisticalPriors()
        
        self._all_entries: Optional[List[KnowledgeEntry]] = None
    
    def get_all_entries(self) -> List[KnowledgeEntry]:
        """Get all knowledge entries from all domains."""
        if self._all_entries is None:
            self._all_entries = (
                self.math.get_all() +
                self.physics.get_all() +
                self.crypto.get_all() +
                self.statistics.get_all()
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
            if entry.domain.value not in by_domain:
                by_domain[entry.domain.value] = 0
            by_domain[entry.domain.value] += 1
        
        return {
            "total_entries": len(entries),
            "by_domain": by_domain,
            "total_weight": sum(e.weight for e in entries)
        }
    
    def __repr__(self):
        stats = self.get_statistics()
        return f"KnowledgeBase({stats['total_entries']} entries)"


# Quick test
if __name__ == "__main__":
    kb = KnowledgeBase()
    print("=== KnowledgeBase Statistics ===")
    stats = kb.get_statistics()
    print(f"Total entries: {stats['total_entries']}")
    print(f"By domain:")
    for domain, count in stats['by_domain'].items():
        print(f"  {domain}: {count}")
    
    print("\n=== Sample Entries ===")
    physics_entries = kb.get_entries_by_domain(Domain.PHYSICS)
    for entry in physics_entries[:5]:
        print(f"  {entry.name}: {entry.expression}")
    
    print("\n=== Crypto Entries ===")
    crypto_entries = kb.get_entries_by_domain(Domain.CRYPTOGRAPHY)
    for entry in crypto_entries:
        print(f"  {entry.name}: {entry.expression}")
