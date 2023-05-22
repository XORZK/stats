#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1-Variable Statistical Analysis:
# Box Plots
# Measures of Central Tendency and Spread
# Outliers
# Straightening Data

def pool(mapped: map) -> map:
    mapped["pooled"] = []
    for x in list(mapped.keys()):
        if (x == "pooled"): continue
        mapped["pooled"].extend(mapped[x])
    return mapped

def convert_index(mapped: map) -> map:
    values = {}
    for x in list(mapped.keys()):
        values[x] = []
        for val in mapped[x]:
            values[x].append(val.value)

    return values

def merged_boxplot(values: map):
    plot_data, positions, labels = [], [], []
    for i in range(len(list(values.keys()))):
        x = list(values.keys())[i]
        if (x == "pooled"): continue
        plot_data.append(values[x])
        positions.append(100/len(list(values.keys())) * i)
        labels.append(x)

    plt.figure(figsize=(100,6))
    plt.boxplot(plot_data, labels=labels)

def save_box(values: list, title = "", dir = "", lb = ""):
    plt.title(title)
    plt.boxplot(values, labels=[lb])
    fn = title.replace(" ", "-").lower()
    plt.savefig(f"{dir}/{fn}")
    plt.clf()

def main():
    happiness = convert_index(pool(map_csv("../data/csv/cantril-ladder.csv", 0, 2, 3)))
    phones = convert_index(pool(map_csv("../data/csv/cell-phones.csv", 0, 1, 2)))
    internet = convert_index(pool(map_csv("../data/csv/internet-users.csv", 0, 1, 2)))


    for x in list(happiness.keys()):
        save_box(happiness[x], f"{x} Cantril Ladder Data", "../data/images/boxplots/happiness", x)

    for x in list(phones.keys()):
       save_box(phones[x], f"{x.upper()} Number of Cell Phones Possessed Per 100 People", "../data/images/boxplots/phones")

    for x in list(internet.keys()):
       save_box(internet[x], f"{x.upper()} Proportion of Internet Users", "../data/images/boxplots/internet")

if (__name__ == "__main__"):
    exec(open("./include.py").read())
    main()
