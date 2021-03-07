from aiogram import types
from misc import bot, dp
from datetime import datetime

list_weekday = ["Дүшәмбе", "Сишәмбе", "Чәршәмбе", "Пәнҗешәмбе", "Җомга", "Шимбә"]
list_weekday_correct = ["1", "Сишәмбегә", "Чәршәмбегә", "Пәнҗешәмбегә", "Җомгага", "2"]
list = [
    "AgACAgIAAxkDAAIDfWAahlr-VAzr-P1MKOAHwQNZW8J7AAJtsDEbP-3ZSAyxbVLgASdqfagjmy4AAwEAAwIAA3cAA_IXAgABHgQ",

    "AgACAgIAAxkDAAIDfmAahlsYhG0mICtR3VQ8r4FGGj36AAJusDEbP-3ZSGayphvYpoQ55tsvmy4AAwEAAwIAA3cAA-0OAgABHgQ",

    "AgACAgIAAxkDAAIDf2AahlzyScu56zChXmJTIMgXRgtEAAJvsDEbP-3ZSMtqHqxkU_-RiJY9my4AAwEAAwIAA3cAA9QFAgABHgQ",

    "AgACAgIAAxkDAAIDgGAahl02Qtoi5VL9J1RefRAuUOwhAAJwsDEbP-3ZSPB-lropBsQIZukymy4AAwEAAwIAA3cAA98yAgABHgQ",

    "AgACAgIAAxkDAAIDgWAahl9MVpBQdifKJwABnoP-n7OclwACcbAxGz_t2Uhv9frnN0JKnz2WPZsuAAMBAAMCAAN3AAMkBAIAAR4E",

    "AgACAgIAAxkDAAIDgmAahmEgtMjOZzBUFhsBK4COWOcCAAJysDEbP-3ZSBA9w_Bzqvz7G240my4AAwEAAwIAA3cAA2spAgABHgQ",
]

@dp.callback_query_handler(text='order_of_calls')
async def order_of_calls(call: types.CallbackQuery):
        time_t = datetime.today().weekday() + 1
        if time_t == 1:
            await bot.send_photo(call.message.chat.id, list[0], caption='Дүшәмбегә кыңгырау бирү тәртибе.')

        elif 6 > time_t > 1:
            for i in range(len(list_weekday)):
                if list_weekday[time_t - 1] == list_weekday[i]:
                    await bot.send_photo(call.message.chat.id, list[i], caption=f'{list_weekday_correct[time_t - 1]} кыңгырау бирү тәртибе.')

        elif time_t == 6:
            await bot.send_photo(call.message.chat.id, list[2], caption='Шимбәгә кыңгырау бирү тәртибе.')

        else:
            await call.message.answer('Бүген якшәмбе.')
            return None

        # for i in range(len(list_weekday)):
        #     pic = await bot.send_photo(call.message.chat.id, types.InputFile(f'Кыңгырау бирү тәртибе/{list_weekday[i]}.png'))
        #     print()
        #     print()
        #     print()
        #     print()
        #     print()
        #     print(i, pic.photo[-1])

        # pic1 = await bot.send_photo(call.message.chat.id, types.InputFile(f'handlers/порядок звонков вт-пт.png'))
        # pic2 = await bot.send_photo(call.message.chat.id, types.InputFile(f'handlers/порядок звонков(сб).png'))
        # print(pic.photo[-1])
        # print()
        # print()
        # print(pic1.photo[-1])
        # print()
        # print()
        # print(pic2.photo[-1])
