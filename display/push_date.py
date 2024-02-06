from aiogram import Bot
from config.config import TOKEN
from config.date_update import day_month_year_hour_min
from config.date_update import check_day, check_month, check_day_plus_one
from data.data_form import sql_status_null
import asyncio
import time

bot = Bot(token=TOKEN)

async def record_push_date(users, day, month, time_date):

    day_t, month_t, year_t, hour_t, min_t = await day_month_year_hour_min()
    year = 2024
    time_date = time_date.split(":")

    if (day == day_t) and (month == month_t) and (year == year_t):
        
        flag = True
        while flag:
            try:
                print(f"Уведомление 1 {day:02}.{month:02} в {time_date[0]}:{time_date[1]}")
                day = f"{day:02}"
                month = f"{month:02}"
                
                date = f"{day}/{month}/{year} {int(time_date[0])-1}:00"
                
                second_future = time.strptime(date, '%d/%m/%Y %H:%M')
                second_future = time.mktime(second_future)
                second_present = time.time()
                
                counting_down = second_future - second_present
                
                if counting_down < 0:
                    return
                
                await asyncio.sleep(counting_down)
                
                await bot.send_message(users, f"Напоминаю {day:02}.{month:02} в {time_date[0]}:{time_date[1]}\nЗапись к Nail.crim")
                
                try:
                    await sql_status_null(users, day, month, f"{time_date[0]}:{time_date[1]}", 1)
                except:
                    print("статус не обновлен")
                
                flag = False
                
                print(f"Уведомление 1 {day:02}.{month:02} в {time_date[0]}:{time_date[1]} отработало")
                
                return
                
            except Exception:
                print("Превышен таймаут семафора")
            
    elif (day == await check_day_plus_one(day_t, month_t)) and ((month == month_t) or (month == month_t+1)) and (int(year) == year_t):
        
        flag = True
        while flag:
            try:
                print(f"Уведомление 2 {day:02}.{month:02} в {time_date[0]}:{time_date[1]}")
                day = f"{day:02}"
                month = f"{month:02}"
                
                date = f"{day}/{month}/{year} {int(time_date[0])-1}:00"
                
                second_future = time.strptime(date, '%d/%m/%Y %H:%M')
                second_future = time.mktime(second_future)
                second_present = time.time()
                
                counting_down = second_future - second_present
                
                if counting_down < 0:
                    return
                
                await asyncio.sleep(counting_down)
                
                await bot.send_message(users, f"Напоминаю {day:02}.{month:02} в {time_date[0]}:{time_date[1]}\nЗапись к Nail.crim")

                try:
                    await sql_status_null(users, day, month, f"{time_date[0]}:{time_date[1]}", 1)
                except:
                    print("статус не обновлен")
                
                flag = False
                
                print(f"Уведомление 2 {day:02}.{month:02} в {time_date[0]}:{time_date[1]} отработало")
                
                return
                
            except Exception:
                print("Превышен таймаут семафора")
        
    else:
        # Первое уведомление за 24 часа
        flag = True
        while flag:
            try:
                print(f"Уведомление 3. 1 {day:02}.{month:02} в {time_date[0]}:{time_date[1]}")
                day_u = await check_day(day, month)
                month_u = await check_month(day, month)
                
                day_u = f"{day_u:02}"
                month_u = f"{month_u:02}"
                
                date = f"{day_u}/{month_u}/{year} {time_date[0]}:{time_date[1]}"
                
                second_future = time.strptime(date, '%d/%m/%Y %H:%M')
                second_future = time.mktime(second_future)
                second_present = time.time()
                
                counting_down = second_future - second_present
                
                if counting_down < 0:
                    return
                
                await asyncio.sleep(counting_down)
                
                await bot.send_message(users, f"Напоминаю {day:02}.{month:02} в {time_date[0]}:{time_date[1]}\nЗапись к Nail.crim")
                      
                flag = False
                
                print(f"Уведомление 3. 1 {day:02}.{month:02} в {time_date[0]}:{time_date[1]} отработало")
                
            except Exception:
                print("Превышен таймаут семафора")
                
        flag = True
        while flag:
            try:
                print(f"Уведомление 3. 2 {day:02}.{month:02} в {time_date[0]}:{time_date[1]}")
                
                day = f"{day:02}"
                month = f"{month:02}"
                
                date = f"{day}/{month}/{year} {int(time_date[0])-1}:00"
                
                second_future = time.strptime(date, '%d/%m/%Y %H:%M')
                second_future = time.mktime(second_future)
                second_present = time.time()
                
                counting_down = second_future - second_present
                
                if counting_down < 0:
                    return
                
                await asyncio.sleep(counting_down)
                
                await bot.send_message(users, f"Напоминаю {day:02}.{month:02} в {time_date[0]}:{time_date[1]}\nЗапись к Nail.crim")
                
                try:
                    await sql_status_null(users, day, month, f"{time_date[0]}:{time_date[1]}", 1)
                except:
                    print("статус не обновлен")
                
                flag = False
                
                print(f"Уведомление 3. 2 {day:02}.{month:02} в {time_date[0]}:{time_date[1]} отработало")
                
                return
                
            except Exception:
                print("Превышен таймаут семафора")
    
    
async def main_push(users, day, month, time):
    
    _ = asyncio.create_task(record_push_date(users, day, month, time))
    
    return
    