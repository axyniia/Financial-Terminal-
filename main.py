import telebot
from telebot import types
from buttons_functions import find_ticker_by_company_name, find_trailing_pe_by_ticker,\
    exchange_rate, find_forward_pe_by_ticker, find_open_quote_by_ticker, \
    find_close_quote_by_ticker, find_trailing_twelve_month_EPS, find_forward_EPS, \
    find_current_year_EPS, find_next_year_quarter_EPS, find_latest_news, find_company_info, \
    predictor_short_term, predictor_mid_term, predictor_long_term, graph

bot = telebot.TeleBot("1628495390:AAGK-Pyl_o6447HB149_9D666exXRiFkWow")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_id = message.chat.id
    stonks = open('/Users/liaomarova/Desktop/stonks.jpeg', 'rb')
    user_id = message.chat.id
    bot.send_photo(user_id, stonks)
    keyboard_start = types.InlineKeyboardMarkup()
    callback_button_start = types.InlineKeyboardButton(text="Start", callback_data="start")
    keyboard_start.add(callback_button_start)
    bot.send_message(message.chat.id, text="Hello, I am your financial terminal", reply_markup=keyboard_start)

def get_start_keyboard():
    btn_price_quotation = types.InlineKeyboardButton(text="Price Quotation", callback_data="priceQuotation")
    btn_exchange_rates = types.InlineKeyboardButton(text="Exchange Rates", callback_data="exchangeRates")
    btn_PE = types.InlineKeyboardButton(text="P/E", callback_data="PE")
    btn_EPS = types.InlineKeyboardButton(text="EPS", callback_data="EPS")
    btn_ticker_symbol_finder = types.InlineKeyboardButton(text="Ticker Symbol finder",
                                                          callback_data="tickerSymbolFinder")
    btn_general_news = types.InlineKeyboardButton(text="General News", callback_data="generalNews")
    btn_company_info = types.InlineKeyboardButton(text="Company info", callback_data="company_info")
    btn_predictor = types.InlineKeyboardButton(text="Predictor", callback_data="predictor")
    btn_graph = types.InlineKeyboardButton(text="Graph", callback_data="graph")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1
    keyboard.add(btn_price_quotation, btn_exchange_rates, btn_PE, btn_EPS, btn_ticker_symbol_finder,
                 btn_general_news, btn_company_info, btn_predictor, btn_graph)
    return keyboard
pass

