import telebot
from telebot import types
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import unirest
from matplotlib import rcParams

bot = telebot.TeleBot("1628495390:AAGK-Pyl_o6447HB149_9D666exXRiFkWow")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_id = message.chat.id
    stonks = open('', 'rb')
    bot.send_photo(user_id, stonks)


@bot.message_handler(content_types=["text"])
def get_start_keyboard(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1
    btn_price_quotation = types.InlineKeyboardButton(text="Price Quotation", callback_data="priceQuotation")
    btn_exchange_rates = types.InlineKeyboardButton(text="Exchange Rates", callback_data="exchangeRates")
    btn_PE = types.InlineKeyboardButton(text="P/E", callback_data="PE")
    btn_ticker_symbol_finder = types.InlineKeyboardButton(text="Ticker Symbol finder",
                                                          callback_data="tickerSymbolFinder")
    btn_my_stoks = types.InlineKeyboardButton(text="My Stocks", callback_data="myStocks")
    btn_history_of_changes = types.InlineKeyboardButton(text="History Of Changes", callback_data="historyOfChanges")
    btn_general_news = types.InlineKeyboardButton(text="General News", callback_data="generalNews")
    btn_analytics = types.InlineKeyboardButton(text="Analytics", callback_data="analytics")
    btn_graphs = types.InlineKeyboardButton(text="Graphs", callback_data="graphs")
    keyboard.add(btn_price_quotation, btn_exchange_rates, btn_PE, btn_ticker_symbol_finder, btn_my_stoks,
                 btn_history_of_changes, btn_general_news, btn_analytics, btn_graphs)
    bot.send_message(message.chat.id, "What are you interested in?", reply_markup=keyboard)


names = {"stonks": "st"}


def send_stock_names(message):
    text = message.text
    user_id = message.chat.id
    answer = ""
    for name, shName in names.items():
        if name.strip() == text.strip():
            answer = shName
    bot.send_message(user_id, text=answer)
    pass



#here is our draft for outputing graphs, using API (draft)
unirest.timeout(15) # 5s timeout

RAPIDAPI_KEY  = "<YOUR_RAPIDAPI_KEY>"
RAPIDAPI_HOST = "<YOUR_RAPIDAPI_ENDPOINT>"

symbol_string = ""
inputdata = {}

def fetchStockData(symbol):

  response = unirest.get("https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts?region=US&lang=en&symbol=" + symbol + "&interval=1d&range=3mo",
    headers={
      "X-RapidAPI-Host": RAPIDAPI_HOST,
      "X-RapidAPI-Key": RAPIDAPI_KEY,
      "Content-Type": "application/json"
    }
  )

  if(response.code == 200):
    return response.body
  else:
    return None


def parseTimestamp(inputdata):

  timestamplist = []

  timestamplist.extend(inputdata["chart"]["result"][0]["timestamp"])
  timestamplist.extend(inputdata["chart"]["result"][0]["timestamp"])

  calendertime = []

  for ts in timestamplist:
    dt = datetime.fromtimestamp(ts)
    calendertime.append(dt.strftime("%m/%d/%Y"))

  return calendertime

def parseValues(inputdata):

  valueList = []
  valueList.extend(inputdata["chart"]["result"][0]["indicators"]["quote"][0]["open"])
  valueList.extend(inputdata["chart"]["result"][0]["indicators"]["quote"][0]["close"])

  return valueList


def attachEvents(inputdata):

  eventlist = []

  for i in range(0,len(inputdata["chart"]["result"][0]["timestamp"])):
    eventlist.append("open")

  for i in range(0,len(inputdata["chart"]["result"][0]["timestamp"])):
    eventlist.append("close")

  return eventlist


if __name__ == "__main__":

  try:

    while len(symbol_string) <= 2:
      symbol_string = raw_input("Enter the stock symbol: ")

    retdata = fetchStockData(symbol_string)



    if (None != inputdata):

      inputdata["Timestamp"] = parseTimestamp(retdata)

      inputdata["Values"] = parseValues(retdata)

      inputdata["Events"] = attachEvents(retdata)

      df = pd.DataFrame(inputdata)

      sns.set(style="darkgrid")

      rcParams['figure.figsize'] = 13,5
      rcParams['figure.subplot.bottom'] = 0.2


      ax = sns.lineplot(x="Timestamp", y="Values", hue="Events",dashes=False, markers=True,
                   data=df, sort=False)


      ax.set_title('Symbol: ' + symbol_string)

      plt.xticks(
          rotation=45,
          horizontalalignment='right',
          fontweight='light',
          fontsize='xx-small'
      )

      plt.show()

  except Exception as e:
    print "Error"
    print e



bot.polling()