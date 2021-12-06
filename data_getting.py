import time

from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def cg_call(method):
    while True:
        try:
            return method()
        except Exception:
            print("Sleep 70 seconds for API delays")
            time.sleep(70)


def _get_current_best_symbols(amount):
    """This method allow us to get the best coins from the api with the endpoint /coins/markets
    :param amount: The amount of best that you want to get
    :return: The list of bests coins
    """
    if amount <= 250:
        call = cg.get_coins_markets("usd", per_page=amount, order="market_cap_desc")
    else:
        call = []
        p = 1
        while amount > 0:
            to_add = cg_call(method=lambda: cg.get_coins_markets("usd", per_page=amount, page=p,
                                                                 order="market_cap_desc"))
            call += to_add
            amount -= 250
            p += 1

    return [e['id'] for e in call]


def get_data(amount: int) -> {str: {int: float}}:
    """This function get the volumes from the API

    :return: The volumes with this format:
    {
        "bitcoin":
        {
            timestamp: volume
        }
    }
    """
    coins = _get_current_best_symbols(10)
    ret = {}
    for c in coins:
        brute_data = cg_call(lambda: cg.get_coin_market_chart_by_id(c, "usd", "max")["total_volumes"])
        ret[c] = {d[0]: d[1] for d in brute_data}

    return ret
