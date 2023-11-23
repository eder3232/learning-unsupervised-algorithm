import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import colormaps
import numpy as np


class clustering_base:
    def __init__(self):
        pass

    def initialize_algorithm(self):
        pass

    def fit(self, x):
        pass

    def get_index(self, nlevel, cluster_number):
        return np.where(np.absolute(self.clustersave[nlevel] - cluster_number) < 1e-5)[
            0
        ]
