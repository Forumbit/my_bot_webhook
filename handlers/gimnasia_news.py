from aiogram import types
from misc import dp, bot
from bs4 import BeautifulSoup as BS
import requests

@dp.callback_query_handler(text='additional_zamena')
async def additional_zamena(call: types.CallbackQuery):
    try:
        d = []
        r = requests.get('http://127.0.0.1:8000/')
        html = BS(r.content, 'html.parser')
        for el in html.select('.additional'):
            d.append(el.text)
        if len(d) != 1:
            new_1 = d[::2]
            new_2 = d[1::2]
            new_5 = []
            for i in range(0, len(new_1)):
                new_6 = i + 1
                new_7 = f'{new_6}. ✅ {new_1[i]} ✅\n\n' \
                        f'<b><i>{new_2[i]}</i></b>'
                new_5.append(new_7)
            await bot.send_message(call.message.chat.id, text='\n\n\n'.join(new_5))
            new_5.clear()
        else:
            await bot.send_message(call.message.chat.id, text='Бүгенгә яңалыклар юк.')
    except:
        await bot.send_message(call.message.chat.id, text='Гафу итегез, хәзерге вакытта техник җитешсезлекләр барлыкка килде.')
