from aiogram import Bot, Dispatcher, types

# fsm - finite service machine
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Storage is in RAM

from asyncio import get_event_loop
import aiohttp  # Don't know how to properly close the session



'''
Throw the token into TOKEN var in config
'''

bot = Bot(token='1332224705:AAG2WJQLUDLgDf4hzjnz_Pq-ZVXvNiqm4mA', parse_mode=types.ParseMode.HTML)  # Just a good parser
storage = MemoryStorage()  # As it is
dp = Dispatcher(bot, storage=storage)  # It updates the handler(keeps everything in it)

# await bot.send_message("dijnd")

'''
This shit is working
'''
loop = get_event_loop()  # Getting the loop
loop.run_until_complete(bot.send_message(chat_id=441330685, text=""))  # Using the async func to send a mes
