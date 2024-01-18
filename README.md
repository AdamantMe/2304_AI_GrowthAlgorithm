# Artificial Intelligence Module (FT/BL)

## Programme Information
- Programme: BSc (Hons) Computing
- Semester: 2304

## Instructor
- Teacher: Jindra Helcl

## Project Title
Delivering Research Outputs

## Overview
This repository contains code and documentation related to the "Delivering Research Outputs" project in the Artificial Intelligence module. The project explores various growth algorithms for generating patterns and shapes.

## Growth Algorithms
The project implements three specific growth algorithms, each with its unique characteristics:
1. **Simple Growth Algorithm**: This algorithm demonstrates regular and even pattern growth.
2. **Probabilistic Growth Algorithm**: Experience random growth patterns resulting in more natural and varied shapes.
3. **Diffusion Growth Algorithm**: Observe gradual and uniform expansion, similar to color dispersion in water.

## Running the Algorithms
To run a specific growth algorithm, you should specify the complete file path to the `GrowthSimulation.py` script along with the desired algorithm name (or cd to the folder containing it). 
Use the following command, replacing `[algorithm]` with the desired algorithm name:

python C:\path\to\GrowthSimulation.py -rule [algorithm]

algorithm names:
'simple' for the Simple Growth Algorithm
'prob' for the Probabilistic Growth Algorithm
'diff' for the Diffusion Growth Algorithm

Example:
python C:\path\to\GrowthSimulation.py -rule prob
