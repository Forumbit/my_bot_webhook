from aiogram import types
from misc import dp, bot
from handlers import keyboards as kb

@dp.callback_query_handler(text='communication')
async def communication(call: types.CallbackQuery):
    await bot.send_message(
    call.message.chat.id,
    text='Әгәр ботны яхшырту буенча теләкләрегез бар икән, минем белән элемтәгә керегез. \n'
    'Әгәр дә ботта ниндидер хата бар икән, ансын да миңа җиткерегез. Рәхмәт!',
    reply_markup=kb.my_telegram
    )
