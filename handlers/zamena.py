from misc import dp, bot
from bs4 import BeautifulSoup as BS
from aiogram import types
import requests

@dp.callback_query_handler(text='zamena')
async def zamena(call: types.CallbackQuery):
    try:
        d = []
        r = requests.get('http://127.0.0.1:8000')
        html = BS(r.content, 'html.parser')
        for el in html.select('.zamena'):
            d.append(el.text)
        if len(d) != 1:
            new_1 = d[::4]
            new_2 = d[1::4]
            new_3 = d[2::4]
            new_4 = d[3::4]
            new_5 = []
            for i in range(0, len(new_1)):
                new_6 = i + 1
                new_7 = f'{new_6} замена.  Класс: {new_3[i]}\n\n' \
                        f'✅ Дәрес: {new_1[i]}\n\n' \
                        f'✅ Предмет: {new_2[i]}\n\n' \
                        f'✅ Кабинет: {new_4[i]}'
                new_5.append(new_7)
            await bot.send_message(call.message.chat.id, text='\n\n\n'.join(new_5))
            new_5.clear()
        else:
            await bot.send_message(call.message.chat.id, text='На сегодня замен нет')

    except:
        await bot.send_message(call.message.chat.id, text='Гафу итегез, хәзерге вакытта техник җитешсезлекләр барлыкка килде.')
