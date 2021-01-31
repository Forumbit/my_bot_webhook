from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from misc import dp, bot
import sqlite3


lesson_number = ["5", "6", "7", "8", "9", "10", "11"]
lesson_letter = ["а", "б"]
lesson_day = ["Дүшәмбе", "Сишәмбе", "Чәршәмбе", "Пәнҗешәмбе", "Җомга", "Шимбә"]


class OrderLesson(StatesGroup):
    waiting_for_lesson_number = State()
    waiting_for_lesson_letter = State()
    waiting_for_lesson_day = State()


@dp.callback_query_handler(text='orientation', state="*")
async def lesson_step_1(call: types.CallbackQuery):
    keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboards.add(lesson_number[0], lesson_number[1], lesson_number[2]).add(lesson_number[3], lesson_number[4], lesson_number[5]).add(lesson_number[6])

    await bot.send_message(chat_id=call.message.chat.id ,text="Cыйныфыңны сайла: ", reply_markup=keyboards)

    await OrderLesson.waiting_for_lesson_number.set()

@dp.message_handler(state=OrderLesson.waiting_for_lesson_number, content_types=types.ContentTypes.TEXT)
async def lesson_step_2(message: types.message, state: FSMContext):

    if message.text.lower() not in lesson_number:
        await message.reply("Зинһар, сыйныфыңның санын түбәнрәк сайла")
        return

    await state.update_data(chosen_number=message.text.lower())

    keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboards.add(lesson_letter[0], lesson_letter[1])


    await message.answer("Хәзер сыйныфыңның хәрефен сайла: ", reply_markup=keyboards)

    await OrderLesson.waiting_for_lesson_letter.set()

@dp.message_handler(state=OrderLesson.waiting_for_lesson_letter, content_types=types.ContentTypes.TEXT)
async def lesson_step_3(message: types.message, state: FSMContext):

    if message.text.lower() not in lesson_letter:
        await message.answer("Зинһар, сыйныфыңның хәрефен сайла: ")
        return

    await state.update_data(chosen_letter=message.text.lower())

    keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboards.add(lesson_day[0], lesson_day[1]).add(lesson_day[2], lesson_day[3]).add(lesson_day[4], lesson_day[5])

    await message.answer("Атнаның көнен сайла: ", reply_markup=keyboards)

    await OrderLesson.waiting_for_lesson_day.set()


@dp.message_handler(state=OrderLesson.waiting_for_lesson_day, content_types=types.ContentTypes.TEXT)
async def lesson_step_4(message: types.message, state: FSMContext):

    if message.text not in lesson_day:
        print(message.text.lower())
        await message.answer("Зинһар, атнаның көнен сайла: ")
        return
        
    user_data = await state.get_data()
    with sqlite3.connect("handlers/database.db") as db:
        cursor = db.cursor()
        for photo in cursor.execute("SELECT * FROM NewPhotos"):
            if photo[2] == user_data['chosen_number'] + user_data['chosen_letter'] + message.text:
                await bot.send_photo(message.chat.id, photo[1], caption='Бу синең дәресләр челтәре', reply_markup=types.ReplyKeyboardRemove())

    await state.finish()