def get_return_keyboard():
    cb_btn_return = types.InlineKeyboardButton(callback_data="Return to the menu")
    return_keyboard = types.InlineKeyboardMarkup()
    return_keyboard.add(cb_btn_return)
    return return_keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_button_menu(call):
    user_id = call.message.chat.id

    if call.data == "start":
        bot.send_message(chat_id=user_id, text="What are you interested in?", reply_markup=get_start_keyboard(), )
    elif call.data == 'PE':
        keyboard_PE = types.InlineKeyboardMarkup()
        keyboard_PE.row_width = 1
        btn_forward_PE = types.InlineKeyboardButton(text="Forward PE", callback_data="forward_PE")
        btn_trailing_PE = types.InlineKeyboardButton(text="Trailing PE", callback_data="trailing_PE")
        btn_return = types.InlineKeyboardButton(text="Return to the menu", callback_data="return")
        keyboard_PE.add(btn_forward_PE, btn_trailing_PE, btn_return)

        bot.send_message(user_id, "What are you interested in?", reply_markup=keyboard_PE)

    elif call.data == "forward_PE":
        msg = bot.send_message(user_id, "To get forward PE rate,enter company ticker:")
        bot.register_next_step_handler(msg, forward_pe_handler)

    elif call.data == "trailing_PE":
        msg = bot.send_message(user_id, "To get trailing PE rate,enter company ticker:")
        bot.register_next_step_handler(msg, trailing_pe_handler)

    elif call.data == 'tickerSymbolFinder':
        msg = bot.send_message(user_id, "To get ticker,enter company name:")
        keyboard_ticker_finder = types.InlineKeyboardMarkup()
        keyboard_ticker_finder.row_width = 1
        btn_return = types.InlineKeyboardButton(text="Return to the menu", callback_data="return")
        keyboard_ticker_finder.add(btn_return)
        bot.register_next_step_handler(msg, ticker_symbol_finder_handler)

    elif call.data == 'exchangeRates':
        msg = bot.send_message(user_id, "To get exchange rate, enter 'from' currency, 'to' currency, "
                                        "amount. Example: RUB,USD,6")
        keyboard_exchange_rate = types.InlineKeyboardMarkup()
        keyboard_exchange_rate.row_width = 1
        btn_return = types.InlineKeyboardButton(text="Return to the menu", callback_data="return")
        keyboard_exchange_rate.add(btn_return)
        bot.register_next_step_handler(msg, exchange_rate_handler)

    elif call.data == 'priceQuotation':
        keyboard_quotes = types.InlineKeyboardMarkup()
        keyboard_quotes.row_width = 1
        btn_open_quote = types.InlineKeyboardButton(text="Open quotation", callback_data="open_quote")
        btn_close_quote = types.InlineKeyboardButton(text="Close quotation", callback_data="close_quote")
        btn_return = types.InlineKeyboardButton(text="Return to the menu", callback_data="return")
        keyboard_quotes.add(btn_open_quote, btn_close_quote, btn_return)
        bot.send_message(user_id, "What are you interested in?", reply_markup=keyboard_quotes)

    elif call.data == 'open_quote':
        msg = bot.send_message(user_id, "To get open quotation, enter company ticker:")
        bot.register_next_step_handler(msg, open_quote_handler)

    elif call.data == 'close_quote':
        msg = bot.send_message(user_id, "To get close quotation, enter company ticker:")
        bot.register_next_step_handler(msg, close_quote_handler)

    elif call.data == 'EPS':
        keyboard_EPS = types.InlineKeyboardMarkup()
        keyboard_EPS.row_width = 1
        btn_trailing_twelve_months_EPS = types.InlineKeyboardButton(text="Trailing Twelwe Months EPS", callback_data="trailing_twelve_month_EPS")
        btn_forward_EPS = types.InlineKeyboardButton(text="Forward EPS", callback_data="forward_EPS")
        btn_current_year_EPS = types.InlineKeyboardButton(text="Current year EPS", callback_data="current_year_EPS")
        btn_next_quarter_EPS = types.InlineKeyboardButton(text="Next year quarter EPS", callback_data="next_year_quarter_EPS")
        btn_return = types.InlineKeyboardButton(text="Return to the menu", callback_data="return")
        keyboard_EPS.add(btn_trailing_twelve_months_EPS, btn_forward_EPS, btn_current_year_EPS, btn_next_quarter_EPS, btn_return)
        bot.send_message(user_id, "What are you interested in?", reply_markup=keyboard_EPS)

    elif call.data == "trailing_twelve_month_EPS":
        msg = bot.send_message(user_id, "To get trailing twelve month EPS, enter company ticker:")
        bot.register_next_step_handler(msg, trailing_twelve_month_EPS_handler)

    elif call.data == "forward_EPS":
        msg = bot.send_message(user_id, "To get forward EPS, enter company ticker:")
        bot.register_next_step_handler(msg, forward_EPS_handler)

    elif call.data == "current_year_EPS":
        msg = bot.send_message(user_id, "To get current year EPS, enter company ticker:")
        bot.register_next_step_handler(msg, current_year_EPS_handler)

    elif call.data == "next_year_quarter_EPS":
        msg = bot.send_message(user_id, "To get next quarter EPS, enter company ticker:")
        bot.register_next_step_handler(msg, next_year_quarter_EPS_handler)

    elif call.data == "generalNews":
        msg = bot.send_message(user_id, "Enter the number of news you are interested in")
        bot.register_next_step_handler(msg, news_handler)


    elif call.data == "graph":
        msg = bot.send_message(user_id, "To get graph, enter company ticker:")
        bot.register_next_step_handler(msg, graph_handler)

    elif call.data == "return":
        bot.send_message(chat_id=user_id, text="Returning to the menu", reply_markup=types.ReplyKeyboardRemove(),
                         parse_mode='HTML', disable_web_page_preview=True)
        bot.send_message(chat_id=user_id, text="What are you interested in?",
                         reply_markup=get_start_keyboard())

    elif call.data == "company_info":
        msg = bot.send_message(user_id, "To get company info, enter company ticker:")
        bot.register_next_step_handler(msg, company_info_handler)

    elif call.data == "predictor":
        keyboard_predictor = types.InlineKeyboardMarkup()
        keyboard_predictor.row_width = 1
        btn_short_term = types.InlineKeyboardButton(text="Short Term", callback_data="short_term_predictor")
        btn_mid_term = types.InlineKeyboardButton(text="Mid Term", callback_data="mid_term_predictor")
        btn_long_term = types.InlineKeyboardButton(text="Long Term", callback_data="long_term_predictor")
        btn_return = types.InlineKeyboardButton(text="Return to the menu", callback_data="return")
        keyboard_predictor.add(btn_short_term, btn_mid_term, btn_long_term, btn_return)
        bot.send_message(chat_id=user_id, text="What are you interested in?", reply_markup=keyboard_predictor)

    elif call.data == "short_term_predictor":
        msg = bot.send_message(user_id, "To get prediction in short term, enter company ticker:")
        bot.register_next_step_handler(msg, predictor_short_term_handler)

    elif call.data == "mid_term_predictor":
        msg = bot.send_message(user_id, "To get prediction in mid term, enter company ticker:")
        bot.register_next_step_handler(msg, predictor_mid_term_handler)

    elif call.data == "long_term_predictor":
        msg = bot.send_message(user_id, "To get prediction in long term, enter company ticker:")
        bot.register_next_step_handler(msg, predictor_long_term_handler)

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

    keyboard_ticker_finder = types.InlineKeyboardMarkup()
    keyboard_ticker_finder.row_width = 1
    btn_return = types.InlineKeyboardButton(text="Return to the menu", callback_data="return")
    keyboard_ticker_finder.add(btn_return)
    bot.send_message(user_id, text="Return to the menu", reply_markup=keyboard_ticker_finder)


