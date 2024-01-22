from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import MessageToDeleteNotFound, MessageCantBeDeleted
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import TOKEN, admin_bot
from config.date_update import day_month_update
from keybord_markup.keyboard import kb_start, kb_back_start, kb_start_admin, kb_admin_action, keyboard_free_time
from display.time_display import display_time
from admin_panel.admin_set_day import start_print_day
from admin_panel.admin_delete_day import start_delete_day
from admin_panel.admin_move_chart import start_chart
from data.data_client import sql_start_users , sql_add_client, sql_make_appointment_status_record
from data.data_client import sql_add_continue_date, sql_add_back_date, sql_print_day, sql_make_appointment_time
from data.data_admin import sql_start_admin, sql_start_admin_viewing_week, sql_add_continue_week, sql_add_back_week
from data.form_record import start_time_choise
from data.data_form import sql_start_form

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

print("Бот запущен!")

sql_start_users()
sql_start_admin()
sql_start_form()
sql_start_admin_viewing_week()

start_print_day(dp)
start_delete_day(dp)
start_chart(dp)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    
    day, month = await day_month_update()
    
    fname = str(message.from_user.first_name)
    lname = str(message.from_user.last_name)
    uname = '@' + str(message.from_user.username)
    
    if message.chat.id in admin_bot:
        await message.answer("Добро пожаловать администратор Nail.crim", reply_markup=kb_start_admin)
        
    else:
        await message.answer("Добро пожаловать к Nail.crim", reply_markup=kb_start)
    
    await sql_add_client(message.chat.id, fname, lname, uname, day, month, "NO")
    
    await message.delete()
    
    
@dp.message_handler(text=["📋 Админ-Панель 📋"])
async def admin_panel(message: types.Message):
    
    if message.chat.id in admin_bot:
        await message.answer("Выберите действие...", reply_markup=kb_admin_action)
        
    else:
        await message.answer("У вас недостаточно прав!")


@dp.message_handler(text=["⬇️ Назад ⬇️"])
async def start(message: types.Message):
    
    day, month = await day_month_update()
    
    if message.chat.id in admin_bot:
        await message.answer("Администратор Nail.crim. Главное меню!", reply_markup=kb_start_admin)
        
    else:
        await message.answer("Запишись ко мне 🥰", reply_markup=kb_start)
        
    await sql_add_client(message.chat.id, "", "", "", day, month, "NO")
    
    
@dp.message_handler(text=["💅🏻 Записаться 💅🏻"])
async def note_time(message: types.Message):
    
    day, month = await day_month_update()
    
    await message.answer(text="График свободных мест на запись", reply_markup=kb_back_start)
    
    await sql_add_client(message.chat.id, "", "", "", day, month, "NO")
    await display_time(message.chat.id, day, month)


@dp.message_handler()
async def del_text(message: types.Message):
    
    await message.delete()
  

@dp.callback_query_handler()
async def note_date_time(callback: types.CallbackQuery):
    
    try:
        
        if callback.data == str(1):
            await sql_add_continue_date(callback.message.chat.id)

            try:
                await bot.delete_message(callback.from_user.id, callback.message.message_id)

            except MessageToDeleteNotFound:
                print("message not found")

        elif callback.data == str(-1):
            await sql_add_back_date(callback.message.chat.id)

            try:
                await bot.delete_message(callback.from_user.id, callback.message.message_id)

            except MessageToDeleteNotFound:
                print("message not found")

        elif callback.data == "Click_day":
            day_p = await sql_print_day(callback.message.chat.id)

            await callback.answer(f"{day_p[1]:02}.{day_p[2]:02}")

        elif callback.data == "make_appointment_time":

            flag = await sql_make_appointment_time(callback.message.chat.id)
            if flag != []:
                await callback.answer(f"Запись есть!")
                await bot.send_message(callback.message.chat.id ,"Выберите время", reply_markup=await keyboard_free_time(flag))

                await sql_make_appointment_status_record(callback.message.chat.id)
                await start_time_choise(dp)

            else:
                await callback.answer(f"Записей нет!")
        
    except MessageCantBeDeleted:
        print("Использование callback запроса для пользователей больше 48 часов!", "MessageCantBeDeleted")
            
    try:

        if callback.data == "Click_week":
            await callback.answer("неделя")

        elif callback.data == "1нед":
            await sql_add_continue_week(callback.message.chat.id)

            try:
                await bot.delete_message(callback.from_user.id, callback.message.message_id)

            except MessageToDeleteNotFound:
                print("message not found")

        elif callback.data == "-1нед":
            await sql_add_back_week(callback.message.chat.id)

            try:
                await bot.delete_message(callback.from_user.id, callback.message.message_id)

            except MessageToDeleteNotFound:
                print("message not found")
    
    except MessageCantBeDeleted:
        print("Использование callback запроса для админа больше 48 часов!", "MessageCantBeDeleted")


if __name__ == "__main__":
    executor.start_polling(dp)