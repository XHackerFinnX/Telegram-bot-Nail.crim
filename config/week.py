
async def check_date_day_minus(day, month):
    
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
        

async def check_date_month_minus(day, month):
    
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
    

async def check_date_day_plus(day, month):
    
    if day == 30:
        
        if month == 4:
            return 1
        
        elif month == 6:
            return 1
        
        elif month == 9:
            return 1
        
        elif month == 11:
            return 1
        
        else:
            return day + 1
        
    elif day == 31:
        
        if month == 1:
            return 1
        
        elif month == 3:
            return 1
        
        elif month == 5:
            return 1
        
        elif month == 7:
            return 1
        
        elif month == 8:
            return 1
        
        elif month == 10:
            return 1
        
        elif month == 12:
            return 1
        
    elif day == 29:
        
        if month == 2:
            return 1
        
        else:
            return day + 1
        
    else:
        return day + 1
        

async def check_date_month_plus(day, month):
    
    if day == 30:
        
        if month == 4:
            return 5
        
        elif month == 6:
            return 7
        
        elif month == 9:
            return 8
        
        elif month == 11:
            return 12
        
        else:
            return month
        
    elif day == 31:
        
        if month == 1:
            return 2
        
        elif month == 3:
            return 4
        
        elif month == 5:
            return 6
        
        elif month == 7:
            return 8
        
        elif month == 8:
            return 9
        
        elif month == 10:
            return 11
        
        elif month == 12:
            return 1
        
    elif day == 29:
        
        if month == 2:
            return 3
        
        else:
            return month
        
    else:
        return month
    
