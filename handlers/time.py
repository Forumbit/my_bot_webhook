from aiogram import types
from misc import dp, bot
from handlers.times import time_lesson, time_lesson_for_monday, time_lesson_for_sat
from datetime import datetime
import pytz
for_t = 0

@dp.callback_query_handler(text='deadline_lesson')
async def deadline_lesson(call: types.CallbackQuery):
    global for_t
    time_t = datetime.now(pytz.timezone('Europe/Moscow')).weekday() + 1

    if time_t == 1:
        for_t = time_lesson_for_monday
    elif 6 > time_t > 1:
        for_t = time_lesson
    elif time_t == 6:
        for_t = time_lesson_for_sat
    else:
        await call.message.answer('Бүген якшәмбе.')
        return None

    for_t.one_more_time()
    if for_t.a or for_t.a == '0':
        await bot.send_message(call.message.chat.id,
                               text='Дәреслар башлана: {} сәгәттән соң {} минуттан соң.'.format(for_t.a,
                                                                                   for_t.c))

    elif for_t.c == 'new_lesson':
        await bot.send_message(call.message.chat.id, text='Хәзерге вакытта тәнәфес бара.')

    elif for_t.c == 'lesson_no':
        await bot.send_message(call.message.chat.id, text='Бүгенгә дәресләр бетте.')

    else:
        await bot.send_message(call.message.chat.id,
                               text='{} дәрес. Дәрес бетәчәк: {} минуттан соң.'.format(for_t.lesson_number, for_t.c))
