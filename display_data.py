from datetime import datetime

import time
import matplotlib.pyplot as plt


def to_datetime(to_convert: int) -> datetime:
    return datetime.fromtimestamp(to_convert / 1000.0)


def display_data(data, since, amount):
    timestamps = []
    volumes = []
    t_minus = int(time.time()) - 1000 * 3600 * 24 * 30 * 12 * since
    for t in data:
        if t > t_minus:
            timestamps.append(to_datetime(t))
            volumes.append(data[t])

    plt.figure(figsize=(24, 10))
    plt.plot(timestamps, volumes)
    plt.xlabel("Dates")
    plt.ylabel("Volumes in $")
    plt.title(f"Evolution of the volume of the {amount} best actual crypto over time")
    plt.grid(axis="y")
    plt.savefig("volumes.png")
