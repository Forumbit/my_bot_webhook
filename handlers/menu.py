from aiogram import types
from misc import dp, bot
import handlers.keyboards as kb

@dp.message_handler(commands=['menu'])
async def menu(message: types.message):
    await bot.send_message(message.chat.id,
                           text='<i><b> Меню </b></i>',
                           reply_markup=kb.orientation1)
