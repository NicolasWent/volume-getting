from data_computing import compute_data
from data_getting import get_data
from display_data import display_data


def main():
    data = get_data(1000)
    data = compute_data(data)
    display_data(data)


if __name__ == "__main__":
    main()
