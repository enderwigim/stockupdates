from stock import StockMachine
from news import NewsRelated
from telegrambot import TelegramMessage
from companies_data import companies
import os


def select_company():
    """"Ask the user for a company in the list and return the company's name and symbol"""
    print("Select a company")
    for company in companies:
        print(f"{company}. {companies[company]['symbol']} - {companies[company]['name']}")
    num = input("Choose by writing it's number: ")
    symbol = companies[num]['symbol']
    name = companies[num]['name']
    return symbol, name


# We first get the company's name and symbol
SYMBOL, COMPANY_NAME = select_company()
# Call for the other classes
my_telegram = TelegramMessage(os.environ.get("TELEGRAM_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID"))
my_stock = StockMachine(SYMBOL, os.environ.get("ALP_KEY"))
my_news = NewsRelated(COMPANY_NAME, day1=my_stock.day_list[1], day2=my_stock.day_list[0])

# After we get all the other classes working, we will compare how much the stocks has changed since yesterday.
percentage = my_stock.percentage
# Checking if it changed more that 1%
if -1 >= percentage or percentage >= 1:
    news_data = my_news.news()
    if percentage >= 1:
        my_telegram.telegram_bot_sendtext(f"{COMPANY_NAME}: 🔺{percentage}%")
    elif percentage <= -1:
        my_telegram.telegram_bot_sendtext(f"{COMPANY_NAME}: 🔻{percentage}%")
    # Now we add the news that could be related to that changes.
    for piece_of_news in my_news.final_data:
        my_telegram.telegram_bot_sendtext(f"Headline: {piece_of_news['title']}\n{piece_of_news['url']}\n")
