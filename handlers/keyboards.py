from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton

# for menu
orientation = InlineKeyboardButton('⚪ Дәрес челтәре ⚪', callback_data='orientation')
additionally = InlineKeyboardButton('<<< Өстәмә >>>', callback_data='additionally')
zamena = InlineKeyboardButton('⚪ Алмаш дәресләр ⚪', callback_data='zamena')
deadline_lesson = InlineKeyboardButton('⚪ Дәрес ахыры ⚪', callback_data='deadline_lesson')
additional_zamena = InlineKeyboardButton("⚪ Яңалыклар ⚪", callback_data='additional_zamena')
order_of_calls = InlineKeyboardButton("⚪ Кыңгырау бирү тәртибе ⚪", callback_data='order_of_calls')
# Бар нинди дә булса хаталар ботта? Минем белән элемтәгә керегез.
# for menu_2
test = InlineKeyboardButton("⚪ ОГЭ/Егэ ⚪", callback_data='test')
news = InlineKeyboardButton("⚪ Ссылкалар ⚪", callback_data='news')
enter = InlineKeyboardButton("⚪ Керү ⚪", callback_data='enter')
cancel_for_menu = InlineKeyboardButton('<<< Артка >>>', callback_data='cancel_for_menu')
modes = InlineKeyboardButton("⚪ Көн тәртибе ⚪", callback_data='modes')
communication = InlineKeyboardButton("⚪ Элемтә ⚪", callback_data='communication')
my_id = InlineKeyboardButton(" Telegram ", url='https://t.me/ForumBit')
# for enter_markup
enter_link = InlineKeyboardButton('Гимназияның сайты', url='http://tbsh.org/#form85065781')

# for links
site = InlineKeyboardButton('Гимназияның сайты', url='http://tbsh.org')
telegram = InlineKeyboardButton('Telegram', url='https://t.me/gimnazia')
instagram = InlineKeyboardButton('Instagram', url='https://www.instagram.com/aktanysh_gimnaziya')
vkontakte = InlineKeyboardButton('VKontakte', url='https://vk.com/giftedhumanitarian')
facebook = InlineKeyboardButton('Facebook', url='https://www.facebook.com/tatbsh')
# markups
my_telegram = InlineKeyboardMarkup().add(my_id)
orientation1 = InlineKeyboardMarkup().add(orientation, zamena).add(additional_zamena, deadline_lesson).add(order_of_calls).add(additionally)
menu_2 = InlineKeyboardMarkup().add(test, modes).add(news, enter).add(communication).add(cancel_for_menu)
enter_markup = InlineKeyboardMarkup().add(enter_link)
links = InlineKeyboardMarkup().add(enter_link).add(telegram, instagram).add(vkontakte, facebook)
