from aiogram import types
from handlers import keyboards as kb
from misc import dp

@dp.callback_query_handler(text='additionally')
async def additionally(call: types.CallbackQuery):
    await call.message.edit_text('<i><b> Өстәмә </b></i>',
                                 reply_markup=kb.menu_2)
