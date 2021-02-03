from aiogram import types
from misc import bot, dp
from datetime import datetime

list_weekday = ["Дүшәмбе", "Сишәмбе", "Чәршәмбе", "Пәнҗешәмбе", "Җомга", "Шимбә"]
list_weekday_correct = ["Сишәмбегә", "Чәршәмбегә", "Пәнҗешәмбегә", "Җомгага"]
list = [
    "AgACAgIAAxkDAAIBOmAYDCxnLE4dSBHBhqPF0dEy-VJhAAJ2sjEb22fASG2wLEx7DkvnGzPtly4AAwEAAwIAA3cAA7FgBgABHgQ",
    "AgACAgIAAxkDAAIBLWAYBu18Cj-9Vj125FYR9Zugu23dAAJosjEb22fASPvKfviFtQQBI_TAly4AAwEAAwIAA3cAA6k_BgABHgQ",
    "AgACAgIAAxkDAAIBLmAYBu-tphJPC-wajIjWT5HSJwXbAAJpsjEb22fASBuob93XPIvvbuhRmC4AAwEAAwIAA3cAAyhWBgABHgQ",
    "AgACAgIAAxkDAAIBL2AYBvAjwlVucPq6fZaddUvQIKiEAAJqsjEb22fASG-O9lX9gDPawUddmi4AAwEAAwIAA3cAAz01BAABHgQ",
    "AgACAgIAAxkDAAIBMGAYBvGLrngECJ86sdBdffVpUb7qAAJrsjEb22fASOZme0yGMTbPQVgRmy4AAwEAAwIAA3cAA-QxAQABHgQ",
    "AgACAgIAAxkDAAIBMWAYBvJgYRByJ2WYs-2ULduk7i7xAAJssjEb22fASEgX2SlrVErYPvVBli4AAwEAAwIAA3cAAz_9BgABHgQ"
]

@dp.callback_query_handler(text='order_of_calls')
async def order_of_calls(call: types.CallbackQuery):
        time_t = datetime.today().weekday() + 1

        if time_t == 1:
            await bot.send_photo(call.message.chat.id, list[0], caption='Дүшәмбегә кыңгырау бирү тәртибе.')

        elif 6 > time_t > 1:
            for i in range(len(list_weekday)):
                if list_weekday[time_t - 1] == list_weekday[i]:
                    await bot.send_photo(call.message.chat.id, list[1], caption=f'{list_weekday[time_t - 1]} кыңгырау бирү тәртибе.')

        elif time_t == 6:
            await bot.send_photo(call.message.chat.id, list[2], caption='Шимбәгә кыңгырау бирү тәртибе.')

        else:
            await call.message.answer('Бүген якшәмбе.')
            return None
        #
        # pic = await bot.send_photo(call.message.chat.id, types.InputFile(f'Кыңгырау бирү тәртибе/Дүшәмбе.png'))
        # pic1 = await bot.send_photo(call.message.chat.id, types.InputFile(f'handlers/порядок звонков вт-пт.png'))
        # pic2 = await bot.send_photo(call.message.chat.id, types.InputFile(f'handlers/порядок звонков(сб).png'))
        # print(pic.photo[-1])
        # print()
        # print()
        # print(pic1.photo[-1])
        # print()
        # print()
        # print(pic2.photo[-1])
