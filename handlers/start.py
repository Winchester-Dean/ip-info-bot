import logging

from aiogram.types import Message
from aiogram.filters.command import Command
from dispatcher import dp

logging.basicConfig(level=logging.INFO)

@dp.message(Command('start'))
async def cmd_start(msg: Message):
    await msg.answer(
        "<strong>"
        "Hello! Enter IP address or domain to get information about it."
        "</strong>"
    )
