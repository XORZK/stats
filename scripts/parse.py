#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Index:
    def __init__(self, year: int, value: float):
        self.year = year
        self.value = value
    def __str__(self):
        return f"{self.year}: {self.value}"

def get_map(f: pd.core.frame.DataFrame, c_index: int, y_index: int, v_index: int) -> map:
    mapped = {}
    for i in range(0, len(f)):
        row = f.loc[i]
        country, year, value = row[c_index], row[y_index], row[v_index]

        if (math.isnan(value)): continue

        index = Index(year, value)

        if (not country in mapped.keys()):
            mapped[country] = [index]
        else:
            mapped[country].append(index)

    return mapped

def plot(values: list):
    x, y = [], []

    for i in values:
        x.append(i.year)
        y.append(i.value)

    plt.plot(x,y)

def map_csv(fn: str, c_index: int, y_index: int, v_index: int) -> map:
    f = pd.read_csv(fn)
    mapped = get_map(f, c_index, y_index, v_index)

    return mapped


def plot_csv(fn: str, c_index: int, y_index: int, v_index: int):
    mapped = map_csv(f, c_index, y_index, v_index)

    for x in list(mapped.keys()):
        plot(mapped[x])

    plt.show()

def plot_map(mapped: map, title = ""):
    plt.title(title)
    for x in mapped.keys():
        plot(mapped[x])

# Happiness: 0, 2, 3
# Phones: 0, 1, 2
# Internet: 0, 1, 2

def main():
    happiness = map_csv("../data/csv/cantril-ladder.csv", 0, 2, 3)
    phones = map_csv("../data/csv/cell-phones.csv", 0, 1, 2)
    internet = map_csv("../data/csv/internet-users.csv", 0, 1, 2)

    plot_map(happiness, "Plot of Cantril Ladder Values")
    plt.show()

if (__name__ == "__main__"):
    main()
