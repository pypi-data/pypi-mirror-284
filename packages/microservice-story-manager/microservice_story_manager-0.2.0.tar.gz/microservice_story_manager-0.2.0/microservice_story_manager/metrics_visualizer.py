# metrics_visualizer.py
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np


class MetricsVisualizer:
    @staticmethod
    def compare_metrics(metrics1: Dict, metrics2: Dict, name1: str, name2: str):
        metrics = list(metrics1.keys())
        values1 = list(metrics1.values())
        values2 = list(metrics2.values())

        x = np.arange(len(metrics))
        width = 0.35

        fig, ax = plt.subplots(figsize=(12, 6))
        rects1 = ax.bar(x - width / 2, values1, width, label=name1)
        rects2 = ax.bar(x + width / 2, values2, width, label=name2)

        ax.set_ylabel('Metric Values')
        ax.set_title('Comparison of Metrics between Two Fitness Functions')
        ax.set_xticks(x)
        ax.set_xticklabels(metrics)
        ax.legend()

        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.annotate(f'{height:.2f}',
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),
                            textcoords="offset points",
                            ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        fig.tight_layout()
        plt.show()

    @staticmethod
    def compare_fitness_values(fitness_values: List[float], function_names: List[str]):
        x = np.arange(len(function_names))

        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(x, fitness_values, width=0.6)

        ax.set_ylabel('Fitness Value')
        ax.set_title('Comparison of Fitness Values')
        ax.set_xticks(x)
        ax.set_xticklabels(function_names)

        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.annotate(f'{height:.2f}',
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),
                            textcoords="offset points",
                            ha='center', va='bottom')

        autolabel(bars)

        fig.tight_layout()
        plt.show()
