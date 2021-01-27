from telegram.ext import Updater,CallbackContext,CommandHandler
from telegram import Update
import random
from imdbscraper import IMDB_scraper,URLS
import logging

#This is given by bot father
TELEGRAM_TOKEN = str(open('token.txt','r').readline())

def start(update:Update,context:CallbackContext):

    """
    This function is the start command.
    """
    message = open("welcome.txt",'r')
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = message.read(),
    )

def content_formating(content:str,meta:tuple) -> str:

    """
    It takes the movie or series and format it properly.
    """

    formatted_string = f"Title: {content}\nRating: {meta[0]}⭐\nLink of IMDB:\n{meta[1]}"
    return formatted_string


def random_object(content:str) -> tuple:

    """
    This function scrapes the content and generates a random object from it.
    """

    url = URLS[content]
    content_dic = IMDB_scraper(url)
    return random.choice(list(content_dic.items()))


def get_movie(update:Update,context:CallbackContext):

    """
    This scrapes the movies from top-250 IMDB Rated Movies.
    """

    chat_id = update.effective_chat.id
    content = "top_100_movies"
    rand_content, rand_meta = random_object(content)
    text = content_formating(rand_content, rand_meta)
    context.bot.send_message(
        chat_id=chat_id,
        text=text
    )


def get_series(update:Update,context:CallbackContext):

    """
    This scrapes the movies from top-250 IMDB Rated Series.
    """

    chat_id = update.effective_chat.id
    content = "top_100_series"
    rand_content, rand_meta = random_object(content)
    text = content_formating(rand_content, rand_meta)
    context.bot.send_message(
        chat_id=chat_id,
        text=text
    )


def trending_series(update:Update,context:CallbackContext):

    """
    This scrapes the series from trending list of IMDB.
    """

    chat_id = update.effective_chat.id
    content = "trending_series"
    rand_content, rand_meta = random_object(content)
    text = content_formating(rand_content, rand_meta)
    context.bot.send_message(
        chat_id=chat_id,
        text=text
    )


def trending_movie(update:Update,context:CallbackContext):

    """
    This scrapes the movie from trending list of IMDB
    """

    chat_id = update.effective_chat.id
    content = "trending_movies"
    rand_content, rand_meta = random_object(content)
    text = content_formating(rand_content, rand_meta)
    context.bot.send_message(
        chat_id=chat_id,
        text=text
    )



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )
updater = Updater(token=TELEGRAM_TOKEN)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start',start)
get_movie_handler = CommandHandler('get_movie', get_movie)
trending_movie_handler = CommandHandler('trending_movie', trending_movie)
get_series_handler = CommandHandler('get_series', get_series)
trending_series_handler = CommandHandler('trending_series', trending_series)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(get_movie_handler)
dispatcher.add_handler(get_series_handler)
dispatcher.add_handler(trending_movie_handler)
dispatcher.add_handler(trending_series_handler)
updater.start_polling()
updater.idle()

