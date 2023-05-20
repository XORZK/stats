#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import pandas as pd

# Predicted => 2.778 + 0.013*[GDP^0.093*SS^1.158*HLE^0.999*FREE^0.506*GEN^0.037*PER^0.020]

class Index:
    def __init__(self, year: int, happiness: float):
        self.year = year
        self.happiness = happiness

    def __str__(self):
        return f"{self.year}: {self.happiness}"

def predicted_index(gdp: float, ss: float, hle: float, free: float):
    x = (gdp**0.093)*(ss*1.158)*(hle*0.999)*(free**0.506)
    return 2.297 + 0.01*x

def predicted_index(stats: list):
    x = (stats[0]**0.093)*(stats[1]*1.158)*(stats[2]*0.999)*(stats[3]**0.506)
    return 2.297 + 0.01*x

def get_map(f: pd.core.frame.DataFrame) -> map:
    count = 0
    happiness_index = {}

    for i in range(0, len(f)):
        row, country = f.loc[i], f.loc[i][0]
        cantrill = row[3]

        if (math.isnan(cantrill)): continue

        index = Index(row[2], cantrill)

        if (not country in happiness_index.keys()):
            happiness_index[country] = [index]
        else:
            happiness_index[country].append(index)

    return happiness_index

def plot(happiness: list):
    x, y = [], []

    for i in happiness:
        x.append(i.year)
        y.append(i.happiness)

    print(x, y)

    plt.plot(x, y)

def parse_xls(fn: str):
    f = pd.read_csv(fn)
    happiness_index = get_map(f)


    for x in list(happiness_index.keys()):
        plot(happiness_index[x])
    plt.show()

def main():
    parse_xls("../data/cantril-ladder.csv")

if (__name__ == "__main__"):
    main()
