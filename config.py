"""
EvoMath Configuration
Centralized constants for energy-efficient symbolic regression
"""

# Numerical safety
EPSILON = 1e-15
INVALID_PENALTY = 1e10
MAX_EXP = 700  # exp() overflow threshold
MAX_MAGNITUDE = 1e100

# Evolution parameters
DEFAULT_POPULATION_SIZE = 100
DEFAULT_LEAKY_GENERATIONS = 10
ELITE_RATIO = 0.05
MUTATION_RATE = 0.15

# Diversity control
IDOTYPIC_SUPPRESSION_FREQ = 5
SUPPRESSION_THRESHOLD = 0.9
SUPPRESSION_PENALTY = 0.95

# Fitness weights
VAR_COVERAGE_WEIGHT = 0.5
ELITE_WEIGHT = 1.5
COMPLEMENT_WEIGHT = 1.5
MEMORY_WEIGHT = 1.2

# Operator modes
class OperatorMode:
    MATH_ONLY = "math"      # +, -, *, /, **, sin, cos, log, sqrt
    BITWISE_ONLY = "bitwise" # ^, &, |, <<, >>
    MIXED = "mixed"          # All operators

# Default to math-only for physics
DEFAULT_OPERATOR_MODE = OperatorMode.MATH_ONLY

# Complexity limits
MAX_TREE_DEPTH = 6
MIN_TREE_DEPTH = 2

# Success criteria
SUCCESS_ERROR_THRESHOLD = 1e-6
HIT_BONUS = 500
HIGH_FITNESS_THRESHOLD = 10000
