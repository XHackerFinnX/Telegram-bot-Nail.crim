from config.week import check_date_day_minus, check_date_month_minus, check_date_day_plus, check_date_month_plus
from display.time_display import display_time
from data.data_admin import sql_admin_make_appointment_time

import sqlite3 as sq
import aiosqlite
import os.path


def sql_start_users():
    base = sq.connect("data/note_users.db")
    cur = base.cursor()
    
    if base:
        print("К базе данных пользователей произошло подключение")
        
    base.execute('''CREATE TABLE IF NOT EXISTS users_data(id_users TEXT,
                                                            fname TEXT,
                                                            lname TEXT,
                                                            uname TEXT,
                                                            day INTEGER,
                                                            month INTEGER,
                                                            status TEXT)''')
    base.commit()
    
    return
    
    
async def sql_add_client(id_users, fname, lname, uname, day, month, status):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_users.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS users_data(id_users TEXT,
                                                                    fname TEXT,
                                                                    lname TEXT,
                                                                    uname TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    status TEXT)''')
        await db.commit()

        await cur.execute(f"SELECT id_users, day, month FROM users_data WHERE id_users == {str(id_users)}")
        users = await cur.fetchall()
        
        if users == []:
            await cur.execute(f"INSERT INTO users_data VALUES (?, ?, ?, ?, ?, ?, ?)", (id_users, fname, lname, uname, day, month, status))
            await db.commit()
            
            return
        
        await cur.execute(f"UPDATE users_data SET day = {day}, month = {month}, status = '{status}' WHERE id_users == {str(id_users)}")
        await db.commit()
        
        return
        
        
async def sql_add_continue_date(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_users.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS users_data(id_users TEXT,
                                                            fname TEXT,
                                                            lname TEXT,
                                                            uname TEXT,
                                                            day INTEGER,
                                                            month INTEGER,
                                                            status TEXT)''')
        await db.commit()
        
        await cur.execute(f"SELECT id_users, day, month FROM users_data WHERE id_users == {str(id_users)}")
        users = await cur.fetchall()
                
        if (int(users[0][1]) in [29, 30, 31]) and (int(users[0][2]) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
            day = await check_date_day_plus(int(users[0][1]), int(users[0][2]))
            month = await check_date_month_plus(int(users[0][1]), int(users[0][2]))
        else:
            day = int(users[0][1]) + 1
            month = int(users[0][2])
        
        await cur.execute(f"UPDATE users_data SET day = {day}, month = {month} WHERE id_users == {str(id_users)}")
        await db.commit()
        
        await display_time(int(id_users), day, month)
                
    return


async def sql_add_back_date(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_users.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS users_data(id_users TEXT,
                                                            fname TEXT,
                                                            lname TEXT,
                                                            uname TEXT,
                                                            day INTEGER,
                                                            month INTEGER,
                                                            status TEXT)''')
        await db.commit()
        
        await cur.execute(f"SELECT id_users, day, month FROM users_data WHERE id_users == {str(id_users)}")
        users = await cur.fetchall()
    
        if (int(users[0][1]) == 1) and (int(users[0][2]) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
            day = await check_date_day_minus(int(users[0][1]), int(users[0][2]))
            month = await check_date_month_minus(int(users[0][1]), int(users[0][2]))
        else:
            day = int(users[0][1]) - 1
            month = int(users[0][2])
        
        await cur.execute(f"UPDATE users_data SET day = {day}, month = {month} WHERE id_users == {str(id_users)}")
        await db.commit()
        
        await display_time(int(id_users), day, month)
                
    return


async def sql_print_day(id_users):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_users.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS users_data(id_users TEXT,
                                                                    fname TEXT,
                                                                    lname TEXT,
                                                                    uname TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    status TEXT)''')
        await db.commit()
        
        await cur.execute(f"SELECT id_users, day, month FROM users_data WHERE id_users == {str(id_users)}")
        users = await cur.fetchall()
        
        return users[0]
    
    
async def sql_make_appointment_time(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_users.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS users_data(id_users TEXT,
                                                                    fname TEXT,
                                                                    lname TEXT,
                                                                    uname TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    status TEXT)''')
        await db.commit()
        
        await cur.execute(f"SELECT day, month FROM users_data WHERE id_users == {str(id_users)}")
        users = await cur.fetchall()
        
        await db.commit()
        
        flag = await sql_admin_make_appointment_time(users)
        
        return flag
    
    
async def sql_make_appointment_status_record(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_users.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS users_data(id_users TEXT,
                                                                    fname TEXT,
                                                                    lname TEXT,
                                                                    uname TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    status TEXT)''')
        await db.commit()
        
        status = "record"
        
        await cur.execute(f"UPDATE users_data SET status = '{status}' WHERE id_users == {str(id_users)}")
        await db.commit()
        
        
async def sql_check_status_for_continue_choise_time(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_users.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS users_data(id_users TEXT,
                                                                    fname TEXT,
                                                                    lname TEXT,
                                                                    uname TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    status TEXT)''')
        await db.commit()
        
        await cur.execute(f"SELECT status FROM users_data WHERE id_users == {str(id_users)}")
        users = await cur.fetchall()
        
        if users[0][0] == "NO":
            await db.commit()
            
            return "NO"
        
        elif users[0][0] == "record":
            await db.commit()
            
            return "record"
        
        elif users[0][0] == "YES":
            await db.commit()
            
            return "YES"
        
        
async def sql_users_for_add_record(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_users.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS users_data(id_users TEXT,
                                                                    fname TEXT,
                                                                    lname TEXT,
                                                                    uname TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    status TEXT)''')
        await db.commit()
        
        await cur.execute(f"SELECT fname, lname, uname, day, month FROM users_data WHERE id_users == {str(id_users)}")
        users = await cur.fetchall()
        
        return users[0][0], users[0][1], users[0][2], users[0][3], users[0][4]