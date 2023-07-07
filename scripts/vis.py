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

def merged_boxplot(values: map, title = "", xlabel = "", ylabel = ""):
    plot_data, positions, labels = [], [], []
    for i in range(len(list(values.keys()))):
        x = list(values.keys())[i]
        if (x == "pooled"): continue
        plot_data.append(values[x])
        positions.append(100/len(list(values.keys())) * i)
        labels.append(x)

    plt.figure(figsize=(100,6))
    plt.boxplot(plot_data, labels=labels)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

def hist(values: list, title = "", dir = "", density = False):
    plt.title(title)
    plt.hist(values, bins=15, density=density)
    fn = title.replace(" ", "-").lower()
    plt.savefig(f"{dir}/{fn}")
    plt.clf()

def save_box(values: list, title = "", dir = "", lb = ""):
    plt.title(title)
    plt.boxplot(values, labels=[lb])
    fn = title.replace(" ", "-").lower()
    plt.savefig(f"{dir}/{fn}")
    plt.clf()

def yr_map(mapped: map):
    year = {}
    for i in range(len(mapped["pooled"])):
        yr = mapped["pooled"][i].year
        if (not yr in year.keys()):
            year[yr] = [mapped["pooled"][i]]
        else:
            year[yr].append(mapped["pooled"][i])

    return year

def main():
    happiness = pool(map_csv("../data/csv/cantril-ladder.csv", 0, 2, 3))
    phones = pool(map_csv("../data/csv/cell-phones.csv", 0, 1, 2))
    internet = pool(map_csv("../data/csv/internet-users.csv", 0, 1, 2))

    yr = convert_index(yr_map(happiness))

    merged_boxplot(yr, "Reported Life Satisfaction by Year", "Year", "Reported Life Satisfaction")

    plt.show()


    #merged_boxplot(happiness)

    #plt.show()

    #hist(happiness["pooled"], "Pooled Cantril Ladder Data", "../data/images/hist", False)
    #hist(happiness["pooled"], "Relative Pooled Cantril Ladder Data", "../data/images/hist", True)

    #hist(phones["pooled"], "Pooled Cell Phone Possession Data", "../data/images/hist", False)
    #hist(phones["pooled"], "Relative Pooled Cell Possession Data", "../data/images/hist", True)

    #hist(internet["pooled"], "Pooled Internet Usage Data", "../data/images/hist", False)
    #hist(internet["pooled"], "Relative Pooled Internet Usage Data", "../data/images/hist", True)

    #for x in list(happiness.keys()):
    #    save_box(happiness[x], f"{x} Cantril Ladder Data", "../data/images/boxplots/happiness", x)

    #for x in list(phones.keys()):
    #   save_box(phones[x], f"{x.upper()} Number of Cell Phones Possessed Per 100 People", "../data/images/boxplots/phones")

    #for x in list(internet.keys()):
    #   save_box(internet[x], f"{x.upper()} Proportion of Internet Users", "../data/images/boxplots/internet")

if (__name__ == "__main__"):
    exec(open("./include.py").read())
    main()
