from handlers.additionally import shedule
from aiogram import types
from misc import dp, bot

@dp.callback_query_handler(text='modes')
async def modes(call: types.CallbackQuery):
    new_6 = []
    await call.message.delete()
    new = shedule.n
    new_1 = new[1::2]
    new_2 = new[::2]
    for i in range(0, len(new_1)):
        new_4 = i + 1
        new_3 = f'📅 {new_4}. {new_2[i]}: {new_1[i]}'
        new_6.append(new_3)
    await bot.send_message(call.message.chat.id,
                           text='<i><b> Көн тәртибе </b></i>\n\n\n' + '\n\n\n'.join(
                               new_6))
