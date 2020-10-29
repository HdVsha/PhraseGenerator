# from utils.set_bot_commands import set_default_commands
import echo



async def on_startup(dp):
    import filters
    import middleware

    filters.setup(dp)
    middleware.setup(dp)

    from utils.notify_admins import on_startup_notify  # Sends the message to all admins saying that the bot is launched
    await on_startup_notify(dp)                        # and is ready to work
    await set_default_commands(dp)


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    # Executor is a longpoller(periodically gets the info from the server and gives it to dispatcher-dp)
    executor.start_polling(dp, on_startup=on_startup)  # On_startup is used to register filters and so on
    echo()
