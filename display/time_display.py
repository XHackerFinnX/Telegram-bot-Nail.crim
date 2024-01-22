from aiogram import Bot, types
from keybord_markup.keyboard import keyboard_date
from data.data_admin import sql_text_for_client
from config.config import TOKEN

bot = Bot(token=TOKEN)

async def display_time(users, day, month):
    text_time_day = await sql_text_for_client(day, month)
    time_schedule = f"""
+---------------------------+
{text_time_day}
+---------------------------+
"""

    await bot.send_message(users, text=time_schedule, reply_markup= await keyboard_date(day, month))