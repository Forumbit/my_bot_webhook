from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from aiogram import Bot, Dispatcher

bot = Bot(token="1547077005:AAEzkOMfPdEU5On_0Jfr3kXNJy9kWm_BqAg", parse_mode="html")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
