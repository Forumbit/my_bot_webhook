from aiogram import types
from misc import bot, dp
from datetime import datetime

list_weekday = ["Дүшәмбегә", "Сишәмбегә", "Чәршәмбегә", "Пәнҗешәмбегә", "Җомгага", "Шимбәгә"]

list = [
    'AgACAgIAAxkDAANtX_XIN1jRy9al77VFzbBZXifeknQAAmiwMRshkLBL8VDvWDXIzdgVziybLgADAQADAgADdwAD8vkAAh4E',
    'AgACAgIAAxkDAANuX_XIO8L83_QRP8hcFv4fjKhRAtsAAmmwMRshkLBL9_GMgVohXS1DVhGbLgADAQADAgADdwADwS4AAh4E',
    'AgACAgIAAxkDAANvX_XIPzZL_MNzNki1nGUzoom1wlsAAmqwMRshkLBLq9DWWHn-PBx55U2eLgADAQADAgADdwADnzEAAh4E',
]

@dp.callback_query_handler(text='order_of_calls')
async def order_of_calls(call: types.CallbackQuery):
        time_t = datetime.today().weekday() + 1

        if time_t == 1:
            await bot.send_photo(call.message.chat.id, list[0], caption='Дүшәмбегә кыңгырау бирү тәртибе.')

        elif 6 > time_t > 1:
            await bot.send_photo(call.message.chat.id, list[1], caption=f'{list_weekday[time_t - 1]} кыңгырау бирү тәртибе.')

        elif time_t == 6:
            await bot.send_photo(call.message.chat.id, list[2], caption='Шимбәгә кыңгырау бирү тәртибе.')

        else:
            await call.message.answer('Бүген якшәмбе.')
            return None
        #
        # pic = await bot.send_photo(call.message.chat.id, types.InputFile(f'handlers/порядок звонков понедельник.png'))
        # pic1 = await bot.send_photo(call.message.chat.id, types.InputFile(f'handlers/порядок звонков вт-пт.png'))
        # pic2 = await bot.send_photo(call.message.chat.id, types.InputFile(f'handlers/порядок звонков(сб).png'))
        # print(pic.photo[-1])
        # print()
        # print()
        # print(pic1.photo[-1])
        # print()
        # print()
        # print(pic2.photo[-1])