def exchange_rate_handler(msg):

    user_id = msg.chat.id
    # user_id2 = msg2.chat.id

    input_string = msg.text
    subject = input_string.split(',')

    from_curr = subject[0]
    to_curr = subject[1]
    quantity = subject[2]

    ex_rate = exchange_rate(from_curr, to_curr, quantity)
    bot.send_message(user_id, "Here is the exchange rate")
    bot.send_message(user_id, ex_rate)

    keyboard_exchange_rate = types.InlineKeyboardMarkup()
    keyboard_exchange_rate.row_width = 1
    btn_return = types.InlineKeyboardButton(text="Return to the menu", callback_data="return")
    keyboard_exchange_rate.add(btn_return)
    bot.send_message(user_id, text="Return to the menu", reply_markup=keyboard_exchange_rate)


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


def graph_handler(msg):
    user_id = msg.chat.id

    ticker = msg.text

    result = graph(ticker)
    bot.send_message(user_id, result)


def company_info_handler(msg):
    user_id = msg.chat.id
    company_name = msg.text

    ticker = find_company_info(company_name)
    bot.send_message(user_id, ticker)

    keyboard_company_info = types.InlineKeyboardMarkup()
    keyboard_company_info.row_width = 1
    btn_return = types.InlineKeyboardButton(text="Return to the menu", callback_data="return")
    keyboard_company_info.add(btn_return)
    bot.send_message(user_id, text="Return to the menu", reply_markup=keyboard_company_info)


def predictor_short_term_handler(msg):
    user_id = msg.chat.id
    company_name = msg.text

    ticker = predictor_short_term(company_name)
    bot.send_message(user_id, "Here is the prediction in short term")
    bot.send_message(user_id, ticker)

def predictor_mid_term_handler(msg):
    user_id = msg.chat.id
    company_name = msg.text

    ticker = predictor_mid_term(company_name)
    bot.send_message(user_id, "Here is the prediction in mid term")
    bot.send_message(user_id, ticker)

def predictor_long_term_handler(msg):
    user_id = msg.chat.id
    company_name = msg.text

    ticker = predictor_long_term(company_name)
    bot.send_message(user_id, "Here is the prediction in long term")
    bot.send_message(user_id, ticker)

def news_handler(msg):
    user_id = msg.chat.id
    n = int(msg.text.strip())
    news_list = find_latest_news(n)
    bot.send_message(user_id, 'Latest news:', parse_mode='Markdown')

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



    keyboard_news1 = types.InlineKeyboardMarkup()
    keyboard_news1.row_width = 1
    btn_return = types.InlineKeyboardButton(text="Return to the menu", callback_data="return")
    keyboard_news1.add(btn_return)
    bot.send_message(user_id, "Tap to return", reply_markup=keyboard_news1)


bot.polling()

