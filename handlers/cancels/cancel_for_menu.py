from aiogram import types
from misc import dp
from handlers import keyboards as kb

@dp.callback_query_handler(text='cancel_for_menu')
async def cancel_for_menu(call: types.CallbackQuery):
    await call.message.edit_text('<i><b> Меню </b></i>',
                                 reply_markup=kb.orientation1)
