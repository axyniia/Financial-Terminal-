import telebot
from telebot import types

bot = telebot.TeleBot("1628495390:AAGK-Pyl_o6447HB149_9D666exXRiFkWow")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    stonks = open('/Users/axyniia/Downloads/photo_2021-02-06 22.38.13.jpeg', 'rb')
    user_id = message.chat.id
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
    keyboard.add(btn_price_quotation, btn_exchange_rates, btn_PE, btn_ticker_symbol_finder, btn_my_stoks,
                 btn_history_of_changes, btn_general_news, btn_analytics)
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


bot.polling()