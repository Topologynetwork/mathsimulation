import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from validator import Validator
from coprocessor import Coprocessor
from task import Task

from config import Config
from simulation import Simulation

def main():
    # Configure the simulation parameters
    config = Config(10, 15, 100, 1000)
    
    # Initialize the simulation with the given configuration
    sim = Simulation(config)
    
    # Run the simulation
    sim.run()
    
    # Export data from the simulation
    validator_data, coprocessor_data, task_data = sim.export_data()
    
    # For demonstration purposes, print the exported data
    print("Validator Data:", validator_data)
    print("Coprocessor Data:", coprocessor_data)
    print("Task Data:", task_data)

if __name__ == "__main__":
    main()
