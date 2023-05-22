#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

# Happiness: 0, 2, 3
# Phones: 0, 1, 2
# Internet: 0, 1, 2

def main():
    happiness = map_csv("../data/csv/cantril-ladder.csv", 0, 2, 3)
    phones = map_csv("../data/csv/cell-phones.csv", 0, 1, 2)
    internet = map_csv("../data/csv/internet-users.csv", 0, 1, 2)

    for x in list(happiness.keys()):
        save_fig(happiness[x], f"{x} Cantril Ladder Data", "../data/images/cantril")

    for x in list(phones.keys()):
        save_fig(phones[x], f"{x.upper()} Number of Cell Phones Possessed Per 100 People", "../data/images/phones")

    for x in list(internet.keys()):
        save_fig(internet[x], f"{x.upper()} Proportion of Internet Users", "../data/images/internet")

if (__name__ == "__main__"):
    exec(open("./include.py").read())
    main()
