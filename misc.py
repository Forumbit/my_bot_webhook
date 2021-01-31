from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from aiogram import Bot, Dispatcher
import os

bot = Bot(token="os.environ.get('BOT_TOKEN')", parse_mode="html")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
