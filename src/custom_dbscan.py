import numpy as np
import matplotlib.pyplot as plt
import math

data = [
    [1, 1],
    [1.1, 1.1],
    [1.3, 1.2],
    [0.9, 1.2],
    [1.15, 1.15],
    [5, 5],
    [5.1, 5.1],
    [5.3, 5.2],
    [4.9, 5.2],
    [5.15, 5.15],
    [10, 10],
    [10.1, 10.1],
    [10.3, 10.2],
    [9.9, 10.2],
    [10.15, 10.15],
    [1, 9],
    [9, 1],
    [5, 9],
]

# plot data

fig, ax = plt.subplots(1, 1)
ax.set_title("Data")
ax.set_xlabel("Feature x0")
ax.set_ylabel("Feature x1")
scat = ax.scatter(
    np.array(data)[:, 0], np.array(data)[:, 1], color="b", marker="o", s=15
)
plt.show()


class eder_dbscan:
    def __init__(self, minpts, epsilon):
        self.minpts = minpts
        self.epsilon = epsilon

    def initialize_algorithm(self):
        # self.objectivesave = []
        # initialize cluster information
        self.list_label = ["unvisited" for _ in range(len(self.data))]
        self.list_neighbour = [[] for _ in range(len(self.data))]
        self.clustersave = np.full(len(self.data), -1)

    def fit(self, data):
        self.data = data
        self.lenData = len(data)
        self.initialize_algorithm()
        cluster_number = -1

        for idx in range(self.lenData):
            # print(self.list_label)
            if self.list_label[idx] != "unvisited":
                continue
            self.list_neighbour[idx] = self.neighbours(idx)
            print(idx)

            print(self.list_neighbour[idx])

            if len(self.list_neighbour[idx]) < self.minpts:
                self.list_label[idx] = "noise"
                continue

            cluster_number += 1
            self.list_label[idx] = "core"

            self.iterar_vecinos(cluster_number, self.list_neighbour[idx])

        print(self.list_label)

        return self.clustersave

    def neighbours(self, idx):
        # return list of indices of points within distance^2 <= epsilon^2 of point idx
        list_neighbour_indices = []

        for i in range(self.lenData):
            if i == idx:
                continue

            if self.calcular_distancia(self.data[idx], self.data[i]) <= self.epsilon:
                list_neighbour_indices.append(i)

        return list_neighbour_indices

    def calcular_distancia(self, punto1, punto2):
        if len(punto1) != len(punto2):
            raise ValueError(
                "Ambos puntos deben tener la misma cantidad de dimensiones"
            )

        distancia = math.sqrt(
            sum((punto2[i] - punto1[i]) ** 2 for i in range(len(punto1)))
        )

        # print(f"Distancia entre {punto1} y {punto2} es {distancia}")

        return distancia

    def iterar_vecinos(self, cluster_number, list_neighbour):
        for i in list_neighbour:
            if self.list_label[i] == "noise":
                self.list_label[i] = "border"
                self.clustersave[i] = cluster_number

            if self.list_label[i] == "unvisited":
                continue

            self.clustersave[i] = cluster_number

            neighbours = self.neighbours(i)

            if len(neighbours) < self.minpts:
                self.list_label[i] = "border"
                continue
            else:
                self.list_label[i] = "core"
                self.list_neighbour[i].extend(neighbours)


pruebas = eder_dbscan(3, 2)
print(pruebas.fit(data))
