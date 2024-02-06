from display.chart_display import admin_chart_display
import sqlite3 as sq
import aiosqlite
import os.path


def sql_start_admin():
    base_a = sq.connect("data/note_admin.db")
    cur_a = base_a.cursor()
    
    if base_a:
        print("К базе данных администратора произошло подключение")
        
    base_a.execute('''CREATE TABLE IF NOT EXISTS admin_data(id_users TEXT,
                                                            day INTEGER,
                                                            month INTEGER,
                                                            time_day TEXT)''')
    base_a.commit()
    
    return


def sql_start_admin_viewing_week():
    
    base_a = sq.connect("data/note_week.db")
    cur_a = base_a.cursor()
    
    if base_a:
        print("К базе данных недель произошло подключение")
        
    base_a.execute('''CREATE TABLE IF NOT EXISTS admin_week(id_users TEXT,
                                                            week INTEGER)''')
    base_a.commit()
    
    return


async def sql_admin_add_day(id_users, day, month, time_day):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_admin.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS admin_data(id_users TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    time_day TEXT)''')
        await db.commit()
        
        await cur.execute(f"SELECT day, month FROM admin_data WHERE day == {day} AND month == {month}")
        users = await cur.fetchall()
        
        if users == []:
            await cur.execute(f"INSERT INTO admin_data VALUES (?, ?, ?, ?)", (id_users, day, month, time_day))
            await db.commit()
            
            return

        await cur.execute(f"UPDATE admin_data SET id_users = '{id_users}',time_day = '{time_day}' WHERE (day == {int(users[0][0])} AND month == {int(users[0][1])})")
        await db.commit()
    
        return
    
    
async def sql_admin_delete_day(day, month):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_admin.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS admin_data(id_users TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    time_day TEXT)''')
        await db.commit()
        try:
            await cur.execute(f"SELECT day, month FROM admin_data WHERE day == {day} AND month == {month}")
            users = await cur.fetchall()

            if users != []:
                await cur.execute(f"DELETE FROM admin_data WHERE (day == {int(day)} AND month == {int(month)})")
                await db.commit()

                return True

            else:
                return False
        except:
            return False
        
        
async def sql_text_for_client(day, month):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_admin.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS admin_data(id_users TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    time_day TEXT)''')
        await db.commit()
        
        await cur.execute(f"SELECT time_day FROM admin_data WHERE day == {day} AND month == {month}")
        users = await cur.fetchall()
        
        if users == []:
            await db.commit()
            
            return "Записей нет!"
        
        return users[0][0]
    
    
async def sql_admin_make_appointment_time(users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_admin.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS admin_data(id_users TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    time_day TEXT)''')
        await db.commit()
        
        await cur.execute(f"SELECT time_day FROM admin_data WHERE day == {int(users[0][0])} AND month == {int(users[0][1])}")
        users_text = await cur.fetchall()
        
        if users_text == []:
            
            return []
        
        there_time = users_text[0][0].split("\n\n")
        time_time = []
        
        for i in there_time:
            time_time.append(i[0:5])
        
        return time_time
    

async def sql_add_week(id_users, week):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_week.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS admin_week(id_users TEXT,
                                                                    week INTEGER)''')
        await db.commit()
        
        await cur.execute(f"SELECT id_users, week FROM admin_week WHERE id_users == '{str(id_users)}'")
        users = await cur.fetchall()
        
        if users == []:
            await cur.execute(f"INSERT INTO admin_week VALUES (?, ?)", (id_users, week))
            await db.commit()
            
        else:
            await cur.execute(f"UPDATE admin_week SET week = {int(week)}, id_users = '{id_users}'")
            await db.commit()
            
        return
        


async def sql_add_continue_week(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_week.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS admin_week(week INTEGER)''')
        await db.commit()
        
        await cur.execute(f"SELECT week FROM admin_week WHERE id_users == '{str(id_users)}'")
        users = await cur.fetchall()
        
        week = int(users[0][0]) + 1
        
        if week > 53:
            return False
        
        await cur.execute(f"UPDATE admin_week SET week = {int(week)}, id_users = '{id_users}'")
        await db.commit()
        
        await admin_chart_display(id_users, week)
        
        return True

async def sql_add_back_week(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_week.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS admin_week(week INTEGER)''')
        await db.commit()
        
        await cur.execute(f"SELECT week FROM admin_week WHERE id_users == '{str(id_users)}'")
        users = await cur.fetchall()
        
        week = int(users[0][0]) - 1
        
        if week < 1:
            return False
        
        await cur.execute(f"UPDATE admin_week SET week = {int(week)}, id_users = '{id_users}'")
        await db.commit()
        
        await admin_chart_display(id_users, week)
        
        return True