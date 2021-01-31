from aiogram import types
from handlers import keyboards as kb
from misc import dp, bot

@dp.callback_query_handler(text='test')
async def test(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,
                           text="Әгәр синең  Огэ, Егэ, ЦТ, ВПР чишәсең килсә, мин сиңа киңәш итәм "
                                "ботны @reshuege_bot")
