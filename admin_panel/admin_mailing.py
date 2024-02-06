from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keybord_markup.keyboard import kb_admin_action, kb_back_admin, kb_yes_no
from config.config import TOKEN, admin_bot
from data.data_mailing import sql_add_client_for_mailing
import asyncio

bot = Bot(token=TOKEN)

class MailingClient(StatesGroup):
  
    text_mailing = State()
    checking_text = State()


async def mailing_client(message: types.Message, state: FSMContext):
    
    if message.chat.id not in admin_bot:
        await message.answer("У вас недостаточно прав!")
        await state.finish()
        
        return
    
    await MailingClient.text_mailing.set()
    await message.answer("Напишите текст для рассылки!", reply_markup=kb_back_admin)
    

async def text_mailing_print(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        
        if message.text == "⬇️ Назад к панели ⬇️":
            await message.answer("Выберите действие...", reply_markup= kb_admin_action)
            await state.finish()

            return
        
        data['text_mailing'] = message.text
        
    await MailingClient.next()
    await message.answer("Всё верно? Отправить рассылку клиентам!", reply_markup=kb_yes_no)
    

async def sending_mailing_text(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        
        if message.text == "✅ Да ✅":
            
            data['checking_text'] = message.text
            
            await message.answer("Рассылка отправлена!", reply_markup= kb_admin_action)
            
            await state.finish()
            
            list_users = await sql_add_client_for_mailing()
            
            mailing_yes = 0
            
            mailing_no = 0
            
            for user in list_users:
                try:
                    await asyncio.sleep(1)
                    await bot.send_message(user, data['text_mailing'])
                    mailing_yes += 1
                except:
                    mailing_no += 1
                    print("Рассылку не получил!")
            
            await message.answer(f"Рассылку получили:\nВсего пользователей: {len(list_users)}\nПолучили: {mailing_yes}\nНе получили: {mailing_no}")
    
        elif message.text == "❌ Нет ❌":

            await message.answer("Отмена рассылки", reply_markup= kb_admin_action)

            await state.finish()
    
def start_mailing(dp: Dispatcher):
    
    dp.register_message_handler(mailing_client, Text(equals="Рассылка ✉️"), state=None)
    dp.register_message_handler(text_mailing_print, state=MailingClient.text_mailing)
    dp.register_message_handler(sending_mailing_text, state=MailingClient.checking_text)