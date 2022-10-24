from aiogram.utils import executor
from bot_conf import dp
from handlers.client_handler import client_handlers


client_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
