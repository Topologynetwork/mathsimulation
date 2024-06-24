import pytest
from simulation import Simulation
from config import Config

def test_simulation_run():
    config = Config(10, 15, 100, 1000)
    sim = Simulation(config)
    sim.run()
    

def test_simulation_export_data():
    config = Config(10, 15, 100, 1000)
    sim = Simulation(config)
    validator_data, coprocessor_data, task_data = sim.export_data()
    