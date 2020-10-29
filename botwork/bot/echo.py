from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Messsage):
    # Let's get char_id and text
    char_id = message.from_user.id
    text = message.text

    from loader import bot

    await bot.send_message(char_id=char_id, text=text)
    #  Or message.answer(text=text)
