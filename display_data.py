from datetime import datetime

import matplotlib.pyplot as plt


def to_datetime(to_convert: int) -> datetime:
    return datetime.fromtimestamp(to_convert / 1000.0)


def display_data(data):
    timestamps = []
    volumes = []
    for t in data:
        if t > 1542408043594:
            timestamps.append(to_datetime(t))
            volumes.append(data[t])

    plt.figure(figsize=(24, 10))
    plt.plot(timestamps, volumes)
    plt.xlabel("Dates")
    plt.ylabel("Volumes")
    plt.title("Evolution of the volume of the 500 best actual crypto over time")
    plt.grid(axis="y")
    plt.savefig("volumes.png")
