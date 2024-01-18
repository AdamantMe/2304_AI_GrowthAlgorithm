import argparse
import os
from GrowthAlgorithm import GrowthAlgorithm
from GrowthRules.DiffusionGrowthRule import DiffusionGrowthRule
from GrowthRules.SimpleGrowthRule import SimpleGrowthRule
from GrowthRules.ProbabilisticGrowthRule import ProbabilisticGrowthRule

class GrowthSimulation:
    def __init__(self, size, growth_rules):
        self.algorithms = [GrowthAlgorithm(size, rule) for rule in growth_rules]
        self.size = size

    def clear_screen(self):
        """Clears the terminal screen. This method is platform-dependent."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def run_simulation(self, growth_rule):
        algorithm = GrowthAlgorithm(self.size, growth_rule)
        algorithm.set_initial_state()

        #Clear the screen before starting
        self.clear_screen()

        #Flag to indicate if the algorithm is currently growing
        algorithm_growing = True

        #Run the simulation for the specified rule
        while algorithm_growing:
            algorithm_growing = False  #Initialize to False at the beginning of each iteration
            if algorithm.growth_rule.changes:
                algorithm_growing = True
                #Print algorithm information
                print(f"Algorithm - {algorithm.growth_rule.__class__.__name__}")
                print("Each number represents the growth step at which the cell was added.")
                print("0: Empty cell, 1+: Growth steps\n")
                algorithm.apply_growth_rules()
                if algorithm.growth_rule.changes:
                    algorithm.grid.print_grid()
                print(f"Iteration: {algorithm.grid.get_highest_step()}")  #Print iteration information

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a growth simulation with a specified rule.")
    parser.add_argument("-rule", required=True, choices=["simple", "prob", "diff"], help="Specify the growth rule (simple/prob/diff)")
    parser.add_argument("-size", type=int, default=9, help="Specify the size of the grid")

    #Parsing the args, running a related growth rule
    args = parser.parse_args()
    growth_rules = {"simple": SimpleGrowthRule, "prob": ProbabilisticGrowthRule, "diff": DiffusionGrowthRule}
    selected_rule = growth_rules.get(args.rule)

    if selected_rule:
        #Create a GrowthSimulation instance and pass the selected growth rule class
        simulation = GrowthSimulation(args.size, [selected_rule])

        #Run the simulation
        simulation.run_simulation(selected_rule())
    else:
        print("Invalid growth rule specified. Use '-rule simple' or '-rule prob' or '-rule diff'.")