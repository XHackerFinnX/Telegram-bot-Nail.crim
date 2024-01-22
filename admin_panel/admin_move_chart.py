from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Text
from config.config import TOKEN, admin_bot
from config.date_update import day_month_update
from config.week_admin import week_update
from keybord_markup.keyboard import kb_back_admin
from display.chart_display import admin_chart_display
from data.data_admin import sql_add_week

bot = Bot(token=TOKEN)


async def chart_day(message: types.Message):
    
    if message.chat.id not in admin_bot:
        await message.answer("У вас недостаточно прав!")
        
        return
    
    day, month = await day_month_update()
    num_week = await week_update(day, month)
    
    await sql_add_week(message.chat.id, num_week)
    
    await admin_chart_display(message.chat.id, num_week)
    
    await message.answer("В разработке")

def start_chart(dp: Dispatcher):
    
    dp.register_message_handler(chart_day, Text(equals="Посмотреть график 📊"))