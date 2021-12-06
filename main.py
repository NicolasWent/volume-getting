from data_getting import get_data
from display_data import display_data


def main():
    data = get_data()
    print(data)
    display_data(data)

if __name__ == "__main__":
    main()
