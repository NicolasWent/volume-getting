import argparse

from data_computing import compute_data
from data_getting import get_data
from display_data import display_data


def parse_arguments():
    parser = argparse.ArgumentParser(description="Get the evolution of the volume of the best actual cryptos")

    parser.add_argument("-a", "--amount", type=int, default=500, help="The amount of crypto that we should use")
    parser.add_argument("-s", '--since', type=int, default=3, help="From how much years should we get the data? "
                                                                   "default = 3")
    return parser.parse_args()


def main():
    args = parse_arguments()
    data = get_data(args.amount)
    data = compute_data(data)
    display_data(data, args.since, args.amount)


if __name__ == "__main__":
    main()
