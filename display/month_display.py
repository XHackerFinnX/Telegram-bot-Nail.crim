from aiogram import Bot, types
from config.config import TOKEN
from keybord_markup.keyboard import keyboard_choice_month

bot = Bot(token=TOKEN)


async def display_month(users, january, february, march, april, may, june, july, august, september, october, november, december):
    
    text_month = "Выберите месяц"
    
    await bot.send_message(users, text=text_month, reply_markup= await keyboard_choice_month(january, february, march, april, may, june, july, august, september, october, november, december))