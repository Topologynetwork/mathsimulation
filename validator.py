import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

class Validator:
    def __init__(self, id, resources, reputation, difficulty_threshold):
        self.id = id
        self.resources = resources
        self.max_resources = resources
        self.reputation = reputation
        self.difficulty_threshold = difficulty_threshold
        self.tasks = []
        self.failed_tasks = 0
        self.total_reward = 0

    def reset_resources(self):
        # Reset resources to max at the start of each period
        self.resources = self.max_resources

    def decide_and_assign_task(self, task, coprocessors):
        if self.resources >= task.difficulty:
            if task.difficulty > self.difficulty_threshold:
                bid = task.reward * random.uniform(0.8, 0.99)
                self.auction_task(task, coprocessors, bid)
            else:
                self.execute_task(task) # No suitable coprocessor, handle internally
        else:
            task.completed = False
            self.failed_tasks += 1


    def auction_task(self, task, coprocessors, bid):
        suitable_coprocessors = [cp for cp in coprocessors if cp.resources >= task.difficulty]
        if not suitable_coprocessors:
            self.execute_task(task)
            return

        bids = [(cp, cp.reputation * random.uniform(0.3, 1) * bid) for cp in suitable_coprocessors]
        winner, winning_bid = min(bids, key=lambda x: x[1])
        winner.execute_task(task, winning_bid)
        if task.completed:
            self.total_reward += (task.reward - winning_bid)
            task.delegated_to = winner.id
        else:
            self.apply_penalties(task)

    def execute_task(self, task):
        success_probability = 0.95 #(base_success + reputation) * (self.computational_power / task.difficulty)
        if success_probability > random.random():  # Simulate task completion success
            if self.resources >= task.difficulty:
                self.resources -= task.difficulty
                self.reputation = min(1, self.reputation + task.risk_factor)
                task.completed = True
                self.total_reward += task.reward
                self.tasks.append(task)
        else:
            task.completed = False
            self.apply_penalties(task)

    def apply_penalties(self, task):
        self.reputation = max(0, self.reputation - task.risk_factor)
        self.failed_tasks += 1
        self.total_reward -= task.slashing

    def calculate_rewards(self, period):
        # Calculate the sum of rewards for completed tasks
        return sum(task.reward for task in self.tasks if task.completed)
    