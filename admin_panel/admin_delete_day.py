from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keybord_markup.keyboard import kb_admin_action, kb_back_admin
from config.config import TOKEN, admin_bot
from data.data_admin import sql_admin_delete_day

bot = Bot(token=TOKEN)

class DayDelete(StatesGroup):
    
    day_del = State()


async def delete_day(message: types.Message, state: FSMContext):
    
    if message.chat.id not in admin_bot:
        await message.answer("У вас недостаточно прав!")
        await state.finish()
        
        return
    
    await DayDelete.day_del.set()
    await message.answer("Для удаления дня напиши в формате:\nдень.месяц\nПримеры: 1.1, 20.5, 4.10, 12.12", reply_markup= kb_back_admin)
    
    
async def day(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        
        if message.text == "⬇️ Назад к панели ⬇️":
            await message.answer("Выберите действие...", reply_markup= kb_admin_action)
            await state.finish()

            return
        
        data['day_del'] = message.text
        
        day_and_month = data['day_del'].split(".")
        day = day_and_month[0]
        month = day_and_month[1]
        
        if await sql_admin_delete_day(day, month):
            await message.answer("Готово", reply_markup= kb_admin_action)
            await state.finish()

            return
        
        else:
            await message.answer("Этот день не назначен", reply_markup= kb_admin_action)
            await state.finish()
            
            return

def start_delete_day(dp: Dispatcher):
    
    dp.register_message_handler(delete_day, Text(equals="Убрать день 🗓"), state=None)
    dp.register_message_handler(day, state=DayDelete.day_del)