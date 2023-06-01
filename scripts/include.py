#!/usr/bin/env python3

class Index:
    def __init__(self, year: int, value: float):
        self.year = year
        self.value = value
    def __str__(self):
        return f"{self.year}: {self.value}"

def convert_index(mapped: map) -> map:
    values = {}
    for x in list(mapped.keys()):
        values[x] = []
        for val in mapped[x]:
            values[x].append(val.value)
        values[x].sort()
    return values

def pool(mapped: map) -> map:
    mapped["pooled"] = []
    for x in list(mapped.keys()):
        if (x == "pooled"): continue
        mapped["pooled"].extend(mapped[x])
    return mapped

def plot(values: list):
    x, y = [], []

    for i in values:
        x.append(i.year)
        y.append(i.value)

    plt.plot(x,y)

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

def map_csv(fn: str, c_index: int, y_index: int, v_index: int) -> map:
    f = pd.read_csv(fn)
    mapped = get_map(f, c_index, y_index, v_index)

    return mapped


def plot_csv(fn: str, c_index: int, y_index: int, v_index: int):
    mapped = map_csv(f, c_index, y_index, v_index)

    for x in list(mapped.keys()):
        plot(mapped[x])

    plt.show()

def save_fig(values: list, title = "", dir = ""):
    plt.title(title)
    plot(values)
    fn = title.replace(" ", "-").lower()
    plt.savefig(f"{dir}/{fn}")
    plt.clf()

def plot_map(mapped: map, title = ""):
    plt.title(title)
    for x in mapped.keys():
        plot(mapped[x])
