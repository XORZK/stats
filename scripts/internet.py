#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import pandas as pd

class Index:
    def __init__(self, year: int, happiness: float):
        self.year = year
        self.happiness = happiness

    def __str__(self):
        return f"{self.year}: {self.happiness}"

def get_map(f: pd.core.frame.DataFrame) -> map:
    count = 0
    data = {}

    for i in range(0, len(f)):
        row, country = f.loc[i], f.loc[i][0]
        internet = row[2]

        if (math.isnan(internet)): continue

        index = Index(row[1], internet)

        if (not country in data.keys()):
            data[country] = [index]
        else:
            data[country].append(index)

    return data

def plot(happiness: list):
    x, y = [], []

    for i in happiness:
        x.append(i.year)
        y.append(i.happiness)

    plt.plot(x, y)


def parse_xls(fn: str):
    f = pd.read_csv(fn)
    data = get_map(f)


    #for x in list(data.keys()):
        #plot(data[x])

    plot(data["fin"])

    plt.show()

def main():
    parse_xls("../data/internet_users.csv")

if (__name__ == "__main__"):
    main()
