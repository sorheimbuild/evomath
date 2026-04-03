"""
Mining simulation for EvoMath.
Tests the algorithm on simplified proof-of-work problems.
"""

import hashlib
import time
import random
from typing import Tuple, Optional
from evomath_v3 import EvoMathV3, Antigen, Node

class MiningSimulator:
    """
    Simplified mining simulation.
    Uses a simplified hash-like function for testing.
    Real SHA256 is intentionally one-way, so we test on tractable problems.
    """
    
    def __init__(self, evo: EvoMathV3):
        self.evo = evo
    
    def simplified_hash(self, data: bytes) -> int:
        """Simplified hash for simulation - reversible-ish patterns"""
        h = 0
        for i, byte in enumerate(data):
            h = (h * 31 + byte) % (2**32)
        return h
    
    def create_hash_puzzle(self, difficulty: int = 8) -> Tuple[dict, int, Antigen]:
        """
        Create a hash puzzle: find input that produces hash with N leading zeros.
        difficulty = number of leading zero bytes (8 = relatively easy)
        """
        target = 2 ** (256 - difficulty * 8)
        
        block_header = random.randint(0, 2**32)
        
        test_cases = []
        for nonce in range(1000):
            data = f"{block_header}:{nonce}".encode()
            hash_val = self.simplified_hash(data)
            test_cases.append(({'h': block_header, 'n': nonce}, hash_val))
        
        antigen = Antigen(
            test_cases=test_cases,
            description=f"Hash puzzle (difficulty={difficulty})"
        )
        
        return {'h': float(block_header)}, target, antigen
    
    def create_xor_puzzle(self) -> Tuple[dict, float, Antigen]:
        """
        Create a puzzle: find x such that (h XOR x) produces a pattern.
        Tests bitwise operations.
        """
        h = random.randint(1, 1000)
        target_val = h ^ 42
        
        test_cases = [
            ({'h': float(h), 'n': 0.0, 'x': 0.0, 'y': 0.0, 'z': 0.0, 't': 0.0}, float(target_val)),
        ]
        
        antigen = Antigen(
            test_cases=test_cases,
            description=f"XOR puzzle: find x where h^x = {target_val}"
        )
        
        return {'h': float(h), 'n': 0.0, 'x': 0.0, 'y': 0.0, 'z': 0.0, 't': 0.0}, float(target_val), antigen
    
    def create_modular_puzzle(self) -> Tuple[dict, float, Antigen]:
        """
        Create a puzzle: find x such that (base * x) % mod = target
        Tests modular arithmetic (common in crypto).
        """
        base = random.randint(7, 50)
        mod = random.randint(100, 500)
        target = random.randint(1, mod - 1)
        
        test_cases = [
            ({'x': 0.0, 'y': float(base), 'z': float(mod), 'n': float(target), 't': 0.0, 'h': 0.0}, float(target)),
        ]
        
        antigen = Antigen(
            test_cases=test_cases,
            description=f"Modular: find n where {base}*n % {mod} = {target}"
        )
        
        return {'x': 0.0, 'y': float(base), 'z': float(mod), 'n': float(target), 't': 0.0, 'h': 0.0}, float(target), antigen
    
    def create_cumulative_puzzle(self) -> Tuple[dict, float, Antigen]:
        """
        Create a puzzle: find sequence pattern.
        This simulates finding mathematical shortcuts in sequences.
        """
        start = random.randint(1, 10)
        step = random.randint(2, 7)
        
        test_cases = []
        for i in range(5):
            test_cases.append(({'x': float(i), 'y': float(start), 'z': float(step), 'n': 0.0, 't': 0.0, 'h': 0.0}, float(start + i * step)))
        
        antigen = Antigen(
            test_cases=test_cases,
            description=f"Arithmetic sequence: {start} + n*{step}"
        )
        
        return {'x': 0.0, 'y': float(start), 'z': float(step), 'n': 0.0, 't': 0.0, 'h': 0.0}, 0.0, antigen
    
    def run_benchmark(self, puzzle_type: str = "all", verbose: bool = True) -> dict:
        """Run mining simulation benchmarks."""
        
        results = {
            "xor_puzzle": None,
            "modular_puzzle": None,
            "cumulative_puzzle": None,
        }
        
        if puzzle_type in ("all", "xor"):
            if verbose:
                print("\n" + "=" * 60)
                print(" Mining Simulation: XOR Puzzle")
                print("=" * 60)
            
            evo = EvoMathV3(population_size=500)
            inputs, target, antigen = self.create_xor_puzzle()
            
            start = time.time()
            solution = evo.solve(antigen, max_generations=200, verbose=verbose)
            elapsed = time.time() - start
            
            results["xor_puzzle"] = {
                "time": elapsed,
                "generations": evo.generation,
                "solution": solution.to_string(),
                "target": inputs
            }
            
            if verbose:
                print(f"\nPuzzle: h ^ x = {target}")
                print(f"Solution: {solution.to_string()}")
                print(f"Time: {elapsed:.2f}s | Generations: {evo.generation}")
        
        if puzzle_type in ("all", "modular"):
            if verbose:
                print("\n" + "=" * 60)
                print(" Mining Simulation: Modular Arithmetic")
                print("=" * 60)
            
            evo = EvoMathV3(population_size=500)
            inputs, target, antigen = self.create_modular_puzzle()
            
            start = time.time()
            solution = evo.solve(antigen, max_generations=200, verbose=verbose)
            elapsed = time.time() - start
            
            results["modular_puzzle"] = {
                "time": elapsed,
                "generations": evo.generation,
                "solution": solution.to_string(),
                "target": inputs
            }
            
            if verbose:
                print(f"\nPuzzle: {inputs['y']} * n % {inputs['z']} = {target}")
                print(f"Solution: {solution.to_string()}")
                print(f"Time: {elapsed:.2f}s | Generations: {evo.generation}")
        
        if puzzle_type in ("all", "cumulative"):
            if verbose:
                print("\n" + "=" * 60)
                print(" Mining Simulation: Cumulative Pattern")
                print("=" * 60)
            
            evo = EvoMathV3(population_size=500)
            inputs, target, antigen = self.create_cumulative_puzzle()
            
            start = time.time()
            solution = evo.solve(antigen, max_generations=200, verbose=verbose)
            elapsed = time.time() - start
            
            results["cumulative_puzzle"] = {
                "time": elapsed,
                "generations": evo.generation,
                "solution": solution.to_string(),
                "target": inputs
            }
            
            if verbose:
                print(f"\nPuzzle: Arithmetic sequence")
                print(f"Solution: {solution.to_string()}")
                print(f"Time: {elapsed:.2f}s | Generations: {evo.generation}")
        
        return results


