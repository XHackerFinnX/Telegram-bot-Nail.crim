from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config.config import TOKEN, chat_record, admin_bot
from data.data_client import sql_check_status_for_continue_choise_time, sql_users_for_add_record
from data.data_form import sql_add_record
from data.data_form import sql_update_make_appointment_time
from keybord_markup.keyboard import kb_yes_no, kb_start, kb_remove, kb_start_admin

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
            
            await ChoiseTime.comment.set()
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
            
            await sql_add_record(message.chat.id, fname, lname, uname, day, month, data['time'], data['comment'])
            
            await sql_update_make_appointment_time(day, month, data['time'])

            await bot.send_message(chat_record, f'<a href="tg://user?id={message.chat.id}">Профиль</a>'
                                                f" Клиента: {fname} {lname}\nТелеграмм: {uname}\nВремя: {day:02}.{month:02} в {data['time']}\nКомментарий: {data['comment']}", parse_mode="html")
            
            if message.chat.id not in admin_bot:
            
                await message.answer(f"Жду вас {day:02}.{month:02} в {data['time']} 🥰", reply_markup= kb_start)
            
            else:
                
                await message.answer(f"Ваша заявка отправлена в вашу группу!", reply_markup= kb_start_admin)
            
            await state.finish()
            
        elif message.text == "❌ Нет ❌":
            
            await message.answer("Отмена записи! Запишитесь ещё раз", reply_markup= kb_start)
            
            await state.finish()



async def start_time_choise(dp: Dispatcher):
    
    await ChoiseTime.time.set()

    dp.register_message_handler(time_for_time_choise, state=ChoiseTime.time)
    dp.register_message_handler(comment_for_time_choise, state=ChoiseTime.comment)
    dp.register_message_handler(check_for_time_choise, state=ChoiseTime.checking_record)