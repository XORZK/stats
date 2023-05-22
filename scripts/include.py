#!/usr/bin/env python3

class Index:
    def __init__(self, year: int, value: float):
        self.year = year
        self.value = value
    def __str__(self):
        return f"{self.year}: {self.value}"

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
