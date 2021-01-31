from aiogram import types
from misc import dp, bot
from handlers import keyboards as kb

@dp.callback_query_handler(text='news')
async def news(call: types.CallbackQuery):
    pic = 'AgACAgIAAxkDAAOMX_bZDLDKsTDGa64h5RZawzoHvgEAApKxMRv2OLlLr19_lWQ2gW7t9xibLgADAQADAgADdwADIDQAAh4E'
    await bot.send_photo(call.message.chat.id, pic, caption='Гимназия турында күбрәк мәгълүматны Сез түбәнрәк белә аласыз.', reply_markup=kb.links)
