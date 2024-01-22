import sqlite3 as sq
import aiosqlite
import os.path


def sql_start_form():
    base = sq.connect("data/note_form.db")
    cur = base.cursor()
    
    if base:
        print("К базе данных записей произошло подключение")
        
    base.execute('''CREATE TABLE IF NOT EXISTS form_data(id_users TEXT,
                                                        fname TEXT,
                                                        lname TEXT,
                                                        uname TEXT,
                                                        day INTEGER,
                                                        month INTEGER,
                                                        time TEXT,
                                                        comment TEXT)''')
    base.commit()
    
    return


async def sql_add_record(id_users, fname, lname, uname, day, month, time, comment):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_form.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS form_data(id_users TEXT,
                                                                fname TEXT,
                                                                lname TEXT,
                                                                uname TEXT,
                                                                day INTEGER,
                                                                month INTEGER,
                                                                time TEXT,
                                                                comment TEXT)''')
        await db.commit()
        
        await cur.execute(f"INSERT INTO form_data VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id_users, fname, lname, uname, day, month, time, comment))
        await db.commit()
        
        
async def sql_update_make_appointment_time(day, month, time):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "note_admin.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''CREATE TABLE IF NOT EXISTS admin_data(id_users TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    time_day TEXT)''')
        await db.commit()
        
        await cur.execute(f"SELECT time_day FROM admin_data WHERE day == {int(day)} AND month == {int(month)}")
        users_text = await cur.fetchall()
        try:
            there_time = users_text[0][0].split("\n\n")

            for i in there_time:
                if time in i:

                    there_time.remove(i)
                    new_text_time = "\n\n".join(there_time)

                    if there_time == []:

                        await cur.execute(f"DELETE FROM admin_data WHERE (day == {int(day)} AND month == {int(month)})")
                        await db.commit()

                        return

                    await cur.execute(f"UPDATE admin_data SET time_day = '{new_text_time}' WHERE day == {int(day)} AND month == {int(month)}")
                    await db.commit()

                    return
            
            return
        except:
            print("Ошибка с выбором времени")
            
            return