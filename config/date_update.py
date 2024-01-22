import time

async def day_month_update():
    
    seconds = time.time()
    result = time.localtime(seconds)
    
    return result.tm_mday, result.tm_mon