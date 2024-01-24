import sqlite3 as sq
import aiosqlite
import os.path

def sql_start_month():
    base = sq.connect("data/number_seats_month.db")
    cur = base.cursor()
    
    if base:
        print("К базе данных месяцев произошло подключение")
        
    base.execute('''CREATE TABLE IF NOT EXISTS month_data(january INTEGER,
                                                            february INTEGER,
                                                            march INTEGER,
                                                            april INTEGER,
                                                            may  INTEGER,
                                                            june INTEGER,
                                                            july INTEGER,
                                                            august INTEGER,
                                                            september INTEGER,
                                                            october INTEGER,
                                                            november INTEGER,
                                                            december INTEGER)''')
    base.commit()
    
    return


async def sql_add_month(january, february, march, april, may, june, july, august, september, october, november, december):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "number_seats_month.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS month_data(january INTEGER,
                                                                february INTEGER,
                                                                march INTEGER,
                                                                april INTEGER,
                                                                may  INTEGER,
                                                                june INTEGER,
                                                                july INTEGER,
                                                                august INTEGER,
                                                                september INTEGER,
                                                                october INTEGER,
                                                                november INTEGER,
                                                                december INTEGER)''')
        await db.commit()
        
        if january == 0 and february == 0 and march == 0 and april == 0 and may == 0 and june == 0 and july == 0 and august == 0 and september == 0 and october == 0 and november == 0 and december == 0:
        
            await cur.execute(f"INSERT INTO month_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (january, february, march, april, may, june, july, august, september, october, november, december))
            await db.commit()
            
            return
        
        else:
            
            await cur.execute(f"UPDATE month_data SET january = {int(january)}, february = {int(february)}, march = {int(march)}, april = {int(april)}, may = {int(may)}, june = {int(june)}, july = {int(july)}, august = {int(august)}, september = {int(september)}, october = {int(october)}, november = {int(november)}, december = {int(december)}")
            await db.commit()
            
            return
        

async def sum_places_month(month):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_admin.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS admin_data(id_users TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    time_day TEXT)''')
        await db.commit()
        
        num_month = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
        
        for i in range(1, month+1):
            await cur.execute(f"SELECT day, time_day FROM admin_data WHERE month == {int(i)}")
            users_text = await cur.fetchall()
            
            if users_text == []:
                num_month[i].append(0)
            
            else:
                time_time = []
                for j in users_text:
                    a = j[1].split("\n\n")
                    for k in a:
                        time_time.append(k)
                        
                len_time_time = len(time_time)
                num_month[i].append(len_time_time)
                time_time = []
        await db.commit()
        return num_month[1][0], num_month[2][0], num_month[3][0], num_month[4][0], num_month[5][0], num_month[6][0], num_month[7][0], num_month[8][0], num_month[9][0], num_month[10][0], num_month[11][0], num_month[12][0]
    

async def sql_choice_month(month):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "number_seats_month.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS month_data(january INTEGER,
                                                                february INTEGER,
                                                                march INTEGER,
                                                                april INTEGER,
                                                                may  INTEGER,
                                                                june INTEGER,
                                                                july INTEGER,
                                                                august INTEGER,
                                                                september INTEGER,
                                                                october INTEGER,
                                                                november INTEGER,
                                                                december INTEGER)''')
        await db.commit()
        
        await cur.execute(f"SELECT {month} FROM month_data")
        num_month = await cur.fetchall()
        
        if num_month[0][0] == 0:
            
            return False
        
        else:
            return True
        
        
async def sql_day_month_choise_month(users, day, month):
    pass