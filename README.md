# Volume Getting

## Aim

The aim of this project is to display the evolution of the volume of the 500 actual best cryptocurrency (classment done by market cap) over time since 3 years.

It will create a graph displaying the volume over time.

## How does it work

It do calls to the coingecko API in order to get the best crypto and their volume over time: [https://www.coingecko.com/en/api](https://www.coingecko.com/en/api)

## How to use

#### Create a virtual env (optional)

> pip -m venv venv
> source venv/bin/activate

#### Install the requirements

> pip install -r requirements.txt

#### Run the program

> python main.py

To get the list of possible arguments:

> python main.py -h

##### Get the resulting image

The resulting image is inside of the file "volumes.png"
