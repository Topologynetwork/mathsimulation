import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

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