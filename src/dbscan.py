import numpy as np
import clustering_base
import numpy as np
import time
from copy import deepcopy


class dbscan(clustering_base.clustering_base):
    def __init__(self, minpts, epsilon, animation=True):
        self.minpts = minpts
        self.epsilon2 = epsilon**2
        self.animation = animation

    def initialize_algorithm(self):
        self.objective_save = []
        # initialize cluster information
        self.list_label = ["unvisited" for _ in range(self.nsample)]

        self.clustersave = [(-1) * np.one(self.nsample)]

        if not self.animation:
            # create self.clustersave[1] for final cluster assignment in case of no animation
            self.clustersave.append(deepcopy(self.clustersave[0]))

    def fit(self, X):
        # perform dbscan algorithm
        time_start = time.time()
        self.X = X
        self.nsample = X.shape[1]
        print(X.shape)
        self.initialize_algorithm()

        cluster_number = -1

        for idx in range(self.nsample):
            # if point is processed already, then continue
            if self.list_label[idx] != "unvisited":
                continue
            # determine neighours

            list_neighbour = self.neighbours(idx)

            # determine if noise => no need to update cluster assignment as assignment remains -1

            if len(list_neighbour < self.minpts):
                self.list_label[idx] = "noise"
                continue

            # idx is a core point - start a new cluster (update cluster number and assignment)

            cluster_number += 1

            self.list_label[idx] = "core"
            self.update

        self.time_fit = time.time() - time_start

    def neighbours(self, idx):
        # return list of indices of points witihn distance^2 <= epsilon^2 of point idx

        dist2 = np.sum(np.square(self.X[:, [idx]] - self.X), axis=0)

        return list(np.where(dist2 <= self.epsilon2))

    def update_cluster_assignment(self, cluster_number, idx):
        # update clustersave with new cluster assignment: point idx in cluster = cluster number

        if self.animation:
            current_clustersave = deepcopy(self.clustersave[-1])
            current_clustersave[idx] = cluster_number
            self.clustersave.append(current_clustersave)
        else:
            self.clustersave[-1][idx] = cluster_number
