import telebot
from telebot import types
from buttons_functions import find_ticker_by_company_name, find_trailing_pe_by_ticker,\
    exchange_rate,find_forward_pe_by_ticker, find_open_quote_by_ticker, \
    find_close_quote_by_ticker, find_trailing_twelve_month_EPS, find_forward_EPS, \
    find_current_year_EPS, find_next_year_quarter_EPS, find_latest_news

bot = telebot.TeleBot("1628495390:AAGK-Pyl_o6447HB149_9D666exXRiFkWow")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    stonks = open(r'C:\Users\sereb\Documents\stonks.jpg', 'rb')
    user_id = message.chat.id
    bot.send_photo(user_id, stonks)


@bot.message_handler(commands=[''])
def get_start_keyboard(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1
    btn_price_quotation = types.InlineKeyboardButton(text="Price Quotation", callback_data="priceQuotation")
    btn_exchange_rates = types.InlineKeyboardButton(text="Exchange Rates", callback_data="exchangeRates")
    btn_PE = types.InlineKeyboardButton(text="P/E", callback_data="PE")
    btn_EPS = types.InlineKeyboardButton(text="EPS", callback_data="EPS")
    btn_ticker_symbol_finder = types.InlineKeyboardButton(text="Ticker Symbol finder",
                                                          callback_data="tickerSymbolFinder")
    btn_my_stoks = types.InlineKeyboardButton(text="My Stocks", callback_data="myStocks")
    btn_history_of_changes = types.InlineKeyboardButton(text="History Of Changes", callback_data="historyOfChanges")
    btn_general_news = types.InlineKeyboardButton(text="General News", callback_data="generalNews")
    btn_analytics = types.InlineKeyboardButton(text="Analytics", callback_data="analytics")
    keyboard.add(btn_price_quotation, btn_exchange_rates, btn_PE, btn_EPS, btn_ticker_symbol_finder, btn_my_stoks,
                 btn_history_of_changes, btn_general_news, btn_analytics)
    bot.send_message(message.chat.id, "What are you interested in?", reply_markup=keyboard)

    names = {"stonks": "st"}


def get_cancel_keyboard():
    cb_btn_cancel = types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
    cancel_keyboard = types.InlineKeyboardMarkup()
    cancel_keyboard.add(cb_btn_cancel)
    return cancel_keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_button_menu(call):
    user_id = call.message.chat.id

    if call.data == 'PE':
        keyboard_PE = types.InlineKeyboardMarkup()
        keyboard_PE.row_width = 1
        btn_forward_PE = types.InlineKeyboardButton(text="Forward PE", callback_data="forward_PE")
        btn_trailing_PE = types.InlineKeyboardButton(text="Trailing PE", callback_data="trailing_PE")
        keyboard_PE.add(btn_forward_PE, btn_trailing_PE)

        bot.send_message(user_id, "What are you interested in?", reply_markup=keyboard_PE)

    elif call.data == "forward_PE":
        msg = bot.send_message(user_id, "To get PE rate,enter company ticker:")
        bot.register_next_step_handler(msg, forward_pe_handler)

    elif call.data == "trailing_PE":
        msg = bot.send_message(user_id, "To get PE rate,enter company ticker:")
        bot.register_next_step_handler(msg, trailing_pe_handler)

    elif call.data == 'tickerSymbolFinder':
        msg = bot.send_message(user_id, "To get ticker,enter company name:")
        bot.register_next_step_handler(msg, ticker_symbol_finder_handler)

    elif call.data == 'exchangeRates':
        msg = bot.send_message(user_id, "To get exchange rate,enter 'from' currency :")
        # msg2 = bot.send_message(user_id, "To get exchange rate,enter 'to' currency :")
        bot.register_next_step_handler(msg, exchange_rate_handler)

    elif call.data == 'priceQuotation':
        keyboard_quotes = types.InlineKeyboardMarkup()
        keyboard_quotes.row_width = 1
        btn_open_quote = types.InlineKeyboardButton(text="Open", callback_data="open_quote")
        btn_close_quote = types.InlineKeyboardButton(text="Close", callback_data="close_quote")
        keyboard_quotes.add(btn_open_quote, btn_close_quote)

        bot.send_message(user_id, "What are you interested in?", reply_markup=keyboard_quotes)

    elif call.data == 'open_quote':
        msg = bot.send_message(user_id, "To get quotation, enter company ticker:")
        bot.register_next_step_handler(msg, open_quote_handler)

    elif call.data == 'close_quote':
        msg = bot.send_message(user_id, "To get quotation, enter company ticker:")
        bot.register_next_step_handler(msg, close_quote_handler)

    elif call.data == 'EPS':
        keyboard_EPS = types.InlineKeyboardMarkup()
        keyboard_EPS.row_width = 1
        btn_trailing_twelve_months_EPS = types.InlineKeyboardButton(text="Trailing Twelwe Months EPS", callback_data="trailing_twelve_month_EPS")
        btn_forward_EPS = types.InlineKeyboardButton(text="Forward EPS", callback_data="forward_EPS")
        btn_current_year_EPS = types.InlineKeyboardButton(text="Current year EPS", callback_data="current_year_EPS")
        btn_next_quarter_EPS = types.InlineKeyboardButton(text="Next year quarter EPS", callback_data="next_year_quarter_EPS")
        btn_cancel = types.InlineKeyboardButton(text="Cancel", callback_data="cancel")
        keyboard_EPS.add(btn_trailing_twelve_months_EPS, btn_forward_EPS, btn_current_year_EPS, btn_next_quarter_EPS, btn_cancel)

        bot.send_message(user_id, "What are you interested in?", reply_markup=keyboard_EPS)

    elif call.data == "trailing_twelve_month_EPS":
        msg = bot.send_message(user_id, "To get EPS, enter company ticker:")
        bot.register_next_step_handler(msg, trailing_twelve_month_EPS_handler)

    elif call.data == "forward_EPS":
        msg = bot.send_message(user_id, "To get EPS, enter company ticker:")
        bot.register_next_step_handler(msg, forward_EPS_handler)

    elif call.data == "current_year_EPS":
        msg = bot.send_message(user_id, "To get EPS, enter company ticker:")
        bot.register_next_step_handler(msg, current_year_EPS_handler)

    elif call.data == "next_year_quarter_EPS":
        msg = bot.send_message(user_id, "To get EPS, enter company ticker:")
        bot.register_next_step_handler(msg, next_year_quarter_EPS_handler)

    elif call.data == "generalNews":
        news_list = find_latest_news(3)

        bot.send_message(user_id, 'Latest news:', parse_mode = 'Markdown')

        for news in news_list:
            title = news['title'].strip()
            summary = news['summary'].strip()
            link = news['link'].strip()

            message = ''
            message += '*' + title + '*' + '\n\n'
            message += summary

            keyboard_news = types.InlineKeyboardMarkup()
            keyboard_news.row_width = 1
            url_button = types.InlineKeyboardButton(text="Link", url=link)
            keyboard_news.add(url_button)
            bot.send_message(user_id, message, parse_mode='Markdown', reply_markup=keyboard_news)


    # elif call.data == "cancel":
    #     bot.send_message(chat_id=user_id, text="Отмена", reply_markup=types.ReplyKeyboardRemove(),
    #                      parse_mode='HTML', disable_web_page_preview=True)
    #     bot.send_message(chat_id=user_id, text="What are you interested in?",
    #                      reply_markup=get_start_keyboard())


def trailing_pe_handler(msg):
    user_id = msg.chat.id
    ticker = msg.text

    trailing_pe = find_trailing_pe_by_ticker(ticker)
    bot.send_message(user_id, "Trailing PE:")
    bot.send_message(user_id, trailing_pe)


def forward_pe_handler(msg):
    user_id = msg.chat.id
    ticker = msg.text

    forward_pe = find_forward_pe_by_ticker(ticker)
    bot.send_message(user_id, "Forward PE:")
    bot.send_message(user_id, forward_pe)


def ticker_symbol_finder_handler(msg):
    user_id = msg.chat.id
    company_name = msg.text

    ticker = find_ticker_by_company_name(company_name)

    bot.send_message(user_id, ticker)


def exchange_rate_handler(msg):

    user_id = msg.chat.id
    # user_id2 = msg2.chat.id

    input_string = msg.text
    subject = input_string.split(',')

    from_curr = subject[0]
    to_curr = subject[1]
    quantity = subject[2]
    # bot.send_message(user_id, from_curr)
    # bot.send_message(user_id, to_curr)
    # bot.send_message(user_id, quantity)

    ex_rate = exchange_rate(from_curr, to_curr, quantity)

    bot.send_message(user_id, ex_rate)


def open_quote_handler(msg):
    user_id = msg.chat.id

    ticker = msg.text

    quote = find_open_quote_by_ticker(ticker)
    bot.send_message(user_id, "Open quote:")
    bot.send_message(user_id, quote)


def close_quote_handler(msg):
    user_id = msg.chat.id

    ticker = msg.text

    quote = find_close_quote_by_ticker(ticker)
    bot.send_message(user_id, "Close quote:")
    bot.send_message(user_id, quote)


def trailing_twelve_month_EPS_handler(msg):
    user_id = msg.chat.id

    ticker = msg.text

    eps = find_trailing_twelve_month_EPS(ticker)
    bot.send_message(user_id, "Trailing twelve month EPS:")
    bot.send_message(user_id, eps)


def forward_EPS_handler(msg):
    user_id = msg.chat.id

    ticker = msg.text

    eps = find_forward_EPS(ticker)
    bot.send_message(user_id, "Forward EPS:")
    bot.send_message(user_id, eps)


def current_year_EPS_handler(msg):
    user_id = msg.chat.id

    ticker = msg.text

    eps = find_current_year_EPS(ticker)
    bot.send_message(user_id, "Current year EPS:")
    bot.send_message(user_id, eps)


def next_year_quarter_EPS_handler(msg):
    user_id = msg.chat.id

    ticker = msg.text

    eps = find_next_year_quarter_EPS(ticker)
    bot.send_message(user_id, "Next year quarter EPS:")
    bot.send_message(user_id, eps)


bot.polling()
