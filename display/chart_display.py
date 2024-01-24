from aiogram import Bot
from config.config import TOKEN
from config.num_week_date import admin_date_weeks, admin_month_weeks
from keybord_markup.keyboard import keyboard_admin_date
from data.data_num_month import sql_info_week_date

bot = Bot(token=TOKEN)

async def admin_chart_display(admin, num_week):
    
    monday_date, tuesday_date, wednesday_date, thursday_date, friday_date, saturday_date, sunday_date = await admin_date_weeks(num_week)
    
    monday_month, tuesday_month, wednesday_month, thursday_month, friday_month, saturday_month, sunday_month = await admin_month_weeks(num_week)
    
    assigned_date_monday, assigned_date_tuesday, assigned_date_wednesday, assigned_date_thursday, assigned_date_friday, assigned_date_saturday, assigned_date_sunday = await sql_info_week_date(monday_date, monday_month, tuesday_date, tuesday_month, wednesday_date, wednesday_month, thursday_date, thursday_month, friday_date, friday_month, saturday_date, saturday_month, sunday_date, sunday_month)
    
    text_week_chart = f"""
*Понедельник {monday_date:02}.{monday_month:02}*
{assigned_date_monday}
*Втроник {tuesday_date:02}.{tuesday_month:02}*
{assigned_date_tuesday}
*Среда {wednesday_date:02}.{wednesday_month:02}*
{assigned_date_wednesday}
*Четверг {thursday_date:02}.{thursday_month:02}*
{assigned_date_thursday}
*Пятница {friday_date:02}.{friday_month:02}*
{assigned_date_friday}
*Суббота {saturday_date:02}.{saturday_month:02}*
{assigned_date_saturday}
*Воскресенье {sunday_date:02}.{sunday_month:02}*
{assigned_date_sunday}
"""
    
    weel_schedule = f"""
+---------------------------+
{text_week_chart}
+---------------------------+
"""

    await bot.send_message(admin, text=weel_schedule, reply_markup= await keyboard_admin_date(num_week), parse_mode="Markdown")