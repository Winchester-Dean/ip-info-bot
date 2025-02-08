import logging

from aiogram import F
from aiogram.types import Message
from dispatcher import dp
from handlers.keyboard import board
from utils import *

logging.basicConfig(level=logging.INFO)

@dp.message(F.text)
async def trigger(msg: Message):
    query = msg.text.strip()

    if not (is_valid_ip(query) or is_valid_domain(query)):
        return await msg.answer(
            "<b>Пожалуйста, введите корректный IP адрес или домен.</b>"
        )

    info = get_ip_info(query)
    emoji = get_emoji(info.get("countryCode"))

    if info:
        domain = info.get("reverse", "N/A")
        ip = info.get("query", "N/A")
        response = (
            f"<b>🌍 IP:</b> <code>{info.get('query', 'N/A')}</code>\n"
            f"<b>├ Provider:</b> <code>{info.get('isp', 'N/A')}</code>\n"
            f"<b>├ Country:</b> {emoji} {info.get('country', 'N/A')}, {info.get('countryCode', 'N/A')}\n"
            f"<b>├ Region:</b> {info.get('regionName', 'N/A')}, {info.get('region', 'N/A')}\n"
            f"<b>├ City:</b> {info.get('city', 'N/A')}\n"
            f"<b>├ Domain:</b> <code>{domain if domain else ip}</code>\n"
            f"<b>├ Mobile:</b> {info.get('mobile', 'N/A')}\n"
            f"<b>├ Proxy:</b> {info.get('proxy', 'N/A')}\n"
            f"<b>├ Hosting:</b> {info.get('hosting', 'N/A')}"
        )
    else:
        response = "<b>Не удалось получить информацию. Проверьте правильность введенного IP адреса или домена.</b>"

    await msg.reply(response, reply_markup=board)
