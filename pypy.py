import numpy as np
import matplotlib.pyplot as plt

# Constants
PHI = (1 + np.sqrt(5)) / 2  # The Golden Ratio
DIMENSIONS = 5  # Ququint (5 states), extendable to Qu-1000+
STEPS = 500
NUM_AGENTS = 200
STATE_SIZE = 10

# Initialize agents
def initialize_agents(num_agents, state_size, dimensions):
    """Initialize agents with random states in higher dimensions."""
    agents = []
    for _ in range(num_agents):
        state = np.random.randint(0, dimensions, size=state_size)  # Random initial states
        agents.append({"state": state, "fitness": 0})
    return agents

# Recursive fitness calculation
def calculate_recursive_fitness(state, previous_fitness, resonance_factor=0.1):
    """Recursive fitness based on Phi and previous states."""
    base_fitness = abs(np.sum(state) - PHI)
    return (1 - resonance_factor) * base_fitness + resonance_factor * previous_fitness

# Fibonacci harmonic mutation
def fibonacci_harmonic_mutation(state, step, dimensions):
    """Mutate states based on Fibonacci harmonic resonance."""
    fib_index = step % len(state)
    state[fib_index] = (state[fib_index] + 1) % dimensions  # Harmonic alignment mutation
    return state

# Apply fractal resonance
def apply_fractal_resonance(agents, threshold=0.1):
    """Spread fractal resonance effects from high-fitness agents."""
    for agent in agents:
        if agent["fitness"] < threshold:  # High fitness implies closeness to Phi
            for neighbor in agents:
                neighbor["state"] = (neighbor["state"] + 1) % DIMENSIONS  # Fractal resonance effect
    return agents

# Simulate one step with fractal resonance
def simulate_step_with_fractal_resonance(agents, step):
    """Simulate one step with fractal resonance."""
    resonance_factor = np.exp(-0.001 * step)  # Dynamic resonance decay
    for agent in agents:
        previous_fitness = agent["fitness"]
        # Mutate state with Fibonacci harmonic adjustment
        agent["state"] = fibonacci_harmonic_mutation(agent["state"], step, DIMENSIONS)
        # Update fitness recursively with dynamic resonance
        agent["fitness"] = calculate_recursive_fitness(agent["state"], previous_fitness, resonance_factor)
    # Apply fractal resonance
    agents = apply_fractal_resonance(agents)
    return agents

# Plot average fitness over time
def plot_fitness_over_time(avg_fitness):
    plt.plot(range(len(avg_fitness)), avg_fitness, color='blue', label="Average Fitness")
    plt.xlabel("Steps")
    plt.ylabel("Fitness")
    plt.title("Fractal Quantum Resonance Algorithm (FQRA) Fitness")
    plt.legend()
    plt.grid()
    plt.show()

# Visualize state distribution
def plot_state_distribution(agents):
    states = [state for agent in agents for state in agent["state"]]
    plt.hist(states, bins=range(DIMENSIONS + 1), alpha=0.7, color='green', edgecolor='black')
    plt.title("State Distribution Across Agents")
    plt.xlabel("State Value")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()

# Main simulation
def run_fqra_simulation():
    agents = initialize_agents(NUM_AGENTS, STATE_SIZE, DIMENSIONS)
    avg_fitness_over_time = []

    for step in range(STEPS):
        agents = simulate_step_with_fractal_resonance(agents, step)
        avg_fitness = np.mean([agent["fitness"] for agent in agents])
        avg_fitness_over_time.append(avg_fitness)

        # Print periodic updates
        if step % (STEPS // 10) == 0 or step == STEPS - 1:
            print(f"Step {step + 1}/{STEPS} | Average Fitness: {avg_fitness:.4f}")

    # Plot results
    plot_fitness_over_time(avg_fitness_over_time)
    plot_state_distribution(agents)

# Execute the simulation
run_fqra_simulation()

