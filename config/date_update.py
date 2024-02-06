import time

async def day_month_update():
    
    seconds = time.time()
    result = time.localtime(seconds)
    
    return result.tm_mday, result.tm_mon


async def day_month_year_hour_min():
    
    seconds = time.time()
    result = time.localtime(seconds)
    
    return result.tm_mday, result.tm_mon, result.tm_year, result.tm_hour, result.tm_min


async def check_day(day, month):
    
    if day == 1:
        
        if month == 1:
            return 31
        
        elif month == 2:
            return 31
        
        elif month == 3:
            return 29
        
        elif month == 4:
            return 31
        
        elif month == 5:
            return 30
        
        elif month == 6:
            return 31
        
        elif month == 7:
            return 30
        
        elif month == 8:
            return 31
        
        elif month == 9:
            return 31
        
        elif month == 10:
            return 30
        
        elif month == 11:
            return 31
        
        elif month == 12:
            return 30
        
    else:
        return day - 1
        

async def check_month(day, month):
    
    if day == 1:
        
        if month == 1:
            return 12
        
        elif month == 2:
            return 1
        
        elif month == 3:
            return 2
        
        elif month == 4:
            return 3
        
        elif month == 5:
            return 4
        
        elif month == 6:
            return 5
        
        elif month == 7:
            return 6
        
        elif month == 8:
            return 7
        
        elif month == 9:
            return 8
        
        elif month == 10:
            return 9
        
        elif month == 11:
            return 10
        
        elif month == 12:
            return 11
        
    else:
        return month
    
    
async def check_day_plus_one(day, month):
    
    if day == 31:
        
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 1
        
        else:
            return day + 1
    
    elif day == 30:
        
        if month in [4, 6, 9, 11]:
            return 1
        
        else:
            return day + 1
        
    elif day == 29:
        
        if month == 2:
            return 1
        
        else:
            return day + 1
    
    else:
        return day + 1