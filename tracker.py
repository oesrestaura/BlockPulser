import requests
from config import ETHERSCAN_API_KEY, BASE_URL


def get_transactions(address):
    """
    Fetch transactions for a given wallet address
    """
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": ETHERSCAN_API_KEY,
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["status"] != "1":
        return []

    return data["result"]
