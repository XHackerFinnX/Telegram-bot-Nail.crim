from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config.config import TOKEN, chat_record, admin_bot, price, address
from data.data_client import sql_check_status_for_continue_choise_time, sql_users_for_add_record
from data.data_form import sql_add_record
from data.data_form import sql_update_make_appointment_time
from keybord_markup.keyboard import kb_yes_no, kb_start, kb_remove, kb_start_admin, kb_back_start
from config.date_update import day_month_year_hour_min
from display.push_date import main_push
import asyncio

bot = Bot(token=TOKEN)

class ChoiseTime(StatesGroup):
    
    time = State()
    comment = State()
    checking_record = State()


async def time_for_time_choise(message: types.Message, state: FSMContext):
        
    if await sql_check_status_for_continue_choise_time(message.chat.id) == "record":
        
        async with state.proxy() as data:
            
            if message.text == "⬇️ Назад ⬇️":
                await state.finish()
                return
            
            data['time'] = message.text
            
            day_t, month_t, year_t, hour_t, min_t = await day_month_year_hour_min()
            year = 2024
            time_date = data['time'].split(":")
            
            fname, lname, uname, day, month = await sql_users_for_add_record(message.chat.id)

            if (day == day_t) and (month == month_t) and (year == year_t):
                
                if hour_t > int(time_date[0]):
                    await bot.send_message(message.chat.id, f"Запись не актуальна!\nЗапишитесь на другой день и время", reply_markup= kb_back_start)
                    await state.finish()
                    return
                
                else:
                    if hour_t == int(time_date[0]):
                        await bot.send_message(message.chat.id, f"Нельзя записываться на время, которое сейчас.\nЗапишитесь на другой день и время", reply_markup= kb_back_start)
                        await state.finish()
                        return
                    
                    elif hour_t <= int(time_date[0]) - 3:
                        print(" ")
                    
                    else:
                        await bot.send_message(message.chat.id, f"Записаться можно за 3 часа.\nЗапишитесь на другой день и время", reply_markup= kb_back_start)
                        await state.finish()
                        return

            elif (day < day_t) and (month <= month_t) and (year <= year_t):
                
                await bot.send_message(message.chat.id, f"Запись не актуальна!\nЗапишитесь на другой день и время", reply_markup= kb_back_start)
                await state.finish()
                return
            
            await ChoiseTime.comment.set()
            await message.answer(address)
            await message.answer("Напишите комментарий", reply_markup= kb_remove)
            

async def comment_for_time_choise(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['comment'] = message.text
        
        await ChoiseTime.checking_record.set()
        await message.answer(f"Всё правильно ???", reply_markup= kb_yes_no)
        
        
async def check_for_time_choise(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        
        if message.text == "✅ Да ✅":
        
            data['checking_record'] = message.text

            fname, lname, uname, day, month = await sql_users_for_add_record(message.chat.id)
            
            await sql_add_record(message.chat.id, fname, lname, uname, day, month, data['time'], data['comment'], 1)
            
            await sql_update_make_appointment_time(day, month, data['time'])

            await bot.send_message(chat_record, f'<a href="tg://user?id={message.chat.id}">Профиль</a>'
                                                f" Клиента: {fname} {lname}\nТелеграмм: {uname}\nВремя: {day:02}.{month:02} в {data['time']}\nКомментарий: {data['comment']}", parse_mode="html")
            
            if message.chat.id not in admin_bot:
            
                await message.answer(f"Жду вас {day:02}.{month:02} в {data['time']} 🥰", reply_markup= kb_start)
                
                try:
                    _ = asyncio.run(await main_push(message.chat.id, day, month, data['time']))
                    
                except RuntimeError:
                    print("None")
                    
                await message.answer(price)
            
            else:
                
                await message.answer(f"Ваша заявка отправлена в вашу группу!", reply_markup= kb_start_admin)
                
                try:
                    _ = asyncio.run(await main_push(message.chat.id, day, month, data['time']))
                    
                except RuntimeError:
                    print("None")
            
            await state.finish()
            
        elif message.text == "❌ Нет ❌":
            
            await message.answer("Отмена записи! Запишитесь ещё раз", reply_markup= kb_start)
            
            await state.finish()



async def start_time_choise(dp: Dispatcher):
    
    await ChoiseTime.time.set()

    dp.register_message_handler(time_for_time_choise, state=ChoiseTime.time)
    dp.register_message_handler(comment_for_time_choise, state=ChoiseTime.comment)
    dp.register_message_handler(check_for_time_choise, state=ChoiseTime.checking_record)