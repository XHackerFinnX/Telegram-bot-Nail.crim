from aiogram import types
from config.week_day import day_week
import datetime

kb_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb_note = types.KeyboardButton("💅🏻 Записаться 💅🏻")
kb_start.add(kb_note)

kb_back_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb_bs = types.KeyboardButton("⬇️ Назад ⬇️")
kb_back_start.add(kb_bs)

kb_back_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb_ba = types.KeyboardButton("⬇️ Назад к панели ⬇️")
kb_back_admin.add(kb_ba)

kb_start_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb_panel = types.KeyboardButton("📋 Админ-Панель 📋")
kb_start_admin.add(kb_panel, kb_note)

kb_yes_no = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb_yes = types.KeyboardButton("✅ Да ✅")
kb_no = types.KeyboardButton("❌ Нет ❌")
kb_yes_no.add(kb_yes, kb_no)

kb_admin_action = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb_day = types.KeyboardButton("Назначить день 🗓")
kb_day_delete = types.KeyboardButton("Убрать день 🗓")
kb_chart_move = types.KeyboardButton("Посмотреть график 📊")
kb_admin_action.add(kb_day, kb_day_delete, kb_chart_move, kb_bs)

kb_remove = types.ReplyKeyboardRemove()

async def keyboard_date(day, month):
    
    date = datetime.datetime(2024, month, day)
    week = await day_week(date.weekday())
    
    kb_date = types.InlineKeyboardMarkup(resize_keyboard=True)
    kb_back = types.InlineKeyboardButton("⬅️  ", callback_data= -1)
    kb_date_number = types.InlineKeyboardButton(f"{day:02}.{month:02} {week}", callback_data="Click_day")
    kb_continue = types.InlineKeyboardButton("  ➡️", callback_data= 1)
    kb_date_note = types.InlineKeyboardButton("    Записаться на время    ", callback_data="make_appointment_time")
    kb_date.add(kb_back, kb_date_number, kb_continue, kb_date_note)
    
    return kb_date


async def keyboard_admin_date(num_week):
    
    kb_date_chart = types.InlineKeyboardMarkup(resize_keyboard=True)
    kb_back = types.InlineKeyboardButton("⬅️  ", callback_data= "-1нед")
    kb_date_number = types.InlineKeyboardButton(f"{num_week} нед.", callback_data="Click_week")
    kb_continue = types.InlineKeyboardButton("  ➡️", callback_data= "1нед")
    kb_date_chart.add(kb_back, kb_date_number, kb_continue)
    
    return kb_date_chart


async def keyboard_free_time(free_time):
    
    kb_free_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    for i in free_time:
        time_add = types.KeyboardButton(f"{i}")
        kb_free_time.add(time_add)
    kb_free_time.add(kb_bs)
    return kb_free_time