from aiogram import types
from misc import dp, bot
import sqlite3
@dp.message_handler(commands=['start'])
async def start_command(message: types.message):
    await bot.send_photo(
        message.chat.id,
        'AgACAgIAAxkDAANyX_bLHcyYjhIodrhj1E9qWC8AAdPjAAKDsTEb9ji5S6_kmTtorYqROX7Xli4AAwEAAwIAA3cAA4wCBgABHgQ',
        caption='Сәләм дустым. Мин синең ярдәмчең булам.\n'
                'Бас /menu -га, аннары мин сиңа ярдәм итәчәкмен.'
    )