def run_full_benchmark():
    """Run comprehensive mining benchmarks."""
    print("=" * 70)
    print(" EvoMath Mining Simulation Benchmark")
    print("=" * 70)
    print("\nTesting on crypto-relevant puzzle types:")
    print("- XOR operations (bitwise manipulation)")
    print("- Modular arithmetic (common in PoW)")
    print("- Cumulative patterns (sequence detection)")
    print("\nNote: Real SHA256 is intentionally one-way.")
    print("This tests the framework on tractable problems.\n")
    
    simulator = MiningSimulator(EvoMathV3())
    results = simulator.run_benchmark(puzzle_type="all", verbose=True)
    
    print("\n" + "=" * 70)
    print(" Benchmark Results Summary")
    print("=" * 70)
    
    total_time = 0
    total_gens = 0
    for name, result in results.items():
        if result:
            print(f"{name:20s}: {result['time']:6.2f}s | {result['generations']:4d} gens | sol={result['solution'][:30]}")
            total_time += result['time']
            total_gens += result['generations']
    
    print(f"{'TOTAL':20s}: {total_time:6.2f}s | {total_gens:4d} gens")
    print("\n" + "=" * 70)


def compare_with_bruteforce():
    """Compare EvoMath vs brute force on a simple problem."""
    print("\n" + "=" * 70)
    print(" EvoMath vs Brute Force Comparison")
    print("=" * 70)
    
    base = 7
    mod = 100
    target = 42
    
    print(f"\nProblem: Find x where {base} * x % {mod} = {target}")
    print("(Brute force would try x = 0, 1, 2, ...)")
    
    for brute_x in range(mod):
        if (base * brute_x) % mod == target:
            print(f"Brute force answer: x = {brute_x}")
            break
    
    print("\n--- EvoMath ---")
    evo = EvoMathV3(population_size=400)
    
    test_cases = [
        ({'x': 0.0, 'y': float(base), 'z': float(mod), 'n': float(target), 't': 0.0, 'h': 0.0}, float(target)),
    ]
    antigen = Antigen(test_cases=test_cases, description="modular")
    
    start = time.time()
    solution = evo.solve(antigen, max_generations=150, verbose=False)
    elapsed = time.time() - start
    
    print(f"EvoMath answer: {solution.to_string()}")
    print(f"Time: {elapsed:.2f}s | Generations: {evo.generation}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    run_full_benchmark()
    compare_with_bruteforce()
