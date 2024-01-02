from GrowthAlgorithm import GrowthAlgorithm
from GrowthRules.SimpleGrowthRule import SimpleGrowthRule

class GrowthSimulation:
    def __init__(self, size, iterations, growth_rule):
        self.algorithm = GrowthAlgorithm(size, growth_rule)
        self.iterations = iterations

    def run_simulation(self):
        self.algorithm.set_initial_state()  # Set the initial state before the iterations
        for iteration in range(self.iterations):  # Main simulation loop
            print(f"Iteration {iteration + 1}:")
            self.algorithm.apply_growth_rules() 
            self.algorithm.display_structure()  
            print(f"End of Iteration {iteration + 1}\n")  # Newline for readability

if __name__ == "__main__":
    size = 10
    iterations = 5

    print("\nSimple Growth Rule:")
    simple_rule_simulation = GrowthSimulation(size, iterations, SimpleGrowthRule())
    simple_rule_simulation.run_simulation()