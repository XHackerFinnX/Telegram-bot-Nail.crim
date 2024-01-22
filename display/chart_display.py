from aiogram import Bot
from config.config import TOKEN
from keybord_markup.keyboard import keyboard_admin_date

bot = Bot(token=TOKEN)

async def admin_chart_display(admin, num_week):
    text_week_chart = 0
    weel_schedule = f"""
+---------------------------+
{text_week_chart}
+---------------------------+
"""

    await bot.send_message(admin, text=weel_schedule, reply_markup= await keyboard_admin_date(num_week))