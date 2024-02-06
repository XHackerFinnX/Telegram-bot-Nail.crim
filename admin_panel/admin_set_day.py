from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keybord_markup.keyboard import kb_remove, kb_admin_action, kb_back_admin
from config.config import TOKEN, admin_bot
from data.data_admin import sql_admin_add_day

bot = Bot(token=TOKEN)

class DayAdd(StatesGroup):
  
    day = State()
    time_day = State()


async def print_day(message: types.Message, state: FSMContext):
    
    if message.chat.id not in admin_bot:
        await message.answer("У вас недостаточно прав!")
        await state.finish()
        
        return
        
    await DayAdd.day.set()
    await message.answer("Для назначения дня напиши в формате:\nдень.месяц\nПримеры: 1.1, 20.5, 4.10, 12.12", reply_markup= kb_back_admin)
    

async def day(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        
        if message.text == "⬇️ Назад к панели ⬇️":
            await message.answer("Выберите действие...", reply_markup= kb_admin_action)
            await state.finish()

            return
        
        data['day'] = message.text
        
    await DayAdd.next()
    await message.answer("Теперь напиши график свободного\n времени в формате:\nВремя - Свободно\nПример: 16:30 - Свободно\n", reply_markup= kb_remove)
    

async def day_time(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['time_day'] = message.text
        try:
            day_and_month = data['day'].split(".")
            day = day_and_month[0]
            month = day_and_month[1]
            
            td = data['time_day'].split("\n\n")
            time_day = []
            
            for i in td:
                time_day.append(i+" - Свободно")
            time_day = "\n\n".join(time_day)

        except IndexError:
            await message.answer("Некорректно ввели дату!", reply_markup= kb_admin_action)
            await state.finish()
            
            return
        
        await sql_admin_add_day(message.chat.id, day, month, time_day)
        
        await message.answer("Готово", reply_markup= kb_admin_action)
        await state.finish()
        
        return

def start_print_day(dp: Dispatcher):
    
    dp.register_message_handler(print_day, Text(equals="Назначить день 🗓"), state=None)
    dp.register_message_handler(day, state=DayAdd.day)
    dp.register_message_handler(day_time, state=DayAdd.time_day)