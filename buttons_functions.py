import json
import requests
from time import sleep


def find_ticker_by_company_name(company_name):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

    querystring = {"q": company_name, "region": "US"}

    headers = {
        'x-rapidapi-key': "ffa9678c02msh1d10b4987f061e7p1aba90jsn2cb8e8bb14fa",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = None
    while response is None:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except:
            print("Сервак прилег нахуй")
            sleep(1)
            continue

    try:
        return json.loads(response.text)['quotes'][0]['symbol']
    except:
        return "Not found"


def find_trailing_pe_by_ticker(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region": "US", "symbols": ticker}

    headers = {
        'x-rapidapi-key': "ffa9678c02msh1d10b4987f061e7p1aba90jsn2cb8e8bb14fa",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = None
    while response is None:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except:
            print("Сервак прилег нахуй")
            sleep(1)
            continue

    try:
        return json.loads(response.text)['quoteResponse']['result'][0]['trailingPE']
    except:
        return "Not found"


def find_forward_pe_by_ticker(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region": "US", "symbols": ticker}

    headers = {
        'x-rapidapi-key': "ffa9678c02msh1d10b4987f061e7p1aba90jsn2cb8e8bb14fa",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = None
    while response is None:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except:
            print("Сервак прилег нахуй")
            sleep(1)
            continue

    try:
        return json.loads(response.text)['quoteResponse']['result'][0]['forwardPE']
    except:
        return "Not found"


def exchange_rate(from_curr, to_curr, quantity):
    url = "https://currency-converter5.p.rapidapi.com/currency/convert"

    querystring = {"format": "json", "from": from_curr, "to": to_curr, "amount": quantity}

    headers = {
    'x-rapidapi-key': "25d1663882mshfedc1904a9d09ecp13065djsnfda0904af45e",
    'x-rapidapi-host': "currency-converter5.p.rapidapi.com"
    }

    response = None
    while response is None:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except:
            print("Сервак прилег нахуй")
            sleep(1)
            continue
    try:
        return json.loads(response.text)['rates'][to_curr]['rate_for_amount']
    except:
        return "Not found"


def find_open_quote_by_ticker(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region": "US", "symbols": ticker}

    headers = {
        'x-rapidapi-key': "ffa9678c02msh1d10b4987f061e7p1aba90jsn2cb8e8bb14fa",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = None
    while response is None:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except:
            print("Сервак прилег нахуй")
            sleep(1)
            continue

    try:
        return json.loads(response.text)['quoteResponse']['result'][0]['regularMarketOpen']
    except:
        return "Not found"


def find_close_quote_by_ticker(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region": "US", "symbols": ticker}

    headers = {
        'x-rapidapi-key': "ffa9678c02msh1d10b4987f061e7p1aba90jsn2cb8e8bb14fa",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = None
    while response is None:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except:
            print("Сервак прилег нахуй")
            sleep(1)
            continue

    try:
        return json.loads(response.text)['quoteResponse']['result'][0]['regularMarketPreviousClose']
    except:
        return "Not found"


def find_trailing_twelve_month_EPS(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region": "US", "symbols": ticker}

    headers = {
        'x-rapidapi-key': "ffa9678c02msh1d10b4987f061e7p1aba90jsn2cb8e8bb14fa",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = None
    while response is None:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except:
            print("Сервак прилег нахуй")
            sleep(1)
            continue

    try:
        return json.loads(response.text)['quoteResponse']['result'][0]['epsTrailingTwelveMonths']
    except:
        return "Not found"


def find_forward_EPS(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region": "US", "symbols": ticker}

    headers = {
        'x-rapidapi-key': "ffa9678c02msh1d10b4987f061e7p1aba90jsn2cb8e8bb14fa",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = None
    while response is None:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except:
            print("Сервак прилег нахуй")
            sleep(1)
            continue

    try:
        return json.loads(response.text)['quoteResponse']['result'][0]['epsForward']
    except:
        return "Not found"


def find_current_year_EPS(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region": "US", "symbols": ticker}

    headers = {
        'x-rapidapi-key': "ffa9678c02msh1d10b4987f061e7p1aba90jsn2cb8e8bb14fa",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = None
    while response is None:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except:
            print("Сервак прилег нахуй")
            sleep(1)
            continue

    try:
        return json.loads(response.text)['quoteResponse']['result'][0]['epsCurrentYear']
    except:
        return "Not found"


def find_next_year_quarter_EPS(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region": "US", "symbols": ticker}

    headers = {
        'x-rapidapi-key': "ffa9678c02msh1d10b4987f061e7p1aba90jsn2cb8e8bb14fa",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = None
    while response is None:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except:
            print("Сервак прилег нахуй")
            sleep(1)
            continue

    try:
        return json.loads(response.text)['quoteResponse']['result'][0]['epsNextQuarter']
    except:
        return "Not found"


def find_latest_news(n_news):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/list"

    querystring = {"category":"generalnews","region":"US"}

    headers = {
        'x-rapidapi-key': "ffa9678c02msh1d10b4987f061e7p1aba90jsn2cb8e8bb14fa",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    response = None
    while response is None:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except:
            print("Сервак прилег нахуй")
            sleep(1)
            continue

    try:
        return json.loads(response.text)['items']['result'][:n_news]
    except:
        return "Not found"
