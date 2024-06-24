import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

class Coprocessor:
    def __init__(self, id, resources, reputation):
        self.id = id
        self.resources = resources
        self.max_resources = resources
        self.reputation = reputation
        self.total_reward = 0

    def execute_task(self, task, bid):
        if random.random() < self.success_probability(task):
            task.completed = True
            self.reputation = min(1, self.reputation + task.risk_factor)
            self.resources = max(0, self.resources - task.difficulty)
            self.total_reward += bid
        else:
            task.completed = False
            self.apply_penalties(task)

    def success_probability(self, task):
        base_success = 0.9
        return base_success * (self.resources / task.difficulty)

    def reset_resources(self):
        # Reset resources to max at the start of each period
        self.resources = self.max_resources

    def apply_penalties(self, task):
        self.reputation = max(0, self.reputation - task.risk_factor)
        self.total_reward -= task.slashing

class Task:
    def __init__(self, id, difficulty, reward, slashing, risk_factor):
        self.id = id
        self.difficulty = difficulty
        self.reward = reward
        self.slashing = slashing
        self.risk_factor = risk_factor
        self.completed = False
        self.delegated_to = None

    def compute_slashing(self, completed, period):
        return self.slashing if not completed else 0