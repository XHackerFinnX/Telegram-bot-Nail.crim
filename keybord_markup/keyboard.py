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
    kb_continue_week = types.InlineKeyboardButton("  ⏩", callback_data= 7)
    kb_back_week = types.InlineKeyboardButton("  ⏪", callback_data= -7)
    kb_date_note = types.InlineKeyboardButton("    Записаться на время    ", callback_data="make_appointment_time")
    kb_date.add(kb_back, kb_date_number, kb_continue)
    kb_date.add(kb_back_week, kb_continue_week)
    kb_date.add(kb_date_note)
    
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


async def keyboard_choice_month(january, february, march, april, may, june, july, august, september, october, november, december):
    
    kb_month = types.InlineKeyboardMarkup(resize_keyboard=True)
    
    kb_january = types.InlineKeyboardButton(f"Январь - {january} мест", callback_data= "january")
    kb_month.add(kb_january)
    
    kb_february = types.InlineKeyboardButton(f"Февраль - {february} мест", callback_data= "february")
    kb_month.add(kb_february)
    
    kb_march = types.InlineKeyboardButton(f"Март - {march} мест", callback_data= "march")
    kb_month.add(kb_march)
    
    kb_april = types.InlineKeyboardButton(f"Апрель - {april} мест", callback_data= "april")
    kb_month.add(kb_april)
    
    kb_may = types.InlineKeyboardButton(f"Май - {may} мест", callback_data= "may")
    kb_month.add(kb_may)
    
    kb_june = types.InlineKeyboardButton(f"Июнь - {june} мест", callback_data= "june")
    kb_month.add(kb_june)
    
    kb_july = types.InlineKeyboardButton(f"Июль - {july} мест", callback_data= "july")
    kb_month.add(kb_july)
    
    kb_august = types.InlineKeyboardButton(f"Август - {august} мест", callback_data= "august")
    kb_month.add(kb_august)
    
    kb_september = types.InlineKeyboardButton(f"Сентябрь - {september} мест", callback_data= "september")
    kb_month.add(kb_september)
    
    kb_october = types.InlineKeyboardButton(f"Октябрь - {october} мест", callback_data= "october")
    kb_month.add(kb_october)
    
    kb_november = types.InlineKeyboardButton(f"Ноябрь - {november} мест", callback_data= "november")
    kb_month.add(kb_november)
    
    kb_december = types.InlineKeyboardButton(f"Декабрь - {december} мест", callback_data= "december")
    kb_month.add(kb_december)
    
    return kb_month
    
    