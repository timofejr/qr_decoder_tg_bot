import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6999337453:AAHnrZYpZeVslUINIoM_Hz-FNvYHBDNJoE8")
dp = Dispatcher()

allowed_users = (333200577, 1012912862)


def decrypt(data: str) -> str:
    decrypted_data = ""
    for i, value in enumerate(data):
        if i % 2 == 0:
            continue
        decrypted_data += value

    date = datetime.fromtimestamp(int(decrypted_data)).strftime("%d.%m.%Y %H:%M")
    return date


@dp.message(Command("start"))
async def cmd_start(message: types.Message, command: CommandObject):
    if message.from_user.id not in allowed_users:
        await message.answer("Нет доступа")
    else:
        date = decrypt(command.args)
        await message.answer(date)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
