#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Computes:
# Mean
# Range
# IQR
# Variance
# Standard Deviation

# Computes the standard deviation for a sample (n-1)
def sd(values: list) -> float:
    s, m = 0.0, sum(values)/len(values)

    for i in range(len(values)):
        s += pow(m - values[i], 2)

    s /= (len(values)-1)

    return math.sqrt(s)

def data(values: list) -> map:
    m = {}

    m["count"] = len(values)
    m["mean"] = sum(values)/len(values)
    m["sum"] = sum(values)
    m["range"] = (max(values) - min(values))
    m["sd"] = sd(values)
    m["variance"] = pow(sd(values), 2)

    return m

def main():
    happiness = convert_index(pool(map_csv("../data/csv/cantril-ladder.csv", 0, 2, 3)))
    phones = convert_index(pool(map_csv("../data/csv/cell-phones.csv", 0, 1, 2)))
    internet = convert_index(pool(map_csv("../data/csv/internet-users.csv", 0, 1, 2)))

    l = [10, 12, 23, 23, 16, 23, 21, 16]

    print(data(l))

if (__name__ == "__main__"):
    exec(open("./include.py").read())
    main()
