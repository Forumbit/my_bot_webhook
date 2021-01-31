from misc import dp
from aiogram import executor
import handlers
from aiogram.bot import api
PATHCED_URL = "https://telegg.ru/orig/bot{token}/{method}"
setattr(api, "API_URL", PATHCED_URL)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
