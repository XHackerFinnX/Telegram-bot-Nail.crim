import sqlite3 as sq
import aiosqlite
import os.path


async def sql_add_client_for_mailing():
    
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
        
        await cur.execute(f"SELECT id_users FROM users_data")
        users = await cur.fetchall()
        
        list_users = []
        
        if users != []:
            
            for client in users:
                list_users.append(client[0])
            
            return list_users
            
        else:
            
            return