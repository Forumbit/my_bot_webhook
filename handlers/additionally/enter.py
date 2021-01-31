from aiogram import types
from misc import dp, bot
from handlers import keyboards as kb

@dp.callback_query_handler(text='enter')
async def enter(call: types.CallbackQuery):
    pic = 'AgACAgIAAxkDAAOLX_bZAy_9bAQ2XyIHi0CaMq6nW18AApGxMRv2OLlLe-0grs4zZ_MjZ4meLgADAQADAgADeAADrjQAAh4E'
    pic = await bot.send_photo(call.message.chat.id, pic, caption='Әгәр телисез икән, укырга керергә гимназиягә, сезгә'
                                                                  ' кирәк җибәрергә үз контактларыгызны безнең сайтка.'
                                                                  ' Без, һичшиксез, сезнең белән элемтәгә керәчәкбез', reply_markup=kb.enter_markup)
