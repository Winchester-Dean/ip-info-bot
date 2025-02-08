import logging

from aiogram.filters.command import Command
from aiogram.types import Message
from dispatcher import dp

logging.basicConfig(level=logging.INFO)

@dp.message(Command('help'))
async def cmd_help(msg: Message):
    help_text = (
        "<strong>"
        "List of commands:\n"
        "/start — restart the bot\n"
        "/help — shows a list of basic commands\n\n"
        "If you have any questions, contact me: stix_r.t.me"
        "</strong>"
    )
    await msg.answer(help_text)
