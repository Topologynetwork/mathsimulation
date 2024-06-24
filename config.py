import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from validator import Validator
from coprocessor import Coprocessor
from task import Task


class Config:
    def __init__(self, num_validators, num_coprocessors, num_tasks, num_periods):
        self.num_validators = num_validators
        self.num_coprocessors = num_coprocessors
        self.num_tasks = num_tasks
        self.num_periods = num_periods